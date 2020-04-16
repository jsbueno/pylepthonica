# -*- coding: utf-8 -*-
    
    
    # "pyleptonica" is a Python wrapper to Leptonica Library
    # Copyright (C) 2010 João Sebastião de Oliveira Bueno <jsbueno@python.org.br>
    
    #This program is free software: you can redistribute it and/or modify
    #it under the terms of the Lesser GNU General Public License as published by
    #the Free Software Foundation, either version 3 of the License, or
    #(at your option) any later version.

    #This program is distributed in the hope that it will be useful,
    #but WITHOUT ANY WARRANTY; without even the implied warranty of
    #MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    #GNU General Public License for more details.

    #You should have received a copy of the Lesser GNU General Public License
    #along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
This file is responsible to parse the Leptonica library
C structures, as defined in the source code header files
and generate corresponding c_types python classes
to interoperate with them.

You may not need to run this to get pyleptonica running - 
check if your leptonica_structures work for your version
of leptonica
"""

from builtins import str
from builtins import range
import sys
from config import leptonica_home

lepton_source_dir = leptonica_home + "/src/"
target_file = "leptonica_structures.py"

# I am feeling quite intimidated by "parsers"
# at this time. let's do it by hand.

# from the "environ.h" file in leptonica source
lepton_types = {
    "l_int8": "ctypes.c_byte", 
    "l_uint8": "ctypes.c_ubyte",
    "l_int16": "ctypes.c_int16",
    "l_uint16": "ctypes.c_uint16",
    "l_int32": "ctypes.c_int32",
    "l_uint32": "ctypes.c_uint32",
    "l_int64": "ctypes.c_int64",
    "l_uint64": "ctypes.c_uint64",
    "l_float32": "ctypes.c_float",
    "l_float64": "ctypes.c_double",
    "l_ok": "ctypes.c_int",
    "char": "ctypes.c_char",
    "void": "ctypes.c_void_p",
    "L_TIMER": "ctypes.c_void_p",
    "size_t": "ctypes.c_size_t",
    "FILE": "ctypes.c_void_p"
    }


def get_file_contents(file_name):
      infile = open(file_name)
      text = infile.readlines()
      infile.close()
      return text
      
def separate_comments(in_list):
    """
    >>> t1 = ''' /* "alo mundo" */ Feliz "/* Natal " /*para*/ "//todos" //mesmo '''
    >>> print separate_comments( [t1])
    (['  Feliz "/* Natal "  "//todos" \n'], ['/* "alo mundo" *//*para*///mesmo \n'])
    """
    comments = []
    code = []
    cl_token = "//"
    cs_token = "/*"
    ce_token = "*/"
    str_token = '"'
    line_comment = False
    multiline_comment = False
    inside_string = False
    for line in in_list:
        multi_start_index = -2 # avoid "/*/" corner case
        code_line = ""
        comment_line = ""
        line_comment = False
        spare = 0
        for index, char in enumerate(line.strip("\n")):
            spare -= 1 
            inside_comment = line_comment or multiline_comment
            if char == str_token and not inside_comment:
                inside_string = not inside_string
            twochar = line[index:index+2]
            if (twochar == cs_token and
                not inside_string and not line_comment):
                multiline_comment = True
                multi_start_index = index
            elif (twochar == ce_token and multiline_comment and
                index - multi_start_index > 1):
                multiline_comment = False
                spare = 2
            elif (twochar == cl_token and not inside_string
                and not multiline_comment):
                line_comment = True
            inside_comment = line_comment or multiline_comment
            if not inside_comment and spare <= 0:
                code_line += char
            else:
                comment_line += char
        comments.append(comment_line + "\n")
        code.append(code_line + "\n")
    return code, comments


def parse_structs(code):
    """
    This can't parse generic C structs - it depends of a 
    specifc formating as the one found on leptonica 1.6
    source files:
    no nested structs are allowed
    structs are always named
    structs are not instantiated on declaration (and more)
    """
    tokens = "".join(code).split()
    struct_level = 0
    kwds = ["struct", "union"]
    
    bracket_level = 0
    structs = {}
    fwd = 1
    sequence = enumerate(tokens)
    while True:
        try:
            for _ in range(fwd):
                index, token = next(sequence)
            fwd = 1
        except StopIteration:
            break
        if (token in kwds and struct_level == 0 and
            tokens[index + 2] == "{"):
            bracket_level += 1
            struct_name = tokens[index + 1]
            struct_level = 1
            struct_body = []
            pre_reqs = set()
            decl_line = []
            fwd = 3
            continue
        if token == "{":
            bracket_level += 1
        elif token[0] == "}":
            bracket_level -= 1
        if struct_level  and bracket_level == 0:
            # use uppercase name: matching names used 
            # in leptonica's typedefs
            structs[struct_name.upper()] = (struct_body, pre_reqs)
            struct_level = 0
            continue
        if struct_level:
            decl_line.append(token)
        if struct_level and token[-1] in (";", ","):
            sep = token[-1]
            if len(token) == 1: #avoid need for the 
                                #separator to be joined to var_name
                decl_line.pop()
            var_name = decl_line[-1].strip(";").strip(",")
            if decl_line[0] in kwds:
                # Convert inner structs  to typedefed names
                var_type = decl_line[1].upper()
            else:
                var_type = " ".join(decl_line[:-1])
            if not var_type in lepton_types:
                pre_reqs.add(var_type)
            struct_body.append((var_name, var_type))
            if sep == ";":
                decl_line = []
            else:
                decl_line = [var_type]
    return structs    

# TODO: Parse the structures comments and add then as docstrings here.
# If a  structure contains pointers to themselves,
# or uses classes not yet declared (despite dependency
# ordering; this is unavoidable with mutual/circular
# dependencies), then we need to declare the class,
# and set the fields afterwards. Let's simply always
# do that:

class_decl_template = '''\
class _%(name)s(ctypes.Structure):
    """%(comments)s
    """
    pass
'''

class_defn_template = '''\
_%(name)s._fields_ = [
        %(rendered_fields)s
    ]

class %(name)s(LeptonObject):
    __metaclass__ = MetaPointer
    _type_ = _%(name)s

    @classmethod
    def from_param(cls, obj):
        return cls._type_.from_param(obj)
'''

field_template = """("%(name)s", %(data_type)s)"""
def render_class(struct_name, body):
    fields = []
    for field_name, data_type in body:
        if data_type in lepton_types:
            data_type = lepton_types[data_type]
            is_native_type = True
        else:
            is_native_type = False
        indirections = 0
        while field_name.startswith("*"):
            indirections += 1
            field_name = field_name[1:].strip()
            if data_type !=  lepton_types["void"] or indirections > 1:
                # FIXME: Maybe make the structures members also be our advanced
                # hybrid type? I think it is not needed
                if is_native_type:
                    data_type = "ctypes.POINTER(%s)" % data_type
                else:
                    data_type = "ctypes.POINTER(_%s)" % data_type
                    is_native_type = True
        rendered = field_template % {"name": field_name, 
            "data_type": ("_" if not is_native_type else "") + data_type}
        fields.append(rendered)
    rendered_fields = ",\n        ".join(fields)
    decl_text = class_decl_template % {"name": struct_name, 
        "comments": "Comments not generated"}
    defn_text = class_defn_template % {"name": struct_name,
        "rendered_fields": rendered_fields}
    return decl_text, defn_text

def parse_file(file_name):
    text = get_file_contents(file_name)
    code, comments = separate_comments(text)
    structs = parse_structs(code)
    return structs

file_template = """
# -*- coding: utf-8 -*-
# Author: João S. O. Bueno
# This is a generated file - do not edit!

from __future__ import absolute_import
import ctypes
from future.utils import with_metaclass
#import weakref

class LeptonObject(object):
    def __new__(cls, *args, **kw):
        \"\"\"
        Constructor for structure types.
        Call with named argument "from_address" to
        point it to an existing structure in memory, 
        else it will try to automatically call Leptonica's
        constructor for this structure
        \"\"\"
        from .leptonica_functions import functions
        data = None
        if not kw or not "from_address" in kw:
            if hasattr(functions, cls.__name__.lower() + "Create"):
                constructor = getattr(functions, cls.__name__.lower() +
                    "Create")
                return constructor(*args)
            data = cls._type_(*args)
            address = ctypes.addressof(data)
        else:
            address = kw["from_address"]
            if isinstance (address, ctypes.c_void_p):
                address = address.value
        #if address in cls._instances_:
        #    return cls._instances_[address]()
        self = object.__new__(cls)
        self._needs_del = True
        if  hasattr(functions, cls.__name__.lower() + "Destroy"):
            self._destructor = getattr(functions, cls.__name__.lower() + "Destroy")
        self._address_ = ctypes.c_void_p(address)
        #cls._instances_[address] = weakref.ref(self)
        if data:
            self._data_ = data
        return self
    def __getattribute__(self, attr):
        if attr in ("_address_", "refcount", "__class__"):
            return object.__getattribute__(self, attr)
        if not self._address_:
            raise ValueError("Object no longer exists")
        if hasattr(self.__class__, "refcount") and self.refcount < 1:
            self._address_ = ctypes.c_void_p(None)
            raise ValueError("Object no longer exists")
        return object.__getattribute__(self, attr)

    def __repr__(self):
        repr_ = "Leptonica %%s object\\n" %% self.__class__.__name__
        if self._address_:
            rendered_fields = []
            for field in self._type_._fields_:
                name = field[0]
                content = getattr(self, name)
                if isinstance(content, LeptonObject):
                    # Add an identation level for nested objects:
                    content = "\\n    ".join(repr(content).split("\\n") )
                rendered_fields.append("    %%s: %%s" %% (name, content))
            repr_ += ",\\n".join(rendered_fields)
        else:
            repr_ += "Not initiated or destroyed\\n"
        return repr_
    def __hash__(self):
        return self._address_.value
    
    def __eq__(self, other):
        return self._address_.value == other._address_.value
    
    def __del__(self):
        cls = self.__class__
        #if self._address_:
        #    del cls._instances_[self._address_.value]
        if not hasattr(cls, "refcount"):
            return
        if self._needs_del and self._destructor:
            self._destructor(ctypes.c_void_p(ctypes.addressof(self._address_)))

def property_factory(raw_structure, field_name):
    return  property(lambda s: getattr(
                        raw_structure.from_address(s._address_.value),
                        field_name),
                     lambda s, val: setattr(
                        raw_structure.from_address(s._address_.value),
                        field_name, val)
                    )

class MetaPointer(type): 
    def __new__(cls, name, bases, dic):
        base_struct = dic["_type_"]
        for field, type_ in base_struct._fields_:
            pr = property_factory(base_struct, field)
            dic[field] = pr
        #dic["_instances_"] = {}
        return type(name, bases, dic)



%(classes)s

%(attributes)s

%(aliases)s

__all__ = %(types)s + ["LeptonObject"]

"""
def render_file(class_tuples, class_list, alias_list):
    aliases = "\n".join("%s = %s" % alias_pair 
        for alias_pair in alias_list)
    decl_list, defn_list = zip(*class_tuples)
    with open(target_file, "wt") as outfile:
        outfile.write(file_template % {
            "classes": "\n".join(decl_list),
            "attributes": "\n".join(defn_list),
            "aliases": aliases,
            "types": (
                [abbrev for abbrev, orig in alias_list] +
                list(class_list))})
    
    

def order_classes(structs, alias_list):
    class_list = []
    rendered = set()
    count = 0
    aliases = dict(map(reversed,alias_list))
    while True:
        if not structs:
            break
        waiting = dict()
        # copy keys to a real list for p3k compatibility
        for struct in list(structs.keys()):
            if '(' in struct or ')' in struct:
                  # avoid macro-computed names, e.g. '__attribute((__packed__))'
                  del structs[struct]
                  continue
            pre_reqs = structs[struct][1]
            missing = pre_reqs.difference(rendered)
            if struct in pre_reqs:
                missing.remove(struct)
            if missing:
                if count > 100:
                    # give up
                    raise Exception("Could not get struct classes in order. Missing prereqs {} for {}".format(
                          missing, struct, rendered))
                def find_transitive(req, target):
                    for req2 in waiting.get(req, []):
                        if (req2 == target or
                            find_transitive(req2, target)):
                            return True
                    return False
                for req in list(missing):
                    if find_transitive(req, struct):
                        # circular/mutual dependency
                        print('cutting out circular dependency "%s" missing from "%s"' % (
                            req, struct))
                        missing.remove(req)
                if missing:
                    waiting[struct] = missing
                    continue
            class_list.append(render_class(struct, structs[struct][0]))
            rendered.add(struct)
            if struct in aliases:
                  rendered.add(aliases[struct])
            del structs[struct]
        count += 1
    return class_list, rendered

def main(file_names):
    structs = {}
    for file_name in file_names:
        structs.update(parse_file(lepton_source_dir + file_name))
    # we are not reading the typedefs, just  infering the typedefs from
    # the structure name, and there are  a few exceptions:
    irregular_names = (("L_BBUFFER", "L_BYTEBUFFER"), 
                       ("DLLIST", "DOUBLELINKEDLIST"), 
                       ("PIXCMAP", "PIXCOLORMAP"),
                       ("BMP_FH", "BMP_FILEHEADER"),
                       ("BMP_IH", "BMP_INFOHEADER"),
                       ("L_AMAP", "L_RBTREE"),
                       ("L_ASET", "L_RBTREE"),
                       ("L_AMAP_NODE", "L_RBTREE_NODE"),
                       ("L_ASET_NODE", "L_RBTREE_NODE"),
                       ("PIXAC", "PIXACOMP"),
                       ("PIXC", "PIXCOMP")
    )
    class_list, class_names = order_classes(structs, irregular_names)
    render_file(class_list, class_names, irregular_names)


all_headers = ['array.h', 'bbuffer.h', 'gplot.h', 'pix.h', 
'regutils.h', 'bmf.h', 'heap.h', 'ptra.h', 'stack.h', 'bmp.h',
'list.h', 'queue.h', 'sudoku.h', 'array.h', 'ccbord.h', 'jbclass.h',
'rbtree.h', 'bmfdata.h', 'bilateral.h', 'dewarp.h', 'imageio.h', 'recog.h', 'stringcode.h',
'morph.h', 'watershed.h', 'endianness.h', 'colorinfo.h']


if __name__ == "__main__":
    main(all_headers)
