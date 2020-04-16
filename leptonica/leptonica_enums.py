
# -*- coding: utf-8 -*-
# Author: João S. O. Bueno
# This is a generated file - do not edit!


from builtins import str
class Const(int):
    "Parent class to all constants"
    def __new__(cls, name, value, doc=""):
        self = int.__new__(cls, value)
        self.name = name
        self.doc = doc
        self.value = value 
        return self
    def __repr__(self):
        return self.name
    def __str__(self):
        return "%s = %s%s" % (self.name,self.value, ("  # " + self.doc) if self.doc else "")

def find_siblings(const, as_string=False):
    '''Helper function to locate blocks of related constants:
       i.e. the constants that used to live in the same "enum" in leptonica's C source files
    '''
    cls = const.__class__
    all_consts = [this_const for this_const in globals().values() if this_const.__class__ == cls]
    all_consts.sort()
    if not as_string:
        return all_consts
    return "\n".join(str(const) for const in all_consts)
    


class ConstType(Const):
    '''
        Numa Interpolation

------------------------------------------------------------------------
Array flags
------------------------------------------------------------------------
enum {
    L_LINEAR_INTERP = 1,        /*!< linear     */
    L_QUADRATIC_INTERP = 2      /*!< quadratic  */
}
    '''

ConstType.__name__ = "numa_interpolation"

L_LINEAR_INTERP = ConstType("L_LINEAR_INTERP", 1, '''< linear
 ''')
L_QUADRATIC_INTERP = ConstType("L_QUADRATIC_INTERP", 2, '''< quadratic
 ''')


del ConstType



class ConstType(Const):
    '''
        Border Adding
enum {
    L_CONTINUED_BORDER = 1,    /*!< extended with same value                  */
    L_SLOPE_BORDER = 2,        /*!< extended with constant normal derivative  */
    L_MIRRORED_BORDER = 3      /*!< mirrored                                  */
}
    '''

ConstType.__name__ = "border_adding"

L_CONTINUED_BORDER = ConstType("L_CONTINUED_BORDER", 1, '''< extended with same value
 ''')
L_SLOPE_BORDER = ConstType("L_SLOPE_BORDER", 2, '''< extended with constant normal derivative
 ''')
L_MIRRORED_BORDER = ConstType("L_MIRRORED_BORDER", 3, '''< mirrored
 ''')


del ConstType



class ConstType(Const):
    '''
        Numa Data Conversion
enum {
    L_INTEGER_VALUE = 1,        /*!< convert to integer  */
    L_FLOAT_VALUE = 2           /*!< convert to float    */
}
    '''

ConstType.__name__ = "numa_data_conversion"

L_INTEGER_VALUE = ConstType("L_INTEGER_VALUE", 1, '''< convert to integer
 ''')
L_FLOAT_VALUE = ConstType("L_FLOAT_VALUE", 2, '''< convert to float
 ''')


del ConstType



class ConstType(Const):
    '''
        Split Text

 Constants for deciding when text block is divided into paragraphs
enum {
    SPLIT_ON_LEADING_WHITE = 1,    /*!< tab or space at beginning of line   */
    SPLIT_ON_BLANK_LINE    = 2,    /*!< newline with optional white space   */
    SPLIT_ON_BOTH          = 3     /*!< leading white space or newline      */
}
    '''

ConstType.__name__ = "split_text"

SPLIT_ON_LEADING_WHITE = ConstType("SPLIT_ON_LEADING_WHITE", 1, '''< tab or space at beginning of line
 ''')
SPLIT_ON_BLANK_LINE = ConstType("SPLIT_ON_BLANK_LINE", 2, '''< newline with optional white space
 ''')
SPLIT_ON_BOTH = ConstType("SPLIT_ON_BOTH", 3, '''< leading white space or newline
 ''')


del ConstType



class ConstType(Const):
    '''
        CCB Coords

 Use in ccbaStepChainsToPixCoords()
enum {
      CCB_LOCAL_COORDS = 1,
      CCB_GLOBAL_COORDS = 2
}
    '''

ConstType.__name__ = "ccb_coords"

CCB_LOCAL_COORDS = ConstType("CCB_LOCAL_COORDS", 1, ''' ''')
CCB_GLOBAL_COORDS = ConstType("CCB_GLOBAL_COORDS", 2, ''' ''')


del ConstType



class ConstType(Const):
    '''
        CCB Points

 Use in ccbaGenerateSPGlobalLocs()
enum {
      CCB_SAVE_ALL_PTS = 1,
      CCB_SAVE_TURNING_PTS = 2
}
    '''

ConstType.__name__ = "ccb_points"

CCB_SAVE_ALL_PTS = ConstType("CCB_SAVE_ALL_PTS", 1, ''' ''')
CCB_SAVE_TURNING_PTS = ConstType("CCB_SAVE_TURNING_PTS", 2, ''' ''')


del ConstType



class ConstType(Const):
    '''
        Search State

------------------------------------------------------------------------
Simple search state variables
------------------------------------------------------------------------
enum {
    L_NOT_FOUND = 0,
    L_FOUND = 1
}
    '''

ConstType.__name__ = "search_state"

L_NOT_FOUND = ConstType("L_NOT_FOUND", 0, ''' ''')
L_FOUND = ConstType("L_FOUND", 1, ''' ''')


del ConstType



class ConstType(Const):
    '''
        Path Separators

------------------------------------------------------------------------
Path separator conversion
------------------------------------------------------------------------
enum {
    UNIX_PATH_SEPCHAR = 0,
    WIN_PATH_SEPCHAR = 1
}
    '''

ConstType.__name__ = "path_separators"

UNIX_PATH_SEPCHAR = ConstType("UNIX_PATH_SEPCHAR", 0, ''' ''')
WIN_PATH_SEPCHAR = ConstType("WIN_PATH_SEPCHAR", 1, ''' ''')


del ConstType



class ConstType(Const):
    '''
        Message Control

 Control printing of error, warning and info messages
enum {
    L_SEVERITY_EXTERNAL = 0,   /* Get the severity from the environment   */
    L_SEVERITY_ALL      = 1,   /* Lowest severity: print all messages     */
    L_SEVERITY_DEBUG    = 2,   /* Print debugging and higher messages     */
    L_SEVERITY_INFO     = 3,   /* Print informational and higher messages */
    L_SEVERITY_WARNING  = 4,   /* Print warning and higher messages       */
    L_SEVERITY_ERROR    = 5,   /* Print error and higher messages         */
    L_SEVERITY_NONE     = 6    /* Highest severity: print no messages     */
}
    '''

ConstType.__name__ = "message_control"

L_SEVERITY_EXTERNAL = ConstType("L_SEVERITY_EXTERNAL", 0, '''Get the severity from the environment
 ''')
L_SEVERITY_ALL = ConstType("L_SEVERITY_ALL", 1, '''Lowest severity: print all messages
 ''')
L_SEVERITY_DEBUG = ConstType("L_SEVERITY_DEBUG", 2, '''Print debugging and higher messages
 ''')
L_SEVERITY_INFO = ConstType("L_SEVERITY_INFO", 3, '''Print informational and higher messages
 ''')
L_SEVERITY_WARNING = ConstType("L_SEVERITY_WARNING", 4, '''Print warning and higher messages
 ''')
L_SEVERITY_ERROR = ConstType("L_SEVERITY_ERROR", 5, '''Print error and higher messages
 ''')
L_SEVERITY_NONE = ConstType("L_SEVERITY_NONE", 6, '''Highest severity: print no messages
 ''')


del ConstType



class ConstType(Const):
    '''
       enum GPLOT_STYLE {
    GPLOT_LINES       = 0,
    GPLOT_POINTS      = 1,
    GPLOT_IMPULSES    = 2,
    GPLOT_LINESPOINTS = 3,
    GPLOT_DOTS        = 4
}
    '''

ConstType.__name__ = "generated_constants"

GPLOT_LINES = ConstType("GPLOT_LINES", 0, ''' ''')
GPLOT_POINTS = ConstType("GPLOT_POINTS", 1, ''' ''')
GPLOT_IMPULSES = ConstType("GPLOT_IMPULSES", 2, ''' ''')
GPLOT_LINESPOINTS = ConstType("GPLOT_LINESPOINTS", 3, ''' ''')
GPLOT_DOTS = ConstType("GPLOT_DOTS", 4, ''' ''')


del ConstType



class ConstType(Const):
    '''
       enum GPLOT_OUTPUT {
    GPLOT_NONE  = 0,
    GPLOT_PNG   = 1,
    GPLOT_PS    = 2,
    GPLOT_EPS   = 3,
    GPLOT_LATEX = 4,
    GPLOT_PNM   = 5,
}
    '''

ConstType.__name__ = "generated_constants"

GPLOT_NONE = ConstType("GPLOT_NONE", 0, ''' ''')
GPLOT_PNG = ConstType("GPLOT_PNG", 1, ''' ''')
GPLOT_PS = ConstType("GPLOT_PS", 2, ''' ''')
GPLOT_EPS = ConstType("GPLOT_EPS", 3, ''' ''')
GPLOT_LATEX = ConstType("GPLOT_LATEX", 4, ''' ''')
GPLOT_PNM = ConstType("GPLOT_PNM", 5, ''' ''')


del ConstType



class ConstType(Const):
    '''
       enum GPLOT_SCALING {
    GPLOT_LINEAR_SCALE  = 0,   /*!< default */
    GPLOT_LOG_SCALE_X   = 1,
    GPLOT_LOG_SCALE_Y   = 2,
    GPLOT_LOG_SCALE_X_Y = 3
}
    '''

ConstType.__name__ = "generated_constants"

GPLOT_LINEAR_SCALE = ConstType("GPLOT_LINEAR_SCALE", 0, '''< default
 ''')
GPLOT_LOG_SCALE_X = ConstType("GPLOT_LOG_SCALE_X", 1, ''' ''')
GPLOT_LOG_SCALE_Y = ConstType("GPLOT_LOG_SCALE_Y", 2, ''' ''')
GPLOT_LOG_SCALE_X_Y = ConstType("GPLOT_LOG_SCALE_X_Y", 3, ''' ''')


del ConstType



class ConstType(Const):
    '''
        Image Formats

The IFF_DEFAULT flag is used to write the file out in the
same (input) file format that the pix was read from.  If the pix
was not read from file, the input format field will be
IFF_UNKNOWN and the output file format will be chosen to
be compressed and lossless; namely, IFF_TIFF_G4 for d = 1
and IFF_PNG for everything else.

In the future, new format types that have defined extensions
will be added before IFF_DEFAULT, and will be kept in sync with
the file format extensions in writefile.c.  The positions of
file formats before IFF_DEFAULT will remain invariant.
enum {
    IFF_UNKNOWN        = 0,
    IFF_BMP            = 1,
    IFF_JFIF_JPEG      = 2,
    IFF_PNG            = 3,
    IFF_TIFF           = 4,
    IFF_TIFF_PACKBITS  = 5,
    IFF_TIFF_RLE       = 6,
    IFF_TIFF_G3        = 7,
    IFF_TIFF_G4        = 8,
    IFF_TIFF_LZW       = 9,
    IFF_TIFF_ZIP       = 10,
    IFF_PNM            = 11,
    IFF_PS             = 12,
    IFF_GIF            = 13,
    IFF_JP2            = 14,
    IFF_WEBP           = 15,
    IFF_LPDF           = 16,
    IFF_TIFF_JPEG      = 17,
    IFF_DEFAULT        = 18,
    IFF_SPIX           = 19
}
    '''

ConstType.__name__ = "image_formats"

IFF_UNKNOWN = ConstType("IFF_UNKNOWN", 0, ''' ''')
IFF_BMP = ConstType("IFF_BMP", 1, ''' ''')
IFF_JFIF_JPEG = ConstType("IFF_JFIF_JPEG", 2, ''' ''')
IFF_PNG = ConstType("IFF_PNG", 3, ''' ''')
IFF_TIFF = ConstType("IFF_TIFF", 4, ''' ''')
IFF_TIFF_PACKBITS = ConstType("IFF_TIFF_PACKBITS", 5, ''' ''')
IFF_TIFF_RLE = ConstType("IFF_TIFF_RLE", 6, ''' ''')
IFF_TIFF_G3 = ConstType("IFF_TIFF_G3", 7, ''' ''')
IFF_TIFF_G4 = ConstType("IFF_TIFF_G4", 8, ''' ''')
IFF_TIFF_LZW = ConstType("IFF_TIFF_LZW", 9, ''' ''')
IFF_TIFF_ZIP = ConstType("IFF_TIFF_ZIP", 10, ''' ''')
IFF_PNM = ConstType("IFF_PNM", 11, ''' ''')
IFF_PS = ConstType("IFF_PS", 12, ''' ''')
IFF_GIF = ConstType("IFF_GIF", 13, ''' ''')
IFF_JP2 = ConstType("IFF_JP2", 14, ''' ''')
IFF_WEBP = ConstType("IFF_WEBP", 15, ''' ''')
IFF_LPDF = ConstType("IFF_LPDF", 16, ''' ''')
IFF_TIFF_JPEG = ConstType("IFF_TIFF_JPEG", 17, ''' ''')
IFF_DEFAULT = ConstType("IFF_DEFAULT", 18, ''' ''')
IFF_SPIX = ConstType("IFF_SPIX", 19, ''' ''')


del ConstType



class ConstType(Const):
    '''
        Header Ids

---------------------------------------------------------------
Format header ids
---------------------------------------------------------------
enum {
    BMP_ID             = 0x4d42,     /*!< BM - for bitmaps    */
    TIFF_BIGEND_ID     = 0x4d4d,     /*!< MM - for 'motorola' */
    TIFF_LITTLEEND_ID  = 0x4949      /*!< II - for 'intel'    */
}
    '''

ConstType.__name__ = "header_ids"

BMP_ID = ConstType("BMP_ID", 19778, '''< BM - for bitmaps
 ''')
TIFF_BIGEND_ID = ConstType("TIFF_BIGEND_ID", 19789, '''< MM - for 'motorola'
 ''')
TIFF_LITTLEEND_ID = ConstType("TIFF_LITTLEEND_ID", 18761, '''< II - for 'intel'
 ''')


del ConstType



class ConstType(Const):
    '''
        Jpeg Hints

---------------------------------------------------------------
Hinting bit flags in jpeg reader
---------------------------------------------------------------
enum {
    L_JPEG_READ_LUMINANCE = 1,   /*!< only want luminance data; no chroma */
    L_JPEG_FAIL_ON_BAD_DATA = 2  /*!< don't return possibly damaged pix */
}
    '''

ConstType.__name__ = "jpeg_hints"

L_JPEG_READ_LUMINANCE = ConstType("L_JPEG_READ_LUMINANCE", 1, '''< only want luminance data; no chroma
 ''')
L_JPEG_FAIL_ON_BAD_DATA = ConstType("L_JPEG_FAIL_ON_BAD_DATA", 2, '''< don't return possibly damaged pix
 ''')


del ConstType



class ConstType(Const):
    '''
        Pdf Encoding

---------------------------------------------------------------
Pdf formatted encoding types
---------------------------------------------------------------
enum {
    L_DEFAULT_ENCODE  = 0,  /*!< use default encoding based on image        */
    L_JPEG_ENCODE     = 1,  /*!< use dct encoding: 8 and 32 bpp, no cmap    */
    L_G4_ENCODE       = 2,  /*!< use ccitt g4 fax encoding: 1 bpp           */
    L_FLATE_ENCODE    = 3,  /*!< use flate encoding: any depth, cmap ok     */
    L_JP2K_ENCODE     = 4   /*!< use jp2k encoding: 8 and 32 bpp, no cmap   */
}
    '''

ConstType.__name__ = "pdf_encoding"

L_DEFAULT_ENCODE = ConstType("L_DEFAULT_ENCODE", 0, '''< use default encoding based on image
 ''')
L_JPEG_ENCODE = ConstType("L_JPEG_ENCODE", 1, '''< use dct encoding: 8 and 32 bpp, no cmap
 ''')
L_G4_ENCODE = ConstType("L_G4_ENCODE", 2, '''< use ccitt g4 fax encoding: 1 bpp
 ''')
L_FLATE_ENCODE = ConstType("L_FLATE_ENCODE", 3, '''< use flate encoding: any depth, cmap ok
 ''')
L_JP2K_ENCODE = ConstType("L_JP2K_ENCODE", 4, '''< use jp2k encoding: 8 and 32 bpp, no cmap
 ''')


del ConstType



class ConstType(Const):
    '''
        Pdf MultiImage

-------------------------------------------------------------------------
Pdf multi image flags
-------------------------------------------------------------------------
enum {
    L_FIRST_IMAGE   = 1,    /*!< first image to be used                      */
    L_NEXT_IMAGE    = 2,    /*!< intermediate image; not first or last       */
    L_LAST_IMAGE    = 3     /*!< last image to be used                       */
}
    '''

ConstType.__name__ = "pdf_multiimage"

L_FIRST_IMAGE = ConstType("L_FIRST_IMAGE", 1, '''< first image to be used
 ''')
L_NEXT_IMAGE = ConstType("L_NEXT_IMAGE", 2, '''< intermediate image; not first or last
 ''')
L_LAST_IMAGE = ConstType("L_LAST_IMAGE", 3, '''< last image to be used
 ''')


del ConstType



class ConstType(Const):
    '''
        JB Classifier
enum {
    JB_RANKHAUS = 0,
    JB_CORRELATION = 1
}
    '''

ConstType.__name__ = "jb_classifier"

JB_RANKHAUS = ConstType("JB_RANKHAUS", 0, ''' ''')
JB_CORRELATION = ConstType("JB_CORRELATION", 1, ''' ''')


del ConstType



class ConstType(Const):
    '''
        JB Component

 For jbGetComponents(): type of component to extract from images
enum {
    JB_CONN_COMPS = 0,
    JB_CHARACTERS = 1,
    JB_WORDS = 2
}
    '''

ConstType.__name__ = "jb_component"

JB_CONN_COMPS = ConstType("JB_CONN_COMPS", 0, ''' ''')
JB_CHARACTERS = ConstType("JB_CHARACTERS", 1, ''' ''')
JB_WORDS = ConstType("JB_WORDS", 2, ''' ''')


del ConstType



class ConstType(Const):
    '''
        Morph Boundary

-------------------------------------------------------------------------
Morphological boundary condition flags

Two types of boundary condition for erosion.
The global variable MORPH_BC takes on one of these two values.
See notes in morph.c for usage.
-------------------------------------------------------------------------
enum {
    SYMMETRIC_MORPH_BC = 0,
    ASYMMETRIC_MORPH_BC = 1
}
    '''

ConstType.__name__ = "morph_boundary"

SYMMETRIC_MORPH_BC = ConstType("SYMMETRIC_MORPH_BC", 0, ''' ''')
ASYMMETRIC_MORPH_BC = ConstType("ASYMMETRIC_MORPH_BC", 1, ''' ''')


del ConstType



class ConstType(Const):
    '''
        SEL Vals

-------------------------------------------------------------------------
Structuring element vals
-------------------------------------------------------------------------
enum {
    SEL_DONT_CARE  = 0,
    SEL_HIT        = 1,
    SEL_MISS       = 2
}
    '''

ConstType.__name__ = "sel_vals"

SEL_DONT_CARE = ConstType("SEL_DONT_CARE", 0, ''' ''')
SEL_HIT = ConstType("SEL_HIT", 1, ''' ''')
SEL_MISS = ConstType("SEL_MISS", 2, ''' ''')


del ConstType



class ConstType(Const):
    '''
        Runlength Polarity

-------------------------------------------------------------------------
Runlength flags for granulometry
-------------------------------------------------------------------------
enum {
    L_RUN_OFF = 0,
    L_RUN_ON  = 1
}
    '''

ConstType.__name__ = "runlength_polarity"

L_RUN_OFF = ConstType("L_RUN_OFF", 0, ''' ''')
L_RUN_ON = ConstType("L_RUN_ON", 1, ''' ''')


del ConstType



class ConstType(Const):
    '''
        Direction Flags

-------------------------------------------------------------------------
Direction flags for grayscale morphology, granulometry,
composable Sels, convolution, etc.
-------------------------------------------------------------------------
enum {
    L_HORIZ            = 1,
    L_VERT             = 2,
    L_BOTH_DIRECTIONS  = 3
}
    '''

ConstType.__name__ = "direction_flags"

L_HORIZ = ConstType("L_HORIZ", 1, ''' ''')
L_VERT = ConstType("L_VERT", 2, ''' ''')
L_BOTH_DIRECTIONS = ConstType("L_BOTH_DIRECTIONS", 3, ''' ''')


del ConstType



class ConstType(Const):
    '''
        Morph Operator

-------------------------------------------------------------------------
Morphological operation flags
-------------------------------------------------------------------------
enum {
    L_MORPH_DILATE    = 1,
    L_MORPH_ERODE     = 2,
    L_MORPH_OPEN      = 3,
    L_MORPH_CLOSE     = 4,
    L_MORPH_HMT       = 5
}
    '''

ConstType.__name__ = "morph_operator"

L_MORPH_DILATE = ConstType("L_MORPH_DILATE", 1, ''' ''')
L_MORPH_ERODE = ConstType("L_MORPH_ERODE", 2, ''' ''')
L_MORPH_OPEN = ConstType("L_MORPH_OPEN", 3, ''' ''')
L_MORPH_CLOSE = ConstType("L_MORPH_CLOSE", 4, ''' ''')
L_MORPH_HMT = ConstType("L_MORPH_HMT", 5, ''' ''')


del ConstType



class ConstType(Const):
    '''
        Pixel Value Scaling

-------------------------------------------------------------------------
Grayscale intensity scaling flags
-------------------------------------------------------------------------
enum {
    L_LINEAR_SCALE  = 1,
    L_LOG_SCALE     = 2
}
    '''

ConstType.__name__ = "pixel_value_scaling"

L_LINEAR_SCALE = ConstType("L_LINEAR_SCALE", 1, ''' ''')
L_LOG_SCALE = ConstType("L_LOG_SCALE", 2, ''' ''')


del ConstType



class ConstType(Const):
    '''
        Morph Tophat

-------------------------------------------------------------------------
Morphological tophat flags
-------------------------------------------------------------------------
enum {
    L_TOPHAT_WHITE = 0,
    L_TOPHAT_BLACK = 1
}
    '''

ConstType.__name__ = "morph_tophat"

L_TOPHAT_WHITE = ConstType("L_TOPHAT_WHITE", 0, ''' ''')
L_TOPHAT_BLACK = ConstType("L_TOPHAT_BLACK", 1, ''' ''')


del ConstType



class ConstType(Const):
    '''
        ArithLogical Ops

-------------------------------------------------------------------------
Arithmetic and logical operator flags
(use on grayscale images and Numas)
-------------------------------------------------------------------------
enum {
    L_ARITH_ADD       = 1,
    L_ARITH_SUBTRACT  = 2,
    L_ARITH_MULTIPLY  = 3,   /* on numas only */
    L_ARITH_DIVIDE    = 4,   /* on numas only */
    L_UNION           = 5,   /* on numas only */
    L_INTERSECTION    = 6,   /* on numas only */
    L_SUBTRACTION     = 7,   /* on numas only */
    L_EXCLUSIVE_OR    = 8    /* on numas only */
}
    '''

ConstType.__name__ = "arithlogical_ops"

L_ARITH_ADD = ConstType("L_ARITH_ADD", 1, ''' ''')
L_ARITH_SUBTRACT = ConstType("L_ARITH_SUBTRACT", 2, ''' ''')
L_ARITH_MULTIPLY = ConstType("L_ARITH_MULTIPLY", 3, '''on numas only
 ''')
L_ARITH_DIVIDE = ConstType("L_ARITH_DIVIDE", 4, '''on numas only
 ''')
L_UNION = ConstType("L_UNION", 5, '''on numas only
 ''')
L_INTERSECTION = ConstType("L_INTERSECTION", 6, '''on numas only
 ''')
L_SUBTRACTION = ConstType("L_SUBTRACTION", 7, '''on numas only
 ''')
L_EXCLUSIVE_OR = ConstType("L_EXCLUSIVE_OR", 8, '''on numas only
 ''')


del ConstType



class ConstType(Const):
    '''
        MinMax Selection

-------------------------------------------------------------------------
Min/max selection flags
-------------------------------------------------------------------------
enum {
    L_CHOOSE_MIN = 1,         /* useful in a downscaling "erosion"       */
    L_CHOOSE_MAX = 2,         /* useful in a downscaling "dilation"      */
    L_CHOOSE_MAXDIFF = 3,     /* useful in a downscaling contrast        */
    L_CHOOSE_MIN_BOOST = 4,   /* use a modification of the min value     */
    L_CHOOSE_MAX_BOOST = 5    /* use a modification of the max value     */
}
    '''

ConstType.__name__ = "minmax_selection"

L_CHOOSE_MIN = ConstType("L_CHOOSE_MIN", 1, '''useful in a downscaling "erosion"
 ''')
L_CHOOSE_MAX = ConstType("L_CHOOSE_MAX", 2, '''useful in a downscaling "dilation"
 ''')
L_CHOOSE_MAXDIFF = ConstType("L_CHOOSE_MAXDIFF", 3, '''useful in a downscaling contrast
 ''')
L_CHOOSE_MIN_BOOST = ConstType("L_CHOOSE_MIN_BOOST", 4, '''use a modification of the min value
 ''')
L_CHOOSE_MAX_BOOST = ConstType("L_CHOOSE_MAX_BOOST", 5, '''use a modification of the max value
 ''')


del ConstType



class ConstType(Const):
    '''
        Exterior Value

-------------------------------------------------------------------------
Exterior value b.c. for distance function flags
-------------------------------------------------------------------------
enum {
    L_BOUNDARY_BG = 1,  /* assume bg outside image */
    L_BOUNDARY_FG = 2   /* assume fg outside image */
}
    '''

ConstType.__name__ = "exterior_value"

L_BOUNDARY_BG = ConstType("L_BOUNDARY_BG", 1, '''assume bg outside image
 ''')
L_BOUNDARY_FG = ConstType("L_BOUNDARY_FG", 2, '''assume fg outside image
 ''')


del ConstType



class ConstType(Const):
    '''
        Image Comparison

-------------------------------------------------------------------------
Image comparison flags
-------------------------------------------------------------------------
enum {
    L_COMPARE_XOR = 1,
    L_COMPARE_SUBTRACT = 2,
    L_COMPARE_ABS_DIFF = 3
}
    '''

ConstType.__name__ = "image_comparison"

L_COMPARE_XOR = ConstType("L_COMPARE_XOR", 1, ''' ''')
L_COMPARE_SUBTRACT = ConstType("L_COMPARE_SUBTRACT", 2, ''' ''')
L_COMPARE_ABS_DIFF = ConstType("L_COMPARE_ABS_DIFF", 3, ''' ''')


del ConstType



class ConstType(Const):
    '''
        RGBA Color

<pre>
Notes:
(1) These are the byte indices for colors in 32 bpp images.
They are used through the GET/SET_DATA_BYTE accessors.
The 4th byte, typically known as the "alpha channel" and used
for blending, is used to a small extent in leptonica.
(2) Do not change these values!  If you redefine them, functions
that have the shifts hardcoded for efficiency and conciseness
(instead of using the constants below) will break.  These
functions are labelled with "***"  next to their names at
the top of the files in which they are defined.
(3) The shifts to extract the red, green, blue and alpha components
from a 32 bit pixel are defined here.
</pre>
enum {
    COLOR_RED = 0,        /*!< red color index in RGBA_QUAD    */
    COLOR_GREEN = 1,      /*!< green color index in RGBA_QUAD  */
    COLOR_BLUE = 2,       /*!< blue color index in RGBA_QUAD   */
    L_ALPHA_CHANNEL = 3   /*!< alpha value index in RGBA_QUAD  */
}
    '''

ConstType.__name__ = "rgba_color"

COLOR_RED = ConstType("COLOR_RED", 0, '''< red color index in RGBA_QUAD
 ''')
COLOR_GREEN = ConstType("COLOR_GREEN", 1, '''< green color index in RGBA_QUAD
 ''')
COLOR_BLUE = ConstType("COLOR_BLUE", 2, '''< blue color index in RGBA_QUAD
 ''')
L_ALPHA_CHANNEL = ConstType("L_ALPHA_CHANNEL", 3, '''< alpha value index in RGBA_QUAD
 ''')


del ConstType



class ConstType(Const):
    '''
        Box Color

-------------------------------------------------------------------------
Colors for drawing boxes
-------------------------------------------------------------------------
enum {
    L_DRAW_RED = 0,         /*!< draw in red                   */
    L_DRAW_GREEN = 1,       /*!< draw in green                 */
    L_DRAW_BLUE = 2,        /*!< draw in blue                  */
    L_DRAW_SPECIFIED = 3,   /*!< draw specified color          */
    L_DRAW_RGB = 4,         /*!< draw as sequence of r,g,b     */
    L_DRAW_RANDOM = 5       /*!< draw randomly chosen colors   */
}
    '''

ConstType.__name__ = "box_color"

L_DRAW_RED = ConstType("L_DRAW_RED", 0, '''< draw in red
 ''')
L_DRAW_GREEN = ConstType("L_DRAW_GREEN", 1, '''< draw in green
 ''')
L_DRAW_BLUE = ConstType("L_DRAW_BLUE", 2, '''< draw in blue
 ''')
L_DRAW_SPECIFIED = ConstType("L_DRAW_SPECIFIED", 3, '''< draw specified color
 ''')
L_DRAW_RGB = ConstType("L_DRAW_RGB", 4, '''< draw as sequence of r,g,b
 ''')
L_DRAW_RANDOM = ConstType("L_DRAW_RANDOM", 5, '''< draw randomly chosen colors
 ''')


del ConstType



class ConstType(Const):
    '''
        Cmap Conversion

-------------------------------------------------------------------------
Flags for colormap conversion
-------------------------------------------------------------------------
enum {
    REMOVE_CMAP_TO_BINARY = 0,     /*!< remove colormap for conv to 1 bpp  */
    REMOVE_CMAP_TO_GRAYSCALE = 1,  /*!< remove colormap for conv to 8 bpp  */
    REMOVE_CMAP_TO_FULL_COLOR = 2, /*!< remove colormap for conv to 32 bpp */
    REMOVE_CMAP_WITH_ALPHA = 3,    /*!< remove colormap and alpha          */
    REMOVE_CMAP_BASED_ON_SRC = 4   /*!< remove depending on src format     */
}
    '''

ConstType.__name__ = "cmap_conversion"

REMOVE_CMAP_TO_BINARY = ConstType("REMOVE_CMAP_TO_BINARY", 0, '''< remove colormap for conv to 1 bpp
 ''')
REMOVE_CMAP_TO_GRAYSCALE = ConstType("REMOVE_CMAP_TO_GRAYSCALE", 1, '''< remove colormap for conv to 8 bpp
 ''')
REMOVE_CMAP_TO_FULL_COLOR = ConstType("REMOVE_CMAP_TO_FULL_COLOR", 2, '''< remove colormap for conv to 32 bpp
 ''')
REMOVE_CMAP_WITH_ALPHA = ConstType("REMOVE_CMAP_WITH_ALPHA", 3, '''< remove colormap and alpha
 ''')
REMOVE_CMAP_BASED_ON_SRC = ConstType("REMOVE_CMAP_BASED_ON_SRC", 4, '''< remove depending on src format
 ''')


del ConstType



class ConstType(Const):
    '''
        Object Access

<pre>
For Pix, Box, Pta and Numa, there are 3 standard methods for handling
the retrieval or insertion of a struct:
(1) direct insertion (Don't do this if there is another handle
somewhere to this same struct!)
(2) copy (Always safe, sets up a refcount of 1 on the new object.
Can be undesirable if very large, such as an image or
an array of images.)
(3) clone (Makes another handle to the same struct, and bumps the
refcount up by 1.  OK to use except in two situations:
(a) You change data through one of the handles but don't
want those changes to be seen by the other handle.
(b) The application is multi-threaded.  Because the clone
operation is not atomic (e.g., locked with a mutex),
it is possible to end up with an incorrect ref count,
causing either a memory leak or a crash.

For Pixa and Boxa, which are structs that hold an array of clonable
structs, there is an additional method:
(4) copy-clone (Makes a new higher-level struct with a refcount
of 1, but clones all the structs in the array.)

Unlike the other structs, when retrieving a string from an Sarray,
you are allowed to get a handle without a copy or clone (i.e., the
string is not owned by the handle).  You must not either free the string
or insert it in some other struct that would own it.  Specifically,
for an Sarray, the copyflag for retrieval is either:
L_COPY or L_NOCOPY
and for insertion, the copyflag is either:
L_COPY or one of {L_INSERT , L_NOCOPY} (the latter are equivalent
for insertion))
Typical patterns are:
(1) Reference a string in an Sarray with L_NOCOPY and insert a copy
of it in another Sarray with L_COPY.
(2) Copy a string from an Sarray with L_COPY and insert it in
another Sarray with L_INSERT (or L_NOCOPY).
In both cases, a copy is made and both Sarrays own their instance
of that string.
</pre>
enum {
    L_NOCOPY = 0,     /*!< do not copy the object; do not delete the ptr  */
    L_INSERT = L_NOCOPY,    /*!< stuff it in; do not copy or clone        */
    L_COPY = 1,       /*!< make/use a copy of the object                  */
    L_CLONE = 2,      /*!< make/use clone (ref count) of the object       */
    L_COPY_CLONE = 3  /*!< make a new array object (e.g., pixa) and fill  */
                      /*!< the array with clones (e.g., pix)              */
}
    '''

ConstType.__name__ = "object_access"

L_NOCOPY = ConstType("L_NOCOPY", 0, '''< do not copy the object; do not delete the ptr
 ''')
L_INSERT = ConstType("L_INSERT", L_NOCOPY, '''< stuff it in; do not copy or clone
 ''')
L_COPY = ConstType("L_COPY", 1, '''< make/use a copy of the object
 ''')
L_CLONE = ConstType("L_CLONE", 2, '''< make/use clone (ref count) of the object
 ''')
L_COPY_CLONE = ConstType("L_COPY_CLONE", 3, '''< make a new array object (e.g., pixa) and fill
 ''')


del ConstType



class ConstType(Const):
    '''
        Sort Mode

----------------------------------------------------------------------------
Sort flags
----------------------------------------------------------------------------
enum {
    L_SHELL_SORT = 1,            /*!< use shell sort                        */
    L_BIN_SORT = 2               /*!< use bin sort                          */
}
    '''

ConstType.__name__ = "sort_mode"

L_SHELL_SORT = ConstType("L_SHELL_SORT", 1, '''< use shell sort
 ''')
L_BIN_SORT = ConstType("L_BIN_SORT", 2, '''< use bin sort
 ''')


del ConstType



class ConstType(Const):
    '''
        Sort Order
enum {
    L_SORT_INCREASING = 1,       /*!< sort in increasing order              */
    L_SORT_DECREASING = 2        /*!< sort in decreasing order              */
}
    '''

ConstType.__name__ = "sort_order"

L_SORT_INCREASING = ConstType("L_SORT_INCREASING", 1, '''< sort in increasing order
 ''')
L_SORT_DECREASING = ConstType("L_SORT_DECREASING", 2, '''< sort in decreasing order
 ''')


del ConstType



class ConstType(Const):
    '''
        Sort Type
enum {
    L_SORT_BY_X = 1,             /*!< sort box or c.c. by left edge location  */
    L_SORT_BY_Y = 2,             /*!< sort box or c.c. by top edge location   */
    L_SORT_BY_RIGHT = 3,         /*!< sort box or c.c. by right edge location */
    L_SORT_BY_BOT = 4,           /*!< sort box or c.c. by bot edge location   */
    L_SORT_BY_WIDTH = 5,         /*!< sort box or c.c. by width               */
    L_SORT_BY_HEIGHT = 6,        /*!< sort box or c.c. by height              */
    L_SORT_BY_MIN_DIMENSION = 7, /*!< sort box or c.c. by min dimension       */
    L_SORT_BY_MAX_DIMENSION = 8, /*!< sort box or c.c. by max dimension       */
    L_SORT_BY_PERIMETER = 9,     /*!< sort box or c.c. by perimeter           */
    L_SORT_BY_AREA = 10,         /*!< sort box or c.c. by area                */
    L_SORT_BY_ASPECT_RATIO = 11  /*!< sort box or c.c. by width/height ratio  */
}
    '''

ConstType.__name__ = "sort_type"

L_SORT_BY_X = ConstType("L_SORT_BY_X", 1, '''< sort box or c.c. by left edge location
 ''')
L_SORT_BY_Y = ConstType("L_SORT_BY_Y", 2, '''< sort box or c.c. by top edge location
 ''')
L_SORT_BY_RIGHT = ConstType("L_SORT_BY_RIGHT", 3, '''< sort box or c.c. by right edge location
 ''')
L_SORT_BY_BOT = ConstType("L_SORT_BY_BOT", 4, '''< sort box or c.c. by bot edge location
 ''')
L_SORT_BY_WIDTH = ConstType("L_SORT_BY_WIDTH", 5, '''< sort box or c.c. by width
 ''')
L_SORT_BY_HEIGHT = ConstType("L_SORT_BY_HEIGHT", 6, '''< sort box or c.c. by height
 ''')
L_SORT_BY_MIN_DIMENSION = ConstType("L_SORT_BY_MIN_DIMENSION", 7, '''< sort box or c.c. by min dimension
 ''')
L_SORT_BY_MAX_DIMENSION = ConstType("L_SORT_BY_MAX_DIMENSION", 8, '''< sort box or c.c. by max dimension
 ''')
L_SORT_BY_PERIMETER = ConstType("L_SORT_BY_PERIMETER", 9, '''< sort box or c.c. by perimeter
 ''')
L_SORT_BY_AREA = ConstType("L_SORT_BY_AREA", 10, '''< sort box or c.c. by area
 ''')
L_SORT_BY_ASPECT_RATIO = ConstType("L_SORT_BY_ASPECT_RATIO", 11, '''< sort box or c.c. by width/height ratio
 ''')


del ConstType



class ConstType(Const):
    '''
        Blend Types

---------------------------------------------------------------------------
Blend flags
---------------------------------------------------------------------------
enum {
    L_BLEND_WITH_INVERSE = 1,     /*!< add some of src inverse to itself     */
    L_BLEND_TO_WHITE = 2,         /*!< shift src colors towards white        */
    L_BLEND_TO_BLACK = 3,         /*!< shift src colors towards black        */
    L_BLEND_GRAY = 4,             /*!< blend src directly with blender       */
    L_BLEND_GRAY_WITH_INVERSE = 5 /*!< add amount of src inverse to itself,  */
                                  /*!< based on blender pix value            */
}
    '''

ConstType.__name__ = "blend_types"

L_BLEND_WITH_INVERSE = ConstType("L_BLEND_WITH_INVERSE", 1, '''< add some of src inverse to itself
 ''')
L_BLEND_TO_WHITE = ConstType("L_BLEND_TO_WHITE", 2, '''< shift src colors towards white
 ''')
L_BLEND_TO_BLACK = ConstType("L_BLEND_TO_BLACK", 3, '''< shift src colors towards black
 ''')
L_BLEND_GRAY = ConstType("L_BLEND_GRAY", 4, '''< blend src directly with blender
 ''')
L_BLEND_GRAY_WITH_INVERSE = ConstType("L_BLEND_GRAY_WITH_INVERSE", 5, '''< add amount of src inverse to itself,
 ''')


del ConstType



class ConstType(Const):
    '''
        Paint Selection
enum {
    L_PAINT_LIGHT = 1,            /*!< colorize non-black pixels             */
    L_PAINT_DARK = 2              /*!< colorize non-white pixels             */
}
    '''

ConstType.__name__ = "paint_selection"

L_PAINT_LIGHT = ConstType("L_PAINT_LIGHT", 1, '''< colorize non-black pixels
 ''')
L_PAINT_DARK = ConstType("L_PAINT_DARK", 2, '''< colorize non-white pixels
 ''')


del ConstType



class ConstType(Const):
    '''
        Pixel Setting

-------------------------------------------------------------------------
Graphics pixel setting
-------------------------------------------------------------------------
enum {
    L_SET_PIXELS = 1,           /*!< set all bits in each pixel to 1       */
    L_CLEAR_PIXELS = 2,         /*!< set all bits in each pixel to 0       */
    L_FLIP_PIXELS = 3           /*!< flip all bits in each pixel           */
}
    '''

ConstType.__name__ = "pixel_setting"

L_SET_PIXELS = ConstType("L_SET_PIXELS", 1, '''< set all bits in each pixel to 1
 ''')
L_CLEAR_PIXELS = ConstType("L_CLEAR_PIXELS", 2, '''< set all bits in each pixel to 0
 ''')
L_FLIP_PIXELS = ConstType("L_FLIP_PIXELS", 3, '''< flip all bits in each pixel
 ''')


del ConstType



class ConstType(Const):
    '''
        Size Comparison

-------------------------------------------------------------------------
Size and location filter flags
-------------------------------------------------------------------------
enum {
    L_SELECT_IF_LT = 1,         /*!< save if value is less than threshold  */
    L_SELECT_IF_GT = 2,         /*!< save if value is more than threshold  */
    L_SELECT_IF_LTE = 3,        /*!< save if value is <= to the threshold  */
    L_SELECT_IF_GTE = 4         /*!< save if value is >= to the threshold  */
}
    '''

ConstType.__name__ = "size_comparison"

L_SELECT_IF_LT = ConstType("L_SELECT_IF_LT", 1, '''< save if value is less than threshold
 ''')
L_SELECT_IF_GT = ConstType("L_SELECT_IF_GT", 2, '''< save if value is more than threshold
 ''')
L_SELECT_IF_LTE = ConstType("L_SELECT_IF_LTE", 3, '''< save if value is <= to the threshold
 ''')
L_SELECT_IF_GTE = ConstType("L_SELECT_IF_GTE", 4, '''< save if value is >= to the threshold
 ''')


del ConstType



class ConstType(Const):
    '''
        Size Selection
enum {
    L_SELECT_BY_WIDTH = 1,          /*!< select by width; 1 bpp            */
    L_SELECT_BY_HEIGHT = 2,         /*!< select by height; 1 bpp           */
    L_SELECT_BY_MAX_DIMENSION = 3,  /*!< select by max of width and        */
                                    /*!< height; 1 bpp                     */
    L_SELECT_BY_AREA = 4,           /*!< select by foreground area; 1 bpp  */
    L_SELECT_BY_PERIMETER = 5       /*!< select by perimeter; 1 bpp        */
}
    '''

ConstType.__name__ = "size_selection"

L_SELECT_BY_WIDTH = ConstType("L_SELECT_BY_WIDTH", 1, '''< select by width; 1 bpp
 ''')
L_SELECT_BY_HEIGHT = ConstType("L_SELECT_BY_HEIGHT", 2, '''< select by height; 1 bpp
 ''')
L_SELECT_BY_MAX_DIMENSION = ConstType("L_SELECT_BY_MAX_DIMENSION", 3, '''< select by max of width and
 ''')
L_SELECT_BY_AREA = ConstType("L_SELECT_BY_AREA", 4, '''< select by foreground area; 1 bpp
 ''')
L_SELECT_BY_PERIMETER = ConstType("L_SELECT_BY_PERIMETER", 5, '''< select by perimeter; 1 bpp
 ''')


del ConstType



class ConstType(Const):
    '''
        Location Filter
enum {
    L_SELECT_WIDTH = 1,         /*!< width must satisfy constraint         */
    L_SELECT_HEIGHT = 2,        /*!< height must satisfy constraint        */
    L_SELECT_XVAL = 3,          /*!< x value must satisfy constraint       */
    L_SELECT_YVAL = 4,          /*!< y value must satisfy constraint       */
    L_SELECT_IF_EITHER = 5,     /*!< either width or height (or xval       */
                                /*!< or yval) can satisfy constraint       */
    L_SELECT_IF_BOTH = 6        /*!< both width and height (or xval        */
                                /*!< and yval must satisfy constraint      */
}
    '''

ConstType.__name__ = "location_filter"

L_SELECT_WIDTH = ConstType("L_SELECT_WIDTH", 1, '''< width must satisfy constraint
 ''')
L_SELECT_HEIGHT = ConstType("L_SELECT_HEIGHT", 2, '''< height must satisfy constraint
 ''')
L_SELECT_XVAL = ConstType("L_SELECT_XVAL", 3, '''< x value must satisfy constraint
 ''')
L_SELECT_YVAL = ConstType("L_SELECT_YVAL", 4, '''< y value must satisfy constraint
 ''')
L_SELECT_IF_EITHER = ConstType("L_SELECT_IF_EITHER", 5, '''< either width or height (or xval
 ''')
L_SELECT_IF_BOTH = ConstType("L_SELECT_IF_BOTH", 6, '''< both width and height (or xval
 ''')


del ConstType



class ConstType(Const):
    '''
        Boxa Check
enum {
    L_CHECK_WIDTH = 1,          /*!< check and possibly modify width       */
    L_CHECK_HEIGHT = 2,         /*!< check and possibly modify height      */
    L_CHECK_BOTH = 3            /*!< check and possibly modify both        */
}
    '''

ConstType.__name__ = "boxa_check"

L_CHECK_WIDTH = ConstType("L_CHECK_WIDTH", 1, '''< check and possibly modify width
 ''')
L_CHECK_HEIGHT = ConstType("L_CHECK_HEIGHT", 2, '''< check and possibly modify height
 ''')
L_CHECK_BOTH = ConstType("L_CHECK_BOTH", 3, '''< check and possibly modify both
 ''')


del ConstType



class ConstType(Const):
    '''
        Color Selection

-------------------------------------------------------------------------
Color component selection flags
-------------------------------------------------------------------------
enum {
    L_SELECT_RED = 1,           /*!< use red component                     */
    L_SELECT_GREEN = 2,         /*!< use green component                   */
    L_SELECT_BLUE = 3,          /*!< use blue component                    */
    L_SELECT_MIN = 4,           /*!< use min color component               */
    L_SELECT_MAX = 5,           /*!< use max color component               */
    L_SELECT_AVERAGE = 6,       /*!< use average of color components       */
    L_SELECT_HUE = 7,           /*!< use hue value (in HSV color space)    */
    L_SELECT_SATURATION = 8     /*!< use saturation value (in HSV space)   */
}
    '''

ConstType.__name__ = "color_selection"

L_SELECT_RED = ConstType("L_SELECT_RED", 1, '''< use red component
 ''')
L_SELECT_GREEN = ConstType("L_SELECT_GREEN", 2, '''< use green component
 ''')
L_SELECT_BLUE = ConstType("L_SELECT_BLUE", 3, '''< use blue component
 ''')
L_SELECT_MIN = ConstType("L_SELECT_MIN", 4, '''< use min color component
 ''')
L_SELECT_MAX = ConstType("L_SELECT_MAX", 5, '''< use max color component
 ''')
L_SELECT_AVERAGE = ConstType("L_SELECT_AVERAGE", 6, '''< use average of color components
 ''')
L_SELECT_HUE = ConstType("L_SELECT_HUE", 7, '''< use hue value (in HSV color space)
 ''')
L_SELECT_SATURATION = ConstType("L_SELECT_SATURATION", 8, '''< use saturation value (in HSV space)
 ''')


del ConstType



class ConstType(Const):
    '''
        Color Content

-------------------------------------------------------------------------
Color content flags
-------------------------------------------------------------------------
enum {
    L_INTERMED_DIFF = 1,        /*!< intermediate of diff component values */
    L_AVE_MAX_DIFF_2 = 2,       /*!< diff average closest comps to third   */
    L_MAX_DIFF = 3              /*!< maximum diff of component values      */
}
    '''

ConstType.__name__ = "color_content"

L_INTERMED_DIFF = ConstType("L_INTERMED_DIFF", 1, '''< intermediate of diff component values
 ''')
L_AVE_MAX_DIFF_2 = ConstType("L_AVE_MAX_DIFF_2", 2, '''< diff average closest comps to third
 ''')
L_MAX_DIFF = ConstType("L_MAX_DIFF", 3, '''< maximum diff of component values
 ''')


del ConstType



class ConstType(Const):
    '''
        16-bit Conversion

-------------------------------------------------------------------------
16-bit conversion flags
-------------------------------------------------------------------------
enum {
    L_LS_BYTE = 1,              /*!< use LSB                               */
    L_MS_BYTE = 2,              /*!< use MSB                               */
    L_AUTO_BYTE = 3,            /*!< use LSB if max(val) < 256; else MSB   */
    L_CLIP_TO_FF = 4,           /*!< use max(val, 255)                     */
    L_LS_TWO_BYTES = 5,         /*!< use two LSB                           */
    L_MS_TWO_BYTES = 6,         /*!< use two MSB                           */
    L_CLIP_TO_FFFF = 7          /*!< use max(val, 65535)                   */
}
    '''

ConstType.__name__ = "16-bit_conversion"

L_LS_BYTE = ConstType("L_LS_BYTE", 1, '''< use LSB
 ''')
L_MS_BYTE = ConstType("L_MS_BYTE", 2, '''< use MSB
 ''')
L_AUTO_BYTE = ConstType("L_AUTO_BYTE", 3, '''< use LSB if max(val) < 256; else MSB
 ''')
L_CLIP_TO_FF = ConstType("L_CLIP_TO_FF", 4, '''< use max(val, 255)
 ''')
L_LS_TWO_BYTES = ConstType("L_LS_TWO_BYTES", 5, '''< use two LSB
 ''')
L_MS_TWO_BYTES = ConstType("L_MS_TWO_BYTES", 6, '''< use two MSB
 ''')
L_CLIP_TO_FFFF = ConstType("L_CLIP_TO_FFFF", 7, '''< use max(val, 65535)
 ''')


del ConstType



class ConstType(Const):
    '''
        Rotation Type

-------------------------------------------------------------------------
Rotate and shear flags
-------------------------------------------------------------------------
enum {
    L_ROTATE_AREA_MAP = 1,     /*!< use area map rotation, if possible     */
    L_ROTATE_SHEAR = 2,        /*!< use shear rotation                     */
    L_ROTATE_SAMPLING = 3      /*!< use sampling                           */
}
    '''

ConstType.__name__ = "rotation_type"

L_ROTATE_AREA_MAP = ConstType("L_ROTATE_AREA_MAP", 1, '''< use area map rotation, if possible
 ''')
L_ROTATE_SHEAR = ConstType("L_ROTATE_SHEAR", 2, '''< use shear rotation
 ''')
L_ROTATE_SAMPLING = ConstType("L_ROTATE_SAMPLING", 3, '''< use sampling
 ''')


del ConstType



class ConstType(Const):
    '''
        Background Color
enum {
    L_BRING_IN_WHITE = 1,      /*!< bring in white pixels from the outside */
    L_BRING_IN_BLACK = 2       /*!< bring in black pixels from the outside */
}
    '''

ConstType.__name__ = "background_color"

L_BRING_IN_WHITE = ConstType("L_BRING_IN_WHITE", 1, '''< bring in white pixels from the outside
 ''')
L_BRING_IN_BLACK = ConstType("L_BRING_IN_BLACK", 2, '''< bring in black pixels from the outside
 ''')


del ConstType



class ConstType(Const):
    '''
        Shear Point
enum {
    L_SHEAR_ABOUT_CORNER = 1,  /*!< shear image about UL corner            */
    L_SHEAR_ABOUT_CENTER = 2   /*!< shear image about center               */
}
    '''

ConstType.__name__ = "shear_point"

L_SHEAR_ABOUT_CORNER = ConstType("L_SHEAR_ABOUT_CORNER", 1, '''< shear image about UL corner
 ''')
L_SHEAR_ABOUT_CENTER = ConstType("L_SHEAR_ABOUT_CENTER", 2, '''< shear image about center
 ''')


del ConstType



class ConstType(Const):
    '''
        Affine Transform Order

-------------------------------------------------------------------------
Affine transform order flags
-------------------------------------------------------------------------
enum {
    L_TR_SC_RO = 1,            /*!< translate, scale, rotate               */
    L_SC_RO_TR = 2,            /*!< scale, rotate, translate               */
    L_RO_TR_SC = 3,            /*!< rotate, translate, scale               */
    L_TR_RO_SC = 4,            /*!< translate, rotate, scale               */
    L_RO_SC_TR = 5,            /*!< rotate, scale, translate               */
    L_SC_TR_RO = 6             /*!< scale, translate, rotate               */
}
    '''

ConstType.__name__ = "affine_transform_order"

L_TR_SC_RO = ConstType("L_TR_SC_RO", 1, '''< translate, scale, rotate
 ''')
L_SC_RO_TR = ConstType("L_SC_RO_TR", 2, '''< scale, rotate, translate
 ''')
L_RO_TR_SC = ConstType("L_RO_TR_SC", 3, '''< rotate, translate, scale
 ''')
L_TR_RO_SC = ConstType("L_TR_RO_SC", 4, '''< translate, rotate, scale
 ''')
L_RO_SC_TR = ConstType("L_RO_SC_TR", 5, '''< rotate, scale, translate
 ''')
L_SC_TR_RO = ConstType("L_SC_TR_RO", 6, '''< scale, translate, rotate
 ''')


del ConstType



class ConstType(Const):
    '''
        Grayscale Fill

-------------------------------------------------------------------------
Grayscale filling flags
-------------------------------------------------------------------------
enum {
    L_FILL_WHITE = 1,         /*!< fill white pixels (e.g, in fg map)      */
    L_FILL_BLACK = 2          /*!< fill black pixels (e.g., in bg map)     */
}
    '''

ConstType.__name__ = "grayscale_fill"

L_FILL_WHITE = ConstType("L_FILL_WHITE", 1, '''< fill white pixels (e.g, in fg map)
 ''')
L_FILL_BLACK = ConstType("L_FILL_BLACK", 2, '''< fill black pixels (e.g., in bg map)
 ''')


del ConstType



class ConstType(Const):
    '''
        BlackWhite Set

-------------------------------------------------------------------------
Flags for setting to white or black
-------------------------------------------------------------------------
enum {
    L_SET_WHITE = 1,         /*!< set pixels to white                      */
    L_SET_BLACK = 2          /*!< set pixels to black                      */
}
    '''

ConstType.__name__ = "blackwhite_set"

L_SET_WHITE = ConstType("L_SET_WHITE", 1, '''< set pixels to white
 ''')
L_SET_BLACK = ConstType("L_SET_BLACK", 2, '''< set pixels to black
 ''')


del ConstType



class ConstType(Const):
    '''
        BlackWhite Get

-------------------------------------------------------------------------
Flags for getting white or black value
-------------------------------------------------------------------------
enum {
    L_GET_WHITE_VAL = 1,     /*!< get white pixel value                    */
    L_GET_BLACK_VAL = 2      /*!< get black pixel value                    */
}
    '''

ConstType.__name__ = "blackwhite_get"

L_GET_WHITE_VAL = ConstType("L_GET_WHITE_VAL", 1, '''< get white pixel value
 ''')
L_GET_BLACK_VAL = ConstType("L_GET_BLACK_VAL", 2, '''< get black pixel value
 ''')


del ConstType



class ConstType(Const):
    '''
        BlackWhite Sum

-------------------------------------------------------------------------
Flags for 8 bit and 16 bit pixel sums
-------------------------------------------------------------------------
enum {
    L_WHITE_IS_MAX = 1, /*!< white pixels are 0xff or 0xffff; black are 0  */
    L_BLACK_IS_MAX = 2  /*!< black pixels are 0xff or 0xffff; white are 0  */
}
    '''

ConstType.__name__ = "blackwhite_sum"

L_WHITE_IS_MAX = ConstType("L_WHITE_IS_MAX", 1, '''< white pixels are 0xff or 0xffff; black are 0
 ''')
L_BLACK_IS_MAX = ConstType("L_BLACK_IS_MAX", 2, '''< black pixels are 0xff or 0xffff; white are 0
 ''')


del ConstType



class ConstType(Const):
    '''
        Dither Distance

-------------------------------------------------------------------------
Dither parameters
If within this grayscale distance from black or white,
do not propagate excess or deficit to neighboring pixels.
-------------------------------------------------------------------------
enum {
    DEFAULT_CLIP_LOWER_1 = 10, /*!< dist to black with no prop; 1 bpp      */
    DEFAULT_CLIP_UPPER_1 = 10, /*!< dist to black with no prop; 1 bpp      */
    DEFAULT_CLIP_LOWER_2 = 5,  /*!< dist to black with no prop; 2 bpp      */
    DEFAULT_CLIP_UPPER_2 = 5   /*!< dist to black with no prop; 2 bpp      */
}
    '''

ConstType.__name__ = "dither_distance"

DEFAULT_CLIP_LOWER_1 = ConstType("DEFAULT_CLIP_LOWER_1", 10, '''< dist to black with no prop; 1 bpp
 ''')
DEFAULT_CLIP_UPPER_1 = ConstType("DEFAULT_CLIP_UPPER_1", 10, '''< dist to black with no prop; 1 bpp
 ''')
DEFAULT_CLIP_LOWER_2 = ConstType("DEFAULT_CLIP_LOWER_2", 5, '''< dist to black with no prop; 2 bpp
 ''')
DEFAULT_CLIP_UPPER_2 = ConstType("DEFAULT_CLIP_UPPER_2", 5, '''< dist to black with no prop; 2 bpp
 ''')


del ConstType



class ConstType(Const):
    '''
        Distance Type

-------------------------------------------------------------------------
Distance type flags
-------------------------------------------------------------------------
enum {
    L_MANHATTAN_DISTANCE = 1,  /*!< L1 distance (e.g., in color space)     */
    L_EUCLIDEAN_DISTANCE = 2   /*!< L2 distance                            */
}
    '''

ConstType.__name__ = "distance_type"

L_MANHATTAN_DISTANCE = ConstType("L_MANHATTAN_DISTANCE", 1, '''< L1 distance (e.g., in color space)
 ''')
L_EUCLIDEAN_DISTANCE = ConstType("L_EUCLIDEAN_DISTANCE", 2, '''< L2 distance
 ''')


del ConstType



class ConstType(Const):
    '''
        Distance Value

-------------------------------------------------------------------------
Distance Value flags
-------------------------------------------------------------------------
enum {
    L_NEGATIVE = 1,      /*!< values < 0                                   */
    L_NON_NEGATIVE = 2,  /*!< values >= 0                                  */
    L_POSITIVE = 3,      /*!< values > 0                                   */
    L_NON_POSITIVE = 4,  /*!< values <= 0                                  */
    L_ZERO = 5,          /*!< values = 0                                   */
    L_ALL = 6            /*!< all values                                   */
}
    '''

ConstType.__name__ = "distance_value"

L_NEGATIVE = ConstType("L_NEGATIVE", 1, '''< values < 0
 ''')
L_NON_NEGATIVE = ConstType("L_NON_NEGATIVE", 2, '''< values >= 0
 ''')
L_POSITIVE = ConstType("L_POSITIVE", 3, '''< values > 0
 ''')
L_NON_POSITIVE = ConstType("L_NON_POSITIVE", 4, '''< values <= 0
 ''')
L_ZERO = ConstType("L_ZERO", 5, '''< values = 0
 ''')
L_ALL = ConstType("L_ALL", 6, '''< all values
 ''')


del ConstType



class ConstType(Const):
    '''
        Stats Type

-------------------------------------------------------------------------
Statistical measures
-------------------------------------------------------------------------
enum {
    L_MEAN_ABSVAL = 1,         /*!< average of abs values                  */
    L_MEDIAN_VAL = 2,          /*!< median value of set                    */
    L_MODE_VAL = 3,            /*!< mode value of set                      */
    L_MODE_COUNT = 4,          /*!< mode count of set                      */
    L_ROOT_MEAN_SQUARE = 5,    /*!< rms of values                          */
    L_STANDARD_DEVIATION = 6,  /*!< standard deviation from mean           */
    L_VARIANCE = 7             /*!< variance of values                     */
}
    '''

ConstType.__name__ = "stats_type"

L_MEAN_ABSVAL = ConstType("L_MEAN_ABSVAL", 1, '''< average of abs values
 ''')
L_MEDIAN_VAL = ConstType("L_MEDIAN_VAL", 2, '''< median value of set
 ''')
L_MODE_VAL = ConstType("L_MODE_VAL", 3, '''< mode value of set
 ''')
L_MODE_COUNT = ConstType("L_MODE_COUNT", 4, '''< mode count of set
 ''')
L_ROOT_MEAN_SQUARE = ConstType("L_ROOT_MEAN_SQUARE", 5, '''< rms of values
 ''')
L_STANDARD_DEVIATION = ConstType("L_STANDARD_DEVIATION", 6, '''< standard deviation from mean
 ''')
L_VARIANCE = ConstType("L_VARIANCE", 7, '''< variance of values
 ''')


del ConstType



class ConstType(Const):
    '''
        Index Selection

-------------------------------------------------------------------------
Set index selection flags
-------------------------------------------------------------------------
enum {
    L_CHOOSE_CONSECUTIVE = 1,  /*!< select 'n' consecutive                 */
    L_CHOOSE_SKIP_BY = 2       /*!< select at intervals of 'n'             */
}
    '''

ConstType.__name__ = "index_selection"

L_CHOOSE_CONSECUTIVE = ConstType("L_CHOOSE_CONSECUTIVE", 1, '''< select 'n' consecutive
 ''')
L_CHOOSE_SKIP_BY = ConstType("L_CHOOSE_SKIP_BY", 2, '''< select at intervals of 'n'
 ''')


del ConstType



class ConstType(Const):
    '''
        Text Orientation

-------------------------------------------------------------------------
Text orientation flags
-------------------------------------------------------------------------
enum {
    L_TEXT_ORIENT_UNKNOWN = 0, /*!< low confidence on text orientation     */
    L_TEXT_ORIENT_UP = 1,      /*!< portrait, text rightside-up            */
    L_TEXT_ORIENT_LEFT = 2,    /*!< landscape, text up to left             */
    L_TEXT_ORIENT_DOWN = 3,    /*!< portrait, text upside-down             */
    L_TEXT_ORIENT_RIGHT = 4    /*!< landscape, text up to right            */
}
    '''

ConstType.__name__ = "text_orientation"

L_TEXT_ORIENT_UNKNOWN = ConstType("L_TEXT_ORIENT_UNKNOWN", 0, '''< low confidence on text orientation
 ''')
L_TEXT_ORIENT_UP = ConstType("L_TEXT_ORIENT_UP", 1, '''< portrait, text rightside-up
 ''')
L_TEXT_ORIENT_LEFT = ConstType("L_TEXT_ORIENT_LEFT", 2, '''< landscape, text up to left
 ''')
L_TEXT_ORIENT_DOWN = ConstType("L_TEXT_ORIENT_DOWN", 3, '''< portrait, text upside-down
 ''')
L_TEXT_ORIENT_RIGHT = ConstType("L_TEXT_ORIENT_RIGHT", 4, '''< landscape, text up to right
 ''')


del ConstType



class ConstType(Const):
    '''
        Edge Orientation

-------------------------------------------------------------------------
Edge orientation flags
-------------------------------------------------------------------------
enum {
    L_HORIZONTAL_EDGES = 0,   /*!< filters for horizontal edges            */
    L_VERTICAL_EDGES = 1,     /*!< filters for vertical edges              */
    L_ALL_EDGES = 2           /*!< filters for all edges                   */
}
    '''

ConstType.__name__ = "edge_orientation"

L_HORIZONTAL_EDGES = ConstType("L_HORIZONTAL_EDGES", 0, '''< filters for horizontal edges
 ''')
L_VERTICAL_EDGES = ConstType("L_VERTICAL_EDGES", 1, '''< filters for vertical edges
 ''')
L_ALL_EDGES = ConstType("L_ALL_EDGES", 2, '''< filters for all edges
 ''')


del ConstType



class ConstType(Const):
    '''
        Line Orientation

-------------------------------------------------------------------------
Line orientation flags
-------------------------------------------------------------------------
enum {
    L_HORIZONTAL_LINE = 0,   /*!< horizontal line                          */
    L_POS_SLOPE_LINE = 1,    /*!< 45 degree line with positive slope       */
    L_VERTICAL_LINE = 2,     /*!< vertical line                            */
    L_NEG_SLOPE_LINE = 3,    /*!< 45 degree line with negative slope       */
    L_OBLIQUE_LINE = 4       /*!< neither horizontal nor vertical */
}
    '''

ConstType.__name__ = "line_orientation"

L_HORIZONTAL_LINE = ConstType("L_HORIZONTAL_LINE", 0, '''< horizontal line
 ''')
L_POS_SLOPE_LINE = ConstType("L_POS_SLOPE_LINE", 1, '''< 45 degree line with positive slope
 ''')
L_VERTICAL_LINE = ConstType("L_VERTICAL_LINE", 2, '''< vertical line
 ''')
L_NEG_SLOPE_LINE = ConstType("L_NEG_SLOPE_LINE", 3, '''< 45 degree line with negative slope
 ''')
L_OBLIQUE_LINE = ConstType("L_OBLIQUE_LINE", 4, '''< neither horizontal nor vertical
 ''')


del ConstType



class ConstType(Const):
    '''
        Image Orientation

-------------------------------------------------------------------------
Image orientation flags
-------------------------------------------------------------------------
enum {
    L_PORTRAIT_MODE = 0,   /*!< typical: page is viewed with height > width  */
    L_LANDSCAPE_MODE = 1   /*!< page is viewed at 90 deg to portrait mode    */
}
    '''

ConstType.__name__ = "image_orientation"

L_PORTRAIT_MODE = ConstType("L_PORTRAIT_MODE", 0, '''< typical: page is viewed with height > width
 ''')
L_LANDSCAPE_MODE = ConstType("L_LANDSCAPE_MODE", 1, '''< page is viewed at 90 deg to portrait mode
 ''')


del ConstType



class ConstType(Const):
    '''
        Scan Direction

-------------------------------------------------------------------------
Scan direction flags
-------------------------------------------------------------------------
enum {
    L_FROM_LEFT = 0,         /*!< scan from left                           */
    L_FROM_RIGHT = 1,        /*!< scan from right                          */
    L_FROM_TOP = 2,          /*!< scan from top                            */
    L_FROM_BOT = 3,          /*!< scan from bottom                         */
    L_SCAN_NEGATIVE = 4,     /*!< scan in negative direction               */
    L_SCAN_POSITIVE = 5,     /*!< scan in positive direction               */
    L_SCAN_BOTH = 6,         /*!< scan in both directions                  */
    L_SCAN_HORIZONTAL = 7,   /*!< horizontal scan (direction unimportant)  */
    L_SCAN_VERTICAL = 8      /*!< vertical scan (direction unimportant)    */
}
    '''

ConstType.__name__ = "scan_direction"

L_FROM_LEFT = ConstType("L_FROM_LEFT", 0, '''< scan from left
 ''')
L_FROM_RIGHT = ConstType("L_FROM_RIGHT", 1, '''< scan from right
 ''')
L_FROM_TOP = ConstType("L_FROM_TOP", 2, '''< scan from top
 ''')
L_FROM_BOT = ConstType("L_FROM_BOT", 3, '''< scan from bottom
 ''')
L_SCAN_NEGATIVE = ConstType("L_SCAN_NEGATIVE", 4, '''< scan in negative direction
 ''')
L_SCAN_POSITIVE = ConstType("L_SCAN_POSITIVE", 5, '''< scan in positive direction
 ''')
L_SCAN_BOTH = ConstType("L_SCAN_BOTH", 6, '''< scan in both directions
 ''')
L_SCAN_HORIZONTAL = ConstType("L_SCAN_HORIZONTAL", 7, '''< horizontal scan (direction unimportant)
 ''')
L_SCAN_VERTICAL = ConstType("L_SCAN_VERTICAL", 8, '''< vertical scan (direction unimportant)
 ''')


del ConstType



class ConstType(Const):
    '''
        Box Adjustment

-------------------------------------------------------------------------
Box size adjustment and location flags
-------------------------------------------------------------------------
enum {
    L_ADJUST_SKIP = 0,           /*!< do not adjust                        */
    L_ADJUST_LEFT = 1,           /*!< adjust left edge                     */
    L_ADJUST_RIGHT = 2,          /*!< adjust right edge                    */
    L_ADJUST_LEFT_AND_RIGHT = 3, /*!< adjust both left and right edges     */
    L_ADJUST_TOP = 4,            /*!< adjust top edge                      */
    L_ADJUST_BOT = 5,            /*!< adjust bottom edge                   */
    L_ADJUST_TOP_AND_BOT = 6,    /*!< adjust both top and bottom edges     */
    L_ADJUST_CHOOSE_MIN = 7,     /*!< choose the min median value          */
    L_ADJUST_CHOOSE_MAX = 8,     /*!< choose the max median value          */
    L_SET_LEFT = 9,              /*!< set left side to a given value       */
    L_SET_RIGHT = 10,            /*!< set right side to a given value      */
    L_SET_TOP = 11,              /*!< set top side to a given value        */
    L_SET_BOT = 12,              /*!< set bottom side to a given value     */
    L_GET_LEFT = 13,             /*!< get left side location               */
    L_GET_RIGHT = 14,            /*!< get right side location              */
    L_GET_TOP = 15,              /*!< get top side location                */
    L_GET_BOT = 16               /*!< get bottom side location             */
}
    '''

ConstType.__name__ = "box_adjustment"

L_ADJUST_SKIP = ConstType("L_ADJUST_SKIP", 0, '''< do not adjust
 ''')
L_ADJUST_LEFT = ConstType("L_ADJUST_LEFT", 1, '''< adjust left edge
 ''')
L_ADJUST_RIGHT = ConstType("L_ADJUST_RIGHT", 2, '''< adjust right edge
 ''')
L_ADJUST_LEFT_AND_RIGHT = ConstType("L_ADJUST_LEFT_AND_RIGHT", 3, '''< adjust both left and right edges
 ''')
L_ADJUST_TOP = ConstType("L_ADJUST_TOP", 4, '''< adjust top edge
 ''')
L_ADJUST_BOT = ConstType("L_ADJUST_BOT", 5, '''< adjust bottom edge
 ''')
L_ADJUST_TOP_AND_BOT = ConstType("L_ADJUST_TOP_AND_BOT", 6, '''< adjust both top and bottom edges
 ''')
L_ADJUST_CHOOSE_MIN = ConstType("L_ADJUST_CHOOSE_MIN", 7, '''< choose the min median value
 ''')
L_ADJUST_CHOOSE_MAX = ConstType("L_ADJUST_CHOOSE_MAX", 8, '''< choose the max median value
 ''')
L_SET_LEFT = ConstType("L_SET_LEFT", 9, '''< set left side to a given value
 ''')
L_SET_RIGHT = ConstType("L_SET_RIGHT", 10, '''< set right side to a given value
 ''')
L_SET_TOP = ConstType("L_SET_TOP", 11, '''< set top side to a given value
 ''')
L_SET_BOT = ConstType("L_SET_BOT", 12, '''< set bottom side to a given value
 ''')
L_GET_LEFT = ConstType("L_GET_LEFT", 13, '''< get left side location
 ''')
L_GET_RIGHT = ConstType("L_GET_RIGHT", 14, '''< get right side location
 ''')
L_GET_TOP = ConstType("L_GET_TOP", 15, '''< get top side location
 ''')
L_GET_BOT = ConstType("L_GET_BOT", 16, '''< get bottom side location
 ''')


del ConstType



class ConstType(Const):
    '''
        Box Boundary Mod

-------------------------------------------------------------------------
Flags for modifying box boundaries using a second box
-------------------------------------------------------------------------
enum {
    L_USE_MINSIZE = 1,           /*!< use boundaries giving min size       */
    L_USE_MAXSIZE = 2,           /*!< use boundaries giving max size       */
    L_SUB_ON_LOC_DIFF = 3,       /*!< modify boundary if big location diff */
    L_SUB_ON_SIZE_DIFF = 4,      /*!< modify boundary if big size diff     */
    L_USE_CAPPED_MIN = 5,        /*!< modify boundary with capped min      */
    L_USE_CAPPED_MAX = 6         /*!< modify boundary with capped max      */
}
    '''

ConstType.__name__ = "box_boundary_mod"

L_USE_MINSIZE = ConstType("L_USE_MINSIZE", 1, '''< use boundaries giving min size
 ''')
L_USE_MAXSIZE = ConstType("L_USE_MAXSIZE", 2, '''< use boundaries giving max size
 ''')
L_SUB_ON_LOC_DIFF = ConstType("L_SUB_ON_LOC_DIFF", 3, '''< modify boundary if big location diff
 ''')
L_SUB_ON_SIZE_DIFF = ConstType("L_SUB_ON_SIZE_DIFF", 4, '''< modify boundary if big size diff
 ''')
L_USE_CAPPED_MIN = ConstType("L_USE_CAPPED_MIN", 5, '''< modify boundary with capped min
 ''')
L_USE_CAPPED_MAX = ConstType("L_USE_CAPPED_MAX", 6, '''< modify boundary with capped max
 ''')


del ConstType



class ConstType(Const):
    '''
        Box Overlap Mod

-------------------------------------------------------------------------
Handling overlapping bounding boxes in boxa
-------------------------------------------------------------------------
enum {
    L_COMBINE = 1,         /*!< resize to bounding region; remove smaller  */
    L_REMOVE_SMALL = 2     /*!< only remove smaller                        */
}
    '''

ConstType.__name__ = "box_overlap_mod"

L_COMBINE = ConstType("L_COMBINE", 1, '''< resize to bounding region; remove smaller
 ''')
L_REMOVE_SMALL = ConstType("L_REMOVE_SMALL", 2, '''< only remove smaller
 ''')


del ConstType



class ConstType(Const):
    '''
        Box Combine or Select

-------------------------------------------------------------------------
Selecting or making a box from two (intersecting) boxes
-------------------------------------------------------------------------
enum {
    L_GEOMETRIC_UNION = 1,         /*!< use union of two boxes             */
    L_GEOMETRIC_INTERSECTION = 2,  /*!< use intersection of two boxes      */
    L_LARGEST_AREA = 3,            /*!< use box with largest area          */
    L_SMALLEST_AREA = 4            /*!< use box with smallest area         */
}
    '''

ConstType.__name__ = "box_combine_or_select"

L_GEOMETRIC_UNION = ConstType("L_GEOMETRIC_UNION", 1, '''< use union of two boxes
 ''')
L_GEOMETRIC_INTERSECTION = ConstType("L_GEOMETRIC_INTERSECTION", 2, '''< use intersection of two boxes
 ''')
L_LARGEST_AREA = ConstType("L_LARGEST_AREA", 3, '''< use box with largest area
 ''')
L_SMALLEST_AREA = ConstType("L_SMALLEST_AREA", 4, '''< use box with smallest area
 ''')


del ConstType



class ConstType(Const):
    '''
        Box Replacement

-------------------------------------------------------------------------
Flags for replacing invalid boxes
-------------------------------------------------------------------------
enum {
    L_USE_ALL_BOXES = 1,         /*!< consider all boxes in the sequence   */
    L_USE_SAME_PARITY_BOXES = 2  /*!< consider boxes with the same parity  */
}
    '''

ConstType.__name__ = "box_replacement"

L_USE_ALL_BOXES = ConstType("L_USE_ALL_BOXES", 1, '''< consider all boxes in the sequence
 ''')
L_USE_SAME_PARITY_BOXES = ConstType("L_USE_SAME_PARITY_BOXES", 2, '''< consider boxes with the same parity
 ''')


del ConstType



class ConstType(Const):
    '''
        Box Corners and Center

-------------------------------------------------------------------------
Flags for box corners and center
-------------------------------------------------------------------------
enum {
    L_UPPER_LEFT = 1,         /*!< UL corner                               */
    L_UPPER_RIGHT = 2,        /*!< UR corner                               */
    L_LOWER_LEFT = 3,         /*!< LL corner                               */
    L_LOWER_RIGHT = 4,        /*!< LR corner                               */
    L_BOX_CENTER = 5          /*!< center                                  */
}
    '''

ConstType.__name__ = "box_corners_and_center"

L_UPPER_LEFT = ConstType("L_UPPER_LEFT", 1, '''< UL corner
 ''')
L_UPPER_RIGHT = ConstType("L_UPPER_RIGHT", 2, '''< UR corner
 ''')
L_LOWER_LEFT = ConstType("L_LOWER_LEFT", 3, '''< LL corner
 ''')
L_LOWER_RIGHT = ConstType("L_LOWER_RIGHT", 4, '''< LR corner
 ''')
L_BOX_CENTER = ConstType("L_BOX_CENTER", 5, '''< center
 ''')


del ConstType



class ConstType(Const):
    '''
        Horiz Warp Stretch

-------------------------------------------------------------------------
Horizontal warp
-------------------------------------------------------------------------
enum {
    L_WARP_TO_LEFT = 1,    /*!< increasing stretch or contraction to left  */
    L_WARP_TO_RIGHT = 2    /*!< increasing stretch or contraction to right */
}
    '''

ConstType.__name__ = "horiz_warp_stretch"

L_WARP_TO_LEFT = ConstType("L_WARP_TO_LEFT", 1, '''< increasing stretch or contraction to left
 ''')
L_WARP_TO_RIGHT = ConstType("L_WARP_TO_RIGHT", 2, '''< increasing stretch or contraction to right
 ''')


del ConstType



class ConstType(Const):
    '''
        Horiz Warp Mode
enum {
    L_LINEAR_WARP = 1,     /*!< stretch or contraction grows linearly      */
    L_QUADRATIC_WARP = 2   /*!< stretch or contraction grows quadratically */
}
    '''

ConstType.__name__ = "horiz_warp_mode"

L_LINEAR_WARP = ConstType("L_LINEAR_WARP", 1, '''< stretch or contraction grows linearly
 ''')
L_QUADRATIC_WARP = ConstType("L_QUADRATIC_WARP", 2, '''< stretch or contraction grows quadratically
 ''')


del ConstType



class ConstType(Const):
    '''
        Pixel Selection

-------------------------------------------------------------------------
Pixel selection for resampling
-------------------------------------------------------------------------
enum {
    L_INTERPOLATED = 1,    /*!< linear interpolation from src pixels       */
    L_SAMPLED = 2          /*!< nearest src pixel sampling only            */
}
    '''

ConstType.__name__ = "pixel_selection"

L_INTERPOLATED = ConstType("L_INTERPOLATED", 1, '''< linear interpolation from src pixels
 ''')
L_SAMPLED = ConstType("L_SAMPLED", 2, '''< nearest src pixel sampling only
 ''')


del ConstType



class ConstType(Const):
    '''
        Thinning Polarity

-------------------------------------------------------------------------
Thinning flags
-------------------------------------------------------------------------
enum {
    L_THIN_FG = 1,             /*!< thin foreground of 1 bpp image         */
    L_THIN_BG = 2              /*!< thin background of 1 bpp image         */
}
    '''

ConstType.__name__ = "thinning_polarity"

L_THIN_FG = ConstType("L_THIN_FG", 1, '''< thin foreground of 1 bpp image
 ''')
L_THIN_BG = ConstType("L_THIN_BG", 2, '''< thin background of 1 bpp image
 ''')


del ConstType



class ConstType(Const):
    '''
        Runlength Direction

-------------------------------------------------------------------------
Runlength flags
-------------------------------------------------------------------------
enum {
    L_HORIZONTAL_RUNS = 0,   /*!< determine runlengths of horizontal runs  */
    L_VERTICAL_RUNS = 1      /*!< determine runlengths of vertical runs    */
}
    '''

ConstType.__name__ = "runlength_direction"

L_HORIZONTAL_RUNS = ConstType("L_HORIZONTAL_RUNS", 0, '''< determine runlengths of horizontal runs
 ''')
L_VERTICAL_RUNS = ConstType("L_VERTICAL_RUNS", 1, '''< determine runlengths of vertical runs
 ''')


del ConstType



class ConstType(Const):
    '''
        Edge Filter

-------------------------------------------------------------------------
Edge filter flags
-------------------------------------------------------------------------
enum {
    L_SOBEL_EDGE = 1,        /*!< Sobel edge filter                        */
    L_TWO_SIDED_EDGE = 2     /*!< Two-sided edge filter                    */
}
    '''

ConstType.__name__ = "edge_filter"

L_SOBEL_EDGE = ConstType("L_SOBEL_EDGE", 1, '''< Sobel edge filter
 ''')
L_TWO_SIDED_EDGE = ConstType("L_TWO_SIDED_EDGE", 2, '''< Two-sided edge filter
 ''')


del ConstType



class ConstType(Const):
    '''
        Subpixel Color Order

-------------------------------------------------------------------------
Subpixel color component ordering in LCD display
-------------------------------------------------------------------------
enum {
    L_SUBPIXEL_ORDER_RGB = 1,   /*!< sensor order left-to-right RGB        */
    L_SUBPIXEL_ORDER_BGR = 2,   /*!< sensor order left-to-right BGR        */
    L_SUBPIXEL_ORDER_VRGB = 3,  /*!< sensor order top-to-bottom RGB        */
    L_SUBPIXEL_ORDER_VBGR = 4   /*!< sensor order top-to-bottom BGR        */
}
    '''

ConstType.__name__ = "subpixel_color_order"

L_SUBPIXEL_ORDER_RGB = ConstType("L_SUBPIXEL_ORDER_RGB", 1, '''< sensor order left-to-right RGB
 ''')
L_SUBPIXEL_ORDER_BGR = ConstType("L_SUBPIXEL_ORDER_BGR", 2, '''< sensor order left-to-right BGR
 ''')
L_SUBPIXEL_ORDER_VRGB = ConstType("L_SUBPIXEL_ORDER_VRGB", 3, '''< sensor order top-to-bottom RGB
 ''')
L_SUBPIXEL_ORDER_VBGR = ConstType("L_SUBPIXEL_ORDER_VBGR", 4, '''< sensor order top-to-bottom BGR
 ''')


del ConstType



class ConstType(Const):
    '''
        HSV Histogram

-------------------------------------------------------------------------
HSV histogram flags
-------------------------------------------------------------------------
enum {
    L_HS_HISTO = 1,            /*!< Use hue-saturation histogram           */
    L_HV_HISTO = 2,            /*!< Use hue-value histogram                */
    L_SV_HISTO = 3             /*!< Use saturation-value histogram         */
}
    '''

ConstType.__name__ = "hsv_histogram"

L_HS_HISTO = ConstType("L_HS_HISTO", 1, '''< Use hue-saturation histogram
 ''')
L_HV_HISTO = ConstType("L_HV_HISTO", 2, '''< Use hue-value histogram
 ''')
L_SV_HISTO = ConstType("L_SV_HISTO", 3, '''< Use saturation-value histogram
 ''')


del ConstType



class ConstType(Const):
    '''
        HSV Region

-------------------------------------------------------------------------
HSV Region flags (inclusion, exclusion)
-------------------------------------------------------------------------
enum {
    L_INCLUDE_REGION = 1,      /*!< Use pixels with specified HSV region   */
    L_EXCLUDE_REGION = 2       /*!< Use pixels outside HSV region          */
}
    '''

ConstType.__name__ = "hsv_region"

L_INCLUDE_REGION = ConstType("L_INCLUDE_REGION", 1, '''< Use pixels with specified HSV region
 ''')
L_EXCLUDE_REGION = ConstType("L_EXCLUDE_REGION", 2, '''< Use pixels outside HSV region
 ''')


del ConstType



class ConstType(Const):
    '''
        Add Text Location

-------------------------------------------------------------------------
Location flags for adding text to a pix
-------------------------------------------------------------------------
enum {
    L_ADD_ABOVE = 1,           /*!< Add text above the image               */
    L_ADD_BELOW = 2,           /*!< Add text below the image               */
    L_ADD_LEFT = 3,            /*!< Add text to the left of the image      */
    L_ADD_RIGHT = 4,           /*!< Add text to the right of the image     */
    L_ADD_AT_TOP = 5,          /*!< Add text over the top of the image     */
    L_ADD_AT_BOT = 6,          /*!< Add text over the bottom of the image  */
    L_ADD_AT_LEFT = 7,         /*!< Add text over left side of the image   */
    L_ADD_AT_RIGHT = 8         /*!< Add text over right side of the image  */
}
    '''

ConstType.__name__ = "add_text_location"

L_ADD_ABOVE = ConstType("L_ADD_ABOVE", 1, '''< Add text above the image
 ''')
L_ADD_BELOW = ConstType("L_ADD_BELOW", 2, '''< Add text below the image
 ''')
L_ADD_LEFT = ConstType("L_ADD_LEFT", 3, '''< Add text to the left of the image
 ''')
L_ADD_RIGHT = ConstType("L_ADD_RIGHT", 4, '''< Add text to the right of the image
 ''')
L_ADD_AT_TOP = ConstType("L_ADD_AT_TOP", 5, '''< Add text over the top of the image
 ''')
L_ADD_AT_BOT = ConstType("L_ADD_AT_BOT", 6, '''< Add text over the bottom of the image
 ''')
L_ADD_AT_LEFT = ConstType("L_ADD_AT_LEFT", 7, '''< Add text over left side of the image
 ''')
L_ADD_AT_RIGHT = ConstType("L_ADD_AT_RIGHT", 8, '''< Add text over right side of the image
 ''')


del ConstType



class ConstType(Const):
    '''
        Pix Plot

-------------------------------------------------------------------------
Flags for plotting on a pix
-------------------------------------------------------------------------
enum {
    L_PLOT_AT_TOP = 1,         /*!< Plot horizontally at top               */
    L_PLOT_AT_MID_HORIZ = 2,   /*!< Plot horizontally at middle            */
    L_PLOT_AT_BOT = 3,         /*!< Plot horizontally at bottom            */
    L_PLOT_AT_LEFT = 4,        /*!< Plot vertically at left                */
    L_PLOT_AT_MID_VERT = 5,    /*!< Plot vertically at middle              */
    L_PLOT_AT_RIGHT = 6        /*!< Plot vertically at right               */
}
    '''

ConstType.__name__ = "pix_plot"

L_PLOT_AT_TOP = ConstType("L_PLOT_AT_TOP", 1, '''< Plot horizontally at top
 ''')
L_PLOT_AT_MID_HORIZ = ConstType("L_PLOT_AT_MID_HORIZ", 2, '''< Plot horizontally at middle
 ''')
L_PLOT_AT_BOT = ConstType("L_PLOT_AT_BOT", 3, '''< Plot horizontally at bottom
 ''')
L_PLOT_AT_LEFT = ConstType("L_PLOT_AT_LEFT", 4, '''< Plot vertically at left
 ''')
L_PLOT_AT_MID_VERT = ConstType("L_PLOT_AT_MID_VERT", 5, '''< Plot vertically at middle
 ''')
L_PLOT_AT_RIGHT = ConstType("L_PLOT_AT_RIGHT", 6, '''< Plot vertically at right
 ''')


del ConstType



class ConstType(Const):
    '''
        Mask Generation

-------------------------------------------------------------------------
Flags for making simple masks
-------------------------------------------------------------------------
enum {
    L_USE_INNER = 1,           /*!< Select the interior part               */
    L_USE_OUTER = 2            /*!< Select the outer part (e.g., a frame)  */
}
    '''

ConstType.__name__ = "mask_generation"

L_USE_INNER = ConstType("L_USE_INNER", 1, '''< Select the interior part
 ''')
L_USE_OUTER = ConstType("L_USE_OUTER", 2, '''< Select the outer part (e.g., a frame)
 ''')


del ConstType



class ConstType(Const):
    '''
        Display Program

-------------------------------------------------------------------------
Flags for selecting display program
-------------------------------------------------------------------------
enum {
    L_DISPLAY_WITH_XZGV = 1,  /*!< Use xzgv with pixDisplay()              */
    L_DISPLAY_WITH_XLI = 2,   /*!< Use xli with pixDisplay()               */
    L_DISPLAY_WITH_XV = 3,    /*!< Use xv with pixDisplay()                */
    L_DISPLAY_WITH_IV = 4,    /*!< Use irfvanview (win) with pixDisplay()  */
    L_DISPLAY_WITH_OPEN = 5   /*!< Use open (apple) with pixDisplay()      */
}
    '''

ConstType.__name__ = "display_program"

L_DISPLAY_WITH_XZGV = ConstType("L_DISPLAY_WITH_XZGV", 1, '''< Use xzgv with pixDisplay()
 ''')
L_DISPLAY_WITH_XLI = ConstType("L_DISPLAY_WITH_XLI", 2, '''< Use xli with pixDisplay()
 ''')
L_DISPLAY_WITH_XV = ConstType("L_DISPLAY_WITH_XV", 3, '''< Use xv with pixDisplay()
 ''')
L_DISPLAY_WITH_IV = ConstType("L_DISPLAY_WITH_IV", 4, '''< Use irfvanview (win) with pixDisplay()
 ''')
L_DISPLAY_WITH_OPEN = ConstType("L_DISPLAY_WITH_OPEN", 5, '''< Use open (apple) with pixDisplay()
 ''')


del ConstType



class ConstType(Const):
    '''
        Flags used in Pix::special

-------------------------------------------------------------------------
Flag(s) used in the 'special' pix field for non-default operations
- 0 is default for chroma sampling in jpeg
- 10-19 are used for zlib compression in png write
- 4 and 8 are used for specifying connectivity in labelling
-------------------------------------------------------------------------
enum {
    L_NO_CHROMA_SAMPLING_JPEG = 1   /*!< Write full resolution chroma      */
}
    '''

ConstType.__name__ = "flags_used_in_pix::special"

L_NO_CHROMA_SAMPLING_JPEG = ConstType("L_NO_CHROMA_SAMPLING_JPEG", 1, '''< Write full resolution chroma
 ''')


del ConstType



class ConstType(Const):
    '''
        Negative Value

-------------------------------------------------------------------------
Handling negative values in conversion to unsigned int
-------------------------------------------------------------------------
enum {
    L_CLIP_TO_ZERO = 1,      /*!< Clip negative values to 0                */
    L_TAKE_ABSVAL = 2        /*!< Convert to positive using L_ABS()        */
}
    '''

ConstType.__name__ = "negative_value"

L_CLIP_TO_ZERO = ConstType("L_CLIP_TO_ZERO", 1, '''< Clip negative values to 0
 ''')
L_TAKE_ABSVAL = ConstType("L_TAKE_ABSVAL", 2, '''< Convert to positive using L_ABS()
 ''')


del ConstType



class ConstType(Const):
    '''
        Relative To Zero

-------------------------------------------------------------------------
Relative to zero flags
-------------------------------------------------------------------------
enum {
    L_LESS_THAN_ZERO = 1,    /*!< Choose values less than zero             */
    L_EQUAL_TO_ZERO = 2,     /*!< Choose values equal to zero              */
    L_GREATER_THAN_ZERO = 3  /*!< Choose values greater than zero          */
}
    '''

ConstType.__name__ = "relative_to_zero"

L_LESS_THAN_ZERO = ConstType("L_LESS_THAN_ZERO", 1, '''< Choose values less than zero
 ''')
L_EQUAL_TO_ZERO = ConstType("L_EQUAL_TO_ZERO", 2, '''< Choose values equal to zero
 ''')
L_GREATER_THAN_ZERO = ConstType("L_GREATER_THAN_ZERO", 3, '''< Choose values greater than zero
 ''')


del ConstType



class ConstType(Const):
    '''
        Trailing Slash

-------------------------------------------------------------------------
Flags for adding or removing trailing slash from string
-------------------------------------------------------------------------
enum {
    L_ADD_TRAIL_SLASH = 1,     /*!< Add trailing slash to string           */
    L_REMOVE_TRAIL_SLASH = 2   /*!< Remove trailing slash from string      */
}
    '''

ConstType.__name__ = "trailing_slash"

L_ADD_TRAIL_SLASH = ConstType("L_ADD_TRAIL_SLASH", 1, '''< Add trailing slash to string
 ''')
L_REMOVE_TRAIL_SLASH = ConstType("L_REMOVE_TRAIL_SLASH", 2, '''< Remove trailing slash from string
 ''')


del ConstType



class ConstType(Const):
    '''
        Ptra Removal

------------------------------------------------------------------------
Accessor and modifier flags for L_Ptra and L_Ptraa
------------------------------------------------------------------------
enum {
    L_NO_COMPACTION = 1,        /*!< null the pointer only                */
    L_COMPACTION = 2            /*!< compact the array                    */
}
    '''

ConstType.__name__ = "ptra_removal"

L_NO_COMPACTION = ConstType("L_NO_COMPACTION", 1, '''< null the pointer only
 ''')
L_COMPACTION = ConstType("L_COMPACTION", 2, '''< compact the array
 ''')


del ConstType



class ConstType(Const):
    '''
        Ptra Insertion
enum {
    L_AUTO_DOWNSHIFT = 0,     /*!< choose based on number of holes        */
    L_MIN_DOWNSHIFT = 1,      /*!< downshifts min # of ptrs below insert  */
    L_FULL_DOWNSHIFT = 2      /*!< downshifts all ptrs below insert       */
}
    '''

ConstType.__name__ = "ptra_insertion"

L_AUTO_DOWNSHIFT = ConstType("L_AUTO_DOWNSHIFT", 0, '''< choose based on number of holes
 ''')
L_MIN_DOWNSHIFT = ConstType("L_MIN_DOWNSHIFT", 1, '''< downshifts min # of ptrs below insert
 ''')
L_FULL_DOWNSHIFT = ConstType("L_FULL_DOWNSHIFT", 2, '''< downshifts all ptrs below insert
 ''')


del ConstType



class ConstType(Const):
    '''
        Ptraa Accessor
enum {
    L_HANDLE_ONLY = 0,     /*!< ptr to L_Ptra; caller can inspect only    */
    L_REMOVE = 1           /*!< caller owns; destroy or save in L_Ptraa   */
}
    '''

ConstType.__name__ = "ptraa_accessor"

L_HANDLE_ONLY = ConstType("L_HANDLE_ONLY", 0, '''< ptr to L_Ptra; caller can inspect only
 ''')
L_REMOVE = ConstType("L_REMOVE", 1, '''< caller owns; destroy or save in L_Ptraa
 ''')


del ConstType



class ConstType(Const):
    '''
        Barcode Method

-----------------------------------------------------------------
Flags for method of extracting barcode widths
-----------------------------------------------------------------
enum {
    L_USE_WIDTHS = 1,     /*!< use histogram of barcode widths           */
    L_USE_WINDOWS = 2     /*!< find best window for decoding transitions */
}
    '''

ConstType.__name__ = "barcode_method"

L_USE_WIDTHS = ConstType("L_USE_WIDTHS", 1, '''< use histogram of barcode widths
 ''')
L_USE_WINDOWS = ConstType("L_USE_WINDOWS", 2, '''< find best window for decoding transitions
 ''')


del ConstType



class ConstType(Const):
    '''
        Barcode Format

-----------------------------------------------------------------
Flags for barcode formats
These are used both to identify a barcode format and to identify
the decoding method to use on a barcode.
-----------------------------------------------------------------
enum {
    L_BF_UNKNOWN = 0,     /*!< unknown format                            */
    L_BF_ANY = 1,         /*!< try decoding with all known formats       */
    L_BF_CODE128 = 2,     /*!< decode with Code128 format                */
    L_BF_EAN8 = 3,        /*!< decode with EAN8 format                   */
    L_BF_EAN13 = 4,       /*!< decode with EAN13 format                  */
    L_BF_CODE2OF5 = 5,    /*!< decode with Code 2 of 5 format            */
    L_BF_CODEI2OF5 = 6,   /*!< decode with Interleaved 2 of 5 format     */
    L_BF_CODE39 = 7,      /*!< decode with Code39 format                 */
    L_BF_CODE93 = 8,      /*!< decode with Code93 format                 */
    L_BF_CODABAR = 9,     /*!< decode with Code93 format                 */
    L_BF_UPCA = 10        /*!< decode with UPC A format                  */
}
    '''

ConstType.__name__ = "barcode_format"

L_BF_UNKNOWN = ConstType("L_BF_UNKNOWN", 0, '''< unknown format
 ''')
L_BF_ANY = ConstType("L_BF_ANY", 1, '''< try decoding with all known formats
 ''')
L_BF_CODE128 = ConstType("L_BF_CODE128", 2, '''< decode with Code128 format
 ''')
L_BF_EAN8 = ConstType("L_BF_EAN8", 3, '''< decode with EAN8 format
 ''')
L_BF_EAN13 = ConstType("L_BF_EAN13", 4, '''< decode with EAN13 format
 ''')
L_BF_CODE2OF5 = ConstType("L_BF_CODE2OF5", 5, '''< decode with Code 2 of 5 format
 ''')
L_BF_CODEI2OF5 = ConstType("L_BF_CODEI2OF5", 6, '''< decode with Interleaved 2 of 5 format
 ''')
L_BF_CODE39 = ConstType("L_BF_CODE39", 7, '''< decode with Code39 format
 ''')
L_BF_CODE93 = ConstType("L_BF_CODE93", 8, '''< decode with Code93 format
 ''')
L_BF_CODABAR = ConstType("L_BF_CODABAR", 9, '''< decode with Code93 format
 ''')
L_BF_UPCA = ConstType("L_BF_UPCA", 10, '''< decode with UPC A format
 ''')


del ConstType



class ConstType(Const):
    '''
        Sudoku Output

 For printing out array data
enum {
    L_SUDOKU_INIT = 0,
    L_SUDOKU_STATE = 1
}
    '''

ConstType.__name__ = "sudoku_output"

L_SUDOKU_INIT = ConstType("L_SUDOKU_INIT", 0, ''' ''')
L_SUDOKU_STATE = ConstType("L_SUDOKU_STATE", 1, ''' ''')


del ConstType



class ConstType(Const):
    '''
        RBTree Key Type

 The three valid key types for red-black trees, maps and sets.
enum {
    L_INT_TYPE = 1,
    L_UINT_TYPE = 2,
    L_FLOAT_TYPE = 3
}
    '''

ConstType.__name__ = "rbtree_key_type"

L_INT_TYPE = ConstType("L_INT_TYPE", 1, ''' ''')
L_UINT_TYPE = ConstType("L_UINT_TYPE", 2, ''' ''')
L_FLOAT_TYPE = ConstType("L_FLOAT_TYPE", 3, ''' ''')


del ConstType



class ConstType(Const):
    '''
        Character Set

-------------------------------------------------------------------------
Flags for describing limited character sets
-------------------------------------------------------------------------
enum {
    L_UNKNOWN = 0,           /*!< character set type is not specified      */
    L_ARABIC_NUMERALS = 1,   /*!< 10 digits                                */
    L_LC_ROMAN_NUMERALS = 2, /*!< 7 lower-case letters (i,v,x,l,c,d,m)     */
    L_UC_ROMAN_NUMERALS = 3, /*!< 7 upper-case letters (I,V,X,L,C,D,M)     */
    L_LC_ALPHA = 4,          /*!< 26 lower-case letters                    */
    L_UC_ALPHA = 5           /*!< 26 upper-case letters                    */
}
    '''

ConstType.__name__ = "character_set"

L_UNKNOWN = ConstType("L_UNKNOWN", 0, '''< character set type is not specified
 ''')
L_ARABIC_NUMERALS = ConstType("L_ARABIC_NUMERALS", 1, '''< 10 digits
 ''')
L_LC_ROMAN_NUMERALS = ConstType("L_LC_ROMAN_NUMERALS", 2, '''< 7 lower-case letters (i,v,x,l,c,d,m)
 ''')
L_UC_ROMAN_NUMERALS = ConstType("L_UC_ROMAN_NUMERALS", 3, '''< 7 upper-case letters (I,V,X,L,C,D,M)
 ''')
L_LC_ALPHA = ConstType("L_LC_ALPHA", 4, '''< 26 lower-case letters
 ''')
L_UC_ALPHA = ConstType("L_UC_ALPHA", 5, '''< 26 upper-case letters
 ''')


del ConstType



class ConstType(Const):
    '''
        Template Select

-------------------------------------------------------------------------
Flags for selecting between using average and all templates:
recog->templ_use
-------------------------------------------------------------------------
enum {
    L_USE_ALL_TEMPLATES = 0,     /*!< use all templates; default            */
    L_USE_AVERAGE_TEMPLATES = 1  /*!< use average templates; special cases  */
}
    '''

ConstType.__name__ = "template_select"

L_USE_ALL_TEMPLATES = ConstType("L_USE_ALL_TEMPLATES", 0, '''< use all templates; default
 ''')
L_USE_AVERAGE_TEMPLATES = ConstType("L_USE_AVERAGE_TEMPLATES", 1, '''< use average templates; special cases
 ''')


del ConstType



class ConstType(Const):
    '''
        Regtest Mode

 Running modes for the test
enum {
    L_REG_GENERATE = 0,
    L_REG_COMPARE = 1,
    L_REG_DISPLAY = 2
}
    '''

ConstType.__name__ = "regtest_mode"

L_REG_GENERATE = ConstType("L_REG_GENERATE", 0, ''' ''')
L_REG_COMPARE = ConstType("L_REG_COMPARE", 1, ''' ''')
L_REG_DISPLAY = ConstType("L_REG_DISPLAY", 2, ''' ''')


del ConstType



class ConstType(Const):
    '''
        Stringcode Select

 Select string in stringcode for a specific serializable data type
enum {
    L_STR_TYPE = 0,      /*!< typedef for the data type                      */
    L_STR_NAME = 1,      /*!< name of the data type                          */
    L_STR_READER = 2,    /*!< reader to get the data type from file          */
    L_STR_MEMREADER = 3  /*!< reader to get the compressed string in memory  */
}
    '''

ConstType.__name__ = "stringcode_select"

L_STR_TYPE = ConstType("L_STR_TYPE", 0, '''< typedef for the data type
 ''')
L_STR_NAME = ConstType("L_STR_NAME", 1, '''< name of the data type
 ''')
L_STR_READER = ConstType("L_STR_READER", 2, '''< reader to get the data type from file
 ''')
L_STR_MEMREADER = ConstType("L_STR_MEMREADER", 3, '''< reader to get the compressed string in memory
 ''')


del ConstType



globals_copy = globals().copy()
__all__ = [const for const in globals_copy if isinstance(globals_copy[const], Const)] + ['find_siblings']

del globals_copy
