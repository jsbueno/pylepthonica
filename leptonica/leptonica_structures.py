
# -*- coding: utf-8 -*-
# Author: João S. O. Bueno
# This is a generated file - do not edit!

from __future__ import absolute_import
from builtins import object
import ctypes
from future.utils import with_metaclass
#import weakref

class LeptonObject(object):
    def __new__(cls, *args, **kw):
        """
        Constructor for structure types.
        Call with named argument "from_address" to
        point it to an existing structure in memory, 
        else it will try to automatically call Leptonica's
        constructor for this structure
        """
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
        repr_ = "Leptonica %s object\n" % self.__class__.__name__
        if self._address_:
            rendered_fields = []
            for field in self._type_._fields_:
                name = field[0]
                content = getattr(self, name)
                if isinstance(content, LeptonObject):
                    # Add an identation level for nested objects:
                    content = "\n    ".join(repr(content).split("\n") )
                rendered_fields.append("    %s: %s" % (name, content))
            repr_ += ",\n".join(rendered_fields)
        else:
            repr_ += "Not initiated or destroyed\n"
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



class _NUMA(ctypes.Structure):
    """Comments not generated
    """
    pass

class _NUMAA(ctypes.Structure):
    """Comments not generated
    """
    pass

class _L_DNA(ctypes.Structure):
    """Comments not generated
    """
    pass

class _L_DNAA(ctypes.Structure):
    """Comments not generated
    """
    pass

class _L_DNAHASH(ctypes.Structure):
    """Comments not generated
    """
    pass

class _SARRAY(ctypes.Structure):
    """Comments not generated
    """
    pass

class _L_BYTEA(ctypes.Structure):
    """Comments not generated
    """
    pass

class _L_BYTEBUFFER(ctypes.Structure):
    """Comments not generated
    """
    pass

class _GPLOT(ctypes.Structure):
    """Comments not generated
    """
    pass

class _PIXCOLORMAP(ctypes.Structure):
    """Comments not generated
    """
    pass

class _RGBA_QUAD(ctypes.Structure):
    """Comments not generated
    """
    pass

class _BOX(ctypes.Structure):
    """Comments not generated
    """
    pass

class _BOXA(ctypes.Structure):
    """Comments not generated
    """
    pass

class _BOXAA(ctypes.Structure):
    """Comments not generated
    """
    pass

class _PTA(ctypes.Structure):
    """Comments not generated
    """
    pass

class _PTAA(ctypes.Structure):
    """Comments not generated
    """
    pass

class _FPIX(ctypes.Structure):
    """Comments not generated
    """
    pass

class _FPIXA(ctypes.Structure):
    """Comments not generated
    """
    pass

class _DPIX(ctypes.Structure):
    """Comments not generated
    """
    pass

class _PIXCOMP(ctypes.Structure):
    """Comments not generated
    """
    pass

class _PIXACOMP(ctypes.Structure):
    """Comments not generated
    """
    pass

class _L_REGPARAMS(ctypes.Structure):
    """Comments not generated
    """
    pass

class _L_HEAP(ctypes.Structure):
    """Comments not generated
    """
    pass

class _L_PTRA(ctypes.Structure):
    """Comments not generated
    """
    pass

class _L_PTRAA(ctypes.Structure):
    """Comments not generated
    """
    pass

class _L_STACK(ctypes.Structure):
    """Comments not generated
    """
    pass

class _BMP_FILEHEADER(ctypes.Structure):
    """Comments not generated
    """
    pass

class _BMP_INFOHEADER(ctypes.Structure):
    """Comments not generated
    """
    pass

class _DOUBLELINKEDLIST(ctypes.Structure):
    """Comments not generated
    """
    pass

class _L_QUEUE(ctypes.Structure):
    """Comments not generated
    """
    pass

class _L_SUDOKU(ctypes.Structure):
    """Comments not generated
    """
    pass

class _RB_TYPE(ctypes.Structure):
    """Comments not generated
    """
    pass

class _L_RBTREE_NODE(ctypes.Structure):
    """Comments not generated
    """
    pass

class _L_COMPRESSED_DATA(ctypes.Structure):
    """Comments not generated
    """
    pass

class _L_PDF_DATA(ctypes.Structure):
    """Comments not generated
    """
    pass

class _L_RCH(ctypes.Structure):
    """Comments not generated
    """
    pass

class _L_RCHA(ctypes.Structure):
    """Comments not generated
    """
    pass

class _L_STRCODE(ctypes.Structure):
    """Comments not generated
    """
    pass

class _SEL(ctypes.Structure):
    """Comments not generated
    """
    pass

class _SELA(ctypes.Structure):
    """Comments not generated
    """
    pass

class _L_KERNEL(ctypes.Structure):
    """Comments not generated
    """
    pass

class _PIX(ctypes.Structure):
    """Comments not generated
    """
    pass

class _PIXA(ctypes.Structure):
    """Comments not generated
    """
    pass

class _PIXAA(ctypes.Structure):
    """Comments not generated
    """
    pass

class _PIXACC(ctypes.Structure):
    """Comments not generated
    """
    pass

class _PIXTILING(ctypes.Structure):
    """Comments not generated
    """
    pass

class _L_BMF(ctypes.Structure):
    """Comments not generated
    """
    pass

class _CCBORD(ctypes.Structure):
    """Comments not generated
    """
    pass

class _CCBORDA(ctypes.Structure):
    """Comments not generated
    """
    pass

class _JBCLASSER(ctypes.Structure):
    """Comments not generated
    """
    pass

class _JBDATA(ctypes.Structure):
    """Comments not generated
    """
    pass

class _L_RBTREE(ctypes.Structure):
    """Comments not generated
    """
    pass

class _L_BILATERAL(ctypes.Structure):
    """Comments not generated
    """
    pass

class _L_DEWARP(ctypes.Structure):
    """Comments not generated
    """
    pass

class _L_RDID(ctypes.Structure):
    """Comments not generated
    """
    pass

class _L_WSHED(ctypes.Structure):
    """Comments not generated
    """
    pass

class _L_COLORINFO(ctypes.Structure):
    """Comments not generated
    """
    pass

class _L_DEWARPA(ctypes.Structure):
    """Comments not generated
    """
    pass

class _L_RECOG(ctypes.Structure):
    """Comments not generated
    """
    pass


_NUMA._fields_ = [
        ("nalloc", ctypes.c_int32),
        ("n", ctypes.c_int32),
        ("refcount", ctypes.c_int32),
        ("startx", ctypes.c_float),
        ("delx", ctypes.c_float),
        ("array", ctypes.POINTER(ctypes.c_float))
    ]

class NUMA(with_metaclass(MetaPointer, LeptonObject)):
    _type_ = _NUMA

    @classmethod
    def from_param(cls, obj):
        return cls._type_.from_param(obj)

_NUMAA._fields_ = [
        ("nalloc", ctypes.c_int32),
        ("n", ctypes.c_int32),
        ("numa", ctypes.POINTER(ctypes.POINTER(_NUMA)))
    ]

class NUMAA(with_metaclass(MetaPointer, LeptonObject)):
    _type_ = _NUMAA

    @classmethod
    def from_param(cls, obj):
        return cls._type_.from_param(obj)

_L_DNA._fields_ = [
        ("nalloc", ctypes.c_int32),
        ("n", ctypes.c_int32),
        ("refcount", ctypes.c_int32),
        ("startx", ctypes.c_double),
        ("delx", ctypes.c_double),
        ("array", ctypes.POINTER(ctypes.c_double))
    ]

class L_DNA(with_metaclass(MetaPointer, LeptonObject)):
    _type_ = _L_DNA

    @classmethod
    def from_param(cls, obj):
        return cls._type_.from_param(obj)

_L_DNAA._fields_ = [
        ("nalloc", ctypes.c_int32),
        ("n", ctypes.c_int32),
        ("dna", ctypes.POINTER(ctypes.POINTER(_L_DNA)))
    ]

class L_DNAA(with_metaclass(MetaPointer, LeptonObject)):
    _type_ = _L_DNAA

    @classmethod
    def from_param(cls, obj):
        return cls._type_.from_param(obj)

_L_DNAHASH._fields_ = [
        ("nbuckets", ctypes.c_int32),
        ("initsize", ctypes.c_int32),
        ("dna", ctypes.POINTER(ctypes.POINTER(_L_DNA)))
    ]

class L_DNAHASH(with_metaclass(MetaPointer, LeptonObject)):
    _type_ = _L_DNAHASH

    @classmethod
    def from_param(cls, obj):
        return cls._type_.from_param(obj)

_SARRAY._fields_ = [
        ("nalloc", ctypes.c_int32),
        ("n", ctypes.c_int32),
        ("refcount", ctypes.c_int32),
        ("array", ctypes.POINTER(ctypes.POINTER(ctypes.c_char)))
    ]

class SARRAY(with_metaclass(MetaPointer, LeptonObject)):
    _type_ = _SARRAY

    @classmethod
    def from_param(cls, obj):
        return cls._type_.from_param(obj)

_L_BYTEA._fields_ = [
        ("nalloc", ctypes.c_size_t),
        ("size", ctypes.c_size_t),
        ("refcount", ctypes.c_int32),
        ("data", ctypes.POINTER(ctypes.c_ubyte))
    ]

class L_BYTEA(with_metaclass(MetaPointer, LeptonObject)):
    _type_ = _L_BYTEA

    @classmethod
    def from_param(cls, obj):
        return cls._type_.from_param(obj)

_L_BYTEBUFFER._fields_ = [
        ("nalloc", ctypes.c_int32),
        ("n", ctypes.c_int32),
        ("nwritten", ctypes.c_int32),
        ("array", ctypes.POINTER(ctypes.c_ubyte))
    ]

class L_BYTEBUFFER(with_metaclass(MetaPointer, LeptonObject)):
    _type_ = _L_BYTEBUFFER

    @classmethod
    def from_param(cls, obj):
        return cls._type_.from_param(obj)

_GPLOT._fields_ = [
        ("rootname", ctypes.POINTER(ctypes.c_char)),
        ("cmdname", ctypes.POINTER(ctypes.c_char)),
        ("cmddata", ctypes.POINTER(_SARRAY)),
        ("datanames", ctypes.POINTER(_SARRAY)),
        ("plotdata", ctypes.POINTER(_SARRAY)),
        ("plotlabels", ctypes.POINTER(_SARRAY)),
        ("plotstyles", ctypes.POINTER(_NUMA)),
        ("nplots", ctypes.c_int32),
        ("outname", ctypes.POINTER(ctypes.c_char)),
        ("outformat", ctypes.c_int32),
        ("scaling", ctypes.c_int32),
        ("title", ctypes.POINTER(ctypes.c_char)),
        ("xlabel", ctypes.POINTER(ctypes.c_char)),
        ("ylabel", ctypes.POINTER(ctypes.c_char))
    ]

class GPLOT(with_metaclass(MetaPointer, LeptonObject)):
    _type_ = _GPLOT

    @classmethod
    def from_param(cls, obj):
        return cls._type_.from_param(obj)

_PIXCOLORMAP._fields_ = [
        ("array", ctypes.c_void_p),
        ("depth", ctypes.c_int32),
        ("nalloc", ctypes.c_int32),
        ("n", ctypes.c_int32)
    ]

class PIXCOLORMAP(with_metaclass(MetaPointer, LeptonObject)):
    _type_ = _PIXCOLORMAP

    @classmethod
    def from_param(cls, obj):
        return cls._type_.from_param(obj)

_RGBA_QUAD._fields_ = [
        ("blue", ctypes.c_ubyte),
        ("green", ctypes.c_ubyte),
        ("red", ctypes.c_ubyte),
        ("alpha", ctypes.c_ubyte)
    ]

class RGBA_QUAD(with_metaclass(MetaPointer, LeptonObject)):
    _type_ = _RGBA_QUAD

    @classmethod
    def from_param(cls, obj):
        return cls._type_.from_param(obj)

_BOX._fields_ = [
        ("x", ctypes.c_int32),
        ("y", ctypes.c_int32),
        ("w", ctypes.c_int32),
        ("h", ctypes.c_int32),
        ("refcount", ctypes.c_uint32)
    ]

class BOX(with_metaclass(MetaPointer, LeptonObject)):
    _type_ = _BOX

    @classmethod
    def from_param(cls, obj):
        return cls._type_.from_param(obj)

_BOXA._fields_ = [
        ("n", ctypes.c_int32),
        ("nalloc", ctypes.c_int32),
        ("refcount", ctypes.c_uint32),
        ("box", ctypes.POINTER(ctypes.POINTER(_BOX)))
    ]

class BOXA(with_metaclass(MetaPointer, LeptonObject)):
    _type_ = _BOXA

    @classmethod
    def from_param(cls, obj):
        return cls._type_.from_param(obj)

_BOXAA._fields_ = [
        ("n", ctypes.c_int32),
        ("nalloc", ctypes.c_int32),
        ("boxa", ctypes.POINTER(ctypes.POINTER(_BOXA)))
    ]

class BOXAA(with_metaclass(MetaPointer, LeptonObject)):
    _type_ = _BOXAA

    @classmethod
    def from_param(cls, obj):
        return cls._type_.from_param(obj)

_PTA._fields_ = [
        ("n", ctypes.c_int32),
        ("nalloc", ctypes.c_int32),
        ("refcount", ctypes.c_uint32),
        ("x", ctypes.POINTER(ctypes.c_float)),
        ("y", ctypes.POINTER(ctypes.c_float))
    ]

class PTA(with_metaclass(MetaPointer, LeptonObject)):
    _type_ = _PTA

    @classmethod
    def from_param(cls, obj):
        return cls._type_.from_param(obj)

_PTAA._fields_ = [
        ("n", ctypes.c_int32),
        ("nalloc", ctypes.c_int32),
        ("pta", ctypes.POINTER(ctypes.POINTER(_PTA)))
    ]

class PTAA(with_metaclass(MetaPointer, LeptonObject)):
    _type_ = _PTAA

    @classmethod
    def from_param(cls, obj):
        return cls._type_.from_param(obj)

_FPIX._fields_ = [
        ("w", ctypes.c_int32),
        ("h", ctypes.c_int32),
        ("wpl", ctypes.c_int32),
        ("refcount", ctypes.c_uint32),
        ("xres", ctypes.c_int32),
        ("yres", ctypes.c_int32),
        ("data", ctypes.POINTER(ctypes.c_float))
    ]

class FPIX(with_metaclass(MetaPointer, LeptonObject)):
    _type_ = _FPIX

    @classmethod
    def from_param(cls, obj):
        return cls._type_.from_param(obj)

_FPIXA._fields_ = [
        ("n", ctypes.c_int32),
        ("nalloc", ctypes.c_int32),
        ("refcount", ctypes.c_uint32),
        ("fpix", ctypes.POINTER(ctypes.POINTER(_FPIX)))
    ]

class FPIXA(with_metaclass(MetaPointer, LeptonObject)):
    _type_ = _FPIXA

    @classmethod
    def from_param(cls, obj):
        return cls._type_.from_param(obj)

_DPIX._fields_ = [
        ("w", ctypes.c_int32),
        ("h", ctypes.c_int32),
        ("wpl", ctypes.c_int32),
        ("refcount", ctypes.c_uint32),
        ("xres", ctypes.c_int32),
        ("yres", ctypes.c_int32),
        ("data", ctypes.POINTER(ctypes.c_double))
    ]

class DPIX(with_metaclass(MetaPointer, LeptonObject)):
    _type_ = _DPIX

    @classmethod
    def from_param(cls, obj):
        return cls._type_.from_param(obj)

_PIXCOMP._fields_ = [
        ("w", ctypes.c_int32),
        ("h", ctypes.c_int32),
        ("d", ctypes.c_int32),
        ("xres", ctypes.c_int32),
        ("yres", ctypes.c_int32),
        ("comptype", ctypes.c_int32),
        ("text", ctypes.POINTER(ctypes.c_char)),
        ("cmapflag", ctypes.c_int32),
        ("data", ctypes.POINTER(ctypes.c_ubyte)),
        ("size", ctypes.c_size_t)
    ]

class PIXCOMP(with_metaclass(MetaPointer, LeptonObject)):
    _type_ = _PIXCOMP

    @classmethod
    def from_param(cls, obj):
        return cls._type_.from_param(obj)

_PIXACOMP._fields_ = [
        ("n", ctypes.c_int32),
        ("nalloc", ctypes.c_int32),
        ("offset", ctypes.c_int32),
        ("pixc", ctypes.POINTER(ctypes.POINTER(_PIXCOMP))),
        ("boxa", ctypes.POINTER(_BOXA))
    ]

class PIXACOMP(with_metaclass(MetaPointer, LeptonObject)):
    _type_ = _PIXACOMP

    @classmethod
    def from_param(cls, obj):
        return cls._type_.from_param(obj)

_L_REGPARAMS._fields_ = [
        ("fp", ctypes.c_void_p),
        ("testname", ctypes.POINTER(ctypes.c_char)),
        ("tempfile", ctypes.POINTER(ctypes.c_char)),
        ("mode", ctypes.c_int32),
        ("index", ctypes.c_int32),
        ("success", ctypes.c_int32),
        ("display", ctypes.c_int32),
        ("tstart", ctypes.c_void_p)
    ]

class L_REGPARAMS(with_metaclass(MetaPointer, LeptonObject)):
    _type_ = _L_REGPARAMS

    @classmethod
    def from_param(cls, obj):
        return cls._type_.from_param(obj)

_L_HEAP._fields_ = [
        ("nalloc", ctypes.c_int32),
        ("n", ctypes.c_int32),
        ("array", ctypes.POINTER(ctypes.c_void_p)),
        ("direction", ctypes.c_int32)
    ]

class L_HEAP(with_metaclass(MetaPointer, LeptonObject)):
    _type_ = _L_HEAP

    @classmethod
    def from_param(cls, obj):
        return cls._type_.from_param(obj)

_L_PTRA._fields_ = [
        ("nalloc", ctypes.c_int32),
        ("imax", ctypes.c_int32),
        ("nactual", ctypes.c_int32),
        ("array", ctypes.POINTER(ctypes.c_void_p))
    ]

class L_PTRA(with_metaclass(MetaPointer, LeptonObject)):
    _type_ = _L_PTRA

    @classmethod
    def from_param(cls, obj):
        return cls._type_.from_param(obj)

_L_PTRAA._fields_ = [
        ("nalloc", ctypes.c_int32),
        ("ptra", ctypes.POINTER(ctypes.POINTER(_L_PTRA)))
    ]

class L_PTRAA(with_metaclass(MetaPointer, LeptonObject)):
    _type_ = _L_PTRAA

    @classmethod
    def from_param(cls, obj):
        return cls._type_.from_param(obj)

_L_STACK._fields_ = [
        ("nalloc", ctypes.c_int32),
        ("n", ctypes.c_int32),
        ("array", ctypes.POINTER(ctypes.c_void_p)),
        ("auxstack", ctypes.POINTER(_L_STACK))
    ]

class L_STACK(with_metaclass(MetaPointer, LeptonObject)):
    _type_ = _L_STACK

    @classmethod
    def from_param(cls, obj):
        return cls._type_.from_param(obj)

_BMP_FILEHEADER._fields_ = [
        ("bfType[2]", ctypes.c_ubyte),
        ("bfSize[4]", ctypes.c_ubyte),
        ("bfReserved1[2]", ctypes.c_ubyte),
        ("bfReserved2[2]", ctypes.c_ubyte),
        ("bfOffBits[4]", ctypes.c_ubyte)
    ]

class BMP_FILEHEADER(with_metaclass(MetaPointer, LeptonObject)):
    _type_ = _BMP_FILEHEADER

    @classmethod
    def from_param(cls, obj):
        return cls._type_.from_param(obj)

_BMP_INFOHEADER._fields_ = [
        ("biSize", ctypes.c_int32),
        ("biWidth", ctypes.c_int32),
        ("biHeight", ctypes.c_int32),
        ("biPlanes", ctypes.c_int16),
        ("biBitCount", ctypes.c_int16),
        ("biCompression", ctypes.c_int32),
        ("biSizeImage", ctypes.c_int32),
        ("biXPelsPerMeter", ctypes.c_int32),
        ("biYPelsPerMeter", ctypes.c_int32),
        ("biClrUsed", ctypes.c_int32),
        ("biClrImportant", ctypes.c_int32)
    ]

class BMP_INFOHEADER(with_metaclass(MetaPointer, LeptonObject)):
    _type_ = _BMP_INFOHEADER

    @classmethod
    def from_param(cls, obj):
        return cls._type_.from_param(obj)

_DOUBLELINKEDLIST._fields_ = [
        ("prev", ctypes.POINTER(_DOUBLELINKEDLIST)),
        ("next", ctypes.POINTER(_DOUBLELINKEDLIST)),
        ("data", ctypes.c_void_p)
    ]

class DOUBLELINKEDLIST(with_metaclass(MetaPointer, LeptonObject)):
    _type_ = _DOUBLELINKEDLIST

    @classmethod
    def from_param(cls, obj):
        return cls._type_.from_param(obj)

_L_QUEUE._fields_ = [
        ("nalloc", ctypes.c_int32),
        ("nhead", ctypes.c_int32),
        ("nelem", ctypes.c_int32),
        ("array", ctypes.POINTER(ctypes.c_void_p)),
        ("stack", ctypes.POINTER(_L_STACK))
    ]

class L_QUEUE(with_metaclass(MetaPointer, LeptonObject)):
    _type_ = _L_QUEUE

    @classmethod
    def from_param(cls, obj):
        return cls._type_.from_param(obj)

_L_SUDOKU._fields_ = [
        ("num", ctypes.c_int32),
        ("locs", ctypes.POINTER(ctypes.c_int32)),
        ("current", ctypes.c_int32),
        ("init", ctypes.POINTER(ctypes.c_int32)),
        ("state", ctypes.POINTER(ctypes.c_int32)),
        ("nguess", ctypes.c_int32),
        ("finished", ctypes.c_int32),
        ("failure", ctypes.c_int32)
    ]

class L_SUDOKU(with_metaclass(MetaPointer, LeptonObject)):
    _type_ = _L_SUDOKU

    @classmethod
    def from_param(cls, obj):
        return cls._type_.from_param(obj)

_RB_TYPE._fields_ = [
        ("itype", ctypes.c_int64),
        ("utype", ctypes.c_uint64),
        ("ftype", ctypes.c_double),
        ("ptype", ctypes.c_void_p)
    ]

class RB_TYPE(with_metaclass(MetaPointer, LeptonObject)):
    _type_ = _RB_TYPE

    @classmethod
    def from_param(cls, obj):
        return cls._type_.from_param(obj)

_L_RBTREE_NODE._fields_ = [
        ("key", _RB_TYPE),
        ("value", _RB_TYPE),
        ("left", ctypes.POINTER(_L_RBTREE_NODE)),
        ("right", ctypes.POINTER(_L_RBTREE_NODE)),
        ("parent", ctypes.POINTER(_L_RBTREE_NODE)),
        ("color", ctypes.c_int32)
    ]

class L_RBTREE_NODE(with_metaclass(MetaPointer, LeptonObject)):
    _type_ = _L_RBTREE_NODE

    @classmethod
    def from_param(cls, obj):
        return cls._type_.from_param(obj)

_L_COMPRESSED_DATA._fields_ = [
        ("type", ctypes.c_int32),
        ("datacomp", ctypes.POINTER(ctypes.c_ubyte)),
        ("nbytescomp", ctypes.c_size_t),
        ("data85", ctypes.POINTER(ctypes.c_char)),
        ("nbytes85", ctypes.c_size_t),
        ("cmapdata85", ctypes.POINTER(ctypes.c_char)),
        ("cmapdatahex", ctypes.POINTER(ctypes.c_char)),
        ("ncolors", ctypes.c_int32),
        ("w", ctypes.c_int32),
        ("h", ctypes.c_int32),
        ("bps", ctypes.c_int32),
        ("spp", ctypes.c_int32),
        ("minisblack", ctypes.c_int32),
        ("predictor", ctypes.c_int32),
        ("nbytes", ctypes.c_size_t),
        ("res", ctypes.c_int32)
    ]

class L_COMPRESSED_DATA(with_metaclass(MetaPointer, LeptonObject)):
    _type_ = _L_COMPRESSED_DATA

    @classmethod
    def from_param(cls, obj):
        return cls._type_.from_param(obj)

_L_PDF_DATA._fields_ = [
        ("title", ctypes.POINTER(ctypes.c_char)),
        ("n", ctypes.c_int32),
        ("ncmap", ctypes.c_int32),
        ("cida", ctypes.POINTER(_L_PTRA)),
        ("id", ctypes.POINTER(ctypes.c_char)),
        ("obj1", ctypes.POINTER(ctypes.c_char)),
        ("obj2", ctypes.POINTER(ctypes.c_char)),
        ("obj3", ctypes.POINTER(ctypes.c_char)),
        ("obj4", ctypes.POINTER(ctypes.c_char)),
        ("obj5", ctypes.POINTER(ctypes.c_char)),
        ("poststream", ctypes.POINTER(ctypes.c_char)),
        ("trailer", ctypes.POINTER(ctypes.c_char)),
        ("xy", ctypes.POINTER(_PTA)),
        ("wh", ctypes.POINTER(_PTA)),
        ("mediabox", ctypes.POINTER(_BOX)),
        ("saprex", ctypes.POINTER(_SARRAY)),
        ("sacmap", ctypes.POINTER(_SARRAY)),
        ("objsize", ctypes.POINTER(_L_DNA)),
        ("objloc", ctypes.POINTER(_L_DNA)),
        ("xrefloc", ctypes.c_int32)
    ]

class L_PDF_DATA(with_metaclass(MetaPointer, LeptonObject)):
    _type_ = _L_PDF_DATA

    @classmethod
    def from_param(cls, obj):
        return cls._type_.from_param(obj)

_L_RCH._fields_ = [
        ("index", ctypes.c_int32),
        ("score", ctypes.c_float),
        ("text", ctypes.POINTER(ctypes.c_char)),
        ("sample", ctypes.c_int32),
        ("xloc", ctypes.c_int32),
        ("yloc", ctypes.c_int32),
        ("width", ctypes.c_int32)
    ]

class L_RCH(with_metaclass(MetaPointer, LeptonObject)):
    _type_ = _L_RCH

    @classmethod
    def from_param(cls, obj):
        return cls._type_.from_param(obj)

_L_RCHA._fields_ = [
        ("naindex", ctypes.POINTER(_NUMA)),
        ("nascore", ctypes.POINTER(_NUMA)),
        ("satext", ctypes.POINTER(_SARRAY)),
        ("nasample", ctypes.POINTER(_NUMA)),
        ("naxloc", ctypes.POINTER(_NUMA)),
        ("nayloc", ctypes.POINTER(_NUMA)),
        ("nawidth", ctypes.POINTER(_NUMA))
    ]

class L_RCHA(with_metaclass(MetaPointer, LeptonObject)):
    _type_ = _L_RCHA

    @classmethod
    def from_param(cls, obj):
        return cls._type_.from_param(obj)

_L_STRCODE._fields_ = [
        ("fileno", ctypes.c_int32),
        ("ifunc", ctypes.c_int32),
        ("function", ctypes.POINTER(_SARRAY)),
        ("data", ctypes.POINTER(_SARRAY)),
        ("descr", ctypes.POINTER(_SARRAY)),
        ("n", ctypes.c_int32)
    ]

class L_STRCODE(with_metaclass(MetaPointer, LeptonObject)):
    _type_ = _L_STRCODE

    @classmethod
    def from_param(cls, obj):
        return cls._type_.from_param(obj)

_SEL._fields_ = [
        ("sy", ctypes.c_int32),
        ("sx", ctypes.c_int32),
        ("cy", ctypes.c_int32),
        ("cx", ctypes.c_int32),
        ("data", ctypes.POINTER(ctypes.POINTER(ctypes.c_int32))),
        ("name", ctypes.POINTER(ctypes.c_char))
    ]

class SEL(with_metaclass(MetaPointer, LeptonObject)):
    _type_ = _SEL

    @classmethod
    def from_param(cls, obj):
        return cls._type_.from_param(obj)

_SELA._fields_ = [
        ("n", ctypes.c_int32),
        ("nalloc", ctypes.c_int32),
        ("sel", ctypes.POINTER(ctypes.POINTER(_SEL)))
    ]

class SELA(with_metaclass(MetaPointer, LeptonObject)):
    _type_ = _SELA

    @classmethod
    def from_param(cls, obj):
        return cls._type_.from_param(obj)

_L_KERNEL._fields_ = [
        ("sy", ctypes.c_int32),
        ("sx", ctypes.c_int32),
        ("cy", ctypes.c_int32),
        ("cx", ctypes.c_int32),
        ("data", ctypes.POINTER(ctypes.POINTER(ctypes.c_float)))
    ]

class L_KERNEL(with_metaclass(MetaPointer, LeptonObject)):
    _type_ = _L_KERNEL

    @classmethod
    def from_param(cls, obj):
        return cls._type_.from_param(obj)

_PIX._fields_ = [
        ("w", ctypes.c_uint32),
        ("h", ctypes.c_uint32),
        ("d", ctypes.c_uint32),
        ("spp", ctypes.c_uint32),
        ("wpl", ctypes.c_uint32),
        ("refcount", ctypes.c_uint32),
        ("xres", ctypes.c_int32),
        ("yres", ctypes.c_int32),
        ("informat", ctypes.c_int32),
        ("special", ctypes.c_int32),
        ("text", ctypes.POINTER(ctypes.c_char)),
        ("colormap", ctypes.POINTER(_PIXCOLORMAP)),
        ("data", ctypes.POINTER(ctypes.c_uint32))
    ]

class PIX(with_metaclass(MetaPointer, LeptonObject)):
    _type_ = _PIX

    @classmethod
    def from_param(cls, obj):
        return cls._type_.from_param(obj)

_PIXA._fields_ = [
        ("n", ctypes.c_int32),
        ("nalloc", ctypes.c_int32),
        ("refcount", ctypes.c_uint32),
        ("pix", ctypes.POINTER(ctypes.POINTER(_PIX))),
        ("boxa", ctypes.POINTER(_BOXA))
    ]

class PIXA(with_metaclass(MetaPointer, LeptonObject)):
    _type_ = _PIXA

    @classmethod
    def from_param(cls, obj):
        return cls._type_.from_param(obj)

_PIXAA._fields_ = [
        ("n", ctypes.c_int32),
        ("nalloc", ctypes.c_int32),
        ("pixa", ctypes.POINTER(ctypes.POINTER(_PIXA))),
        ("boxa", ctypes.POINTER(_BOXA))
    ]

class PIXAA(with_metaclass(MetaPointer, LeptonObject)):
    _type_ = _PIXAA

    @classmethod
    def from_param(cls, obj):
        return cls._type_.from_param(obj)

_PIXACC._fields_ = [
        ("w", ctypes.c_int32),
        ("h", ctypes.c_int32),
        ("offset", ctypes.c_int32),
        ("pix", ctypes.POINTER(_PIX))
    ]

class PIXACC(with_metaclass(MetaPointer, LeptonObject)):
    _type_ = _PIXACC

    @classmethod
    def from_param(cls, obj):
        return cls._type_.from_param(obj)

_PIXTILING._fields_ = [
        ("pix", ctypes.POINTER(_PIX)),
        ("nx", ctypes.c_int32),
        ("ny", ctypes.c_int32),
        ("w", ctypes.c_int32),
        ("h", ctypes.c_int32),
        ("xoverlap", ctypes.c_int32),
        ("yoverlap", ctypes.c_int32),
        ("strip", ctypes.c_int32)
    ]

class PIXTILING(with_metaclass(MetaPointer, LeptonObject)):
    _type_ = _PIXTILING

    @classmethod
    def from_param(cls, obj):
        return cls._type_.from_param(obj)

_L_BMF._fields_ = [
        ("pixa", ctypes.POINTER(_PIXA)),
        ("size", ctypes.c_int32),
        ("directory", ctypes.POINTER(ctypes.c_char)),
        ("baseline1", ctypes.c_int32),
        ("baseline2", ctypes.c_int32),
        ("baseline3", ctypes.c_int32),
        ("lineheight", ctypes.c_int32),
        ("kernwidth", ctypes.c_int32),
        ("spacewidth", ctypes.c_int32),
        ("vertlinesep", ctypes.c_int32),
        ("fonttab", ctypes.POINTER(ctypes.c_int32)),
        ("baselinetab", ctypes.POINTER(ctypes.c_int32)),
        ("widthtab", ctypes.POINTER(ctypes.c_int32))
    ]

class L_BMF(with_metaclass(MetaPointer, LeptonObject)):
    _type_ = _L_BMF

    @classmethod
    def from_param(cls, obj):
        return cls._type_.from_param(obj)

_CCBORD._fields_ = [
        ("pix", ctypes.POINTER(_PIX)),
        ("boxa", ctypes.POINTER(_BOXA)),
        ("start", ctypes.POINTER(_PTA)),
        ("refcount", ctypes.c_int32),
        ("local", ctypes.POINTER(_PTAA)),
        ("global", ctypes.POINTER(_PTAA)),
        ("step", ctypes.POINTER(_NUMAA)),
        ("splocal", ctypes.POINTER(_PTA)),
        ("spglobal", ctypes.POINTER(_PTA))
    ]

class CCBORD(with_metaclass(MetaPointer, LeptonObject)):
    _type_ = _CCBORD

    @classmethod
    def from_param(cls, obj):
        return cls._type_.from_param(obj)

_CCBORDA._fields_ = [
        ("pix", ctypes.POINTER(_PIX)),
        ("w", ctypes.c_int32),
        ("h", ctypes.c_int32),
        ("n", ctypes.c_int32),
        ("nalloc", ctypes.c_int32),
        ("ccb", ctypes.POINTER(ctypes.POINTER(_CCBORD)))
    ]

class CCBORDA(with_metaclass(MetaPointer, LeptonObject)):
    _type_ = _CCBORDA

    @classmethod
    def from_param(cls, obj):
        return cls._type_.from_param(obj)

_JBCLASSER._fields_ = [
        ("safiles", ctypes.POINTER(_SARRAY)),
        ("method", ctypes.c_int32),
        ("components", ctypes.c_int32),
        ("maxwidth", ctypes.c_int32),
        ("maxheight", ctypes.c_int32),
        ("npages", ctypes.c_int32),
        ("baseindex", ctypes.c_int32),
        ("nacomps", ctypes.POINTER(_NUMA)),
        ("sizehaus", ctypes.c_int32),
        ("rankhaus", ctypes.c_float),
        ("thresh", ctypes.c_float),
        ("weightfactor", ctypes.c_float),
        ("naarea", ctypes.POINTER(_NUMA)),
        ("w", ctypes.c_int32),
        ("h", ctypes.c_int32),
        ("nclass", ctypes.c_int32),
        ("keep_pixaa", ctypes.c_int32),
        ("pixaa", ctypes.POINTER(_PIXAA)),
        ("pixat", ctypes.POINTER(_PIXA)),
        ("pixatd", ctypes.POINTER(_PIXA)),
        ("dahash", ctypes.POINTER(_L_DNAHASH)),
        ("nafgt", ctypes.POINTER(_NUMA)),
        ("ptac", ctypes.POINTER(_PTA)),
        ("ptact", ctypes.POINTER(_PTA)),
        ("naclass", ctypes.POINTER(_NUMA)),
        ("napage", ctypes.POINTER(_NUMA)),
        ("ptaul", ctypes.POINTER(_PTA)),
        ("ptall", ctypes.POINTER(_PTA))
    ]

class JBCLASSER(with_metaclass(MetaPointer, LeptonObject)):
    _type_ = _JBCLASSER

    @classmethod
    def from_param(cls, obj):
        return cls._type_.from_param(obj)

_JBDATA._fields_ = [
        ("pix", ctypes.POINTER(_PIX)),
        ("npages", ctypes.c_int32),
        ("w", ctypes.c_int32),
        ("h", ctypes.c_int32),
        ("nclass", ctypes.c_int32),
        ("latticew", ctypes.c_int32),
        ("latticeh", ctypes.c_int32),
        ("naclass", ctypes.POINTER(_NUMA)),
        ("napage", ctypes.POINTER(_NUMA)),
        ("ptaul", ctypes.POINTER(_PTA))
    ]

class JBDATA(with_metaclass(MetaPointer, LeptonObject)):
    _type_ = _JBDATA

    @classmethod
    def from_param(cls, obj):
        return cls._type_.from_param(obj)

_L_RBTREE._fields_ = [
        ("root", ctypes.POINTER(_L_RBTREE_NODE)),
        ("keytype", ctypes.c_int32)
    ]

class L_RBTREE(with_metaclass(MetaPointer, LeptonObject)):
    _type_ = _L_RBTREE

    @classmethod
    def from_param(cls, obj):
        return cls._type_.from_param(obj)

_L_BILATERAL._fields_ = [
        ("pixs", ctypes.POINTER(_PIX)),
        ("pixsc", ctypes.POINTER(_PIX)),
        ("reduction", ctypes.c_int32),
        ("spatial_stdev", ctypes.c_float),
        ("range_stdev", ctypes.c_float),
        ("spatial", ctypes.POINTER(ctypes.c_float)),
        ("range", ctypes.POINTER(ctypes.c_float)),
        ("minval", ctypes.c_int32),
        ("maxval", ctypes.c_int32),
        ("ncomps", ctypes.c_int32),
        ("nc", ctypes.POINTER(ctypes.c_int32)),
        ("kindex", ctypes.POINTER(ctypes.c_int32)),
        ("kfract", ctypes.POINTER(ctypes.c_float)),
        ("pixac", ctypes.POINTER(_PIXA)),
        ("lineset", ctypes.POINTER(ctypes.POINTER(ctypes.POINTER(ctypes.c_uint32))))
    ]

class L_BILATERAL(with_metaclass(MetaPointer, LeptonObject)):
    _type_ = _L_BILATERAL

    @classmethod
    def from_param(cls, obj):
        return cls._type_.from_param(obj)

_L_DEWARP._fields_ = [
        ("dewa", ctypes.POINTER(_L_DEWARPA)),
        ("pixs", ctypes.POINTER(_PIX)),
        ("sampvdispar", ctypes.POINTER(_FPIX)),
        ("samphdispar", ctypes.POINTER(_FPIX)),
        ("sampydispar", ctypes.POINTER(_FPIX)),
        ("fullvdispar", ctypes.POINTER(_FPIX)),
        ("fullhdispar", ctypes.POINTER(_FPIX)),
        ("fullydispar", ctypes.POINTER(_FPIX)),
        ("namidys", ctypes.POINTER(_NUMA)),
        ("nacurves", ctypes.POINTER(_NUMA)),
        ("w", ctypes.c_int32),
        ("h", ctypes.c_int32),
        ("pageno", ctypes.c_int32),
        ("sampling", ctypes.c_int32),
        ("redfactor", ctypes.c_int32),
        ("minlines", ctypes.c_int32),
        ("nlines", ctypes.c_int32),
        ("mincurv", ctypes.c_int32),
        ("maxcurv", ctypes.c_int32),
        ("leftslope", ctypes.c_int32),
        ("rightslope", ctypes.c_int32),
        ("leftcurv", ctypes.c_int32),
        ("rightcurv", ctypes.c_int32),
        ("nx", ctypes.c_int32),
        ("ny", ctypes.c_int32),
        ("hasref", ctypes.c_int32),
        ("refpage", ctypes.c_int32),
        ("vsuccess", ctypes.c_int32),
        ("hsuccess", ctypes.c_int32),
        ("ysuccess", ctypes.c_int32),
        ("vvalid", ctypes.c_int32),
        ("hvalid", ctypes.c_int32),
        ("skip_horiz", ctypes.c_int32),
        ("debug", ctypes.c_int32)
    ]

class L_DEWARP(with_metaclass(MetaPointer, LeptonObject)):
    _type_ = _L_DEWARP

    @classmethod
    def from_param(cls, obj):
        return cls._type_.from_param(obj)

_L_RDID._fields_ = [
        ("pixs", ctypes.POINTER(_PIX)),
        ("counta", ctypes.POINTER(ctypes.POINTER(ctypes.c_int32))),
        ("delya", ctypes.POINTER(ctypes.POINTER(ctypes.c_int32))),
        ("narray", ctypes.c_int32),
        ("size", ctypes.c_int32),
        ("setwidth", ctypes.POINTER(ctypes.c_int32)),
        ("nasum", ctypes.POINTER(_NUMA)),
        ("namoment", ctypes.POINTER(_NUMA)),
        ("fullarrays", ctypes.c_int32),
        ("beta", ctypes.POINTER(ctypes.c_float)),
        ("gamma", ctypes.POINTER(ctypes.c_float)),
        ("trellisscore", ctypes.POINTER(ctypes.c_float)),
        ("trellistempl", ctypes.POINTER(ctypes.c_int32)),
        ("natempl", ctypes.POINTER(_NUMA)),
        ("naxloc", ctypes.POINTER(_NUMA)),
        ("nadely", ctypes.POINTER(_NUMA)),
        ("nawidth", ctypes.POINTER(_NUMA)),
        ("boxa", ctypes.POINTER(_BOXA)),
        ("nascore", ctypes.POINTER(_NUMA)),
        ("natempl_r", ctypes.POINTER(_NUMA)),
        ("nasample_r", ctypes.POINTER(_NUMA)),
        ("naxloc_r", ctypes.POINTER(_NUMA)),
        ("nadely_r", ctypes.POINTER(_NUMA)),
        ("nawidth_r", ctypes.POINTER(_NUMA)),
        ("nascore_r", ctypes.POINTER(_NUMA))
    ]

class L_RDID(with_metaclass(MetaPointer, LeptonObject)):
    _type_ = _L_RDID

    @classmethod
    def from_param(cls, obj):
        return cls._type_.from_param(obj)

_L_WSHED._fields_ = [
        ("pixs", ctypes.POINTER(_PIX)),
        ("pixm", ctypes.POINTER(_PIX)),
        ("mindepth", ctypes.c_int32),
        ("pixlab", ctypes.POINTER(_PIX)),
        ("pixt", ctypes.POINTER(_PIX)),
        ("lines8", ctypes.POINTER(ctypes.c_void_p)),
        ("linem1", ctypes.POINTER(ctypes.c_void_p)),
        ("linelab32", ctypes.POINTER(ctypes.c_void_p)),
        ("linet1", ctypes.POINTER(ctypes.c_void_p)),
        ("pixad", ctypes.POINTER(_PIXA)),
        ("ptas", ctypes.POINTER(_PTA)),
        ("nasi", ctypes.POINTER(_NUMA)),
        ("nash", ctypes.POINTER(_NUMA)),
        ("namh", ctypes.POINTER(_NUMA)),
        ("nalevels", ctypes.POINTER(_NUMA)),
        ("nseeds", ctypes.c_int32),
        ("nother", ctypes.c_int32),
        ("lut", ctypes.POINTER(ctypes.c_int32)),
        ("links", ctypes.POINTER(ctypes.POINTER(_NUMA))),
        ("arraysize", ctypes.c_int32),
        ("debug", ctypes.c_int32)
    ]

class L_WSHED(with_metaclass(MetaPointer, LeptonObject)):
    _type_ = _L_WSHED

    @classmethod
    def from_param(cls, obj):
        return cls._type_.from_param(obj)

_L_COLORINFO._fields_ = [
        ("pixs", ctypes.POINTER(_PIX)),
        ("pixst", ctypes.POINTER(_PIX)),
        ("nx", ctypes.c_int32),
        ("ny", ctypes.c_int32),
        ("tw", ctypes.c_int32),
        ("th", ctypes.c_int32),
        ("minarea", ctypes.c_int32),
        ("boxas", ctypes.POINTER(_BOXA)),
        ("pixas", ctypes.POINTER(_PIXA)),
        ("pixam", ctypes.POINTER(_PIXA)),
        ("naa", ctypes.POINTER(_NUMAA)),
        ("dnaa", ctypes.POINTER(_L_DNAA)),
        ("pixadb", ctypes.POINTER(_PIXA))
    ]

class L_COLORINFO(with_metaclass(MetaPointer, LeptonObject)):
    _type_ = _L_COLORINFO

    @classmethod
    def from_param(cls, obj):
        return cls._type_.from_param(obj)

_L_DEWARPA._fields_ = [
        ("nalloc", ctypes.c_int32),
        ("maxpage", ctypes.c_int32),
        ("dewarp", ctypes.POINTER(ctypes.POINTER(_L_DEWARP))),
        ("dewarpcache", ctypes.POINTER(ctypes.POINTER(_L_DEWARP))),
        ("namodels", ctypes.POINTER(_NUMA)),
        ("napages", ctypes.POINTER(_NUMA)),
        ("redfactor", ctypes.c_int32),
        ("sampling", ctypes.c_int32),
        ("minlines", ctypes.c_int32),
        ("maxdist", ctypes.c_int32),
        ("max_linecurv", ctypes.c_int32),
        ("min_diff_linecurv", ctypes.c_int32),
        ("max_diff_linecurv", ctypes.c_int32),
        ("max_edgeslope", ctypes.c_int32),
        ("max_edgecurv", ctypes.c_int32),
        ("max_diff_edgecurv", ctypes.c_int32),
        ("useboth", ctypes.c_int32),
        ("check_columns", ctypes.c_int32),
        ("modelsready", ctypes.c_int32)
    ]

class L_DEWARPA(with_metaclass(MetaPointer, LeptonObject)):
    _type_ = _L_DEWARPA

    @classmethod
    def from_param(cls, obj):
        return cls._type_.from_param(obj)

_L_RECOG._fields_ = [
        ("scalew", ctypes.c_int32),
        ("scaleh", ctypes.c_int32),
        ("linew", ctypes.c_int32),
        ("templ_use", ctypes.c_int32),
        ("maxarraysize", ctypes.c_int32),
        ("setsize", ctypes.c_int32),
        ("threshold", ctypes.c_int32),
        ("maxyshift", ctypes.c_int32),
        ("charset_type", ctypes.c_int32),
        ("charset_size", ctypes.c_int32),
        ("min_nopad", ctypes.c_int32),
        ("num_samples", ctypes.c_int32),
        ("minwidth_u", ctypes.c_int32),
        ("maxwidth_u", ctypes.c_int32),
        ("minheight_u", ctypes.c_int32),
        ("maxheight_u", ctypes.c_int32),
        ("minwidth", ctypes.c_int32),
        ("maxwidth", ctypes.c_int32),
        ("ave_done", ctypes.c_int32),
        ("train_done", ctypes.c_int32),
        ("max_wh_ratio", ctypes.c_float),
        ("max_ht_ratio", ctypes.c_float),
        ("min_splitw", ctypes.c_int32),
        ("max_splith", ctypes.c_int32),
        ("sa_text", ctypes.POINTER(_SARRAY)),
        ("dna_tochar", ctypes.POINTER(_L_DNA)),
        ("centtab", ctypes.POINTER(ctypes.c_int32)),
        ("sumtab", ctypes.POINTER(ctypes.c_int32)),
        ("pixaa_u", ctypes.POINTER(_PIXAA)),
        ("ptaa_u", ctypes.POINTER(_PTAA)),
        ("naasum_u", ctypes.POINTER(_NUMAA)),
        ("pixaa", ctypes.POINTER(_PIXAA)),
        ("ptaa", ctypes.POINTER(_PTAA)),
        ("naasum", ctypes.POINTER(_NUMAA)),
        ("pixa_u", ctypes.POINTER(_PIXA)),
        ("pta_u", ctypes.POINTER(_PTA)),
        ("nasum_u", ctypes.POINTER(_NUMA)),
        ("pixa", ctypes.POINTER(_PIXA)),
        ("pta", ctypes.POINTER(_PTA)),
        ("nasum", ctypes.POINTER(_NUMA)),
        ("pixa_tr", ctypes.POINTER(_PIXA)),
        ("pixadb_ave", ctypes.POINTER(_PIXA)),
        ("pixa_id", ctypes.POINTER(_PIXA)),
        ("pixdb_ave", ctypes.POINTER(_PIX)),
        ("pixdb_range", ctypes.POINTER(_PIX)),
        ("pixadb_boot", ctypes.POINTER(_PIXA)),
        ("pixadb_split", ctypes.POINTER(_PIXA)),
        ("bmf", ctypes.POINTER(_L_BMF)),
        ("bmf_size", ctypes.c_int32),
        ("did", ctypes.POINTER(_L_RDID)),
        ("rch", ctypes.POINTER(_L_RCH)),
        ("rcha", ctypes.POINTER(_L_RCHA))
    ]

class L_RECOG(with_metaclass(MetaPointer, LeptonObject)):
    _type_ = _L_RECOG

    @classmethod
    def from_param(cls, obj):
        return cls._type_.from_param(obj)


L_BBUFFER = L_BYTEBUFFER
DLLIST = DOUBLELINKEDLIST
PIXCMAP = PIXCOLORMAP
BMP_FH = BMP_FILEHEADER
BMP_IH = BMP_INFOHEADER
L_AMAP = L_RBTREE
L_ASET = L_RBTREE
L_AMAP_NODE = L_RBTREE_NODE
L_ASET_NODE = L_RBTREE_NODE
PIXAC = PIXACOMP
PIXC = PIXCOMP

__all__ = ['L_BBUFFER', 'DLLIST', 'PIXCMAP', 'BMP_FH', 'BMP_IH', 'L_AMAP', 'L_ASET', 'L_AMAP_NODE', 'L_ASET_NODE', 'PIXAC', 'PIXC', 'L_DNAHASH', 'L_KERNEL', 'L_ASET_NODE', 'L_PTRA', 'PIXCOMP', 'CCBORDA', 'L_BBUFFER', 'RB_TYPE', 'L_COLORINFO', 'BMP_INFOHEADER', 'PTA', 'FPIXA', 'PIXA', 'L_RBTREE_NODE', 'L_DEWARP', 'PIXCMAP', 'L_COMPRESSED_DATA', 'GPLOT', 'PIXCOLORMAP', 'L_ASET', 'PIXC', 'BMP_FILEHEADER', 'BOXAA', 'BOXA', 'BMP_FH', 'SEL', 'DLLIST', 'L_BILATERAL', 'BMP_IH', 'L_PTRAA', 'PIXTILING', 'DOUBLELINKEDLIST', 'SELA', 'CCBORD', 'NUMA', 'PTAA', 'PIX', 'PIXACC', 'JBCLASSER', 'RGBA_QUAD', 'L_RBTREE', 'L_STACK', 'L_DEWARPA', 'L_RCHA', 'L_WSHED', 'PIXAA', 'BOX', 'L_BMF', 'L_BYTEBUFFER', 'L_REGPARAMS', 'PIXAC', 'L_RDID', 'L_BYTEA', 'L_SUDOKU', 'L_QUEUE', 'FPIX', 'L_PDF_DATA', 'L_DNAA', 'L_RCH', 'L_RECOG', 'L_HEAP', 'SARRAY', 'L_DNA', 'DPIX', 'L_STRCODE', 'PIXACOMP', 'NUMAA', 'JBDATA'] + ["LeptonObject"]

