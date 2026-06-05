from _typeshed import Incomplete
from typing import ClassVar, Iterator, overload, Any
from numpy import typing as npt

AutoStride: int
BOX: VECSEMANTICS
CHAR: BASETYPE
COLOR: VECSEMANTICS
DOUBLE: BASETYPE
FLOAT: BASETYPE
HALF: BASETYPE
INT: BASETYPE
INT16: BASETYPE
INT32: BASETYPE
INT64: BASETYPE
INT8: BASETYPE
INTRO_STRING: str
KEYCODE: VECSEMANTICS
LASTBASE: BASETYPE
LONGLONG: BASETYPE
MATRIX33: AGGREGATE
MATRIX44: AGGREGATE
MakeTxBumpWithSlopes: MakeTextureMode
MakeTxEnvLatl: MakeTextureMode
MakeTxEnvLatlFromLightProbe: MakeTextureMode
MakeTxShadow: MakeTextureMode
MakeTxTexture: MakeTextureMode
NONE: BASETYPE
NONFINITE_BLACK: NonFiniteFixMode
NONFINITE_BOX3: NonFiniteFixMode
NONFINITE_NONE: NonFiniteFixMode
NORMAL: VECSEMANTICS
NOSEMANTICS: VECSEMANTICS
NOXFORM: VECSEMANTICS
OpenColorIO_version_hex: int
POINT: VECSEMANTICS
PTR: BASETYPE
RATIONAL: VECSEMANTICS
SCALAR: AGGREGATE
SHORT: BASETYPE
STRING: BASETYPE
TIMECODE: VECSEMANTICS
TypeBox2: TypeDesc
TypeBox2i: TypeDesc
TypeBox3: TypeDesc
TypeBox3i: TypeDesc
TypeColor: TypeDesc
TypeFloat: TypeDesc
TypeFloat2: TypeDesc
TypeFloat4: TypeDesc
TypeHalf: TypeDesc
TypeInt: TypeDesc
TypeInt16: TypeDesc
TypeInt32: TypeDesc
TypeInt64: TypeDesc
TypeInt8: TypeDesc
TypeKeyCode: TypeDesc
TypeMatrix: TypeDesc
TypeMatrix33: TypeDesc
TypeMatrix44: TypeDesc
TypeNormal: TypeDesc
TypePoint: TypeDesc
TypePointer: TypeDesc
TypeRational: TypeDesc
TypeString: TypeDesc
TypeTimeCode: TypeDesc
TypeUInt: TypeDesc
TypeUInt16: TypeDesc
TypeUInt32: TypeDesc
TypeUInt64: TypeDesc
TypeUInt8: TypeDesc
TypeUnknown: TypeDesc
TypeVector: TypeDesc
TypeVector2: TypeDesc
TypeVector2i: TypeDesc
TypeVector3i: TypeDesc
TypeVector4: TypeDesc
UCHAR: BASETYPE
UINT: BASETYPE
UINT16: BASETYPE
UINT32: BASETYPE
UINT64: BASETYPE
UINT8: BASETYPE
ULONGLONG: BASETYPE
UNKNOWN: BASETYPE
USHORT: BASETYPE
VEC2: AGGREGATE
VEC3: AGGREGATE
VEC4: AGGREGATE
VECTOR: VECSEMANTICS
VERSION: int
VERSION_MAJOR: int
VERSION_MINOR: int
VERSION_PATCH: int
VERSION_STRING: str
__version__: str
openimageio_version: int
supportsOpenColorIO: bool

class AGGREGATE:
    __members__: ClassVar[dict] = ...  # read-only
    MATRIX33: ClassVar[AGGREGATE] = ...
    MATRIX44: ClassVar[AGGREGATE] = ...
    SCALAR: ClassVar[AGGREGATE] = ...
    VEC2: ClassVar[AGGREGATE] = ...
    VEC3: ClassVar[AGGREGATE] = ...
    VEC4: ClassVar[AGGREGATE] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, value: int) -> None:
        """__init__(self: OpenImageIO.OpenImageIO.AGGREGATE, value: int) -> None"""
    def _pybind11_conduit_v1_(self, *args, **kwargs): ...
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: OpenImageIO.OpenImageIO.AGGREGATE) -> int"""
    def __int__(self) -> int:
        """__int__(self: OpenImageIO.OpenImageIO.AGGREGATE) -> int"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class BASETYPE:
    __members__: ClassVar[dict] = ...  # read-only
    CHAR: ClassVar[BASETYPE] = ...
    DOUBLE: ClassVar[BASETYPE] = ...
    FLOAT: ClassVar[BASETYPE] = ...
    HALF: ClassVar[BASETYPE] = ...
    INT: ClassVar[BASETYPE] = ...
    INT16: ClassVar[BASETYPE] = ...
    INT32: ClassVar[BASETYPE] = ...
    INT64: ClassVar[BASETYPE] = ...
    INT8: ClassVar[BASETYPE] = ...
    LASTBASE: ClassVar[BASETYPE] = ...
    LONGLONG: ClassVar[BASETYPE] = ...
    NONE: ClassVar[BASETYPE] = ...
    PTR: ClassVar[BASETYPE] = ...
    SHORT: ClassVar[BASETYPE] = ...
    STRING: ClassVar[BASETYPE] = ...
    UCHAR: ClassVar[BASETYPE] = ...
    UINT: ClassVar[BASETYPE] = ...
    UINT16: ClassVar[BASETYPE] = ...
    UINT32: ClassVar[BASETYPE] = ...
    UINT64: ClassVar[BASETYPE] = ...
    UINT8: ClassVar[BASETYPE] = ...
    ULONGLONG: ClassVar[BASETYPE] = ...
    UNKNOWN: ClassVar[BASETYPE] = ...
    USHORT: ClassVar[BASETYPE] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, value: int) -> None:
        """__init__(self: OpenImageIO.OpenImageIO.BASETYPE, value: int) -> None"""
    def _pybind11_conduit_v1_(self, *args, **kwargs): ...
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: OpenImageIO.OpenImageIO.BASETYPE) -> int"""
    def __int__(self) -> int:
        """__int__(self: OpenImageIO.OpenImageIO.BASETYPE) -> int"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class ColorConfig:
    @overload
    def __init__(self) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: OpenImageIO.OpenImageIO.ColorConfig) -> None

        2. __init__(self: OpenImageIO.OpenImageIO.ColorConfig, arg0: str) -> None
        """
    @overload
    def __init__(self, arg0: str) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: OpenImageIO.OpenImageIO.ColorConfig) -> None

        2. __init__(self: OpenImageIO.OpenImageIO.ColorConfig, arg0: str) -> None
        """
    def _pybind11_conduit_v1_(self, *args, **kwargs): ...
    def configname(self) -> str:
        """configname(self: OpenImageIO.OpenImageIO.ColorConfig) -> str"""
    @staticmethod
    def default_colorconfig() -> ColorConfig:
        """default_colorconfig() -> OpenImageIO.OpenImageIO.ColorConfig"""
    def equivalent(self, color_space: str, other_color_space: str) -> bool:
        """equivalent(self: OpenImageIO.OpenImageIO.ColorConfig, color_space: str, other_color_space: str) -> bool"""
    def getAliases(self, arg0: str) -> list[str]:
        """getAliases(self: OpenImageIO.OpenImageIO.ColorConfig, arg0: str) -> list[str]"""
    def getColorSpaceDataType(self, name: str) -> tuple[TypeDesc, int]:
        """getColorSpaceDataType(self: OpenImageIO.OpenImageIO.ColorConfig, name: str) -> tuple[OpenImageIO.OpenImageIO.TypeDesc, int]"""
    def getColorSpaceFamilyByName(self, name: str) -> str:
        """getColorSpaceFamilyByName(self: OpenImageIO.OpenImageIO.ColorConfig, name: str) -> str"""
    def getColorSpaceFromFilepath(self, arg0: str) -> str:
        """getColorSpaceFromFilepath(self: OpenImageIO.OpenImageIO.ColorConfig, arg0: str) -> str"""
    def getColorSpaceIndex(self, name: str) -> int:
        """getColorSpaceIndex(self: OpenImageIO.OpenImageIO.ColorConfig, name: str) -> int"""
    def getColorSpaceNameByIndex(self, arg0: int) -> str:
        """getColorSpaceNameByIndex(self: OpenImageIO.OpenImageIO.ColorConfig, arg0: int) -> str"""
    def getColorSpaceNameByRole(self, role: str) -> str:
        """getColorSpaceNameByRole(self: OpenImageIO.OpenImageIO.ColorConfig, role: str) -> str"""
    def getColorSpaceNames(self) -> list[str]:
        """getColorSpaceNames(self: OpenImageIO.OpenImageIO.ColorConfig) -> list[str]"""
    def getDefaultDisplayName(self) -> str:
        """getDefaultDisplayName(self: OpenImageIO.OpenImageIO.ColorConfig) -> str"""
    def getDefaultViewName(self, display: str = ...) -> str:
        """getDefaultViewName(self: OpenImageIO.OpenImageIO.ColorConfig, display: str = '') -> str"""
    def getDisplayNameByIndex(self, arg0: int) -> str:
        """getDisplayNameByIndex(self: OpenImageIO.OpenImageIO.ColorConfig, arg0: int) -> str"""
    def getDisplayNames(self) -> list[str]:
        """getDisplayNames(self: OpenImageIO.OpenImageIO.ColorConfig) -> list[str]"""
    def getDisplayViewColorSpaceName(self, display: str, view: str) -> str:
        """getDisplayViewColorSpaceName(self: OpenImageIO.OpenImageIO.ColorConfig, display: str, view: str) -> str"""
    def getDisplayViewLooks(self, display: str, view: str) -> str:
        """getDisplayViewLooks(self: OpenImageIO.OpenImageIO.ColorConfig, display: str, view: str) -> str"""
    def getLookNameByIndex(self, arg0: int) -> str:
        """getLookNameByIndex(self: OpenImageIO.OpenImageIO.ColorConfig, arg0: int) -> str"""
    def getLookNames(self) -> list[str]:
        """getLookNames(self: OpenImageIO.OpenImageIO.ColorConfig) -> list[str]"""
    def getNamedTransformAliases(self, arg0: str) -> list[str]:
        """getNamedTransformAliases(self: OpenImageIO.OpenImageIO.ColorConfig, arg0: str) -> list[str]"""
    def getNamedTransformNameByIndex(self, arg0: int) -> str:
        """getNamedTransformNameByIndex(self: OpenImageIO.OpenImageIO.ColorConfig, arg0: int) -> str"""
    def getNamedTransformNames(self) -> list[str]:
        """getNamedTransformNames(self: OpenImageIO.OpenImageIO.ColorConfig) -> list[str]"""
    def getNumColorSpaces(self) -> int:
        """getNumColorSpaces(self: OpenImageIO.OpenImageIO.ColorConfig) -> int"""
    def getNumDisplays(self) -> int:
        """getNumDisplays(self: OpenImageIO.OpenImageIO.ColorConfig) -> int"""
    def getNumLooks(self) -> int:
        """getNumLooks(self: OpenImageIO.OpenImageIO.ColorConfig) -> int"""
    def getNumNamedTransforms(self) -> int:
        """getNumNamedTransforms(self: OpenImageIO.OpenImageIO.ColorConfig) -> int"""
    def getNumRoles(self) -> int:
        """getNumRoles(self: OpenImageIO.OpenImageIO.ColorConfig) -> int"""
    def getNumViews(self, display: str = ...) -> int:
        """getNumViews(self: OpenImageIO.OpenImageIO.ColorConfig, display: str = '') -> int"""
    def getRoleByIndex(self, arg0: int) -> str:
        """getRoleByIndex(self: OpenImageIO.OpenImageIO.ColorConfig, arg0: int) -> str"""
    def getRoles(self) -> list[str]:
        """getRoles(self: OpenImageIO.OpenImageIO.ColorConfig) -> list[str]"""
    def getViewNameByIndex(self, display: str = ..., index: int) -> str:
        """getViewNameByIndex(self: OpenImageIO.OpenImageIO.ColorConfig, display: str = '', index: int) -> str"""
    def getViewNames(self, display: str = ...) -> list[str]:
        """getViewNames(self: OpenImageIO.OpenImageIO.ColorConfig, display: str = '') -> list[str]"""
    def geterror(self) -> str:
        """geterror(self: OpenImageIO.OpenImageIO.ColorConfig) -> str"""
    def parseColorSpaceFromString(self, arg0: str) -> str:
        """parseColorSpaceFromString(self: OpenImageIO.OpenImageIO.ColorConfig, arg0: str) -> str"""
    def resolve(self, name: str) -> str:
        """resolve(self: OpenImageIO.OpenImageIO.ColorConfig, name: str) -> str"""

class CompareResults:
    def __init__(self) -> None:
        """__init__(self: OpenImageIO.OpenImageIO.CompareResults) -> None"""
    def _pybind11_conduit_v1_(self, *args, **kwargs): ...
    @property
    def PSNR(self) -> float: ...
    @property
    def error(self) -> bool: ...
    @property
    def maxc(self) -> int: ...
    @property
    def maxerror(self) -> float: ...
    @property
    def maxx(self) -> int: ...
    @property
    def maxy(self) -> int: ...
    @property
    def maxz(self) -> int: ...
    @property
    def meanerror(self) -> float: ...
    @property
    def nfail(self) -> int: ...
    @property
    def nwarn(self) -> int: ...
    @property
    def rms_error(self) -> float: ...

class DeepData:
    def __init__(self) -> None:
        """__init__(self: OpenImageIO.OpenImageIO.DeepData) -> None"""
    def _pybind11_conduit_v1_(self, *args, **kwargs): ...
    def allocated(self) -> bool:
        """allocated(self: OpenImageIO.OpenImageIO.DeepData) -> bool"""
    def capacity(self, pixel: int) -> int:
        """capacity(self: OpenImageIO.OpenImageIO.DeepData, pixel: int) -> int"""
    def channelname(self, arg0: int) -> str:
        """channelname(self: OpenImageIO.OpenImageIO.DeepData, arg0: int) -> str"""
    def channelsize(self, arg0: int) -> int:
        """channelsize(self: OpenImageIO.OpenImageIO.DeepData, arg0: int) -> int"""
    def channeltype(self, arg0: int) -> TypeDesc:
        """channeltype(self: OpenImageIO.OpenImageIO.DeepData, arg0: int) -> OpenImageIO.OpenImageIO.TypeDesc"""
    def clear(self) -> None:
        """clear(self: OpenImageIO.OpenImageIO.DeepData) -> None"""
    def copy_deep_pixel(self, pixel: int, src: DeepData, srcpixel: int) -> bool:
        """copy_deep_pixel(self: OpenImageIO.OpenImageIO.DeepData, pixel: int, src: OpenImageIO.OpenImageIO.DeepData, srcpixel: int) -> bool"""
    def copy_deep_sample(self, pixel: int, sample: int, src: DeepData, srcpixel: int, srcsample: int) -> bool:
        """copy_deep_sample(self: OpenImageIO.OpenImageIO.DeepData, pixel: int, sample: int, src: OpenImageIO.OpenImageIO.DeepData, srcpixel: int, srcsample: int) -> bool"""
    def deep_value(self, pixel: int, channel: int, sample: int) -> float:
        """deep_value(self: OpenImageIO.OpenImageIO.DeepData, pixel: int, channel: int, sample: int) -> float"""
    def deep_value_uint(self, pixel: int, channel: int, sample: int) -> int:
        """deep_value_uint(self: OpenImageIO.OpenImageIO.DeepData, pixel: int, channel: int, sample: int) -> int"""
    def erase_samples(self, pixel: int, samplepos: int, nsamples: int = ...) -> None:
        """erase_samples(self: OpenImageIO.OpenImageIO.DeepData, pixel: int, samplepos: int, nsamples: int = 1) -> None"""
    def free(self) -> None:
        """free(self: OpenImageIO.OpenImageIO.DeepData) -> None"""
    @overload
    def init(self, npixels: int, nchannels: int, channeltypes: object, channelnames: object) -> None:
        """init(*args, **kwargs)
        Overloaded function.

        1. init(self: OpenImageIO.OpenImageIO.DeepData, npixels: int, nchannels: int, channeltypes: object, channelnames: object) -> None

        2. init(self: OpenImageIO.OpenImageIO.DeepData, arg0: OpenImageIO.OpenImageIO.ImageSpec) -> None
        """
    @overload
    def init(self, arg0: ImageSpec) -> None:
        """init(*args, **kwargs)
        Overloaded function.

        1. init(self: OpenImageIO.OpenImageIO.DeepData, npixels: int, nchannels: int, channeltypes: object, channelnames: object) -> None

        2. init(self: OpenImageIO.OpenImageIO.DeepData, arg0: OpenImageIO.OpenImageIO.ImageSpec) -> None
        """
    def initialized(self) -> bool:
        """initialized(self: OpenImageIO.OpenImageIO.DeepData) -> bool"""
    def insert_samples(self, pixel: int, samplepos: int, nsamples: int = ...) -> None:
        """insert_samples(self: OpenImageIO.OpenImageIO.DeepData, pixel: int, samplepos: int, nsamples: int = 1) -> None"""
    def merge_deep_pixels(self, pixel: int, src: DeepData, srcpixel: int) -> None:
        """merge_deep_pixels(self: OpenImageIO.OpenImageIO.DeepData, pixel: int, src: OpenImageIO.OpenImageIO.DeepData, srcpixel: int) -> None"""
    def merge_overlaps(self, pixel: int) -> None:
        """merge_overlaps(self: OpenImageIO.OpenImageIO.DeepData, pixel: int) -> None"""
    def occlusion_cull(self, pixel: int) -> None:
        """occlusion_cull(self: OpenImageIO.OpenImageIO.DeepData, pixel: int) -> None"""
    def opaque_z(self, pixel: int) -> float:
        """opaque_z(self: OpenImageIO.OpenImageIO.DeepData, pixel: int) -> float"""
    def same_channeltypes(self, arg0: DeepData) -> bool:
        """same_channeltypes(self: OpenImageIO.OpenImageIO.DeepData, arg0: OpenImageIO.OpenImageIO.DeepData) -> bool"""
    def samples(self, pixel: int) -> int:
        """samples(self: OpenImageIO.OpenImageIO.DeepData, pixel: int) -> int"""
    def samplesize(self) -> int:
        """samplesize(self: OpenImageIO.OpenImageIO.DeepData) -> int"""
    def set_capacity(self, pixel: int, nsamples: int) -> None:
        """set_capacity(self: OpenImageIO.OpenImageIO.DeepData, pixel: int, nsamples: int) -> None"""
    def set_deep_value(self, pixel: int, channel: int, sample: int, value: float) -> None:
        """set_deep_value(self: OpenImageIO.OpenImageIO.DeepData, pixel: int, channel: int, sample: int, value: float) -> None"""
    def set_deep_value_uint(self, pixel: int, channel: int, sample: int, value: int) -> None:
        """set_deep_value_uint(self: OpenImageIO.OpenImageIO.DeepData, pixel: int, channel: int, sample: int, value: int) -> None"""
    def set_samples(self, pixel: int, nsamples: int) -> None:
        """set_samples(self: OpenImageIO.OpenImageIO.DeepData, pixel: int, nsamples: int) -> None"""
    def sort(self, pixel: int) -> None:
        """sort(self: OpenImageIO.OpenImageIO.DeepData, pixel: int) -> None"""
    def split(self, pixel: int, depth: float) -> bool:
        """split(self: OpenImageIO.OpenImageIO.DeepData, pixel: int, depth: float) -> bool"""
    @property
    def AB_channel(self) -> int: ...
    @property
    def AG_channel(self) -> int: ...
    @property
    def AR_channel(self) -> int: ...
    @property
    def A_channel(self) -> int: ...
    @property
    def Z_channel(self) -> int: ...
    @property
    def Zback_channel(self) -> int: ...
    @property
    def channels(self) -> int: ...
    @property
    def pixels(self) -> int: ...

class ImageBuf:
    orientation: int
    roi_full: ROI
    @overload
    def __init__(self) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: OpenImageIO.OpenImageIO.ImageBuf) -> None

        2. __init__(self: OpenImageIO.OpenImageIO.ImageBuf, arg0: str) -> None

        3. __init__(self: OpenImageIO.OpenImageIO.ImageBuf, arg0: str, arg1: int, arg2: int) -> None

        4. __init__(self: OpenImageIO.OpenImageIO.ImageBuf, arg0: OpenImageIO.OpenImageIO.ImageSpec) -> None

        5. __init__(self: OpenImageIO.OpenImageIO.ImageBuf, arg0: OpenImageIO.OpenImageIO.ImageSpec, arg1: bool) -> None

        6. __init__(self: OpenImageIO.OpenImageIO.ImageBuf, name: str, subimage: int, miplevel: int, config: OpenImageIO.OpenImageIO.ImageSpec) -> None

        7. __init__(self: OpenImageIO.OpenImageIO.ImageBuf, buffer: Buffer) -> None
        """
    @overload
    def __init__(self, arg0: str) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: OpenImageIO.OpenImageIO.ImageBuf) -> None

        2. __init__(self: OpenImageIO.OpenImageIO.ImageBuf, arg0: str) -> None

        3. __init__(self: OpenImageIO.OpenImageIO.ImageBuf, arg0: str, arg1: int, arg2: int) -> None

        4. __init__(self: OpenImageIO.OpenImageIO.ImageBuf, arg0: OpenImageIO.OpenImageIO.ImageSpec) -> None

        5. __init__(self: OpenImageIO.OpenImageIO.ImageBuf, arg0: OpenImageIO.OpenImageIO.ImageSpec, arg1: bool) -> None

        6. __init__(self: OpenImageIO.OpenImageIO.ImageBuf, name: str, subimage: int, miplevel: int, config: OpenImageIO.OpenImageIO.ImageSpec) -> None

        7. __init__(self: OpenImageIO.OpenImageIO.ImageBuf, buffer: Buffer) -> None
        """
    @overload
    def __init__(self, arg0: str, arg1: int, arg2: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: OpenImageIO.OpenImageIO.ImageBuf) -> None

        2. __init__(self: OpenImageIO.OpenImageIO.ImageBuf, arg0: str) -> None

        3. __init__(self: OpenImageIO.OpenImageIO.ImageBuf, arg0: str, arg1: int, arg2: int) -> None

        4. __init__(self: OpenImageIO.OpenImageIO.ImageBuf, arg0: OpenImageIO.OpenImageIO.ImageSpec) -> None

        5. __init__(self: OpenImageIO.OpenImageIO.ImageBuf, arg0: OpenImageIO.OpenImageIO.ImageSpec, arg1: bool) -> None

        6. __init__(self: OpenImageIO.OpenImageIO.ImageBuf, name: str, subimage: int, miplevel: int, config: OpenImageIO.OpenImageIO.ImageSpec) -> None

        7. __init__(self: OpenImageIO.OpenImageIO.ImageBuf, buffer: Buffer) -> None
        """
    @overload
    def __init__(self, arg0: ImageSpec) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: OpenImageIO.OpenImageIO.ImageBuf) -> None

        2. __init__(self: OpenImageIO.OpenImageIO.ImageBuf, arg0: str) -> None

        3. __init__(self: OpenImageIO.OpenImageIO.ImageBuf, arg0: str, arg1: int, arg2: int) -> None

        4. __init__(self: OpenImageIO.OpenImageIO.ImageBuf, arg0: OpenImageIO.OpenImageIO.ImageSpec) -> None

        5. __init__(self: OpenImageIO.OpenImageIO.ImageBuf, arg0: OpenImageIO.OpenImageIO.ImageSpec, arg1: bool) -> None

        6. __init__(self: OpenImageIO.OpenImageIO.ImageBuf, name: str, subimage: int, miplevel: int, config: OpenImageIO.OpenImageIO.ImageSpec) -> None

        7. __init__(self: OpenImageIO.OpenImageIO.ImageBuf, buffer: Buffer) -> None
        """
    @overload
    def __init__(self, arg0: ImageSpec, arg1: bool) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: OpenImageIO.OpenImageIO.ImageBuf) -> None

        2. __init__(self: OpenImageIO.OpenImageIO.ImageBuf, arg0: str) -> None

        3. __init__(self: OpenImageIO.OpenImageIO.ImageBuf, arg0: str, arg1: int, arg2: int) -> None

        4. __init__(self: OpenImageIO.OpenImageIO.ImageBuf, arg0: OpenImageIO.OpenImageIO.ImageSpec) -> None

        5. __init__(self: OpenImageIO.OpenImageIO.ImageBuf, arg0: OpenImageIO.OpenImageIO.ImageSpec, arg1: bool) -> None

        6. __init__(self: OpenImageIO.OpenImageIO.ImageBuf, name: str, subimage: int, miplevel: int, config: OpenImageIO.OpenImageIO.ImageSpec) -> None

        7. __init__(self: OpenImageIO.OpenImageIO.ImageBuf, buffer: Buffer) -> None
        """
    @overload
    def __init__(self, name: str, subimage: int, miplevel: int, config: ImageSpec) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: OpenImageIO.OpenImageIO.ImageBuf) -> None

        2. __init__(self: OpenImageIO.OpenImageIO.ImageBuf, arg0: str) -> None

        3. __init__(self: OpenImageIO.OpenImageIO.ImageBuf, arg0: str, arg1: int, arg2: int) -> None

        4. __init__(self: OpenImageIO.OpenImageIO.ImageBuf, arg0: OpenImageIO.OpenImageIO.ImageSpec) -> None

        5. __init__(self: OpenImageIO.OpenImageIO.ImageBuf, arg0: OpenImageIO.OpenImageIO.ImageSpec, arg1: bool) -> None

        6. __init__(self: OpenImageIO.OpenImageIO.ImageBuf, name: str, subimage: int, miplevel: int, config: OpenImageIO.OpenImageIO.ImageSpec) -> None

        7. __init__(self: OpenImageIO.OpenImageIO.ImageBuf, buffer: Buffer) -> None
        """
    @overload
    def __init__(self, buffer: Buffer) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: OpenImageIO.OpenImageIO.ImageBuf) -> None

        2. __init__(self: OpenImageIO.OpenImageIO.ImageBuf, arg0: str) -> None

        3. __init__(self: OpenImageIO.OpenImageIO.ImageBuf, arg0: str, arg1: int, arg2: int) -> None

        4. __init__(self: OpenImageIO.OpenImageIO.ImageBuf, arg0: OpenImageIO.OpenImageIO.ImageSpec) -> None

        5. __init__(self: OpenImageIO.OpenImageIO.ImageBuf, arg0: OpenImageIO.OpenImageIO.ImageSpec, arg1: bool) -> None

        6. __init__(self: OpenImageIO.OpenImageIO.ImageBuf, name: str, subimage: int, miplevel: int, config: OpenImageIO.OpenImageIO.ImageSpec) -> None

        7. __init__(self: OpenImageIO.OpenImageIO.ImageBuf, buffer: Buffer) -> None
        """
    def _pybind11_conduit_v1_(self, *args, **kwargs): ...
    def clear(self) -> None:
        """clear(self: OpenImageIO.OpenImageIO.ImageBuf) -> None"""
    def clear_thumbnail(self) -> None:
        """clear_thumbnail(self: OpenImageIO.OpenImageIO.ImageBuf) -> None"""
    @overload
    def copy(self, src: ImageBuf, format: TypeDesc = ...) -> bool:
        """copy(*args, **kwargs)
        Overloaded function.

        1. copy(self: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, format: OpenImageIO.OpenImageIO.TypeDesc = <TypeDesc 'unknown'>) -> bool

        2. copy(self: OpenImageIO.OpenImageIO.ImageBuf, format: OpenImageIO.OpenImageIO.TypeDesc = <TypeDesc 'unknown'>) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    def copy(self, format: TypeDesc = ...) -> ImageBuf:
        """copy(*args, **kwargs)
        Overloaded function.

        1. copy(self: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, format: OpenImageIO.OpenImageIO.TypeDesc = <TypeDesc 'unknown'>) -> bool

        2. copy(self: OpenImageIO.OpenImageIO.ImageBuf, format: OpenImageIO.OpenImageIO.TypeDesc = <TypeDesc 'unknown'>) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    def copy_metadata(self, arg0: ImageBuf) -> None:
        """copy_metadata(self: OpenImageIO.OpenImageIO.ImageBuf, arg0: OpenImageIO.OpenImageIO.ImageBuf) -> None"""
    def copy_pixels(self, arg0: ImageBuf) -> bool:
        """copy_pixels(self: OpenImageIO.OpenImageIO.ImageBuf, arg0: OpenImageIO.OpenImageIO.ImageBuf) -> bool"""
    def deep_erase_samples(self, x: int, y: int, z: int = ..., samplepos: int, nsamples: int = ...) -> None:
        """deep_erase_samples(self: OpenImageIO.OpenImageIO.ImageBuf, x: int, y: int, z: int = 0, samplepos: int, nsamples: int = 1) -> None"""
    def deep_insert_samples(self, x: int, y: int, z: int = ..., samplepos: int, nsamples: int = ...) -> None:
        """deep_insert_samples(self: OpenImageIO.OpenImageIO.ImageBuf, x: int, y: int, z: int = 0, samplepos: int, nsamples: int = 1) -> None"""
    def deep_samples(self, x: int, y: int, z: int = ...) -> int:
        """deep_samples(self: OpenImageIO.OpenImageIO.ImageBuf, x: int, y: int, z: int = 0) -> int"""
    def deep_value(self, x: int, y: int, z: int, channel: int, sample: int) -> float:
        """deep_value(self: OpenImageIO.OpenImageIO.ImageBuf, x: int, y: int, z: int, channel: int, sample: int) -> float"""
    def deep_value_uint(self, x: int, y: int, z: int, channel: int, sample: int) -> int:
        """deep_value_uint(self: OpenImageIO.OpenImageIO.ImageBuf, x: int, y: int, z: int, channel: int, sample: int) -> int"""
    def deepdata(self) -> DeepData:
        """deepdata(self: OpenImageIO.OpenImageIO.ImageBuf) -> OpenImageIO.OpenImageIO.DeepData"""
    def get_pixels(self, format: TypeDesc = ..., roi: ROI = ...) -> object:
        """get_pixels(self: OpenImageIO.OpenImageIO.ImageBuf, format: OpenImageIO.OpenImageIO.TypeDesc = <TypeDesc 'float'>, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>) -> object"""
    def get_thumbnail(self) -> ImageBuf:
        """get_thumbnail(self: OpenImageIO.OpenImageIO.ImageBuf) -> OpenImageIO.OpenImageIO.ImageBuf"""
    def getchannel(self, x: int, y: int, z: int, c: int, wrap=...) -> float:
        """getchannel(self: OpenImageIO.OpenImageIO.ImageBuf, x: int, y: int, z: int, c: int, wrap: OpenImageIO_v3_0::ImageBuf::WrapMode = 'black') -> float"""
    def geterror(self, clear: bool = ...) -> str:
        """geterror(self: OpenImageIO.OpenImageIO.ImageBuf, clear: bool = True) -> str"""
    def getpixel(self, x: int, y: int, z: int = ..., wrap: str = ...) -> tuple:
        """getpixel(self: OpenImageIO.OpenImageIO.ImageBuf, x: int, y: int, z: int = 0, wrap: str = 'black') -> tuple"""
    def init_spec(self, filename: str, subimage: int = ..., miplevel: int = ...) -> None:
        """init_spec(self: OpenImageIO.OpenImageIO.ImageBuf, filename: str, subimage: int = 0, miplevel: int = 0) -> None"""
    def interppixel(self, x: float, y: float, wrap: str = ...) -> tuple:
        """interppixel(self: OpenImageIO.OpenImageIO.ImageBuf, x: float, y: float, wrap: str = 'black') -> tuple"""
    def interppixel_NDC(self, x: float, y: float, wrap: str = ...) -> tuple:
        """interppixel_NDC(self: OpenImageIO.OpenImageIO.ImageBuf, x: float, y: float, wrap: str = 'black') -> tuple"""
    def interppixel_NDC_full(self, x: float, y: float, wrap: str = ...) -> tuple:
        """interppixel_NDC_full(self: OpenImageIO.OpenImageIO.ImageBuf, x: float, y: float, wrap: str = 'black') -> tuple"""
    def interppixel_bicubic(self, x: float, y: float, wrap: str = ...) -> tuple:
        """interppixel_bicubic(self: OpenImageIO.OpenImageIO.ImageBuf, x: float, y: float, wrap: str = 'black') -> tuple"""
    def interppixel_bicubic_NDC(self, x: float, y: float, wrap: str = ...) -> tuple:
        """interppixel_bicubic_NDC(self: OpenImageIO.OpenImageIO.ImageBuf, x: float, y: float, wrap: str = 'black') -> tuple"""
    def make_writable(self, keep_cache_type: bool = ...) -> bool:
        """make_writable(self: OpenImageIO.OpenImageIO.ImageBuf, keep_cache_type: bool = False) -> bool"""
    def nativespec(self) -> ImageSpec:
        """nativespec(self: OpenImageIO.OpenImageIO.ImageBuf) -> OpenImageIO.OpenImageIO.ImageSpec"""
    def pixelindex(self, x: int, y: int, z: int, check_range: bool = ...) -> int:
        """pixelindex(self: OpenImageIO.OpenImageIO.ImageBuf, x: int, y: int, z: int, check_range: bool = False) -> int"""
    @overload
    def read(self, subimage: int, miplevel: int, chbegin: int, chend: int, force: bool, convert: TypeDesc) -> bool:
        """read(*args, **kwargs)
        Overloaded function.

        1. read(self: OpenImageIO.OpenImageIO.ImageBuf, subimage: int, miplevel: int, chbegin: int, chend: int, force: bool, convert: OpenImageIO.OpenImageIO.TypeDesc) -> bool

        2. read(self: OpenImageIO.OpenImageIO.ImageBuf, subimage: int = 0, miplevel: int = 0, force: bool = False, convert: OpenImageIO.OpenImageIO.TypeDesc = <TypeDesc 'unknown'>) -> bool
        """
    @overload
    def read(self, subimage: int = ..., miplevel: int = ..., force: bool = ..., convert: TypeDesc = ...) -> bool:
        """read(*args, **kwargs)
        Overloaded function.

        1. read(self: OpenImageIO.OpenImageIO.ImageBuf, subimage: int, miplevel: int, chbegin: int, chend: int, force: bool, convert: OpenImageIO.OpenImageIO.TypeDesc) -> bool

        2. read(self: OpenImageIO.OpenImageIO.ImageBuf, subimage: int = 0, miplevel: int = 0, force: bool = False, convert: OpenImageIO.OpenImageIO.TypeDesc = <TypeDesc 'unknown'>) -> bool
        """
    @overload
    def reset(self, name: str, subimage: int = ..., miplevel: int = ...) -> None:
        """reset(*args, **kwargs)
        Overloaded function.

        1. reset(self: OpenImageIO.OpenImageIO.ImageBuf, name: str, subimage: int = 0, miplevel: int = 0) -> None

        2. reset(self: OpenImageIO.OpenImageIO.ImageBuf, name: str, subimage: int = 0, miplevel: int = 0, config: OpenImageIO.OpenImageIO.ImageSpec = <OpenImageIO.OpenImageIO.ImageSpec object>) -> None

        3. reset(self: OpenImageIO.OpenImageIO.ImageBuf, spec: OpenImageIO.OpenImageIO.ImageSpec, zero: bool = True) -> None

        4. reset(self: OpenImageIO.OpenImageIO.ImageBuf, buffer: Buffer) -> None
        """
    @overload
    def reset(self, name: str, subimage: int = ..., miplevel: int = ..., config: ImageSpec = ...) -> None:
        """reset(*args, **kwargs)
        Overloaded function.

        1. reset(self: OpenImageIO.OpenImageIO.ImageBuf, name: str, subimage: int = 0, miplevel: int = 0) -> None

        2. reset(self: OpenImageIO.OpenImageIO.ImageBuf, name: str, subimage: int = 0, miplevel: int = 0, config: OpenImageIO.OpenImageIO.ImageSpec = <OpenImageIO.OpenImageIO.ImageSpec object>) -> None

        3. reset(self: OpenImageIO.OpenImageIO.ImageBuf, spec: OpenImageIO.OpenImageIO.ImageSpec, zero: bool = True) -> None

        4. reset(self: OpenImageIO.OpenImageIO.ImageBuf, buffer: Buffer) -> None
        """
    @overload
    def reset(self, spec: ImageSpec, zero: bool = ...) -> None:
        """reset(*args, **kwargs)
        Overloaded function.

        1. reset(self: OpenImageIO.OpenImageIO.ImageBuf, name: str, subimage: int = 0, miplevel: int = 0) -> None

        2. reset(self: OpenImageIO.OpenImageIO.ImageBuf, name: str, subimage: int = 0, miplevel: int = 0, config: OpenImageIO.OpenImageIO.ImageSpec = <OpenImageIO.OpenImageIO.ImageSpec object>) -> None

        3. reset(self: OpenImageIO.OpenImageIO.ImageBuf, spec: OpenImageIO.OpenImageIO.ImageSpec, zero: bool = True) -> None

        4. reset(self: OpenImageIO.OpenImageIO.ImageBuf, buffer: Buffer) -> None
        """
    @overload
    def reset(self, buffer: Buffer) -> None:
        """reset(*args, **kwargs)
        Overloaded function.

        1. reset(self: OpenImageIO.OpenImageIO.ImageBuf, name: str, subimage: int = 0, miplevel: int = 0) -> None

        2. reset(self: OpenImageIO.OpenImageIO.ImageBuf, name: str, subimage: int = 0, miplevel: int = 0, config: OpenImageIO.OpenImageIO.ImageSpec = <OpenImageIO.OpenImageIO.ImageSpec object>) -> None

        3. reset(self: OpenImageIO.OpenImageIO.ImageBuf, spec: OpenImageIO.OpenImageIO.ImageSpec, zero: bool = True) -> None

        4. reset(self: OpenImageIO.OpenImageIO.ImageBuf, buffer: Buffer) -> None
        """
    def set_deep_samples(self, x: int, y: int, z: int = ..., nsamples: int = ...) -> None:
        """set_deep_samples(self: OpenImageIO.OpenImageIO.ImageBuf, x: int, y: int, z: int = 0, nsamples: int = 1) -> None"""
    def set_deep_value(self, x: int, y: int, z: int, channel: int, sample: int, value: float = ...) -> None:
        """set_deep_value(self: OpenImageIO.OpenImageIO.ImageBuf, x: int, y: int, z: int, channel: int, sample: int, value: float = 0.0) -> None"""
    def set_deep_value_uint(self, x: int, y: int, z: int, channel: int, sample: int, value: int = ...) -> None:
        """set_deep_value_uint(self: OpenImageIO.OpenImageIO.ImageBuf, x: int, y: int, z: int, channel: int, sample: int, value: int = 0) -> None"""
    def set_full(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> None:
        """set_full(self: OpenImageIO.OpenImageIO.ImageBuf, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> None"""
    def set_origin(self, x: int, y: int, z: int = ...) -> None:
        """set_origin(self: OpenImageIO.OpenImageIO.ImageBuf, x: int, y: int, z: int = 0) -> None"""
    def set_pixels(self, roi: ROI, pixels: Buffer) -> bool:
        """set_pixels(self: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI, pixels: Buffer) -> bool"""
    def set_thumbnail(self, thumb: ImageBuf) -> None:
        """set_thumbnail(self: OpenImageIO.OpenImageIO.ImageBuf, thumb: OpenImageIO.OpenImageIO.ImageBuf) -> None"""
    def set_write_format(self, arg0: object) -> None:
        """set_write_format(self: OpenImageIO.OpenImageIO.ImageBuf, arg0: object) -> None"""
    def set_write_tiles(self, width: int = ..., height: int = ..., depth: int = ...) -> None:
        """set_write_tiles(self: OpenImageIO.OpenImageIO.ImageBuf, width: int = 0, height: int = 0, depth: int = 0) -> None"""
    @overload
    def setpixel(self, x: int, y: int, z: int, pixel: object) -> None:
        """setpixel(*args, **kwargs)
        Overloaded function.

        1. setpixel(self: OpenImageIO.OpenImageIO.ImageBuf, x: int, y: int, z: int, pixel: object) -> None

        2. setpixel(self: OpenImageIO.OpenImageIO.ImageBuf, x: int, y: int, pixel: object) -> None

        3. setpixel(self: OpenImageIO.OpenImageIO.ImageBuf, i: int, pixel: object) -> None
        """
    @overload
    def setpixel(self, x: int, y: int, pixel: object) -> None:
        """setpixel(*args, **kwargs)
        Overloaded function.

        1. setpixel(self: OpenImageIO.OpenImageIO.ImageBuf, x: int, y: int, z: int, pixel: object) -> None

        2. setpixel(self: OpenImageIO.OpenImageIO.ImageBuf, x: int, y: int, pixel: object) -> None

        3. setpixel(self: OpenImageIO.OpenImageIO.ImageBuf, i: int, pixel: object) -> None
        """
    @overload
    def setpixel(self, i: int, pixel: object) -> None:
        """setpixel(*args, **kwargs)
        Overloaded function.

        1. setpixel(self: OpenImageIO.OpenImageIO.ImageBuf, x: int, y: int, z: int, pixel: object) -> None

        2. setpixel(self: OpenImageIO.OpenImageIO.ImageBuf, x: int, y: int, pixel: object) -> None

        3. setpixel(self: OpenImageIO.OpenImageIO.ImageBuf, i: int, pixel: object) -> None
        """
    def spec(self) -> ImageSpec:
        """spec(self: OpenImageIO.OpenImageIO.ImageBuf) -> OpenImageIO.OpenImageIO.ImageSpec"""
    def specmod(self) -> ImageSpec:
        """specmod(self: OpenImageIO.OpenImageIO.ImageBuf) -> OpenImageIO.OpenImageIO.ImageSpec"""
    def swap(self, arg0: ImageBuf) -> None:
        """swap(self: OpenImageIO.OpenImageIO.ImageBuf, arg0: OpenImageIO.OpenImageIO.ImageBuf) -> None"""
    @overload
    def write(self, filename: str, dtype: TypeDesc = ..., fileformat: str = ...) -> bool:
        """write(*args, **kwargs)
        Overloaded function.

        1. write(self: OpenImageIO.OpenImageIO.ImageBuf, filename: str, dtype: OpenImageIO.OpenImageIO.TypeDesc = <TypeDesc 'unknown'>, fileformat: str = '') -> bool

        2. write(self: OpenImageIO.OpenImageIO.ImageBuf, out: OpenImageIO.OpenImageIO.ImageOutput) -> bool
        """
    @overload
    def write(self, out: ImageOutput) -> bool:
        """write(*args, **kwargs)
        Overloaded function.

        1. write(self: OpenImageIO.OpenImageIO.ImageBuf, filename: str, dtype: OpenImageIO.OpenImageIO.TypeDesc = <TypeDesc 'unknown'>, fileformat: str = '') -> bool

        2. write(self: OpenImageIO.OpenImageIO.ImageBuf, out: OpenImageIO.OpenImageIO.ImageOutput) -> bool
        """
    @property
    def deep(self) -> bool: ...
    @property
    def file_format_name(self) -> str: ...
    @property
    def has_error(self) -> bool: ...
    @property
    def has_thumbnail(self) -> bool: ...
    @property
    def initialized(self) -> bool: ...
    @property
    def miplevel(self) -> int: ...
    @property
    def name(self) -> str: ...
    @property
    def nchannels(self) -> int: ...
    @property
    def nmiplevels(self) -> int: ...
    @property
    def nsubimages(self) -> int: ...
    @property
    def oriented_full_height(self) -> int: ...
    @property
    def oriented_full_width(self) -> int: ...
    @property
    def oriented_full_x(self) -> int: ...
    @property
    def oriented_full_y(self) -> int: ...
    @property
    def oriented_height(self) -> int: ...
    @property
    def oriented_width(self) -> int: ...
    @property
    def oriented_x(self) -> int: ...
    @property
    def oriented_y(self) -> int: ...
    @property
    def pixels_valid(self) -> bool: ...
    @property
    def pixeltype(self) -> TypeDesc: ...
    @property
    def roi(self) -> ROI: ...
    @property
    def subimage(self) -> int: ...
    @property
    def xbegin(self) -> int: ...
    @property
    def xend(self) -> int: ...
    @property
    def xmax(self) -> int: ...
    @property
    def xmin(self) -> int: ...
    @property
    def ybegin(self) -> int: ...
    @property
    def yend(self) -> int: ...
    @property
    def ymax(self) -> int: ...
    @property
    def ymin(self) -> int: ...
    @property
    def zbegin(self) -> int: ...
    @property
    def zend(self) -> int: ...
    @property
    def zmax(self) -> int: ...
    @property
    def zmin(self) -> int: ...

class ImageBufAlgo:
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def _pybind11_conduit_v1_(self, *args, **kwargs): ...
    @overload
    @staticmethod
    def abs(dst: ImageBuf, A: ImageBuf, roi: ROI = ..., nthreads: int = ...) -> bool:
        """abs(*args, **kwargs)
        Overloaded function.

        1. abs(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. abs(A: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def abs(A: ImageBuf, roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """abs(*args, **kwargs)
        Overloaded function.

        1. abs(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. abs(A: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def absdiff(dst: ImageBuf, A: ImageBuf, B: ImageBuf, roi: ROI = ..., nthreads: int = ...) -> bool:
        """absdiff(*args, **kwargs)
        Overloaded function.

        1. absdiff(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. absdiff(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        3. absdiff(A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        4. absdiff(A: OpenImageIO.OpenImageIO.ImageBuf, B: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def absdiff(dst: ImageBuf, A: ImageBuf, B: object, roi: ROI = ..., nthreads: int = ...) -> bool:
        """absdiff(*args, **kwargs)
        Overloaded function.

        1. absdiff(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. absdiff(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        3. absdiff(A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        4. absdiff(A: OpenImageIO.OpenImageIO.ImageBuf, B: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def absdiff(A: ImageBuf, B: ImageBuf, roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """absdiff(*args, **kwargs)
        Overloaded function.

        1. absdiff(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. absdiff(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        3. absdiff(A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        4. absdiff(A: OpenImageIO.OpenImageIO.ImageBuf, B: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def absdiff(A: ImageBuf, B: object, roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """absdiff(*args, **kwargs)
        Overloaded function.

        1. absdiff(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. absdiff(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        3. absdiff(A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        4. absdiff(A: OpenImageIO.OpenImageIO.ImageBuf, B: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def add(dst: ImageBuf, A: ImageBuf, B: ImageBuf, roi: ROI = ..., nthreads: int = ...) -> bool:
        """add(*args, **kwargs)
        Overloaded function.

        1. add(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. add(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        3. add(A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        4. add(A: OpenImageIO.OpenImageIO.ImageBuf, B: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def add(dst: ImageBuf, A: ImageBuf, B: object, roi: ROI = ..., nthreads: int = ...) -> bool:
        """add(*args, **kwargs)
        Overloaded function.

        1. add(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. add(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        3. add(A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        4. add(A: OpenImageIO.OpenImageIO.ImageBuf, B: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def add(A: ImageBuf, B: ImageBuf, roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """add(*args, **kwargs)
        Overloaded function.

        1. add(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. add(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        3. add(A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        4. add(A: OpenImageIO.OpenImageIO.ImageBuf, B: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def add(A: ImageBuf, B: object, roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """add(*args, **kwargs)
        Overloaded function.

        1. add(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. add(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        3. add(A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        4. add(A: OpenImageIO.OpenImageIO.ImageBuf, B: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @staticmethod
    def bluenoise_image() -> ImageBuf:
        """bluenoise_image() -> OpenImageIO.OpenImageIO.ImageBuf"""
    @overload
    @staticmethod
    def channel_append(dst: ImageBuf, A: ImageBuf, B: ImageBuf, roi: ROI = ..., nthreads: int = ...) -> bool:
        """channel_append(*args, **kwargs)
        Overloaded function.

        1. channel_append(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. channel_append(A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def channel_append(A: ImageBuf, B: ImageBuf, roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """channel_append(*args, **kwargs)
        Overloaded function.

        1. channel_append(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. channel_append(A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def channel_sum(dst: ImageBuf, src: ImageBuf, roi: ROI = ..., nthreads: int = ...) -> bool:
        """channel_sum(*args, **kwargs)
        Overloaded function.

        1. channel_sum(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. channel_sum(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, weight: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        3. channel_sum(src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        4. channel_sum(src: OpenImageIO.OpenImageIO.ImageBuf, weight: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def channel_sum(dst: ImageBuf, src: ImageBuf, weight: object, roi: ROI = ..., nthreads: int = ...) -> bool:
        """channel_sum(*args, **kwargs)
        Overloaded function.

        1. channel_sum(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. channel_sum(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, weight: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        3. channel_sum(src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        4. channel_sum(src: OpenImageIO.OpenImageIO.ImageBuf, weight: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def channel_sum(src: ImageBuf, roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """channel_sum(*args, **kwargs)
        Overloaded function.

        1. channel_sum(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. channel_sum(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, weight: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        3. channel_sum(src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        4. channel_sum(src: OpenImageIO.OpenImageIO.ImageBuf, weight: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def channel_sum(src: ImageBuf, weight: object, roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """channel_sum(*args, **kwargs)
        Overloaded function.

        1. channel_sum(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. channel_sum(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, weight: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        3. channel_sum(src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        4. channel_sum(src: OpenImageIO.OpenImageIO.ImageBuf, weight: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def channels(dst: ImageBuf, src: ImageBuf, channelorder: tuple, newchannelnames: tuple = ..., shuffle_channel_names: bool = ..., nthreads: int = ...) -> bool:
        """channels(*args, **kwargs)
        Overloaded function.

        1. channels(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, channelorder: tuple, newchannelnames: tuple = (), shuffle_channel_names: bool = False, nthreads: int = 0) -> bool

        2. channels(src: OpenImageIO.OpenImageIO.ImageBuf, channelorder: tuple, newchannelnames: tuple = (), shuffle_channel_names: bool = False, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def channels(src: ImageBuf, channelorder: tuple, newchannelnames: tuple = ..., shuffle_channel_names: bool = ..., nthreads: int = ...) -> ImageBuf:
        """channels(*args, **kwargs)
        Overloaded function.

        1. channels(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, channelorder: tuple, newchannelnames: tuple = (), shuffle_channel_names: bool = False, nthreads: int = 0) -> bool

        2. channels(src: OpenImageIO.OpenImageIO.ImageBuf, channelorder: tuple, newchannelnames: tuple = (), shuffle_channel_names: bool = False, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def checker(dst: ImageBuf, width: int, height: int, depth: int, color1: object, color2: object, xoffset: int = ..., yoffset: int = ..., zoffset: int = ..., roi: ROI = ..., nthreads: int = ...) -> bool:
        """checker(*args, **kwargs)
        Overloaded function.

        1. checker(dst: OpenImageIO.OpenImageIO.ImageBuf, width: int, height: int, depth: int, color1: object, color2: object, xoffset: int = 0, yoffset: int = 0, zoffset: int = 0, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. checker(width: int, height: int, depth: int, color1: object, color2: object, xoffset: int = 0, yoffset: int = 0, zoffset: int = 0, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def checker(width: int, height: int, depth: int, color1: object, color2: object, xoffset: int = ..., yoffset: int = ..., zoffset: int = ..., roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """checker(*args, **kwargs)
        Overloaded function.

        1. checker(dst: OpenImageIO.OpenImageIO.ImageBuf, width: int, height: int, depth: int, color1: object, color2: object, xoffset: int = 0, yoffset: int = 0, zoffset: int = 0, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. checker(width: int, height: int, depth: int, color1: object, color2: object, xoffset: int = 0, yoffset: int = 0, zoffset: int = 0, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def circular_shift(dst: ImageBuf, src: ImageBuf, xshift: int, yshift: int, zshift: int = ..., roi: ROI = ..., nthreads: int = ...) -> bool:
        """circular_shift(*args, **kwargs)
        Overloaded function.

        1. circular_shift(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, xshift: int, yshift: int, zshift: int = 0, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. circular_shift(src: OpenImageIO.OpenImageIO.ImageBuf, xshift: int, yshift: int, zshift: int = 0, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def circular_shift(src: ImageBuf, xshift: int, yshift: int, zshift: int = ..., roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """circular_shift(*args, **kwargs)
        Overloaded function.

        1. circular_shift(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, xshift: int, yshift: int, zshift: int = 0, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. circular_shift(src: OpenImageIO.OpenImageIO.ImageBuf, xshift: int, yshift: int, zshift: int = 0, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def clamp(dst: ImageBuf, src: ImageBuf, min: object, max: object, clampalpha01: bool = ..., roi: ROI = ..., nthreads: int = ...) -> bool:
        """clamp(*args, **kwargs)
        Overloaded function.

        1. clamp(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, min: object, max: object, clampalpha01: bool = False, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. clamp(src: OpenImageIO.OpenImageIO.ImageBuf, min: object, max: object, clampalpha01: bool = False, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def clamp(src: ImageBuf, min: object, max: object, clampalpha01: bool = ..., roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """clamp(*args, **kwargs)
        Overloaded function.

        1. clamp(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, min: object, max: object, clampalpha01: bool = False, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. clamp(src: OpenImageIO.OpenImageIO.ImageBuf, min: object, max: object, clampalpha01: bool = False, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def color_map(dst: ImageBuf, src: ImageBuf, srcchannel: int, mapname: str, roi: ROI = ..., nthreads: int = ...) -> bool:
        """color_map(*args, **kwargs)
        Overloaded function.

        1. color_map(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, srcchannel: int, mapname: str, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. color_map(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, srcchannel: int, nknots: int, channels: int, knots: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        3. color_map(src: OpenImageIO.OpenImageIO.ImageBuf, srcchannel: int, mapname: str, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        4. color_map(src: OpenImageIO.OpenImageIO.ImageBuf, srcchannel: int, nknots: int, channels: int, knots: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def color_map(dst: ImageBuf, src: ImageBuf, srcchannel: int, nknots: int, channels: int, knots: object, roi: ROI = ..., nthreads: int = ...) -> bool:
        """color_map(*args, **kwargs)
        Overloaded function.

        1. color_map(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, srcchannel: int, mapname: str, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. color_map(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, srcchannel: int, nknots: int, channels: int, knots: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        3. color_map(src: OpenImageIO.OpenImageIO.ImageBuf, srcchannel: int, mapname: str, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        4. color_map(src: OpenImageIO.OpenImageIO.ImageBuf, srcchannel: int, nknots: int, channels: int, knots: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def color_map(src: ImageBuf, srcchannel: int, mapname: str, roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """color_map(*args, **kwargs)
        Overloaded function.

        1. color_map(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, srcchannel: int, mapname: str, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. color_map(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, srcchannel: int, nknots: int, channels: int, knots: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        3. color_map(src: OpenImageIO.OpenImageIO.ImageBuf, srcchannel: int, mapname: str, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        4. color_map(src: OpenImageIO.OpenImageIO.ImageBuf, srcchannel: int, nknots: int, channels: int, knots: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def color_map(src: ImageBuf, srcchannel: int, nknots: int, channels: int, knots: object, roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """color_map(*args, **kwargs)
        Overloaded function.

        1. color_map(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, srcchannel: int, mapname: str, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. color_map(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, srcchannel: int, nknots: int, channels: int, knots: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        3. color_map(src: OpenImageIO.OpenImageIO.ImageBuf, srcchannel: int, mapname: str, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        4. color_map(src: OpenImageIO.OpenImageIO.ImageBuf, srcchannel: int, nknots: int, channels: int, knots: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @staticmethod
    def color_range_check(src: ImageBuf, low: object, high: object, roi: ROI = ..., nthreads: int = ...) -> object:
        """color_range_check(src: OpenImageIO.OpenImageIO.ImageBuf, low: object, high: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> object"""
    @overload
    @staticmethod
    def colorconvert(dst: ImageBuf, src: ImageBuf, fromspace: str, tospace: str, unpremult: bool = ..., roi: ROI = ..., nthreads: int = ...) -> bool:
        """colorconvert(*args, **kwargs)
        Overloaded function.

        1. colorconvert(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, fromspace: str, tospace: str, unpremult: bool = True, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. colorconvert(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, fromspace: str, tospace: str, unpremult: bool = True, context_key: str = '', context_value: str = '', colorconfig: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        3. colorconvert(src: OpenImageIO.OpenImageIO.ImageBuf, fromspace: str, tospace: str, unpremult: bool = True, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        4. colorconvert(src: OpenImageIO.OpenImageIO.ImageBuf, fromspace: str, tospace: str, unpremult: bool = True, context_key: str = '', context_value: str = '', colorconfig: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def colorconvert(dst: ImageBuf, src: ImageBuf, fromspace: str, tospace: str, unpremult: bool = ..., context_key: str = ..., context_value: str = ..., colorconfig: str = ..., roi: ROI = ..., nthreads: int = ...) -> bool:
        """colorconvert(*args, **kwargs)
        Overloaded function.

        1. colorconvert(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, fromspace: str, tospace: str, unpremult: bool = True, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. colorconvert(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, fromspace: str, tospace: str, unpremult: bool = True, context_key: str = '', context_value: str = '', colorconfig: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        3. colorconvert(src: OpenImageIO.OpenImageIO.ImageBuf, fromspace: str, tospace: str, unpremult: bool = True, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        4. colorconvert(src: OpenImageIO.OpenImageIO.ImageBuf, fromspace: str, tospace: str, unpremult: bool = True, context_key: str = '', context_value: str = '', colorconfig: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def colorconvert(src: ImageBuf, fromspace: str, tospace: str, unpremult: bool = ..., roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """colorconvert(*args, **kwargs)
        Overloaded function.

        1. colorconvert(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, fromspace: str, tospace: str, unpremult: bool = True, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. colorconvert(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, fromspace: str, tospace: str, unpremult: bool = True, context_key: str = '', context_value: str = '', colorconfig: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        3. colorconvert(src: OpenImageIO.OpenImageIO.ImageBuf, fromspace: str, tospace: str, unpremult: bool = True, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        4. colorconvert(src: OpenImageIO.OpenImageIO.ImageBuf, fromspace: str, tospace: str, unpremult: bool = True, context_key: str = '', context_value: str = '', colorconfig: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def colorconvert(src: ImageBuf, fromspace: str, tospace: str, unpremult: bool = ..., context_key: str = ..., context_value: str = ..., colorconfig: str = ..., roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """colorconvert(*args, **kwargs)
        Overloaded function.

        1. colorconvert(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, fromspace: str, tospace: str, unpremult: bool = True, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. colorconvert(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, fromspace: str, tospace: str, unpremult: bool = True, context_key: str = '', context_value: str = '', colorconfig: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        3. colorconvert(src: OpenImageIO.OpenImageIO.ImageBuf, fromspace: str, tospace: str, unpremult: bool = True, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        4. colorconvert(src: OpenImageIO.OpenImageIO.ImageBuf, fromspace: str, tospace: str, unpremult: bool = True, context_key: str = '', context_value: str = '', colorconfig: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def colormatrixtransform(dst: ImageBuf, src: ImageBuf, M: object, unpremult: bool = ..., roi: ROI = ..., nthreads: int = ...) -> bool:
        """colormatrixtransform(*args, **kwargs)
        Overloaded function.

        1. colormatrixtransform(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, M: object, unpremult: bool = True, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. colormatrixtransform(src: OpenImageIO.OpenImageIO.ImageBuf, M: object, unpremult: bool = True, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def colormatrixtransform(src: ImageBuf, M: object, unpremult: bool = ..., roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """colormatrixtransform(*args, **kwargs)
        Overloaded function.

        1. colormatrixtransform(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, M: object, unpremult: bool = True, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. colormatrixtransform(src: OpenImageIO.OpenImageIO.ImageBuf, M: object, unpremult: bool = True, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def compare(A: ImageBuf, B: ImageBuf, failthresh: float, warnthresh: float, result: CompareResults, roi: ROI = ..., nthreads: int = ...) -> bool:
        """compare(*args, **kwargs)
        Overloaded function.

        1. compare(A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, failthresh: float, warnthresh: float, result: OpenImageIO.OpenImageIO.CompareResults, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. compare(A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, failthresh: float, warnthresh: float, failrelative: float = 0.0, warnrelative: float = 0.0, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.CompareResults

        3. compare(A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, failthresh: float, warnthresh: float, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.CompareResults
        """
    @overload
    @staticmethod
    def compare(A: ImageBuf, B: ImageBuf, failthresh: float, warnthresh: float, failrelative: float = ..., warnrelative: float = ..., roi: ROI = ..., nthreads: int = ...) -> CompareResults:
        """compare(*args, **kwargs)
        Overloaded function.

        1. compare(A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, failthresh: float, warnthresh: float, result: OpenImageIO.OpenImageIO.CompareResults, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. compare(A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, failthresh: float, warnthresh: float, failrelative: float = 0.0, warnrelative: float = 0.0, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.CompareResults

        3. compare(A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, failthresh: float, warnthresh: float, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.CompareResults
        """
    @overload
    @staticmethod
    def compare(A: ImageBuf, B: ImageBuf, failthresh: float, warnthresh: float, roi: ROI = ..., nthreads: int = ...) -> CompareResults:
        """compare(*args, **kwargs)
        Overloaded function.

        1. compare(A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, failthresh: float, warnthresh: float, result: OpenImageIO.OpenImageIO.CompareResults, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. compare(A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, failthresh: float, warnthresh: float, failrelative: float = 0.0, warnrelative: float = 0.0, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.CompareResults

        3. compare(A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, failthresh: float, warnthresh: float, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.CompareResults
        """
    @staticmethod
    def compare_Yee(A: ImageBuf, B: ImageBuf, result: CompareResults, luminance: float = ..., fov: float = ..., roi: ROI = ..., nthreads: int = ...) -> bool:
        """compare_Yee(A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, result: OpenImageIO.OpenImageIO.CompareResults, luminance: float = 100, fov: float = 45, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool"""
    @overload
    @staticmethod
    def complex_to_polar(dst: ImageBuf, src: ImageBuf, roi: ROI = ..., nthreads: int = ...) -> bool:
        """complex_to_polar(*args, **kwargs)
        Overloaded function.

        1. complex_to_polar(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. complex_to_polar(src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def complex_to_polar(src: ImageBuf, roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """complex_to_polar(*args, **kwargs)
        Overloaded function.

        1. complex_to_polar(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. complex_to_polar(src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @staticmethod
    def computePixelHashSHA1(src: ImageBuf, extrainfo: str = ..., roi: ROI = ..., blocksize: int = ..., nthreads: int = ...) -> str:
        """computePixelHashSHA1(src: OpenImageIO.OpenImageIO.ImageBuf, extrainfo: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, blocksize: int = 0, nthreads: int = 0) -> str"""
    @overload
    @staticmethod
    def computePixelStats(src: ImageBuf, stats: PixelStats, roi: ROI = ..., nthreads: int = ...) -> bool:
        """computePixelStats(*args, **kwargs)
        Overloaded function.

        1. computePixelStats(src: OpenImageIO.OpenImageIO.ImageBuf, stats: OpenImageIO.OpenImageIO.PixelStats, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. computePixelStats(src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.PixelStats
        """
    @overload
    @staticmethod
    def computePixelStats(src: ImageBuf, roi: ROI = ..., nthreads: int = ...) -> PixelStats:
        """computePixelStats(*args, **kwargs)
        Overloaded function.

        1. computePixelStats(src: OpenImageIO.OpenImageIO.ImageBuf, stats: OpenImageIO.OpenImageIO.PixelStats, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. computePixelStats(src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.PixelStats
        """
    @overload
    @staticmethod
    def contrast_remap(dst: ImageBuf, src: ImageBuf, black: object = ..., white: object = ..., min: object = ..., max: object = ..., scontrast: object = ..., sthresh: object = ..., roi: ROI = ..., nthreads: int = ...) -> bool:
        """contrast_remap(*args, **kwargs)
        Overloaded function.

        1. contrast_remap(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, black: object = 0.0, white: object = 1.0, min: object = 0.0, max: object = 1.0, scontrast: object = 1.0, sthresh: object = 0.5, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. contrast_remap(src: OpenImageIO.OpenImageIO.ImageBuf, black: object = 0.0, white: object = 1.0, min: object = 0.0, max: object = 1.0, scontrast: object = 1.0, sthresh: object = 0.5, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def contrast_remap(src: ImageBuf, black: object = ..., white: object = ..., min: object = ..., max: object = ..., scontrast: object = ..., sthresh: object = ..., roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """contrast_remap(*args, **kwargs)
        Overloaded function.

        1. contrast_remap(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, black: object = 0.0, white: object = 1.0, min: object = 0.0, max: object = 1.0, scontrast: object = 1.0, sthresh: object = 0.5, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. contrast_remap(src: OpenImageIO.OpenImageIO.ImageBuf, black: object = 0.0, white: object = 1.0, min: object = 0.0, max: object = 1.0, scontrast: object = 1.0, sthresh: object = 0.5, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def convolve(dst: ImageBuf, src: ImageBuf, kernel: ImageBuf, normalze: bool = ..., roi: ROI = ..., nthreads: int = ...) -> bool:
        """convolve(*args, **kwargs)
        Overloaded function.

        1. convolve(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, kernel: OpenImageIO.OpenImageIO.ImageBuf, normalze: bool = True, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. convolve(src: OpenImageIO.OpenImageIO.ImageBuf, kernel: OpenImageIO.OpenImageIO.ImageBuf, normalze: bool = True, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def convolve(src: ImageBuf, kernel: ImageBuf, normalze: bool = ..., roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """convolve(*args, **kwargs)
        Overloaded function.

        1. convolve(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, kernel: OpenImageIO.OpenImageIO.ImageBuf, normalze: bool = True, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. convolve(src: OpenImageIO.OpenImageIO.ImageBuf, kernel: OpenImageIO.OpenImageIO.ImageBuf, normalze: bool = True, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def copy(dst: ImageBuf, src: ImageBuf, convert: TypeDesc = ..., roi: ROI = ..., nthreads: int = ...) -> bool:
        """copy(*args, **kwargs)
        Overloaded function.

        1. copy(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, convert: OpenImageIO.OpenImageIO.TypeDesc = <TypeDesc 'unknown'>, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. copy(src: OpenImageIO.OpenImageIO.ImageBuf, convert: OpenImageIO.OpenImageIO.TypeDesc = <TypeDesc 'unknown'>, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def copy(src: ImageBuf, convert: TypeDesc = ..., roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """copy(*args, **kwargs)
        Overloaded function.

        1. copy(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, convert: OpenImageIO.OpenImageIO.TypeDesc = <TypeDesc 'unknown'>, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. copy(src: OpenImageIO.OpenImageIO.ImageBuf, convert: OpenImageIO.OpenImageIO.TypeDesc = <TypeDesc 'unknown'>, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def crop(dst: ImageBuf, src: ImageBuf, roi: ROI = ..., nthreads: int = ...) -> bool:
        """crop(*args, **kwargs)
        Overloaded function.

        1. crop(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. crop(src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def crop(src: ImageBuf, roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """crop(*args, **kwargs)
        Overloaded function.

        1. crop(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. crop(src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def cut(dst: ImageBuf, src: ImageBuf, roi: ROI = ..., nthreads: int = ...) -> bool:
        """cut(*args, **kwargs)
        Overloaded function.

        1. cut(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. cut(src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def cut(src: ImageBuf, roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """cut(*args, **kwargs)
        Overloaded function.

        1. cut(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. cut(src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def deep_holdout(dst: ImageBuf, src: ImageBuf, holdout: ImageBuf, roi: ROI = ..., nthreads: int = ...) -> bool:
        """deep_holdout(*args, **kwargs)
        Overloaded function.

        1. deep_holdout(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, holdout: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. deep_holdout(src: OpenImageIO.OpenImageIO.ImageBuf, holdout: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def deep_holdout(src: ImageBuf, holdout: ImageBuf, roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """deep_holdout(*args, **kwargs)
        Overloaded function.

        1. deep_holdout(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, holdout: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. deep_holdout(src: OpenImageIO.OpenImageIO.ImageBuf, holdout: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def deep_merge(dst: ImageBuf, A: ImageBuf, B: ImageBuf, occlusion_cull: bool = ..., roi: ROI = ..., nthreads: int = ...) -> bool:
        """deep_merge(*args, **kwargs)
        Overloaded function.

        1. deep_merge(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, occlusion_cull: bool = True, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. deep_merge(A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, occlusion_cull: bool = True, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def deep_merge(A: ImageBuf, B: ImageBuf, occlusion_cull: bool = ..., roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """deep_merge(*args, **kwargs)
        Overloaded function.

        1. deep_merge(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, occlusion_cull: bool = True, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. deep_merge(A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, occlusion_cull: bool = True, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def deepen(dst: ImageBuf, src: ImageBuf, zvalue: float = ..., roi: ROI = ..., nthreads: int = ...) -> bool:
        """deepen(*args, **kwargs)
        Overloaded function.

        1. deepen(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, zvalue: float = 1.0, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. deepen(src: OpenImageIO.OpenImageIO.ImageBuf, zvalue: float = 1.0, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def deepen(src: ImageBuf, zvalue: float = ..., roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """deepen(*args, **kwargs)
        Overloaded function.

        1. deepen(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, zvalue: float = 1.0, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. deepen(src: OpenImageIO.OpenImageIO.ImageBuf, zvalue: float = 1.0, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def demosaic(dst: ImageBuf, src: ImageBuf, pattern: str = ..., algorithm: str = ..., layout: str = ..., white_balance: object = ..., roi: ROI = ..., nthreads: int = ...) -> bool:
        """demosaic(*args, **kwargs)
        Overloaded function.

        1. demosaic(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, pattern: str = '', algorithm: str = '', layout: str = '', white_balance: object = None, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. demosaic(src: OpenImageIO.OpenImageIO.ImageBuf, pattern: str = '', algorithm: str = '', layout: str = '', white_balance: object = None, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def demosaic(src: ImageBuf, pattern: str = ..., algorithm: str = ..., layout: str = ..., white_balance: object = ..., roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """demosaic(*args, **kwargs)
        Overloaded function.

        1. demosaic(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, pattern: str = '', algorithm: str = '', layout: str = '', white_balance: object = None, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. demosaic(src: OpenImageIO.OpenImageIO.ImageBuf, pattern: str = '', algorithm: str = '', layout: str = '', white_balance: object = None, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def dilate(dst: ImageBuf, src: ImageBuf, width: int = ..., height: int = ..., roi: ROI = ..., nthreads: int = ...) -> bool:
        """dilate(*args, **kwargs)
        Overloaded function.

        1. dilate(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, width: int = 3, height: int = -1, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. dilate(src: OpenImageIO.OpenImageIO.ImageBuf, width: int = 3, height: int = -1, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def dilate(src: ImageBuf, width: int = ..., height: int = ..., roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """dilate(*args, **kwargs)
        Overloaded function.

        1. dilate(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, width: int = 3, height: int = -1, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. dilate(src: OpenImageIO.OpenImageIO.ImageBuf, width: int = 3, height: int = -1, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def div(dst: ImageBuf, A: ImageBuf, B: ImageBuf, roi: ROI = ..., nthreads: int = ...) -> bool:
        """div(*args, **kwargs)
        Overloaded function.

        1. div(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. div(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        3. div(A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        4. div(A: OpenImageIO.OpenImageIO.ImageBuf, B: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def div(dst: ImageBuf, A: ImageBuf, B: object, roi: ROI = ..., nthreads: int = ...) -> bool:
        """div(*args, **kwargs)
        Overloaded function.

        1. div(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. div(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        3. div(A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        4. div(A: OpenImageIO.OpenImageIO.ImageBuf, B: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def div(A: ImageBuf, B: ImageBuf, roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """div(*args, **kwargs)
        Overloaded function.

        1. div(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. div(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        3. div(A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        4. div(A: OpenImageIO.OpenImageIO.ImageBuf, B: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def div(A: ImageBuf, B: object, roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """div(*args, **kwargs)
        Overloaded function.

        1. div(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. div(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        3. div(A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        4. div(A: OpenImageIO.OpenImageIO.ImageBuf, B: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def erode(dst: ImageBuf, src: ImageBuf, width: int = ..., height: int = ..., roi: ROI = ..., nthreads: int = ...) -> bool:
        """erode(*args, **kwargs)
        Overloaded function.

        1. erode(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, width: int = 3, height: int = -1, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. erode(src: OpenImageIO.OpenImageIO.ImageBuf, width: int = 3, height: int = -1, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def erode(src: ImageBuf, width: int = ..., height: int = ..., roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """erode(*args, **kwargs)
        Overloaded function.

        1. erode(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, width: int = 3, height: int = -1, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. erode(src: OpenImageIO.OpenImageIO.ImageBuf, width: int = 3, height: int = -1, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def fft(dst: ImageBuf, src: ImageBuf, roi: ROI = ..., nthreads: int = ...) -> bool:
        """fft(*args, **kwargs)
        Overloaded function.

        1. fft(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. fft(src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def fft(src: ImageBuf, roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """fft(*args, **kwargs)
        Overloaded function.

        1. fft(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. fft(src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def fill(dst: ImageBuf, values: object, roi: ROI = ..., nthreads: int = ...) -> bool:
        """fill(*args, **kwargs)
        Overloaded function.

        1. fill(dst: OpenImageIO.OpenImageIO.ImageBuf, values: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. fill(dst: OpenImageIO.OpenImageIO.ImageBuf, top: object, bottom: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        3. fill(dst: OpenImageIO.OpenImageIO.ImageBuf, topleft: object, topright: object, bottomleft: object, bottomright: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        4. fill(values: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        5. fill(top: object, bottom: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        6. fill(topleft: object, topright: object, bottomleft: object, bottomright: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def fill(dst: ImageBuf, top: object, bottom: object, roi: ROI = ..., nthreads: int = ...) -> bool:
        """fill(*args, **kwargs)
        Overloaded function.

        1. fill(dst: OpenImageIO.OpenImageIO.ImageBuf, values: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. fill(dst: OpenImageIO.OpenImageIO.ImageBuf, top: object, bottom: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        3. fill(dst: OpenImageIO.OpenImageIO.ImageBuf, topleft: object, topright: object, bottomleft: object, bottomright: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        4. fill(values: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        5. fill(top: object, bottom: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        6. fill(topleft: object, topright: object, bottomleft: object, bottomright: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def fill(dst: ImageBuf, topleft: object, topright: object, bottomleft: object, bottomright: object, roi: ROI = ..., nthreads: int = ...) -> bool:
        """fill(*args, **kwargs)
        Overloaded function.

        1. fill(dst: OpenImageIO.OpenImageIO.ImageBuf, values: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. fill(dst: OpenImageIO.OpenImageIO.ImageBuf, top: object, bottom: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        3. fill(dst: OpenImageIO.OpenImageIO.ImageBuf, topleft: object, topright: object, bottomleft: object, bottomright: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        4. fill(values: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        5. fill(top: object, bottom: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        6. fill(topleft: object, topright: object, bottomleft: object, bottomright: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def fill(values: object, roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """fill(*args, **kwargs)
        Overloaded function.

        1. fill(dst: OpenImageIO.OpenImageIO.ImageBuf, values: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. fill(dst: OpenImageIO.OpenImageIO.ImageBuf, top: object, bottom: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        3. fill(dst: OpenImageIO.OpenImageIO.ImageBuf, topleft: object, topright: object, bottomleft: object, bottomright: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        4. fill(values: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        5. fill(top: object, bottom: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        6. fill(topleft: object, topright: object, bottomleft: object, bottomright: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def fill(top: object, bottom: object, roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """fill(*args, **kwargs)
        Overloaded function.

        1. fill(dst: OpenImageIO.OpenImageIO.ImageBuf, values: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. fill(dst: OpenImageIO.OpenImageIO.ImageBuf, top: object, bottom: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        3. fill(dst: OpenImageIO.OpenImageIO.ImageBuf, topleft: object, topright: object, bottomleft: object, bottomright: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        4. fill(values: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        5. fill(top: object, bottom: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        6. fill(topleft: object, topright: object, bottomleft: object, bottomright: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def fill(topleft: object, topright: object, bottomleft: object, bottomright: object, roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """fill(*args, **kwargs)
        Overloaded function.

        1. fill(dst: OpenImageIO.OpenImageIO.ImageBuf, values: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. fill(dst: OpenImageIO.OpenImageIO.ImageBuf, top: object, bottom: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        3. fill(dst: OpenImageIO.OpenImageIO.ImageBuf, topleft: object, topright: object, bottomleft: object, bottomright: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        4. fill(values: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        5. fill(top: object, bottom: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        6. fill(topleft: object, topright: object, bottomleft: object, bottomright: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def fillholes_pushpull(dst: ImageBuf, src: ImageBuf, roi: ROI = ..., nthreads: int = ...) -> bool:
        """fillholes_pushpull(*args, **kwargs)
        Overloaded function.

        1. fillholes_pushpull(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. fillholes_pushpull(src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def fillholes_pushpull(src: ImageBuf, roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """fillholes_pushpull(*args, **kwargs)
        Overloaded function.

        1. fillholes_pushpull(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. fillholes_pushpull(src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def fit(dst: ImageBuf, src: ImageBuf, filtername: str = ..., filterwidth: float = ..., fillmode: str = ..., exact: bool = ..., roi: ROI = ..., nthreads: int = ...) -> bool:
        """fit(*args, **kwargs)
        Overloaded function.

        1. fit(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, filtername: str = '', filterwidth: float = 0.0, fillmode: str = 'letterbox', exact: bool = False, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. fit(src: OpenImageIO.OpenImageIO.ImageBuf, filtername: str = '', filterwidth: float = 0.0, fillmode: str = 'letterbox', exact: bool = False, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def fit(src: ImageBuf, filtername: str = ..., filterwidth: float = ..., fillmode: str = ..., exact: bool = ..., roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """fit(*args, **kwargs)
        Overloaded function.

        1. fit(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, filtername: str = '', filterwidth: float = 0.0, fillmode: str = 'letterbox', exact: bool = False, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. fit(src: OpenImageIO.OpenImageIO.ImageBuf, filtername: str = '', filterwidth: float = 0.0, fillmode: str = 'letterbox', exact: bool = False, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def fixNonFinite(dst: ImageBuf, src: ImageBuf, mode: NonFiniteFixMode = ..., roi: ROI = ..., nthreads: int = ...) -> bool:
        """fixNonFinite(*args, **kwargs)
        Overloaded function.

        1. fixNonFinite(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, mode: OpenImageIO.OpenImageIO.NonFiniteFixMode = <NonFiniteFixMode.NONFINITE_BOX3: 2>, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. fixNonFinite(src: OpenImageIO.OpenImageIO.ImageBuf, mode: OpenImageIO.OpenImageIO.NonFiniteFixMode = <NonFiniteFixMode.NONFINITE_BOX3: 2>, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def fixNonFinite(src: ImageBuf, mode: NonFiniteFixMode = ..., roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """fixNonFinite(*args, **kwargs)
        Overloaded function.

        1. fixNonFinite(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, mode: OpenImageIO.OpenImageIO.NonFiniteFixMode = <NonFiniteFixMode.NONFINITE_BOX3: 2>, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. fixNonFinite(src: OpenImageIO.OpenImageIO.ImageBuf, mode: OpenImageIO.OpenImageIO.NonFiniteFixMode = <NonFiniteFixMode.NONFINITE_BOX3: 2>, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def flatten(dst: ImageBuf, src: ImageBuf, roi: ROI = ..., nthreads: int = ...) -> bool:
        """flatten(*args, **kwargs)
        Overloaded function.

        1. flatten(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. flatten(src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def flatten(src: ImageBuf, roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """flatten(*args, **kwargs)
        Overloaded function.

        1. flatten(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. flatten(src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def flip(dst: ImageBuf, src: ImageBuf, roi: ROI = ..., nthreads: int = ...) -> bool:
        """flip(*args, **kwargs)
        Overloaded function.

        1. flip(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. flip(src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def flip(src: ImageBuf, roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """flip(*args, **kwargs)
        Overloaded function.

        1. flip(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. flip(src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def flop(dst: ImageBuf, src: ImageBuf, roi: ROI = ..., nthreads: int = ...) -> bool:
        """flop(*args, **kwargs)
        Overloaded function.

        1. flop(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. flop(src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def flop(src: ImageBuf, roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """flop(*args, **kwargs)
        Overloaded function.

        1. flop(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. flop(src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @staticmethod
    def histogram(src: ImageBuf, channel: int = ..., bins: int = ..., min: float = ..., max: float = ..., ignore_empty: bool = ..., roi: ROI = ..., nthreads: int = ...) -> object:
        """histogram(src: OpenImageIO.OpenImageIO.ImageBuf, channel: int = 0, bins: int = 256, min: float = 0.0, max: float = 1.0, ignore_empty: bool = False, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> object"""
    @overload
    @staticmethod
    def ifft(dst: ImageBuf, src: ImageBuf, roi: ROI = ..., nthreads: int = ...) -> bool:
        """ifft(*args, **kwargs)
        Overloaded function.

        1. ifft(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. ifft(src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def ifft(src: ImageBuf, roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """ifft(*args, **kwargs)
        Overloaded function.

        1. ifft(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. ifft(src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def invert(dst: ImageBuf, A: ImageBuf, roi: ROI = ..., nthreads: int = ...) -> bool:
        """invert(*args, **kwargs)
        Overloaded function.

        1. invert(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. invert(A: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def invert(A: ImageBuf, roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """invert(*args, **kwargs)
        Overloaded function.

        1. invert(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. invert(A: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @staticmethod
    def isConstantChannel(src: ImageBuf, channel: int, val: float, threshold: float = ..., roi: ROI = ..., nthreads: int = ...) -> bool:
        """isConstantChannel(src: OpenImageIO.OpenImageIO.ImageBuf, channel: int, val: float, threshold: float = 0.0, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool"""
    @staticmethod
    def isConstantColor(src: ImageBuf, threshold: float = ..., roi: ROI = ..., nthreads: int = ...) -> object:
        """isConstantColor(src: OpenImageIO.OpenImageIO.ImageBuf, threshold: float = 0.0, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> object"""
    @staticmethod
    def isMonochrome(src: ImageBuf, threshold: float = ..., roi: ROI = ..., nthreads: int = ...) -> bool:
        """isMonochrome(src: OpenImageIO.OpenImageIO.ImageBuf, threshold: float = 0.0, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool"""
    @overload
    @staticmethod
    def laplacian(dst: ImageBuf, src: ImageBuf, roi: ROI = ..., nthreads: int = ...) -> bool:
        """laplacian(*args, **kwargs)
        Overloaded function.

        1. laplacian(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. laplacian(src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def laplacian(src: ImageBuf, roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """laplacian(*args, **kwargs)
        Overloaded function.

        1. laplacian(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. laplacian(src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def mad(dst: ImageBuf, A: ImageBuf, B: ImageBuf, C: ImageBuf, roi: ROI = ..., nthreads: int = ...) -> bool:
        """mad(*args, **kwargs)
        Overloaded function.

        1. mad(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, C: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. mad(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: object, C: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        3. mad(dst: OpenImageIO.OpenImageIO.ImageBuf, A: object, B: OpenImageIO.OpenImageIO.ImageBuf, C: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        4. mad(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: object, C: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        5. mad(A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, C: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        6. mad(A: OpenImageIO.OpenImageIO.ImageBuf, B: object, C: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        7. mad(A: object, B: OpenImageIO.OpenImageIO.ImageBuf, C: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        8. mad(A: OpenImageIO.OpenImageIO.ImageBuf, B: object, C: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def mad(dst: ImageBuf, A: ImageBuf, B: object, C: ImageBuf, roi: ROI = ..., nthreads: int = ...) -> bool:
        """mad(*args, **kwargs)
        Overloaded function.

        1. mad(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, C: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. mad(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: object, C: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        3. mad(dst: OpenImageIO.OpenImageIO.ImageBuf, A: object, B: OpenImageIO.OpenImageIO.ImageBuf, C: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        4. mad(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: object, C: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        5. mad(A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, C: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        6. mad(A: OpenImageIO.OpenImageIO.ImageBuf, B: object, C: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        7. mad(A: object, B: OpenImageIO.OpenImageIO.ImageBuf, C: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        8. mad(A: OpenImageIO.OpenImageIO.ImageBuf, B: object, C: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def mad(dst: ImageBuf, A: object, B: ImageBuf, C: ImageBuf, roi: ROI = ..., nthreads: int = ...) -> bool:
        """mad(*args, **kwargs)
        Overloaded function.

        1. mad(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, C: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. mad(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: object, C: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        3. mad(dst: OpenImageIO.OpenImageIO.ImageBuf, A: object, B: OpenImageIO.OpenImageIO.ImageBuf, C: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        4. mad(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: object, C: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        5. mad(A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, C: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        6. mad(A: OpenImageIO.OpenImageIO.ImageBuf, B: object, C: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        7. mad(A: object, B: OpenImageIO.OpenImageIO.ImageBuf, C: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        8. mad(A: OpenImageIO.OpenImageIO.ImageBuf, B: object, C: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def mad(dst: ImageBuf, A: ImageBuf, B: object, C: object, roi: ROI = ..., nthreads: int = ...) -> bool:
        """mad(*args, **kwargs)
        Overloaded function.

        1. mad(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, C: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. mad(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: object, C: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        3. mad(dst: OpenImageIO.OpenImageIO.ImageBuf, A: object, B: OpenImageIO.OpenImageIO.ImageBuf, C: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        4. mad(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: object, C: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        5. mad(A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, C: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        6. mad(A: OpenImageIO.OpenImageIO.ImageBuf, B: object, C: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        7. mad(A: object, B: OpenImageIO.OpenImageIO.ImageBuf, C: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        8. mad(A: OpenImageIO.OpenImageIO.ImageBuf, B: object, C: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def mad(A: ImageBuf, B: ImageBuf, C: ImageBuf, roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """mad(*args, **kwargs)
        Overloaded function.

        1. mad(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, C: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. mad(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: object, C: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        3. mad(dst: OpenImageIO.OpenImageIO.ImageBuf, A: object, B: OpenImageIO.OpenImageIO.ImageBuf, C: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        4. mad(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: object, C: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        5. mad(A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, C: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        6. mad(A: OpenImageIO.OpenImageIO.ImageBuf, B: object, C: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        7. mad(A: object, B: OpenImageIO.OpenImageIO.ImageBuf, C: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        8. mad(A: OpenImageIO.OpenImageIO.ImageBuf, B: object, C: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def mad(A: ImageBuf, B: object, C: ImageBuf, roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """mad(*args, **kwargs)
        Overloaded function.

        1. mad(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, C: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. mad(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: object, C: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        3. mad(dst: OpenImageIO.OpenImageIO.ImageBuf, A: object, B: OpenImageIO.OpenImageIO.ImageBuf, C: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        4. mad(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: object, C: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        5. mad(A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, C: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        6. mad(A: OpenImageIO.OpenImageIO.ImageBuf, B: object, C: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        7. mad(A: object, B: OpenImageIO.OpenImageIO.ImageBuf, C: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        8. mad(A: OpenImageIO.OpenImageIO.ImageBuf, B: object, C: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def mad(A: object, B: ImageBuf, C: ImageBuf, roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """mad(*args, **kwargs)
        Overloaded function.

        1. mad(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, C: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. mad(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: object, C: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        3. mad(dst: OpenImageIO.OpenImageIO.ImageBuf, A: object, B: OpenImageIO.OpenImageIO.ImageBuf, C: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        4. mad(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: object, C: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        5. mad(A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, C: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        6. mad(A: OpenImageIO.OpenImageIO.ImageBuf, B: object, C: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        7. mad(A: object, B: OpenImageIO.OpenImageIO.ImageBuf, C: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        8. mad(A: OpenImageIO.OpenImageIO.ImageBuf, B: object, C: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def mad(A: ImageBuf, B: object, C: object, roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """mad(*args, **kwargs)
        Overloaded function.

        1. mad(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, C: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. mad(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: object, C: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        3. mad(dst: OpenImageIO.OpenImageIO.ImageBuf, A: object, B: OpenImageIO.OpenImageIO.ImageBuf, C: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        4. mad(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: object, C: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        5. mad(A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, C: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        6. mad(A: OpenImageIO.OpenImageIO.ImageBuf, B: object, C: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        7. mad(A: object, B: OpenImageIO.OpenImageIO.ImageBuf, C: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        8. mad(A: OpenImageIO.OpenImageIO.ImageBuf, B: object, C: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def make_kernel(dst: ImageBuf, name: str, width: float, height: float, depth: float = ..., normalize: bool = ...) -> bool:
        """make_kernel(*args, **kwargs)
        Overloaded function.

        1. make_kernel(dst: OpenImageIO.OpenImageIO.ImageBuf, name: str, width: float, height: float, depth: float = 1.0, normalize: bool = True) -> bool

        2. make_kernel(name: str, width: float, height: float, depth: float = 1.0, normalize: bool = True) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def make_kernel(name: str, width: float, height: float, depth: float = ..., normalize: bool = ...) -> ImageBuf:
        """make_kernel(*args, **kwargs)
        Overloaded function.

        1. make_kernel(dst: OpenImageIO.OpenImageIO.ImageBuf, name: str, width: float, height: float, depth: float = 1.0, normalize: bool = True) -> bool

        2. make_kernel(name: str, width: float, height: float, depth: float = 1.0, normalize: bool = True) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def make_texture(mode: MakeTextureMode, filename: str, outputfilename: str, config: ImageSpec = ...) -> bool:
        """make_texture(*args, **kwargs)
        Overloaded function.

        1. make_texture(mode: OpenImageIO.OpenImageIO.MakeTextureMode, filename: str, outputfilename: str, config: OpenImageIO.OpenImageIO.ImageSpec = <OpenImageIO.OpenImageIO.ImageSpec object>) -> bool

        2. make_texture(mode: OpenImageIO.OpenImageIO.MakeTextureMode, buf: OpenImageIO.OpenImageIO.ImageBuf, outputfilename: str, config: OpenImageIO.OpenImageIO.ImageSpec = <OpenImageIO.OpenImageIO.ImageSpec object>) -> bool
        """
    @overload
    @staticmethod
    def make_texture(mode: MakeTextureMode, buf: ImageBuf, outputfilename: str, config: ImageSpec = ...) -> bool:
        """make_texture(*args, **kwargs)
        Overloaded function.

        1. make_texture(mode: OpenImageIO.OpenImageIO.MakeTextureMode, filename: str, outputfilename: str, config: OpenImageIO.OpenImageIO.ImageSpec = <OpenImageIO.OpenImageIO.ImageSpec object>) -> bool

        2. make_texture(mode: OpenImageIO.OpenImageIO.MakeTextureMode, buf: OpenImageIO.OpenImageIO.ImageBuf, outputfilename: str, config: OpenImageIO.OpenImageIO.ImageSpec = <OpenImageIO.OpenImageIO.ImageSpec object>) -> bool
        """
    @overload
    @staticmethod
    def max(dst: ImageBuf, A: ImageBuf, B: ImageBuf, roi: ROI = ..., nthreads: int = ...) -> bool:
        """max(*args, **kwargs)
        Overloaded function.

        1. max(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. max(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        3. max(A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        4. max(A: OpenImageIO.OpenImageIO.ImageBuf, B: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def max(dst: ImageBuf, A: ImageBuf, B: object, roi: ROI = ..., nthreads: int = ...) -> bool:
        """max(*args, **kwargs)
        Overloaded function.

        1. max(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. max(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        3. max(A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        4. max(A: OpenImageIO.OpenImageIO.ImageBuf, B: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def max(A: ImageBuf, B: ImageBuf, roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """max(*args, **kwargs)
        Overloaded function.

        1. max(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. max(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        3. max(A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        4. max(A: OpenImageIO.OpenImageIO.ImageBuf, B: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def max(A: ImageBuf, B: object, roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """max(*args, **kwargs)
        Overloaded function.

        1. max(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. max(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        3. max(A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        4. max(A: OpenImageIO.OpenImageIO.ImageBuf, B: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def maxchan(dst: ImageBuf, src: ImageBuf, roi: ROI = ..., nthreads: int = ...) -> bool:
        """maxchan(*args, **kwargs)
        Overloaded function.

        1. maxchan(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. maxchan(src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def maxchan(src: ImageBuf, roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """maxchan(*args, **kwargs)
        Overloaded function.

        1. maxchan(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. maxchan(src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def median_filter(dst: ImageBuf, src: ImageBuf, width: int = ..., height: int = ..., roi: ROI = ..., nthreads: int = ...) -> bool:
        """median_filter(*args, **kwargs)
        Overloaded function.

        1. median_filter(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, width: int = 3, height: int = -1, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. median_filter(src: OpenImageIO.OpenImageIO.ImageBuf, width: int = 3, height: int = -1, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def median_filter(src: ImageBuf, width: int = ..., height: int = ..., roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """median_filter(*args, **kwargs)
        Overloaded function.

        1. median_filter(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, width: int = 3, height: int = -1, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. median_filter(src: OpenImageIO.OpenImageIO.ImageBuf, width: int = 3, height: int = -1, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def min(dst: ImageBuf, A: ImageBuf, B: ImageBuf, roi: ROI = ..., nthreads: int = ...) -> bool:
        """min(*args, **kwargs)
        Overloaded function.

        1. min(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. min(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        3. min(A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        4. min(A: OpenImageIO.OpenImageIO.ImageBuf, B: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def min(dst: ImageBuf, A: ImageBuf, B: object, roi: ROI = ..., nthreads: int = ...) -> bool:
        """min(*args, **kwargs)
        Overloaded function.

        1. min(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. min(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        3. min(A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        4. min(A: OpenImageIO.OpenImageIO.ImageBuf, B: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def min(A: ImageBuf, B: ImageBuf, roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """min(*args, **kwargs)
        Overloaded function.

        1. min(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. min(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        3. min(A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        4. min(A: OpenImageIO.OpenImageIO.ImageBuf, B: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def min(A: ImageBuf, B: object, roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """min(*args, **kwargs)
        Overloaded function.

        1. min(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. min(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        3. min(A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        4. min(A: OpenImageIO.OpenImageIO.ImageBuf, B: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def minchan(dst: ImageBuf, src: ImageBuf, roi: ROI = ..., nthreads: int = ...) -> bool:
        """minchan(*args, **kwargs)
        Overloaded function.

        1. minchan(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. minchan(src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def minchan(src: ImageBuf, roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """minchan(*args, **kwargs)
        Overloaded function.

        1. minchan(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. minchan(src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def mul(dst: ImageBuf, A: ImageBuf, B: ImageBuf, roi: ROI = ..., nthreads: int = ...) -> bool:
        """mul(*args, **kwargs)
        Overloaded function.

        1. mul(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. mul(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        3. mul(A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        4. mul(A: OpenImageIO.OpenImageIO.ImageBuf, B: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def mul(dst: ImageBuf, A: ImageBuf, B: object, roi: ROI = ..., nthreads: int = ...) -> bool:
        """mul(*args, **kwargs)
        Overloaded function.

        1. mul(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. mul(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        3. mul(A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        4. mul(A: OpenImageIO.OpenImageIO.ImageBuf, B: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def mul(A: ImageBuf, B: ImageBuf, roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """mul(*args, **kwargs)
        Overloaded function.

        1. mul(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. mul(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        3. mul(A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        4. mul(A: OpenImageIO.OpenImageIO.ImageBuf, B: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def mul(A: ImageBuf, B: object, roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """mul(*args, **kwargs)
        Overloaded function.

        1. mul(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. mul(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        3. mul(A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        4. mul(A: OpenImageIO.OpenImageIO.ImageBuf, B: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def noise(dst: ImageBuf, type: str = ..., A: float = ..., B: float = ..., mono: bool = ..., seed: int = ..., roi: ROI = ..., nthreads: int = ...) -> bool:
        """noise(*args, **kwargs)
        Overloaded function.

        1. noise(dst: OpenImageIO.OpenImageIO.ImageBuf, type: str = 'gaussian', A: float = 0.0, B: float = 0.10000000149011612, mono: bool = False, seed: int = 0, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. noise(type: str = 'gaussian', A: float = 0.0, B: float = 0.10000000149011612, mono: bool = False, seed: int = 0, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def noise(type: str = ..., A: float = ..., B: float = ..., mono: bool = ..., seed: int = ..., roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """noise(*args, **kwargs)
        Overloaded function.

        1. noise(dst: OpenImageIO.OpenImageIO.ImageBuf, type: str = 'gaussian', A: float = 0.0, B: float = 0.10000000149011612, mono: bool = False, seed: int = 0, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. noise(type: str = 'gaussian', A: float = 0.0, B: float = 0.10000000149011612, mono: bool = False, seed: int = 0, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @staticmethod
    def nonzero_region(src: ImageBuf, roi: ROI = ..., nthreads: int = ...) -> ROI:
        """nonzero_region(src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ROI"""
    @overload
    @staticmethod
    def normalize(dst: ImageBuf, src: ImageBuf, inCenter: float = ..., outCenter: float = ..., scale: float = ..., roi: ROI = ..., nthreads: int = ...) -> bool:
        """normalize(*args, **kwargs)
        Overloaded function.

        1. normalize(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, inCenter: float = 0.0, outCenter: float = 0.0, scale: float = 1.0, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. normalize(src: OpenImageIO.OpenImageIO.ImageBuf, inCenter: float = 0.0, outCenter: float = 0.0, scale: float = 1.0, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def normalize(src: ImageBuf, inCenter: float = ..., outCenter: float = ..., scale: float = ..., roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """normalize(*args, **kwargs)
        Overloaded function.

        1. normalize(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, inCenter: float = 0.0, outCenter: float = 0.0, scale: float = 1.0, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. normalize(src: OpenImageIO.OpenImageIO.ImageBuf, inCenter: float = 0.0, outCenter: float = 0.0, scale: float = 1.0, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def ociodisplay(dst: ImageBuf, src: ImageBuf, display: str, view: str, fromspace: str = ..., looks: str = ..., unpremult: bool = ..., inverse: bool = ..., context_key: str = ..., context_value: str = ..., roi: ROI = ..., nthreads: int = ...) -> bool:
        """ociodisplay(*args, **kwargs)
        Overloaded function.

        1. ociodisplay(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, display: str, view: str, fromspace: str = '', looks: str = '', unpremult: bool = True, inverse: bool = False, context_key: str = '', context_value: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. ociodisplay(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, display: str, view: str, fromspace: str = '', looks: str = '', unpremult: bool = True, inverse: bool = False, context_key: str = '', context_value: str = '', colorconfig: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        3. ociodisplay(src: OpenImageIO.OpenImageIO.ImageBuf, display: str, view: str, fromspace: str = '', looks: str = '', unpremult: bool = True, inverse: bool = False, context_key: str = '', context_value: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        4. ociodisplay(src: OpenImageIO.OpenImageIO.ImageBuf, display: str, view: str, fromspace: str = '', looks: str = '', unpremult: bool = True, inverse: bool = False, context_key: str = '', context_value: str = '', colorconfig: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        5. ociodisplay(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, display: str, view: str, fromspace: str, looks: str, unpremult: bool, context_key: str, context_value: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        6. ociodisplay(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, display: str, view: str, fromspace: str, looks: str, unpremult: bool, context_key: str, context_value: str, colorconfig: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        7. ociodisplay(src: OpenImageIO.OpenImageIO.ImageBuf, display: str, view: str, fromspace: str, looks: str, unpremult: bool, context_key: str, context_value: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        8. ociodisplay(src: OpenImageIO.OpenImageIO.ImageBuf, display: str, view: str, fromspace: str, looks: str, unpremult: bool, context_key: str, context_value: str = '', colorconfig: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def ociodisplay(dst: ImageBuf, src: ImageBuf, display: str, view: str, fromspace: str = ..., looks: str = ..., unpremult: bool = ..., inverse: bool = ..., context_key: str = ..., context_value: str = ..., colorconfig: str = ..., roi: ROI = ..., nthreads: int = ...) -> bool:
        """ociodisplay(*args, **kwargs)
        Overloaded function.

        1. ociodisplay(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, display: str, view: str, fromspace: str = '', looks: str = '', unpremult: bool = True, inverse: bool = False, context_key: str = '', context_value: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. ociodisplay(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, display: str, view: str, fromspace: str = '', looks: str = '', unpremult: bool = True, inverse: bool = False, context_key: str = '', context_value: str = '', colorconfig: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        3. ociodisplay(src: OpenImageIO.OpenImageIO.ImageBuf, display: str, view: str, fromspace: str = '', looks: str = '', unpremult: bool = True, inverse: bool = False, context_key: str = '', context_value: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        4. ociodisplay(src: OpenImageIO.OpenImageIO.ImageBuf, display: str, view: str, fromspace: str = '', looks: str = '', unpremult: bool = True, inverse: bool = False, context_key: str = '', context_value: str = '', colorconfig: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        5. ociodisplay(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, display: str, view: str, fromspace: str, looks: str, unpremult: bool, context_key: str, context_value: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        6. ociodisplay(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, display: str, view: str, fromspace: str, looks: str, unpremult: bool, context_key: str, context_value: str, colorconfig: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        7. ociodisplay(src: OpenImageIO.OpenImageIO.ImageBuf, display: str, view: str, fromspace: str, looks: str, unpremult: bool, context_key: str, context_value: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        8. ociodisplay(src: OpenImageIO.OpenImageIO.ImageBuf, display: str, view: str, fromspace: str, looks: str, unpremult: bool, context_key: str, context_value: str = '', colorconfig: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def ociodisplay(src: ImageBuf, display: str, view: str, fromspace: str = ..., looks: str = ..., unpremult: bool = ..., inverse: bool = ..., context_key: str = ..., context_value: str = ..., roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """ociodisplay(*args, **kwargs)
        Overloaded function.

        1. ociodisplay(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, display: str, view: str, fromspace: str = '', looks: str = '', unpremult: bool = True, inverse: bool = False, context_key: str = '', context_value: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. ociodisplay(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, display: str, view: str, fromspace: str = '', looks: str = '', unpremult: bool = True, inverse: bool = False, context_key: str = '', context_value: str = '', colorconfig: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        3. ociodisplay(src: OpenImageIO.OpenImageIO.ImageBuf, display: str, view: str, fromspace: str = '', looks: str = '', unpremult: bool = True, inverse: bool = False, context_key: str = '', context_value: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        4. ociodisplay(src: OpenImageIO.OpenImageIO.ImageBuf, display: str, view: str, fromspace: str = '', looks: str = '', unpremult: bool = True, inverse: bool = False, context_key: str = '', context_value: str = '', colorconfig: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        5. ociodisplay(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, display: str, view: str, fromspace: str, looks: str, unpremult: bool, context_key: str, context_value: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        6. ociodisplay(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, display: str, view: str, fromspace: str, looks: str, unpremult: bool, context_key: str, context_value: str, colorconfig: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        7. ociodisplay(src: OpenImageIO.OpenImageIO.ImageBuf, display: str, view: str, fromspace: str, looks: str, unpremult: bool, context_key: str, context_value: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        8. ociodisplay(src: OpenImageIO.OpenImageIO.ImageBuf, display: str, view: str, fromspace: str, looks: str, unpremult: bool, context_key: str, context_value: str = '', colorconfig: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def ociodisplay(src: ImageBuf, display: str, view: str, fromspace: str = ..., looks: str = ..., unpremult: bool = ..., inverse: bool = ..., context_key: str = ..., context_value: str = ..., colorconfig: str = ..., roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """ociodisplay(*args, **kwargs)
        Overloaded function.

        1. ociodisplay(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, display: str, view: str, fromspace: str = '', looks: str = '', unpremult: bool = True, inverse: bool = False, context_key: str = '', context_value: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. ociodisplay(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, display: str, view: str, fromspace: str = '', looks: str = '', unpremult: bool = True, inverse: bool = False, context_key: str = '', context_value: str = '', colorconfig: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        3. ociodisplay(src: OpenImageIO.OpenImageIO.ImageBuf, display: str, view: str, fromspace: str = '', looks: str = '', unpremult: bool = True, inverse: bool = False, context_key: str = '', context_value: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        4. ociodisplay(src: OpenImageIO.OpenImageIO.ImageBuf, display: str, view: str, fromspace: str = '', looks: str = '', unpremult: bool = True, inverse: bool = False, context_key: str = '', context_value: str = '', colorconfig: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        5. ociodisplay(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, display: str, view: str, fromspace: str, looks: str, unpremult: bool, context_key: str, context_value: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        6. ociodisplay(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, display: str, view: str, fromspace: str, looks: str, unpremult: bool, context_key: str, context_value: str, colorconfig: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        7. ociodisplay(src: OpenImageIO.OpenImageIO.ImageBuf, display: str, view: str, fromspace: str, looks: str, unpremult: bool, context_key: str, context_value: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        8. ociodisplay(src: OpenImageIO.OpenImageIO.ImageBuf, display: str, view: str, fromspace: str, looks: str, unpremult: bool, context_key: str, context_value: str = '', colorconfig: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def ociodisplay(dst: ImageBuf, src: ImageBuf, display: str, view: str, fromspace: str, looks: str, unpremult: bool, context_key: str, context_value: str = ..., roi: ROI = ..., nthreads: int = ...) -> bool:
        """ociodisplay(*args, **kwargs)
        Overloaded function.

        1. ociodisplay(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, display: str, view: str, fromspace: str = '', looks: str = '', unpremult: bool = True, inverse: bool = False, context_key: str = '', context_value: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. ociodisplay(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, display: str, view: str, fromspace: str = '', looks: str = '', unpremult: bool = True, inverse: bool = False, context_key: str = '', context_value: str = '', colorconfig: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        3. ociodisplay(src: OpenImageIO.OpenImageIO.ImageBuf, display: str, view: str, fromspace: str = '', looks: str = '', unpremult: bool = True, inverse: bool = False, context_key: str = '', context_value: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        4. ociodisplay(src: OpenImageIO.OpenImageIO.ImageBuf, display: str, view: str, fromspace: str = '', looks: str = '', unpremult: bool = True, inverse: bool = False, context_key: str = '', context_value: str = '', colorconfig: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        5. ociodisplay(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, display: str, view: str, fromspace: str, looks: str, unpremult: bool, context_key: str, context_value: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        6. ociodisplay(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, display: str, view: str, fromspace: str, looks: str, unpremult: bool, context_key: str, context_value: str, colorconfig: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        7. ociodisplay(src: OpenImageIO.OpenImageIO.ImageBuf, display: str, view: str, fromspace: str, looks: str, unpremult: bool, context_key: str, context_value: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        8. ociodisplay(src: OpenImageIO.OpenImageIO.ImageBuf, display: str, view: str, fromspace: str, looks: str, unpremult: bool, context_key: str, context_value: str = '', colorconfig: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def ociodisplay(dst: ImageBuf, src: ImageBuf, display: str, view: str, fromspace: str, looks: str, unpremult: bool, context_key: str, context_value: str, colorconfig: str = ..., roi: ROI = ..., nthreads: int = ...) -> bool:
        """ociodisplay(*args, **kwargs)
        Overloaded function.

        1. ociodisplay(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, display: str, view: str, fromspace: str = '', looks: str = '', unpremult: bool = True, inverse: bool = False, context_key: str = '', context_value: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. ociodisplay(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, display: str, view: str, fromspace: str = '', looks: str = '', unpremult: bool = True, inverse: bool = False, context_key: str = '', context_value: str = '', colorconfig: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        3. ociodisplay(src: OpenImageIO.OpenImageIO.ImageBuf, display: str, view: str, fromspace: str = '', looks: str = '', unpremult: bool = True, inverse: bool = False, context_key: str = '', context_value: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        4. ociodisplay(src: OpenImageIO.OpenImageIO.ImageBuf, display: str, view: str, fromspace: str = '', looks: str = '', unpremult: bool = True, inverse: bool = False, context_key: str = '', context_value: str = '', colorconfig: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        5. ociodisplay(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, display: str, view: str, fromspace: str, looks: str, unpremult: bool, context_key: str, context_value: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        6. ociodisplay(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, display: str, view: str, fromspace: str, looks: str, unpremult: bool, context_key: str, context_value: str, colorconfig: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        7. ociodisplay(src: OpenImageIO.OpenImageIO.ImageBuf, display: str, view: str, fromspace: str, looks: str, unpremult: bool, context_key: str, context_value: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        8. ociodisplay(src: OpenImageIO.OpenImageIO.ImageBuf, display: str, view: str, fromspace: str, looks: str, unpremult: bool, context_key: str, context_value: str = '', colorconfig: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def ociodisplay(src: ImageBuf, display: str, view: str, fromspace: str, looks: str, unpremult: bool, context_key: str, context_value: str = ..., roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """ociodisplay(*args, **kwargs)
        Overloaded function.

        1. ociodisplay(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, display: str, view: str, fromspace: str = '', looks: str = '', unpremult: bool = True, inverse: bool = False, context_key: str = '', context_value: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. ociodisplay(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, display: str, view: str, fromspace: str = '', looks: str = '', unpremult: bool = True, inverse: bool = False, context_key: str = '', context_value: str = '', colorconfig: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        3. ociodisplay(src: OpenImageIO.OpenImageIO.ImageBuf, display: str, view: str, fromspace: str = '', looks: str = '', unpremult: bool = True, inverse: bool = False, context_key: str = '', context_value: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        4. ociodisplay(src: OpenImageIO.OpenImageIO.ImageBuf, display: str, view: str, fromspace: str = '', looks: str = '', unpremult: bool = True, inverse: bool = False, context_key: str = '', context_value: str = '', colorconfig: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        5. ociodisplay(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, display: str, view: str, fromspace: str, looks: str, unpremult: bool, context_key: str, context_value: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        6. ociodisplay(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, display: str, view: str, fromspace: str, looks: str, unpremult: bool, context_key: str, context_value: str, colorconfig: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        7. ociodisplay(src: OpenImageIO.OpenImageIO.ImageBuf, display: str, view: str, fromspace: str, looks: str, unpremult: bool, context_key: str, context_value: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        8. ociodisplay(src: OpenImageIO.OpenImageIO.ImageBuf, display: str, view: str, fromspace: str, looks: str, unpremult: bool, context_key: str, context_value: str = '', colorconfig: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def ociodisplay(src: ImageBuf, display: str, view: str, fromspace: str, looks: str, unpremult: bool, context_key: str, context_value: str = ..., colorconfig: str = ..., roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """ociodisplay(*args, **kwargs)
        Overloaded function.

        1. ociodisplay(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, display: str, view: str, fromspace: str = '', looks: str = '', unpremult: bool = True, inverse: bool = False, context_key: str = '', context_value: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. ociodisplay(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, display: str, view: str, fromspace: str = '', looks: str = '', unpremult: bool = True, inverse: bool = False, context_key: str = '', context_value: str = '', colorconfig: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        3. ociodisplay(src: OpenImageIO.OpenImageIO.ImageBuf, display: str, view: str, fromspace: str = '', looks: str = '', unpremult: bool = True, inverse: bool = False, context_key: str = '', context_value: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        4. ociodisplay(src: OpenImageIO.OpenImageIO.ImageBuf, display: str, view: str, fromspace: str = '', looks: str = '', unpremult: bool = True, inverse: bool = False, context_key: str = '', context_value: str = '', colorconfig: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        5. ociodisplay(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, display: str, view: str, fromspace: str, looks: str, unpremult: bool, context_key: str, context_value: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        6. ociodisplay(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, display: str, view: str, fromspace: str, looks: str, unpremult: bool, context_key: str, context_value: str, colorconfig: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        7. ociodisplay(src: OpenImageIO.OpenImageIO.ImageBuf, display: str, view: str, fromspace: str, looks: str, unpremult: bool, context_key: str, context_value: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        8. ociodisplay(src: OpenImageIO.OpenImageIO.ImageBuf, display: str, view: str, fromspace: str, looks: str, unpremult: bool, context_key: str, context_value: str = '', colorconfig: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def ociofiletransform(dst: ImageBuf, src: ImageBuf, name: str, unpremult: bool = ..., inverse: bool = ..., roi: ROI = ..., nthreads: int = ...) -> bool:
        """ociofiletransform(*args, **kwargs)
        Overloaded function.

        1. ociofiletransform(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, name: str, unpremult: bool = True, inverse: bool = False, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. ociofiletransform(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, name: str, unpremult: bool = True, inverse: bool = False, colorconfig: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        3. ociofiletransform(src: OpenImageIO.OpenImageIO.ImageBuf, name: str, unpremult: bool = True, inverse: bool = False, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        4. ociofiletransform(src: OpenImageIO.OpenImageIO.ImageBuf, name: str, unpremult: bool = True, inverse: bool = False, colorconfig: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def ociofiletransform(dst: ImageBuf, src: ImageBuf, name: str, unpremult: bool = ..., inverse: bool = ..., colorconfig: str = ..., roi: ROI = ..., nthreads: int = ...) -> bool:
        """ociofiletransform(*args, **kwargs)
        Overloaded function.

        1. ociofiletransform(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, name: str, unpremult: bool = True, inverse: bool = False, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. ociofiletransform(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, name: str, unpremult: bool = True, inverse: bool = False, colorconfig: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        3. ociofiletransform(src: OpenImageIO.OpenImageIO.ImageBuf, name: str, unpremult: bool = True, inverse: bool = False, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        4. ociofiletransform(src: OpenImageIO.OpenImageIO.ImageBuf, name: str, unpremult: bool = True, inverse: bool = False, colorconfig: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def ociofiletransform(src: ImageBuf, name: str, unpremult: bool = ..., inverse: bool = ..., roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """ociofiletransform(*args, **kwargs)
        Overloaded function.

        1. ociofiletransform(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, name: str, unpremult: bool = True, inverse: bool = False, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. ociofiletransform(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, name: str, unpremult: bool = True, inverse: bool = False, colorconfig: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        3. ociofiletransform(src: OpenImageIO.OpenImageIO.ImageBuf, name: str, unpremult: bool = True, inverse: bool = False, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        4. ociofiletransform(src: OpenImageIO.OpenImageIO.ImageBuf, name: str, unpremult: bool = True, inverse: bool = False, colorconfig: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def ociofiletransform(src: ImageBuf, name: str, unpremult: bool = ..., inverse: bool = ..., colorconfig: str = ..., roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """ociofiletransform(*args, **kwargs)
        Overloaded function.

        1. ociofiletransform(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, name: str, unpremult: bool = True, inverse: bool = False, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. ociofiletransform(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, name: str, unpremult: bool = True, inverse: bool = False, colorconfig: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        3. ociofiletransform(src: OpenImageIO.OpenImageIO.ImageBuf, name: str, unpremult: bool = True, inverse: bool = False, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        4. ociofiletransform(src: OpenImageIO.OpenImageIO.ImageBuf, name: str, unpremult: bool = True, inverse: bool = False, colorconfig: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def ociolook(dst: ImageBuf, src: ImageBuf, looks: str, fromspace: str, tospace: str, unpremult: bool = ..., inverse: bool = ..., context_key: str = ..., context_value: str = ..., roi: ROI = ..., nthreads: int = ...) -> bool:
        """ociolook(*args, **kwargs)
        Overloaded function.

        1. ociolook(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, looks: str, fromspace: str, tospace: str, unpremult: bool = True, inverse: bool = False, context_key: str = '', context_value: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. ociolook(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, looks: str, fromspace: str, tospace: str, unpremult: bool = True, inverse: bool = False, context_key: str = '', context_value: str = '', colorconfig: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        3. ociolook(src: OpenImageIO.OpenImageIO.ImageBuf, looks: str, fromspace: str, tospace: str, unpremult: bool = True, inverse: bool = False, context_key: str = '', context_value: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        4. ociolook(src: OpenImageIO.OpenImageIO.ImageBuf, looks: str, fromspace: str, tospace: str, unpremult: bool = True, inverse: bool = False, context_key: str = '', context_value: str = '', colorconfig: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def ociolook(dst: ImageBuf, src: ImageBuf, looks: str, fromspace: str, tospace: str, unpremult: bool = ..., inverse: bool = ..., context_key: str = ..., context_value: str = ..., colorconfig: str = ..., roi: ROI = ..., nthreads: int = ...) -> bool:
        """ociolook(*args, **kwargs)
        Overloaded function.

        1. ociolook(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, looks: str, fromspace: str, tospace: str, unpremult: bool = True, inverse: bool = False, context_key: str = '', context_value: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. ociolook(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, looks: str, fromspace: str, tospace: str, unpremult: bool = True, inverse: bool = False, context_key: str = '', context_value: str = '', colorconfig: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        3. ociolook(src: OpenImageIO.OpenImageIO.ImageBuf, looks: str, fromspace: str, tospace: str, unpremult: bool = True, inverse: bool = False, context_key: str = '', context_value: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        4. ociolook(src: OpenImageIO.OpenImageIO.ImageBuf, looks: str, fromspace: str, tospace: str, unpremult: bool = True, inverse: bool = False, context_key: str = '', context_value: str = '', colorconfig: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def ociolook(src: ImageBuf, looks: str, fromspace: str, tospace: str, unpremult: bool = ..., inverse: bool = ..., context_key: str = ..., context_value: str = ..., roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """ociolook(*args, **kwargs)
        Overloaded function.

        1. ociolook(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, looks: str, fromspace: str, tospace: str, unpremult: bool = True, inverse: bool = False, context_key: str = '', context_value: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. ociolook(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, looks: str, fromspace: str, tospace: str, unpremult: bool = True, inverse: bool = False, context_key: str = '', context_value: str = '', colorconfig: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        3. ociolook(src: OpenImageIO.OpenImageIO.ImageBuf, looks: str, fromspace: str, tospace: str, unpremult: bool = True, inverse: bool = False, context_key: str = '', context_value: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        4. ociolook(src: OpenImageIO.OpenImageIO.ImageBuf, looks: str, fromspace: str, tospace: str, unpremult: bool = True, inverse: bool = False, context_key: str = '', context_value: str = '', colorconfig: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def ociolook(src: ImageBuf, looks: str, fromspace: str, tospace: str, unpremult: bool = ..., inverse: bool = ..., context_key: str = ..., context_value: str = ..., colorconfig: str = ..., roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """ociolook(*args, **kwargs)
        Overloaded function.

        1. ociolook(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, looks: str, fromspace: str, tospace: str, unpremult: bool = True, inverse: bool = False, context_key: str = '', context_value: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. ociolook(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, looks: str, fromspace: str, tospace: str, unpremult: bool = True, inverse: bool = False, context_key: str = '', context_value: str = '', colorconfig: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        3. ociolook(src: OpenImageIO.OpenImageIO.ImageBuf, looks: str, fromspace: str, tospace: str, unpremult: bool = True, inverse: bool = False, context_key: str = '', context_value: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        4. ociolook(src: OpenImageIO.OpenImageIO.ImageBuf, looks: str, fromspace: str, tospace: str, unpremult: bool = True, inverse: bool = False, context_key: str = '', context_value: str = '', colorconfig: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def ocionamedtransform(dst: ImageBuf, src: ImageBuf, name: str, unpremult: bool = ..., inverse: bool = ..., context_key: str = ..., context_value: str = ..., roi: ROI = ..., nthreads: int = ...) -> bool:
        """ocionamedtransform(*args, **kwargs)
        Overloaded function.

        1. ocionamedtransform(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, name: str, unpremult: bool = True, inverse: bool = False, context_key: str = '', context_value: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. ocionamedtransform(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, name: str, unpremult: bool = True, inverse: bool = False, context_key: str = '', context_value: str = '', colorconfig: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        3. ocionamedtransform(src: OpenImageIO.OpenImageIO.ImageBuf, name: str, unpremult: bool = True, inverse: bool = False, context_key: str = '', context_value: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        4. ocionamedtransform(src: OpenImageIO.OpenImageIO.ImageBuf, name: str, unpremult: bool = True, inverse: bool = False, context_key: str = '', context_value: str = '', colorconfig: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def ocionamedtransform(dst: ImageBuf, src: ImageBuf, name: str, unpremult: bool = ..., inverse: bool = ..., context_key: str = ..., context_value: str = ..., colorconfig: str = ..., roi: ROI = ..., nthreads: int = ...) -> bool:
        """ocionamedtransform(*args, **kwargs)
        Overloaded function.

        1. ocionamedtransform(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, name: str, unpremult: bool = True, inverse: bool = False, context_key: str = '', context_value: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. ocionamedtransform(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, name: str, unpremult: bool = True, inverse: bool = False, context_key: str = '', context_value: str = '', colorconfig: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        3. ocionamedtransform(src: OpenImageIO.OpenImageIO.ImageBuf, name: str, unpremult: bool = True, inverse: bool = False, context_key: str = '', context_value: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        4. ocionamedtransform(src: OpenImageIO.OpenImageIO.ImageBuf, name: str, unpremult: bool = True, inverse: bool = False, context_key: str = '', context_value: str = '', colorconfig: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def ocionamedtransform(src: ImageBuf, name: str, unpremult: bool = ..., inverse: bool = ..., context_key: str = ..., context_value: str = ..., roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """ocionamedtransform(*args, **kwargs)
        Overloaded function.

        1. ocionamedtransform(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, name: str, unpremult: bool = True, inverse: bool = False, context_key: str = '', context_value: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. ocionamedtransform(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, name: str, unpremult: bool = True, inverse: bool = False, context_key: str = '', context_value: str = '', colorconfig: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        3. ocionamedtransform(src: OpenImageIO.OpenImageIO.ImageBuf, name: str, unpremult: bool = True, inverse: bool = False, context_key: str = '', context_value: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        4. ocionamedtransform(src: OpenImageIO.OpenImageIO.ImageBuf, name: str, unpremult: bool = True, inverse: bool = False, context_key: str = '', context_value: str = '', colorconfig: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def ocionamedtransform(src: ImageBuf, name: str, unpremult: bool = ..., inverse: bool = ..., context_key: str = ..., context_value: str = ..., colorconfig: str = ..., roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """ocionamedtransform(*args, **kwargs)
        Overloaded function.

        1. ocionamedtransform(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, name: str, unpremult: bool = True, inverse: bool = False, context_key: str = '', context_value: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. ocionamedtransform(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, name: str, unpremult: bool = True, inverse: bool = False, context_key: str = '', context_value: str = '', colorconfig: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        3. ocionamedtransform(src: OpenImageIO.OpenImageIO.ImageBuf, name: str, unpremult: bool = True, inverse: bool = False, context_key: str = '', context_value: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        4. ocionamedtransform(src: OpenImageIO.OpenImageIO.ImageBuf, name: str, unpremult: bool = True, inverse: bool = False, context_key: str = '', context_value: str = '', colorconfig: str = '', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def over(dst: ImageBuf, A: ImageBuf, B: ImageBuf, roi: ROI = ..., nthreads: int = ...) -> bool:
        """over(*args, **kwargs)
        Overloaded function.

        1. over(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. over(A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def over(A: ImageBuf, B: ImageBuf, roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """over(*args, **kwargs)
        Overloaded function.

        1. over(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. over(A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @staticmethod
    def paste(dst: ImageBuf, xbegin: int, ybegin: int, zbegin: int, chbegin: int, src: ImageBuf, roi: ROI = ..., nthreads: int = ...) -> bool:
        """paste(dst: OpenImageIO.OpenImageIO.ImageBuf, xbegin: int, ybegin: int, zbegin: int, chbegin: int, src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool"""
    @overload
    @staticmethod
    def polar_to_complex(dst: ImageBuf, src: ImageBuf, roi: ROI = ..., nthreads: int = ...) -> bool:
        """polar_to_complex(*args, **kwargs)
        Overloaded function.

        1. polar_to_complex(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. polar_to_complex(src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def polar_to_complex(src: ImageBuf, roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """polar_to_complex(*args, **kwargs)
        Overloaded function.

        1. polar_to_complex(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. polar_to_complex(src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def pow(dst: ImageBuf, A: ImageBuf, B: object, roi: ROI = ..., nthreads: int = ...) -> bool:
        """pow(*args, **kwargs)
        Overloaded function.

        1. pow(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. pow(A: OpenImageIO.OpenImageIO.ImageBuf, B: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def pow(A: ImageBuf, B: object, roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """pow(*args, **kwargs)
        Overloaded function.

        1. pow(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. pow(A: OpenImageIO.OpenImageIO.ImageBuf, B: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def premult(dst: ImageBuf, src: ImageBuf, roi: ROI = ..., nthreads: int = ...) -> bool:
        """premult(*args, **kwargs)
        Overloaded function.

        1. premult(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. premult(src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def premult(src: ImageBuf, roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """premult(*args, **kwargs)
        Overloaded function.

        1. premult(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. premult(src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def rangecompress(dst: ImageBuf, src: ImageBuf, useluma: bool = ..., roi: ROI = ..., nthreads: int = ...) -> bool:
        """rangecompress(*args, **kwargs)
        Overloaded function.

        1. rangecompress(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, useluma: bool = False, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. rangecompress(src: OpenImageIO.OpenImageIO.ImageBuf, useluma: bool = False, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def rangecompress(src: ImageBuf, useluma: bool = ..., roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """rangecompress(*args, **kwargs)
        Overloaded function.

        1. rangecompress(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, useluma: bool = False, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. rangecompress(src: OpenImageIO.OpenImageIO.ImageBuf, useluma: bool = False, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def rangeexpand(dst: ImageBuf, src: ImageBuf, useluma: bool = ..., roi: ROI = ..., nthreads: int = ...) -> bool:
        """rangeexpand(*args, **kwargs)
        Overloaded function.

        1. rangeexpand(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, useluma: bool = False, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. rangeexpand(src: OpenImageIO.OpenImageIO.ImageBuf, useluma: bool = False, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def rangeexpand(src: ImageBuf, useluma: bool = ..., roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """rangeexpand(*args, **kwargs)
        Overloaded function.

        1. rangeexpand(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, useluma: bool = False, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. rangeexpand(src: OpenImageIO.OpenImageIO.ImageBuf, useluma: bool = False, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @staticmethod
    def render_box(dst: ImageBuf, x1: int, y1: int, x2: int, y2: int, color: object = ..., fill: bool = ...) -> bool:
        """render_box(dst: OpenImageIO.OpenImageIO.ImageBuf, x1: int, y1: int, x2: int, y2: int, color: object = None, fill: bool = False) -> bool"""
    @staticmethod
    def render_line(dst: ImageBuf, x1: int, y1: int, x2: int, y2: int, color: object = ..., skip_first_point: bool = ...) -> bool:
        """render_line(dst: OpenImageIO.OpenImageIO.ImageBuf, x1: int, y1: int, x2: int, y2: int, color: object = None, skip_first_point: bool = False) -> bool"""
    @staticmethod
    def render_point(dst: ImageBuf, x: int, y: int, color: object = ...) -> bool:
        """render_point(dst: OpenImageIO.OpenImageIO.ImageBuf, x: int, y: int, color: object = None) -> bool"""
    @staticmethod
    def render_text(dst: ImageBuf, x: int, y: int, text: str, fontsize: int = ..., fontname: str = ..., textcolor: object = ..., alignx: str = ..., aligny: str = ..., shadow: int = ..., roi: ROI = ..., nthreads: int = ...) -> bool:
        """render_text(dst: OpenImageIO.OpenImageIO.ImageBuf, x: int, y: int, text: str, fontsize: int = 16, fontname: str = '', textcolor: object = (), alignx: str = 'left', aligny: str = 'baseline', shadow: int = 0, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool"""
    @overload
    @staticmethod
    def reorient(dst: ImageBuf, src: ImageBuf, nthreads: int = ...) -> bool:
        """reorient(*args, **kwargs)
        Overloaded function.

        1. reorient(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, nthreads: int = 0) -> bool

        2. reorient(src: OpenImageIO.OpenImageIO.ImageBuf, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def reorient(src: ImageBuf, nthreads: int = ...) -> ImageBuf:
        """reorient(*args, **kwargs)
        Overloaded function.

        1. reorient(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, nthreads: int = 0) -> bool

        2. reorient(src: OpenImageIO.OpenImageIO.ImageBuf, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def repremult(dst: ImageBuf, src: ImageBuf, roi: ROI = ..., nthreads: int = ...) -> bool:
        """repremult(*args, **kwargs)
        Overloaded function.

        1. repremult(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. repremult(src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def repremult(src: ImageBuf, roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """repremult(*args, **kwargs)
        Overloaded function.

        1. repremult(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. repremult(src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def resample(dst: ImageBuf, src: ImageBuf, interpolate: bool = ..., roi: ROI = ..., nthreads: int = ...) -> bool:
        """resample(*args, **kwargs)
        Overloaded function.

        1. resample(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, interpolate: bool = True, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. resample(src: OpenImageIO.OpenImageIO.ImageBuf, interpolate: bool = True, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def resample(src: ImageBuf, interpolate: bool = ..., roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """resample(*args, **kwargs)
        Overloaded function.

        1. resample(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, interpolate: bool = True, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. resample(src: OpenImageIO.OpenImageIO.ImageBuf, interpolate: bool = True, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def resize(dst: ImageBuf, src: ImageBuf, filtername: str = ..., filterwidth: float = ..., roi: ROI = ..., nthreads: int = ...) -> bool:
        """resize(*args, **kwargs)
        Overloaded function.

        1. resize(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, filtername: str = '', filterwidth: float = 0.0, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. resize(src: OpenImageIO.OpenImageIO.ImageBuf, filtername: str = '', filterwidth: float = 0.0, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def resize(src: ImageBuf, filtername: str = ..., filterwidth: float = ..., roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """resize(*args, **kwargs)
        Overloaded function.

        1. resize(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, filtername: str = '', filterwidth: float = 0.0, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. resize(src: OpenImageIO.OpenImageIO.ImageBuf, filtername: str = '', filterwidth: float = 0.0, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def rotate(dst: ImageBuf, src: ImageBuf, angle: float, filtername: str = ..., filterwidth: float = ..., recompute_roi: bool = ..., roi: ROI = ..., nthreads: int = ...) -> bool:
        """rotate(*args, **kwargs)
        Overloaded function.

        1. rotate(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, angle: float, filtername: str = '', filterwidth: float = 0.0, recompute_roi: bool = False, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. rotate(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, angle: float, center_x: float, center_y: float, filtername: str = '', filterwidth: float = 0.0, recompute_roi: bool = False, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        3. rotate(src: OpenImageIO.OpenImageIO.ImageBuf, angle: float, filtername: str = '', filterwidth: float = 0.0, recompute_roi: bool = False, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        4. rotate(src: OpenImageIO.OpenImageIO.ImageBuf, angle: float, center_x: float, center_y: float, filtername: str = '', filterwidth: float = 0.0, recompute_roi: bool = False, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def rotate(dst: ImageBuf, src: ImageBuf, angle: float, center_x: float, center_y: float, filtername: str = ..., filterwidth: float = ..., recompute_roi: bool = ..., roi: ROI = ..., nthreads: int = ...) -> bool:
        """rotate(*args, **kwargs)
        Overloaded function.

        1. rotate(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, angle: float, filtername: str = '', filterwidth: float = 0.0, recompute_roi: bool = False, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. rotate(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, angle: float, center_x: float, center_y: float, filtername: str = '', filterwidth: float = 0.0, recompute_roi: bool = False, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        3. rotate(src: OpenImageIO.OpenImageIO.ImageBuf, angle: float, filtername: str = '', filterwidth: float = 0.0, recompute_roi: bool = False, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        4. rotate(src: OpenImageIO.OpenImageIO.ImageBuf, angle: float, center_x: float, center_y: float, filtername: str = '', filterwidth: float = 0.0, recompute_roi: bool = False, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def rotate(src: ImageBuf, angle: float, filtername: str = ..., filterwidth: float = ..., recompute_roi: bool = ..., roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """rotate(*args, **kwargs)
        Overloaded function.

        1. rotate(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, angle: float, filtername: str = '', filterwidth: float = 0.0, recompute_roi: bool = False, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. rotate(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, angle: float, center_x: float, center_y: float, filtername: str = '', filterwidth: float = 0.0, recompute_roi: bool = False, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        3. rotate(src: OpenImageIO.OpenImageIO.ImageBuf, angle: float, filtername: str = '', filterwidth: float = 0.0, recompute_roi: bool = False, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        4. rotate(src: OpenImageIO.OpenImageIO.ImageBuf, angle: float, center_x: float, center_y: float, filtername: str = '', filterwidth: float = 0.0, recompute_roi: bool = False, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def rotate(src: ImageBuf, angle: float, center_x: float, center_y: float, filtername: str = ..., filterwidth: float = ..., recompute_roi: bool = ..., roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """rotate(*args, **kwargs)
        Overloaded function.

        1. rotate(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, angle: float, filtername: str = '', filterwidth: float = 0.0, recompute_roi: bool = False, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. rotate(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, angle: float, center_x: float, center_y: float, filtername: str = '', filterwidth: float = 0.0, recompute_roi: bool = False, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        3. rotate(src: OpenImageIO.OpenImageIO.ImageBuf, angle: float, filtername: str = '', filterwidth: float = 0.0, recompute_roi: bool = False, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        4. rotate(src: OpenImageIO.OpenImageIO.ImageBuf, angle: float, center_x: float, center_y: float, filtername: str = '', filterwidth: float = 0.0, recompute_roi: bool = False, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def rotate180(dst: ImageBuf, src: ImageBuf, roi: ROI = ..., nthreads: int = ...) -> bool:
        """rotate180(*args, **kwargs)
        Overloaded function.

        1. rotate180(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. rotate180(src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def rotate180(src: ImageBuf, roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """rotate180(*args, **kwargs)
        Overloaded function.

        1. rotate180(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. rotate180(src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def rotate270(dst: ImageBuf, src: ImageBuf, roi: ROI = ..., nthreads: int = ...) -> bool:
        """rotate270(*args, **kwargs)
        Overloaded function.

        1. rotate270(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. rotate270(src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def rotate270(src: ImageBuf, roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """rotate270(*args, **kwargs)
        Overloaded function.

        1. rotate270(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. rotate270(src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def rotate90(dst: ImageBuf, src: ImageBuf, roi: ROI = ..., nthreads: int = ...) -> bool:
        """rotate90(*args, **kwargs)
        Overloaded function.

        1. rotate90(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. rotate90(src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def rotate90(src: ImageBuf, roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """rotate90(*args, **kwargs)
        Overloaded function.

        1. rotate90(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. rotate90(src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def saturate(dst: ImageBuf, src: ImageBuf, scale: float = ..., firstchannel: int = ..., roi: ROI = ..., nthreads: int = ...) -> bool:
        """saturate(*args, **kwargs)
        Overloaded function.

        1. saturate(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, scale: float = 0.0, firstchannel: int = 0, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. saturate(src: OpenImageIO.OpenImageIO.ImageBuf, scale: float = 0.0, firstchannel: int = 0, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def saturate(src: ImageBuf, scale: float = ..., firstchannel: int = ..., roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """saturate(*args, **kwargs)
        Overloaded function.

        1. saturate(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, scale: float = 0.0, firstchannel: int = 0, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. saturate(src: OpenImageIO.OpenImageIO.ImageBuf, scale: float = 0.0, firstchannel: int = 0, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def scale(dst: ImageBuf, A: ImageBuf, B: ImageBuf, roi: ROI = ..., nthreads: int = ...) -> bool:
        """scale(*args, **kwargs)
        Overloaded function.

        1. scale(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. scale(A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def scale(A: ImageBuf, B: ImageBuf, roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """scale(*args, **kwargs)
        Overloaded function.

        1. scale(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. scale(A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def st_warp(dst: ImageBuf, src: ImageBuf, stbuf: ImageBuf, filtername: str = ..., filterwidth: float = ..., chan_s: int = ..., chan_t: int = ..., flip_s: bool = ..., flip_t: bool = ..., roi: ROI = ..., nthreads: int = ...) -> bool:
        """st_warp(*args, **kwargs)
        Overloaded function.

        1. st_warp(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, stbuf: OpenImageIO.OpenImageIO.ImageBuf, filtername: str = '', filterwidth: float = 0.0, chan_s: int = 0, chan_t: int = 1, flip_s: bool = False, flip_t: bool = False, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. st_warp(src: OpenImageIO.OpenImageIO.ImageBuf, stbuf: OpenImageIO.OpenImageIO.ImageBuf, filtername: str = '', filterwidth: float = 0.0, chan_s: int = 0, chan_t: int = 1, flip_s: bool = False, flip_t: bool = False, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def st_warp(src: ImageBuf, stbuf: ImageBuf, filtername: str = ..., filterwidth: float = ..., chan_s: int = ..., chan_t: int = ..., flip_s: bool = ..., flip_t: bool = ..., roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """st_warp(*args, **kwargs)
        Overloaded function.

        1. st_warp(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, stbuf: OpenImageIO.OpenImageIO.ImageBuf, filtername: str = '', filterwidth: float = 0.0, chan_s: int = 0, chan_t: int = 1, flip_s: bool = False, flip_t: bool = False, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. st_warp(src: OpenImageIO.OpenImageIO.ImageBuf, stbuf: OpenImageIO.OpenImageIO.ImageBuf, filtername: str = '', filterwidth: float = 0.0, chan_s: int = 0, chan_t: int = 1, flip_s: bool = False, flip_t: bool = False, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def sub(dst: ImageBuf, A: ImageBuf, B: ImageBuf, roi: ROI = ..., nthreads: int = ...) -> bool:
        """sub(*args, **kwargs)
        Overloaded function.

        1. sub(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. sub(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        3. sub(A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        4. sub(A: OpenImageIO.OpenImageIO.ImageBuf, B: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def sub(dst: ImageBuf, A: ImageBuf, B: object, roi: ROI = ..., nthreads: int = ...) -> bool:
        """sub(*args, **kwargs)
        Overloaded function.

        1. sub(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. sub(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        3. sub(A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        4. sub(A: OpenImageIO.OpenImageIO.ImageBuf, B: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def sub(A: ImageBuf, B: ImageBuf, roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """sub(*args, **kwargs)
        Overloaded function.

        1. sub(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. sub(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        3. sub(A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        4. sub(A: OpenImageIO.OpenImageIO.ImageBuf, B: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def sub(A: ImageBuf, B: object, roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """sub(*args, **kwargs)
        Overloaded function.

        1. sub(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. sub(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        3. sub(A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf

        4. sub(A: OpenImageIO.OpenImageIO.ImageBuf, B: object, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @staticmethod
    def text_size(text: str, fontsize: int = ..., fontname: str = ...) -> ROI:
        """text_size(text: str, fontsize: int = 16, fontname: str = '') -> OpenImageIO.OpenImageIO.ROI"""
    @overload
    @staticmethod
    def transpose(dst: ImageBuf, src: ImageBuf, roi: ROI = ..., nthreads: int = ...) -> bool:
        """transpose(*args, **kwargs)
        Overloaded function.

        1. transpose(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. transpose(src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def transpose(src: ImageBuf, roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """transpose(*args, **kwargs)
        Overloaded function.

        1. transpose(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. transpose(src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def unpremult(dst: ImageBuf, src: ImageBuf, roi: ROI = ..., nthreads: int = ...) -> bool:
        """unpremult(*args, **kwargs)
        Overloaded function.

        1. unpremult(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. unpremult(src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def unpremult(src: ImageBuf, roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """unpremult(*args, **kwargs)
        Overloaded function.

        1. unpremult(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. unpremult(src: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def unsharp_mask(dst: ImageBuf, src: ImageBuf, kernel: str = ..., width: float = ..., contrast: float = ..., threshold: float = ..., roi: ROI = ..., nthreads: int = ...) -> bool:
        """unsharp_mask(*args, **kwargs)
        Overloaded function.

        1. unsharp_mask(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, kernel: str = 'gaussian', width: float = 3.0, contrast: float = 1.0, threshold: float = 0.0, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. unsharp_mask(src: OpenImageIO.OpenImageIO.ImageBuf, kernel: str = 'gaussian', width: float = 3.0, contrast: float = 1.0, threshold: float = 0.0, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def unsharp_mask(src: ImageBuf, kernel: str = ..., width: float = ..., contrast: float = ..., threshold: float = ..., roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """unsharp_mask(*args, **kwargs)
        Overloaded function.

        1. unsharp_mask(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, kernel: str = 'gaussian', width: float = 3.0, contrast: float = 1.0, threshold: float = 0.0, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. unsharp_mask(src: OpenImageIO.OpenImageIO.ImageBuf, kernel: str = 'gaussian', width: float = 3.0, contrast: float = 1.0, threshold: float = 0.0, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def warp(dst: ImageBuf, src: ImageBuf, M: object, filtername: str = ..., filterwidth: float = ..., recompute_roi: bool = ..., wrap: str = ..., roi: ROI = ..., nthreads: int = ...) -> bool:
        """warp(*args, **kwargs)
        Overloaded function.

        1. warp(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, M: object, filtername: str = '', filterwidth: float = 0.0, recompute_roi: bool = False, wrap: str = 'default', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. warp(src: OpenImageIO.OpenImageIO.ImageBuf, M: object, filtername: str = '', filterwidth: float = 0.0, recompute_roi: bool = False, wrap: str = 'default', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def warp(src: ImageBuf, M: object, filtername: str = ..., filterwidth: float = ..., recompute_roi: bool = ..., wrap: str = ..., roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """warp(*args, **kwargs)
        Overloaded function.

        1. warp(dst: OpenImageIO.OpenImageIO.ImageBuf, src: OpenImageIO.OpenImageIO.ImageBuf, M: object, filtername: str = '', filterwidth: float = 0.0, recompute_roi: bool = False, wrap: str = 'default', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. warp(src: OpenImageIO.OpenImageIO.ImageBuf, M: object, filtername: str = '', filterwidth: float = 0.0, recompute_roi: bool = False, wrap: str = 'default', roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def zero(dst: ImageBuf, roi: ROI = ..., nthreads: int = ...) -> bool:
        """zero(*args, **kwargs)
        Overloaded function.

        1. zero(dst: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. zero(roi: OpenImageIO.OpenImageIO.ROI, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def zero(roi: ROI, nthreads: int = ...) -> ImageBuf:
        """zero(*args, **kwargs)
        Overloaded function.

        1. zero(dst: OpenImageIO.OpenImageIO.ImageBuf, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. zero(roi: OpenImageIO.OpenImageIO.ROI, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def zover(dst: ImageBuf, A: ImageBuf, B: ImageBuf, z_zeroisinf: bool = ..., roi: ROI = ..., nthreads: int = ...) -> bool:
        """zover(*args, **kwargs)
        Overloaded function.

        1. zover(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, z_zeroisinf: bool = False, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. zover(A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, z_zeroisinf: bool = False, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """
    @overload
    @staticmethod
    def zover(A: ImageBuf, B: ImageBuf, z_zeroisinf: bool = ..., roi: ROI = ..., nthreads: int = ...) -> ImageBuf:
        """zover(*args, **kwargs)
        Overloaded function.

        1. zover(dst: OpenImageIO.OpenImageIO.ImageBuf, A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, z_zeroisinf: bool = False, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> bool

        2. zover(A: OpenImageIO.OpenImageIO.ImageBuf, B: OpenImageIO.OpenImageIO.ImageBuf, z_zeroisinf: bool = False, roi: OpenImageIO.OpenImageIO.ROI = <OpenImageIO.OpenImageIO.ROI object>, nthreads: int = 0) -> OpenImageIO.OpenImageIO.ImageBuf
        """

class ImageCache:
    def __init__(self, shared: bool = ...) -> None:
        """__init__(self: OpenImageIO.OpenImageIO.ImageCache, shared: bool = True) -> None"""
    def _pybind11_conduit_v1_(self, *args, **kwargs): ...
    @overload
    def attribute(self, arg0: str, arg1: float) -> None:
        """attribute(*args, **kwargs)
        Overloaded function.

        1. attribute(self: OpenImageIO.OpenImageIO.ImageCache, arg0: str, arg1: float) -> None

        2. attribute(self: OpenImageIO.OpenImageIO.ImageCache, arg0: str, arg1: int) -> None

        3. attribute(self: OpenImageIO.OpenImageIO.ImageCache, arg0: str, arg1: str) -> None

        4. attribute(self: OpenImageIO.OpenImageIO.ImageCache, arg0: str, arg1: OpenImageIO.OpenImageIO.TypeDesc, arg2: object) -> None
        """
    @overload
    def attribute(self, arg0: str, arg1: int) -> None:
        """attribute(*args, **kwargs)
        Overloaded function.

        1. attribute(self: OpenImageIO.OpenImageIO.ImageCache, arg0: str, arg1: float) -> None

        2. attribute(self: OpenImageIO.OpenImageIO.ImageCache, arg0: str, arg1: int) -> None

        3. attribute(self: OpenImageIO.OpenImageIO.ImageCache, arg0: str, arg1: str) -> None

        4. attribute(self: OpenImageIO.OpenImageIO.ImageCache, arg0: str, arg1: OpenImageIO.OpenImageIO.TypeDesc, arg2: object) -> None
        """
    @overload
    def attribute(self, arg0: str, arg1: str) -> None:
        """attribute(*args, **kwargs)
        Overloaded function.

        1. attribute(self: OpenImageIO.OpenImageIO.ImageCache, arg0: str, arg1: float) -> None

        2. attribute(self: OpenImageIO.OpenImageIO.ImageCache, arg0: str, arg1: int) -> None

        3. attribute(self: OpenImageIO.OpenImageIO.ImageCache, arg0: str, arg1: str) -> None

        4. attribute(self: OpenImageIO.OpenImageIO.ImageCache, arg0: str, arg1: OpenImageIO.OpenImageIO.TypeDesc, arg2: object) -> None
        """
    @overload
    def attribute(self, arg0: str, arg1: TypeDesc, arg2: object) -> None:
        """attribute(*args, **kwargs)
        Overloaded function.

        1. attribute(self: OpenImageIO.OpenImageIO.ImageCache, arg0: str, arg1: float) -> None

        2. attribute(self: OpenImageIO.OpenImageIO.ImageCache, arg0: str, arg1: int) -> None

        3. attribute(self: OpenImageIO.OpenImageIO.ImageCache, arg0: str, arg1: str) -> None

        4. attribute(self: OpenImageIO.OpenImageIO.ImageCache, arg0: str, arg1: OpenImageIO.OpenImageIO.TypeDesc, arg2: object) -> None
        """
    @staticmethod
    def destroy(cache: ImageCache, teardown: bool = ...) -> None:
        """destroy(cache: OpenImageIO.OpenImageIO.ImageCache, teardown: bool = False) -> None"""
    def get_cache_dimensions(self, filename: str, subimage: int = ..., miplevel: int = ...) -> ImageSpec:
        """get_cache_dimensions(self: OpenImageIO.OpenImageIO.ImageCache, filename: str, subimage: int = 0, miplevel: int = 0) -> OpenImageIO.OpenImageIO.ImageSpec"""
    def get_imagespec(self, filename: str, subimage: int = ...) -> ImageSpec:
        """get_imagespec(self: OpenImageIO.OpenImageIO.ImageCache, filename: str, subimage: int = 0) -> OpenImageIO.OpenImageIO.ImageSpec"""
    def get_pixels(self, filename: str, subimage: int, miplevel: int, xbegin: int, xend: int, ybegin: int, yend: int, zbegin: int = ..., zend: int = ..., datatype: TypeDesc = ...) -> object:
        """get_pixels(self: OpenImageIO.OpenImageIO.ImageCache, filename: str, subimage: int, miplevel: int, xbegin: int, xend: int, ybegin: int, yend: int, zbegin: int = 0, zend: int = 1, datatype: OpenImageIO.OpenImageIO.TypeDesc = <TypeDesc 'unknown'>) -> object"""
    def getattribute(self, name: str, type: TypeDesc = ...) -> object:
        """getattribute(self: OpenImageIO.OpenImageIO.ImageCache, name: str, type: OpenImageIO.OpenImageIO.TypeDesc = <TypeDesc 'unknown'>) -> object"""
    def getattributetype(self, name: str) -> TypeDesc:
        """getattributetype(self: OpenImageIO.OpenImageIO.ImageCache, name: str) -> OpenImageIO.OpenImageIO.TypeDesc"""
    def geterror(self, clear: bool = ...) -> str:
        """geterror(self: OpenImageIO.OpenImageIO.ImageCache, clear: bool = True) -> str"""
    def getstats(self, level: int = ...) -> str:
        """getstats(self: OpenImageIO.OpenImageIO.ImageCache, level: int = 1) -> str"""
    def invalidate(self, filename: str, force: bool = ...) -> None:
        """invalidate(self: OpenImageIO.OpenImageIO.ImageCache, filename: str, force: bool = True) -> None"""
    def invalidate_all(self, force: bool = ...) -> None:
        """invalidate_all(self: OpenImageIO.OpenImageIO.ImageCache, force: bool = False) -> None"""
    def resolve_filename(self, arg0: str) -> str:
        """resolve_filename(self: OpenImageIO.OpenImageIO.ImageCache, arg0: str) -> str"""
    @property
    def has_error(self) -> bool: ...

class ImageInput:
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def _pybind11_conduit_v1_(self, *args, **kwargs): ...
    def close(self) -> bool:
        """close(self: OpenImageIO.OpenImageIO.ImageInput) -> bool"""
    @staticmethod
    def create(filename: str, plugin_searchpath: str = ...) -> object:
        """create(filename: str, plugin_searchpath: str = '') -> object"""
    def current_miplevel(self) -> int:
        """current_miplevel(self: OpenImageIO.OpenImageIO.ImageInput) -> int"""
    def current_subimage(self) -> int:
        """current_subimage(self: OpenImageIO.OpenImageIO.ImageInput) -> int"""
    def format_name(self) -> str:
        """format_name(self: OpenImageIO.OpenImageIO.ImageInput) -> str"""
    def get_thumbnail(self, *args, **kwargs):
        """get_thumbnail(self: OpenImageIO.OpenImageIO.ImageInput, subimage: int = 0) -> OpenImageIO_v3_0::ImageBuf"""
    def geterror(self, clear: bool = ...) -> str:
        """geterror(self: OpenImageIO.OpenImageIO.ImageInput, clear: bool = True) -> str"""
    @overload
    @staticmethod
    def open(filename: str) -> ImageInput:
        """open(*args, **kwargs)
        Overloaded function.

        1. open(filename: str) -> object

        2. open(filename: str, config: OpenImageIO.OpenImageIO.ImageSpec) -> object
        """
    @overload
    @staticmethod
    def open(filename: str, config: ImageSpec) -> ImageInput:
        """open(*args, **kwargs)
        Overloaded function.

        1. open(filename: str) -> object

        2. open(filename: str, config: OpenImageIO.OpenImageIO.ImageSpec) -> object
        """
    @overload
    def read_image(self, subimage: int, miplevel: int, chbegin: int, chend: int, format: TypeDesc = ...) -> npt.NDArray[Any]:
        """read_image(*args, **kwargs)
        Overloaded function.

        1. read_image(self: OpenImageIO.OpenImageIO.ImageInput, subimage: int, miplevel: int, chbegin: int, chend: int, format: OpenImageIO.OpenImageIO.TypeDesc = <TypeDesc 'float'>) -> object

        2. read_image(self: OpenImageIO.OpenImageIO.ImageInput, chbegin: int, chend: int, format: OpenImageIO.OpenImageIO.TypeDesc = <TypeDesc 'float'>) -> object

        3. read_image(self: OpenImageIO.OpenImageIO.ImageInput, format: OpenImageIO.OpenImageIO.TypeDesc = <TypeDesc 'float'>) -> object
        """
    @overload
    def read_image(self, chbegin: int, chend: int, format: TypeDesc = ...) -> object:
        """read_image(*args, **kwargs)
        Overloaded function.

        1. read_image(self: OpenImageIO.OpenImageIO.ImageInput, subimage: int, miplevel: int, chbegin: int, chend: int, format: OpenImageIO.OpenImageIO.TypeDesc = <TypeDesc 'float'>) -> object

        2. read_image(self: OpenImageIO.OpenImageIO.ImageInput, chbegin: int, chend: int, format: OpenImageIO.OpenImageIO.TypeDesc = <TypeDesc 'float'>) -> object

        3. read_image(self: OpenImageIO.OpenImageIO.ImageInput, format: OpenImageIO.OpenImageIO.TypeDesc = <TypeDesc 'float'>) -> object
        """
    @overload
    def read_image(self, format: TypeDesc = ...) -> object:
        """read_image(*args, **kwargs)
        Overloaded function.

        1. read_image(self: OpenImageIO.OpenImageIO.ImageInput, subimage: int, miplevel: int, chbegin: int, chend: int, format: OpenImageIO.OpenImageIO.TypeDesc = <TypeDesc 'float'>) -> object

        2. read_image(self: OpenImageIO.OpenImageIO.ImageInput, chbegin: int, chend: int, format: OpenImageIO.OpenImageIO.TypeDesc = <TypeDesc 'float'>) -> object

        3. read_image(self: OpenImageIO.OpenImageIO.ImageInput, format: OpenImageIO.OpenImageIO.TypeDesc = <TypeDesc 'float'>) -> object
        """
    def read_native_deep_image(self, subimage: int = ..., miplevel: int = ...) -> object:
        """read_native_deep_image(self: OpenImageIO.OpenImageIO.ImageInput, subimage: int = 0, miplevel: int = 0) -> object"""
    def read_native_deep_scanlines(self, subimage: int, miplevel: int, ybegin: int, yend: int, z: int, chbegin: int, chend: int) -> object:
        """read_native_deep_scanlines(self: OpenImageIO.OpenImageIO.ImageInput, subimage: int, miplevel: int, ybegin: int, yend: int, z: int, chbegin: int, chend: int) -> object"""
    def read_native_deep_tiles(self, subimage: int, miplevel: int, xbegin: int, xend: int, ybegin: int, yend: int, zbegin: int, zend: int, chbegin: int, chend: int) -> object:
        """read_native_deep_tiles(self: OpenImageIO.OpenImageIO.ImageInput, subimage: int, miplevel: int, xbegin: int, xend: int, ybegin: int, yend: int, zbegin: int, zend: int, chbegin: int, chend: int) -> object"""
    def read_scanline(self, y: int, z: int = ..., format: TypeDesc = ...) -> object:
        """read_scanline(self: OpenImageIO.OpenImageIO.ImageInput, y: int, z: int = 0, format: OpenImageIO.OpenImageIO.TypeDesc = <TypeDesc 'float'>) -> object"""
    @overload
    def read_scanlines(self, subimage: int, miplevel: int, ybegin: int, yend: int, z: int, chbegin: int, chend: int, format: TypeDesc = ...) -> object:
        """read_scanlines(*args, **kwargs)
        Overloaded function.

        1. read_scanlines(self: OpenImageIO.OpenImageIO.ImageInput, subimage: int, miplevel: int, ybegin: int, yend: int, z: int, chbegin: int, chend: int, format: OpenImageIO.OpenImageIO.TypeDesc = <TypeDesc 'float'>) -> object

        2. read_scanlines(self: OpenImageIO.OpenImageIO.ImageInput, ybegin: int, yend: int, z: int, chbegin: int, chend: int, format: OpenImageIO.OpenImageIO.TypeDesc = <TypeDesc 'float'>) -> object
        """
    @overload
    def read_scanlines(self, ybegin: int, yend: int, z: int, chbegin: int, chend: int, format: TypeDesc = ...) -> object:
        """read_scanlines(*args, **kwargs)
        Overloaded function.

        1. read_scanlines(self: OpenImageIO.OpenImageIO.ImageInput, subimage: int, miplevel: int, ybegin: int, yend: int, z: int, chbegin: int, chend: int, format: OpenImageIO.OpenImageIO.TypeDesc = <TypeDesc 'float'>) -> object

        2. read_scanlines(self: OpenImageIO.OpenImageIO.ImageInput, ybegin: int, yend: int, z: int, chbegin: int, chend: int, format: OpenImageIO.OpenImageIO.TypeDesc = <TypeDesc 'float'>) -> object
        """
    def read_tile(self, x: int, y: int, z: int, format: TypeDesc = ...) -> object:
        """read_tile(self: OpenImageIO.OpenImageIO.ImageInput, x: int, y: int, z: int, format: OpenImageIO.OpenImageIO.TypeDesc = <TypeDesc 'float'>) -> object"""
    @overload
    def read_tiles(self, subimage: int, miplevel: int, xbegin: int, xend: int, ybegin: int, yend: int, zbegin: int, zend: int, chbegin: int, chend: int, format: TypeDesc = ...) -> object:
        """read_tiles(*args, **kwargs)
        Overloaded function.

        1. read_tiles(self: OpenImageIO.OpenImageIO.ImageInput, subimage: int, miplevel: int, xbegin: int, xend: int, ybegin: int, yend: int, zbegin: int, zend: int, chbegin: int, chend: int, format: OpenImageIO.OpenImageIO.TypeDesc = <TypeDesc 'float'>) -> object

        2. read_tiles(self: OpenImageIO.OpenImageIO.ImageInput, xbegin: int, xend: int, ybegin: int, yend: int, zbegin: int, zend: int, chbegin: int, chend: int, format: OpenImageIO.OpenImageIO.TypeDesc = <TypeDesc 'float'>) -> object
        """
    @overload
    def read_tiles(self, xbegin: int, xend: int, ybegin: int, yend: int, zbegin: int, zend: int, chbegin: int, chend: int, format: TypeDesc = ...) -> object:
        """read_tiles(*args, **kwargs)
        Overloaded function.

        1. read_tiles(self: OpenImageIO.OpenImageIO.ImageInput, subimage: int, miplevel: int, xbegin: int, xend: int, ybegin: int, yend: int, zbegin: int, zend: int, chbegin: int, chend: int, format: OpenImageIO.OpenImageIO.TypeDesc = <TypeDesc 'float'>) -> object

        2. read_tiles(self: OpenImageIO.OpenImageIO.ImageInput, xbegin: int, xend: int, ybegin: int, yend: int, zbegin: int, zend: int, chbegin: int, chend: int, format: OpenImageIO.OpenImageIO.TypeDesc = <TypeDesc 'float'>) -> object
        """
    def seek_subimage(self, arg0: int, arg1: int) -> bool:
        """seek_subimage(self: OpenImageIO.OpenImageIO.ImageInput, arg0: int, arg1: int) -> bool"""
    @overload
    def spec(self) -> ImageSpec:
        """spec(*args, **kwargs)
        Overloaded function.

        1. spec(self: OpenImageIO.OpenImageIO.ImageInput) -> OpenImageIO.OpenImageIO.ImageSpec

        2. spec(self: OpenImageIO.OpenImageIO.ImageInput, subimage: int, miplevel: int = 0) -> OpenImageIO.OpenImageIO.ImageSpec
        """
    @overload
    def spec(self, subimage: int, miplevel: int = ...) -> ImageSpec:
        """spec(*args, **kwargs)
        Overloaded function.

        1. spec(self: OpenImageIO.OpenImageIO.ImageInput) -> OpenImageIO.OpenImageIO.ImageSpec

        2. spec(self: OpenImageIO.OpenImageIO.ImageInput, subimage: int, miplevel: int = 0) -> OpenImageIO.OpenImageIO.ImageSpec
        """
    def spec_dimensions(self, subimage: int, miplevel: int = ...) -> ImageSpec:
        """spec_dimensions(self: OpenImageIO.OpenImageIO.ImageInput, subimage: int, miplevel: int = 0) -> OpenImageIO.OpenImageIO.ImageSpec"""
    def supports(self, arg0: str) -> int:
        """supports(self: OpenImageIO.OpenImageIO.ImageInput, arg0: str) -> int"""
    def valid_file(self, arg0: str) -> bool:
        """valid_file(self: OpenImageIO.OpenImageIO.ImageInput, arg0: str) -> bool"""
    @property
    def has_error(self) -> bool: ...

class ImageOutput:
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def _pybind11_conduit_v1_(self, *args, **kwargs): ...
    def close(self) -> bool:
        """close(self: OpenImageIO.OpenImageIO.ImageOutput) -> bool"""
    def copy_image(self, arg0: ImageInput) -> bool:
        """copy_image(self: OpenImageIO.OpenImageIO.ImageOutput, arg0: OpenImageIO.OpenImageIO.ImageInput) -> bool"""
    @staticmethod
    def create(filename: str, plugin_searchpath: str = ...) -> ImageOutput:
        """create(filename: str, plugin_searchpath: str = '') -> object"""
    def format_name(self) -> str:
        """format_name(self: OpenImageIO.OpenImageIO.ImageOutput) -> str"""
    def geterror(self, clear: bool = ...) -> str:
        """geterror(self: OpenImageIO.OpenImageIO.ImageOutput, clear: bool = True) -> str"""
    @overload
    def open(self, filename: str, spec: ImageSpec, mode: str = ...) -> bool:
        """open(*args, **kwargs)
        Overloaded function.

        1. open(self: OpenImageIO.OpenImageIO.ImageOutput, filename: str, spec: OpenImageIO.OpenImageIO.ImageSpec, mode: str = 'Create') -> bool

        2. open(self: OpenImageIO.OpenImageIO.ImageOutput, filename: str, specs: list[OpenImageIO.OpenImageIO.ImageSpec]) -> bool

        3. open(self: OpenImageIO.OpenImageIO.ImageOutput, arg0: str, arg1: tuple) -> bool
        """
    @overload
    def open(self, filename: str, specs: list[ImageSpec]) -> bool:
        """open(*args, **kwargs)
        Overloaded function.

        1. open(self: OpenImageIO.OpenImageIO.ImageOutput, filename: str, spec: OpenImageIO.OpenImageIO.ImageSpec, mode: str = 'Create') -> bool

        2. open(self: OpenImageIO.OpenImageIO.ImageOutput, filename: str, specs: list[OpenImageIO.OpenImageIO.ImageSpec]) -> bool

        3. open(self: OpenImageIO.OpenImageIO.ImageOutput, arg0: str, arg1: tuple) -> bool
        """
    @overload
    def open(self, arg0: str, arg1: tuple) -> bool:
        """open(*args, **kwargs)
        Overloaded function.

        1. open(self: OpenImageIO.OpenImageIO.ImageOutput, filename: str, spec: OpenImageIO.OpenImageIO.ImageSpec, mode: str = 'Create') -> bool

        2. open(self: OpenImageIO.OpenImageIO.ImageOutput, filename: str, specs: list[OpenImageIO.OpenImageIO.ImageSpec]) -> bool

        3. open(self: OpenImageIO.OpenImageIO.ImageOutput, arg0: str, arg1: tuple) -> bool
        """
    def set_thumbnail(self, arg0) -> bool:
        """set_thumbnail(self: OpenImageIO.OpenImageIO.ImageOutput, arg0: OpenImageIO_v3_0::ImageBuf) -> bool"""
    def spec(self) -> ImageSpec:
        """spec(self: OpenImageIO.OpenImageIO.ImageOutput) -> OpenImageIO.OpenImageIO.ImageSpec"""
    def supports(self, arg0: str) -> int:
        """supports(self: OpenImageIO.OpenImageIO.ImageOutput, arg0: str) -> int"""
    def write_deep_image(self, arg0: DeepData) -> bool:
        """write_deep_image(self: OpenImageIO.OpenImageIO.ImageOutput, arg0: OpenImageIO.OpenImageIO.DeepData) -> bool"""
    def write_deep_scanlines(self, ybegin: int, yend: int, z: int, deepdata: DeepData) -> bool:
        """write_deep_scanlines(self: OpenImageIO.OpenImageIO.ImageOutput, ybegin: int, yend: int, z: int, deepdata: OpenImageIO.OpenImageIO.DeepData) -> bool"""
    def write_deep_tiles(self, xbegin: int, xend: int, ybegin: int, yend: int, zbegin: int, zend: int, deepdata: DeepData) -> bool:
        """write_deep_tiles(self: OpenImageIO.OpenImageIO.ImageOutput, xbegin: int, xend: int, ybegin: int, yend: int, zbegin: int, zend: int, deepdata: OpenImageIO.OpenImageIO.DeepData) -> bool"""
    def write_image(self, arg0: Buffer) -> bool:
        """write_image(self: OpenImageIO.OpenImageIO.ImageOutput, arg0: Buffer) -> bool"""
    def write_scanline(self, y: int, z: int, pixels: Buffer) -> bool:
        """write_scanline(self: OpenImageIO.OpenImageIO.ImageOutput, y: int, z: int, pixels: Buffer) -> bool"""
    def write_scanlines(self, ybegin: int, yend: int, z: int, pixels: Buffer) -> bool:
        """write_scanlines(self: OpenImageIO.OpenImageIO.ImageOutput, ybegin: int, yend: int, z: int, pixels: Buffer) -> bool"""
    def write_tile(self, x: int, y: int, z: int, pixels: Buffer) -> bool:
        """write_tile(self: OpenImageIO.OpenImageIO.ImageOutput, x: int, y: int, z: int, pixels: Buffer) -> bool"""
    def write_tiles(self, xbegin: int, xend: int, ybegin: int, yend: int, zbegin: int, zend: int, pixels: Buffer) -> bool:
        """write_tiles(self: OpenImageIO.OpenImageIO.ImageOutput, xbegin: int, xend: int, ybegin: int, yend: int, zbegin: int, zend: int, pixels: Buffer) -> bool"""
    @property
    def has_error(self) -> bool: ...

class ImageSpec:
    alpha_channel: int
    channelformats: tuple
    channelnames: tuple
    deep: bool
    depth: int
    extra_attribs: ParamValueList
    format: TypeDesc
    full_depth: int
    full_height: int
    full_width: int
    full_x: int
    full_y: int
    full_z: int
    height: int
    nchannels: int
    roi: Incomplete
    roi_full: Incomplete
    tile_depth: int
    tile_height: int
    tile_width: int
    width: int
    x: int
    y: int
    z: int
    z_channel: int
    @overload
    def __init__(self) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: OpenImageIO.OpenImageIO.ImageSpec) -> None

        2. __init__(self: OpenImageIO.OpenImageIO.ImageSpec, arg0: int, arg1: int, arg2: int, arg3: OpenImageIO.OpenImageIO.TypeDesc) -> None

        3. __init__(self: OpenImageIO.OpenImageIO.ImageSpec, arg0: OpenImageIO_v3_0::ROI, arg1: OpenImageIO.OpenImageIO.TypeDesc) -> None

        4. __init__(self: OpenImageIO.OpenImageIO.ImageSpec, arg0: OpenImageIO.OpenImageIO.TypeDesc) -> None

        5. __init__(self: OpenImageIO.OpenImageIO.ImageSpec, arg0: OpenImageIO.OpenImageIO.ImageSpec) -> None
        """
    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: BASETYPE) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: OpenImageIO.OpenImageIO.ImageSpec) -> None

        2. __init__(self: OpenImageIO.OpenImageIO.ImageSpec, arg0: int, arg1: int, arg2: int, arg3: OpenImageIO.OpenImageIO.TypeDesc) -> None

        3. __init__(self: OpenImageIO.OpenImageIO.ImageSpec, arg0: OpenImageIO_v3_0::ROI, arg1: OpenImageIO.OpenImageIO.TypeDesc) -> None

        4. __init__(self: OpenImageIO.OpenImageIO.ImageSpec, arg0: OpenImageIO.OpenImageIO.TypeDesc) -> None

        5. __init__(self: OpenImageIO.OpenImageIO.ImageSpec, arg0: OpenImageIO.OpenImageIO.ImageSpec) -> None
        """
    @overload
    def __init__(self, arg0, arg1: TypeDesc) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: OpenImageIO.OpenImageIO.ImageSpec) -> None

        2. __init__(self: OpenImageIO.OpenImageIO.ImageSpec, arg0: int, arg1: int, arg2: int, arg3: OpenImageIO.OpenImageIO.TypeDesc) -> None

        3. __init__(self: OpenImageIO.OpenImageIO.ImageSpec, arg0: OpenImageIO_v3_0::ROI, arg1: OpenImageIO.OpenImageIO.TypeDesc) -> None

        4. __init__(self: OpenImageIO.OpenImageIO.ImageSpec, arg0: OpenImageIO.OpenImageIO.TypeDesc) -> None

        5. __init__(self: OpenImageIO.OpenImageIO.ImageSpec, arg0: OpenImageIO.OpenImageIO.ImageSpec) -> None
        """
    @overload
    def __init__(self, arg0: TypeDesc) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: OpenImageIO.OpenImageIO.ImageSpec) -> None

        2. __init__(self: OpenImageIO.OpenImageIO.ImageSpec, arg0: int, arg1: int, arg2: int, arg3: OpenImageIO.OpenImageIO.TypeDesc) -> None

        3. __init__(self: OpenImageIO.OpenImageIO.ImageSpec, arg0: OpenImageIO_v3_0::ROI, arg1: OpenImageIO.OpenImageIO.TypeDesc) -> None

        4. __init__(self: OpenImageIO.OpenImageIO.ImageSpec, arg0: OpenImageIO.OpenImageIO.TypeDesc) -> None

        5. __init__(self: OpenImageIO.OpenImageIO.ImageSpec, arg0: OpenImageIO.OpenImageIO.ImageSpec) -> None
        """
    @overload
    def __init__(self, arg0: ImageSpec) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: OpenImageIO.OpenImageIO.ImageSpec) -> None

        2. __init__(self: OpenImageIO.OpenImageIO.ImageSpec, arg0: int, arg1: int, arg2: int, arg3: OpenImageIO.OpenImageIO.TypeDesc) -> None

        3. __init__(self: OpenImageIO.OpenImageIO.ImageSpec, arg0: OpenImageIO_v3_0::ROI, arg1: OpenImageIO.OpenImageIO.TypeDesc) -> None

        4. __init__(self: OpenImageIO.OpenImageIO.ImageSpec, arg0: OpenImageIO.OpenImageIO.TypeDesc) -> None

        5. __init__(self: OpenImageIO.OpenImageIO.ImageSpec, arg0: OpenImageIO.OpenImageIO.ImageSpec) -> None
        """
    def _pybind11_conduit_v1_(self, *args, **kwargs): ...
    @overload
    def attribute(self, arg0: str, arg1: float) -> None:
        """attribute(*args, **kwargs)
        Overloaded function.

        1. attribute(self: OpenImageIO.OpenImageIO.ImageSpec, arg0: str, arg1: float) -> None

        2. attribute(self: OpenImageIO.OpenImageIO.ImageSpec, arg0: str, arg1: int) -> None

        3. attribute(self: OpenImageIO.OpenImageIO.ImageSpec, arg0: str, arg1: str) -> None

        4. attribute(self: OpenImageIO.OpenImageIO.ImageSpec, arg0: str, arg1: OpenImageIO.OpenImageIO.TypeDesc, arg2: object) -> None
        """
    @overload
    def attribute(self, arg0: str, arg1: int) -> None:
        """attribute(*args, **kwargs)
        Overloaded function.

        1. attribute(self: OpenImageIO.OpenImageIO.ImageSpec, arg0: str, arg1: float) -> None

        2. attribute(self: OpenImageIO.OpenImageIO.ImageSpec, arg0: str, arg1: int) -> None

        3. attribute(self: OpenImageIO.OpenImageIO.ImageSpec, arg0: str, arg1: str) -> None

        4. attribute(self: OpenImageIO.OpenImageIO.ImageSpec, arg0: str, arg1: OpenImageIO.OpenImageIO.TypeDesc, arg2: object) -> None
        """
    @overload
    def attribute(self, arg0: str, arg1: str) -> None:
        """attribute(*args, **kwargs)
        Overloaded function.

        1. attribute(self: OpenImageIO.OpenImageIO.ImageSpec, arg0: str, arg1: float) -> None

        2. attribute(self: OpenImageIO.OpenImageIO.ImageSpec, arg0: str, arg1: int) -> None

        3. attribute(self: OpenImageIO.OpenImageIO.ImageSpec, arg0: str, arg1: str) -> None

        4. attribute(self: OpenImageIO.OpenImageIO.ImageSpec, arg0: str, arg1: OpenImageIO.OpenImageIO.TypeDesc, arg2: object) -> None
        """
    @overload
    def attribute(self, arg0: str, arg1: TypeDesc, arg2: object) -> None:
        """attribute(*args, **kwargs)
        Overloaded function.

        1. attribute(self: OpenImageIO.OpenImageIO.ImageSpec, arg0: str, arg1: float) -> None

        2. attribute(self: OpenImageIO.OpenImageIO.ImageSpec, arg0: str, arg1: int) -> None

        3. attribute(self: OpenImageIO.OpenImageIO.ImageSpec, arg0: str, arg1: str) -> None

        4. attribute(self: OpenImageIO.OpenImageIO.ImageSpec, arg0: str, arg1: OpenImageIO.OpenImageIO.TypeDesc, arg2: object) -> None
        """
    @overload
    def channel_bytes(self) -> int:
        """channel_bytes(*args, **kwargs)
        Overloaded function.

        1. channel_bytes(self: OpenImageIO.OpenImageIO.ImageSpec) -> int

        2. channel_bytes(self: OpenImageIO.OpenImageIO.ImageSpec, channel: int, native: bool = False) -> int
        """
    @overload
    def channel_bytes(self, channel: int, native: bool = ...) -> int:
        """channel_bytes(*args, **kwargs)
        Overloaded function.

        1. channel_bytes(self: OpenImageIO.OpenImageIO.ImageSpec) -> int

        2. channel_bytes(self: OpenImageIO.OpenImageIO.ImageSpec, channel: int, native: bool = False) -> int
        """
    def channel_name(self, arg0: int) -> str:
        """channel_name(self: OpenImageIO.OpenImageIO.ImageSpec, arg0: int) -> str"""
    def channelformat(self, arg0: int) -> TypeDesc:
        """channelformat(self: OpenImageIO.OpenImageIO.ImageSpec, arg0: int) -> OpenImageIO.OpenImageIO.TypeDesc"""
    def channelindex(self, arg0: str) -> int:
        """channelindex(self: OpenImageIO.OpenImageIO.ImageSpec, arg0: str) -> int"""
    def copy(self) -> ImageSpec:
        """copy(self: OpenImageIO.OpenImageIO.ImageSpec) -> OpenImageIO.OpenImageIO.ImageSpec"""
    def copy_dimensions(self, other: ImageSpec) -> None:
        """copy_dimensions(self: OpenImageIO.OpenImageIO.ImageSpec, other: OpenImageIO.OpenImageIO.ImageSpec) -> None"""
    def default_channel_names(self) -> None:
        """default_channel_names(self: OpenImageIO.OpenImageIO.ImageSpec) -> None"""
    def erase_attribute(self, name: str = ..., type: TypeDesc = ..., casesensitive: bool = ...) -> None:
        """erase_attribute(self: OpenImageIO.OpenImageIO.ImageSpec, name: str = '', type: OpenImageIO.OpenImageIO.TypeDesc = <TypeDesc 'unknown'>, casesensitive: bool = False) -> None"""
    def from_xml(self, arg0: str) -> None:
        """from_xml(self: OpenImageIO.OpenImageIO.ImageSpec, arg0: str) -> None"""
    def get(self, key: str, default: object = ...) -> object:
        """get(self: OpenImageIO.OpenImageIO.ImageSpec, key: str, default: object = None) -> object"""
    def get_bytes_attribute(self, name: str, defaultval: str = ...) -> bytes:
        """get_bytes_attribute(self: OpenImageIO.OpenImageIO.ImageSpec, name: str, defaultval: str = '') -> bytes"""
    def get_channelformats(self) -> tuple:
        """get_channelformats(self: OpenImageIO.OpenImageIO.ImageSpec) -> tuple"""
    def get_float_attribute(self, name: str, defaultval: float = ...) -> float:
        """get_float_attribute(self: OpenImageIO.OpenImageIO.ImageSpec, name: str, defaultval: float = 0.0) -> float"""
    def get_int_attribute(self, name: str, defaultval: int = ...) -> int:
        """get_int_attribute(self: OpenImageIO.OpenImageIO.ImageSpec, name: str, defaultval: int = 0) -> int"""
    def get_string_attribute(self, name: str, defaultval: str = ...) -> str:
        """get_string_attribute(self: OpenImageIO.OpenImageIO.ImageSpec, name: str, defaultval: str = '') -> str"""
    def getattribute(self, name: str, type: TypeDesc = ...) -> object:
        """getattribute(self: OpenImageIO.OpenImageIO.ImageSpec, name: str, type: OpenImageIO.OpenImageIO.TypeDesc = <TypeDesc 'unknown'>) -> object"""
    def image_bytes(self, native: bool = ...) -> int:
        """image_bytes(self: OpenImageIO.OpenImageIO.ImageSpec, native: bool = False) -> int"""
    def image_pixels(self) -> int:
        """image_pixels(self: OpenImageIO.OpenImageIO.ImageSpec) -> int"""
    @staticmethod
    def metadata_val(param: ParamValue, human: bool = ...) -> str:
        """metadata_val(param: OpenImageIO.OpenImageIO.ParamValue, human: bool = False) -> str"""
    @overload
    def pixel_bytes(self, native: bool = ...) -> int:
        """pixel_bytes(*args, **kwargs)
        Overloaded function.

        1. pixel_bytes(self: OpenImageIO.OpenImageIO.ImageSpec, native: bool = False) -> int

        2. pixel_bytes(self: OpenImageIO.OpenImageIO.ImageSpec, chbegin: int, chend: int, native: bool = False) -> int
        """
    @overload
    def pixel_bytes(self, chbegin: int, chend: int, native: bool = ...) -> int:
        """pixel_bytes(*args, **kwargs)
        Overloaded function.

        1. pixel_bytes(self: OpenImageIO.OpenImageIO.ImageSpec, native: bool = False) -> int

        2. pixel_bytes(self: OpenImageIO.OpenImageIO.ImageSpec, chbegin: int, chend: int, native: bool = False) -> int
        """
    def scanline_bytes(self, native: bool = ...) -> int:
        """scanline_bytes(self: OpenImageIO.OpenImageIO.ImageSpec, native: bool = False) -> int"""
    def serialize(self, format: str = ..., verbose: str = ...) -> str:
        """serialize(self: OpenImageIO.OpenImageIO.ImageSpec, format: str = 'text', verbose: str = 'detailed') -> str"""
    def set_colorspace(self, name: str) -> None:
        """set_colorspace(self: OpenImageIO.OpenImageIO.ImageSpec, name: str) -> None"""
    def set_format(self, arg0: TypeDesc) -> None:
        """set_format(self: OpenImageIO.OpenImageIO.ImageSpec, arg0: OpenImageIO.OpenImageIO.TypeDesc) -> None"""
    def size_t_safe(self) -> bool:
        """size_t_safe(self: OpenImageIO.OpenImageIO.ImageSpec) -> bool"""
    def tile_bytes(self, native: bool = ...) -> int:
        """tile_bytes(self: OpenImageIO.OpenImageIO.ImageSpec, native: bool = False) -> int"""
    def tile_pixels(self) -> int:
        """tile_pixels(self: OpenImageIO.OpenImageIO.ImageSpec) -> int"""
    def to_xml(self) -> str:
        """to_xml(self: OpenImageIO.OpenImageIO.ImageSpec) -> str"""
    def valid_tile_range(self, xbegin: int, xend: int, ybegin: int, yend: int, zbegin: int, zend: int) -> bool:
        """valid_tile_range(self: OpenImageIO.OpenImageIO.ImageSpec, xbegin: int, xend: int, ybegin: int, yend: int, zbegin: int, zend: int) -> bool"""
    def __contains__(self, arg0: str) -> bool:
        """__contains__(self: OpenImageIO.OpenImageIO.ImageSpec, arg0: str) -> bool"""
    def __delitem__(self, arg0: str) -> None:
        """__delitem__(self: OpenImageIO.OpenImageIO.ImageSpec, arg0: str) -> None"""
    def __getitem__(self, arg0: str) -> object:
        """__getitem__(self: OpenImageIO.OpenImageIO.ImageSpec, arg0: str) -> object"""
    def __setitem__(self, arg0: str, arg1: object) -> None:
        """__setitem__(self: OpenImageIO.OpenImageIO.ImageSpec, arg0: str, arg1: object) -> None"""

class Interp:
    __members__: ClassVar[dict] = ...  # read-only
    CONSTANT: ClassVar[Interp] = ...
    INTERP_CONSTANT: ClassVar[Interp] = ...
    INTERP_LINEAR: ClassVar[Interp] = ...
    INTERP_PERPIECE: ClassVar[Interp] = ...
    INTERP_VERTEX: ClassVar[Interp] = ...
    LINEAR: ClassVar[Interp] = ...
    PERPIECE: ClassVar[Interp] = ...
    VERTEX: ClassVar[Interp] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, value: int) -> None:
        """__init__(self: OpenImageIO.OpenImageIO.Interp, value: int) -> None"""
    def _pybind11_conduit_v1_(self, *args, **kwargs): ...
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: OpenImageIO.OpenImageIO.Interp) -> int"""
    def __int__(self) -> int:
        """__int__(self: OpenImageIO.OpenImageIO.Interp) -> int"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class InterpMode:
    __members__: ClassVar[dict] = ...  # read-only
    Bicubic: ClassVar[InterpMode] = ...
    Bilinear: ClassVar[InterpMode] = ...
    Closest: ClassVar[InterpMode] = ...
    SmartBicubic: ClassVar[InterpMode] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, value: int) -> None:
        """__init__(self: OpenImageIO.OpenImageIO.InterpMode, value: int) -> None"""
    def _pybind11_conduit_v1_(self, *args, **kwargs): ...
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: OpenImageIO.OpenImageIO.InterpMode) -> int"""
    def __int__(self) -> int:
        """__int__(self: OpenImageIO.OpenImageIO.InterpMode) -> int"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class MakeTextureMode:
    __members__: ClassVar[dict] = ...  # read-only
    MakeTxBumpWithSlopes: ClassVar[MakeTextureMode] = ...
    MakeTxEnvLatl: ClassVar[MakeTextureMode] = ...
    MakeTxEnvLatlFromLightProbe: ClassVar[MakeTextureMode] = ...
    MakeTxShadow: ClassVar[MakeTextureMode] = ...
    MakeTxTexture: ClassVar[MakeTextureMode] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, value: int) -> None:
        """__init__(self: OpenImageIO.OpenImageIO.MakeTextureMode, value: int) -> None"""
    def _pybind11_conduit_v1_(self, *args, **kwargs): ...
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: OpenImageIO.OpenImageIO.MakeTextureMode) -> int"""
    def __int__(self) -> int:
        """__int__(self: OpenImageIO.OpenImageIO.MakeTextureMode) -> int"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class MipMode:
    __members__: ClassVar[dict] = ...  # read-only
    Aniso: ClassVar[MipMode] = ...
    Default: ClassVar[MipMode] = ...
    NoMIP: ClassVar[MipMode] = ...
    OneLevel: ClassVar[MipMode] = ...
    Trilinear: ClassVar[MipMode] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, value: int) -> None:
        """__init__(self: OpenImageIO.OpenImageIO.MipMode, value: int) -> None"""
    def _pybind11_conduit_v1_(self, *args, **kwargs): ...
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: OpenImageIO.OpenImageIO.MipMode) -> int"""
    def __int__(self) -> int:
        """__int__(self: OpenImageIO.OpenImageIO.MipMode) -> int"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class NonFiniteFixMode:
    __members__: ClassVar[dict] = ...  # read-only
    NONFINITE_BLACK: ClassVar[NonFiniteFixMode] = ...
    NONFINITE_BOX3: ClassVar[NonFiniteFixMode] = ...
    NONFINITE_NONE: ClassVar[NonFiniteFixMode] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, value: int) -> None:
        """__init__(self: OpenImageIO.OpenImageIO.NonFiniteFixMode, value: int) -> None"""
    def _pybind11_conduit_v1_(self, *args, **kwargs): ...
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: OpenImageIO.OpenImageIO.NonFiniteFixMode) -> int"""
    def __int__(self) -> int:
        """__int__(self: OpenImageIO.OpenImageIO.NonFiniteFixMode) -> int"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class ParamValue:
    @overload
    def __init__(self, arg0: str, arg1: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: OpenImageIO.OpenImageIO.ParamValue, arg0: str, arg1: int) -> None

        2. __init__(self: OpenImageIO.OpenImageIO.ParamValue, arg0: str, arg1: float) -> None

        3. __init__(self: OpenImageIO.OpenImageIO.ParamValue, arg0: str, arg1: str) -> None

        4. __init__(self: OpenImageIO.OpenImageIO.ParamValue, name: str, type: OpenImageIO.OpenImageIO.TypeDesc, value: object) -> None

        5. __init__(self: OpenImageIO.OpenImageIO.ParamValue, name: str, type: OpenImageIO.OpenImageIO.TypeDesc, nvalues: int, interp: OpenImageIO.OpenImageIO.Interp, value: object) -> None
        """
    @overload
    def __init__(self, arg0: str, arg1: float) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: OpenImageIO.OpenImageIO.ParamValue, arg0: str, arg1: int) -> None

        2. __init__(self: OpenImageIO.OpenImageIO.ParamValue, arg0: str, arg1: float) -> None

        3. __init__(self: OpenImageIO.OpenImageIO.ParamValue, arg0: str, arg1: str) -> None

        4. __init__(self: OpenImageIO.OpenImageIO.ParamValue, name: str, type: OpenImageIO.OpenImageIO.TypeDesc, value: object) -> None

        5. __init__(self: OpenImageIO.OpenImageIO.ParamValue, name: str, type: OpenImageIO.OpenImageIO.TypeDesc, nvalues: int, interp: OpenImageIO.OpenImageIO.Interp, value: object) -> None
        """
    @overload
    def __init__(self, arg0: str, arg1: str) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: OpenImageIO.OpenImageIO.ParamValue, arg0: str, arg1: int) -> None

        2. __init__(self: OpenImageIO.OpenImageIO.ParamValue, arg0: str, arg1: float) -> None

        3. __init__(self: OpenImageIO.OpenImageIO.ParamValue, arg0: str, arg1: str) -> None

        4. __init__(self: OpenImageIO.OpenImageIO.ParamValue, name: str, type: OpenImageIO.OpenImageIO.TypeDesc, value: object) -> None

        5. __init__(self: OpenImageIO.OpenImageIO.ParamValue, name: str, type: OpenImageIO.OpenImageIO.TypeDesc, nvalues: int, interp: OpenImageIO.OpenImageIO.Interp, value: object) -> None
        """
    @overload
    def __init__(self, name: str, type: TypeDesc, value: object) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: OpenImageIO.OpenImageIO.ParamValue, arg0: str, arg1: int) -> None

        2. __init__(self: OpenImageIO.OpenImageIO.ParamValue, arg0: str, arg1: float) -> None

        3. __init__(self: OpenImageIO.OpenImageIO.ParamValue, arg0: str, arg1: str) -> None

        4. __init__(self: OpenImageIO.OpenImageIO.ParamValue, name: str, type: OpenImageIO.OpenImageIO.TypeDesc, value: object) -> None

        5. __init__(self: OpenImageIO.OpenImageIO.ParamValue, name: str, type: OpenImageIO.OpenImageIO.TypeDesc, nvalues: int, interp: OpenImageIO.OpenImageIO.Interp, value: object) -> None
        """
    @overload
    def __init__(self, name: str, type: TypeDesc, nvalues: int, interp: Interp, value: object) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: OpenImageIO.OpenImageIO.ParamValue, arg0: str, arg1: int) -> None

        2. __init__(self: OpenImageIO.OpenImageIO.ParamValue, arg0: str, arg1: float) -> None

        3. __init__(self: OpenImageIO.OpenImageIO.ParamValue, arg0: str, arg1: str) -> None

        4. __init__(self: OpenImageIO.OpenImageIO.ParamValue, name: str, type: OpenImageIO.OpenImageIO.TypeDesc, value: object) -> None

        5. __init__(self: OpenImageIO.OpenImageIO.ParamValue, name: str, type: OpenImageIO.OpenImageIO.TypeDesc, nvalues: int, interp: OpenImageIO.OpenImageIO.Interp, value: object) -> None
        """
    def _pybind11_conduit_v1_(self, *args, **kwargs): ...
    @property
    def name(self) -> str: ...
    @property
    def type(self) -> TypeDesc: ...
    @property
    def value(self) -> object: ...
    @property
    def __len__(self) -> int: ...

class ParamValueList:
    def __init__(self) -> None:
        """__init__(self: OpenImageIO.OpenImageIO.ParamValueList) -> None"""
    def _pybind11_conduit_v1_(self, *args, **kwargs): ...
    def add_or_replace(self, value: ParamValue, casesensitive: bool = ...) -> None:
        """add_or_replace(self: OpenImageIO.OpenImageIO.ParamValueList, value: OpenImageIO.OpenImageIO.ParamValue, casesensitive: bool = True) -> None"""
    def append(self, arg0: ParamValue) -> None:
        """append(self: OpenImageIO.OpenImageIO.ParamValueList, arg0: OpenImageIO.OpenImageIO.ParamValue) -> None"""
    @overload
    def attribute(self, arg0: str, arg1: float) -> None:
        """attribute(*args, **kwargs)
        Overloaded function.

        1. attribute(self: OpenImageIO.OpenImageIO.ParamValueList, arg0: str, arg1: float) -> None

        2. attribute(self: OpenImageIO.OpenImageIO.ParamValueList, arg0: str, arg1: int) -> None

        3. attribute(self: OpenImageIO.OpenImageIO.ParamValueList, arg0: str, arg1: str) -> None

        4. attribute(self: OpenImageIO.OpenImageIO.ParamValueList, arg0: str, arg1: OpenImageIO.OpenImageIO.TypeDesc, arg2: object) -> None

        5. attribute(self: OpenImageIO.OpenImageIO.ParamValueList, arg0: str, arg1: OpenImageIO.OpenImageIO.TypeDesc, arg2: int, arg3: object) -> None
        """
    @overload
    def attribute(self, arg0: str, arg1: int) -> None:
        """attribute(*args, **kwargs)
        Overloaded function.

        1. attribute(self: OpenImageIO.OpenImageIO.ParamValueList, arg0: str, arg1: float) -> None

        2. attribute(self: OpenImageIO.OpenImageIO.ParamValueList, arg0: str, arg1: int) -> None

        3. attribute(self: OpenImageIO.OpenImageIO.ParamValueList, arg0: str, arg1: str) -> None

        4. attribute(self: OpenImageIO.OpenImageIO.ParamValueList, arg0: str, arg1: OpenImageIO.OpenImageIO.TypeDesc, arg2: object) -> None

        5. attribute(self: OpenImageIO.OpenImageIO.ParamValueList, arg0: str, arg1: OpenImageIO.OpenImageIO.TypeDesc, arg2: int, arg3: object) -> None
        """
    @overload
    def attribute(self, arg0: str, arg1: str) -> None:
        """attribute(*args, **kwargs)
        Overloaded function.

        1. attribute(self: OpenImageIO.OpenImageIO.ParamValueList, arg0: str, arg1: float) -> None

        2. attribute(self: OpenImageIO.OpenImageIO.ParamValueList, arg0: str, arg1: int) -> None

        3. attribute(self: OpenImageIO.OpenImageIO.ParamValueList, arg0: str, arg1: str) -> None

        4. attribute(self: OpenImageIO.OpenImageIO.ParamValueList, arg0: str, arg1: OpenImageIO.OpenImageIO.TypeDesc, arg2: object) -> None

        5. attribute(self: OpenImageIO.OpenImageIO.ParamValueList, arg0: str, arg1: OpenImageIO.OpenImageIO.TypeDesc, arg2: int, arg3: object) -> None
        """
    @overload
    def attribute(self, arg0: str, arg1: TypeDesc, arg2: object) -> None:
        """attribute(*args, **kwargs)
        Overloaded function.

        1. attribute(self: OpenImageIO.OpenImageIO.ParamValueList, arg0: str, arg1: float) -> None

        2. attribute(self: OpenImageIO.OpenImageIO.ParamValueList, arg0: str, arg1: int) -> None

        3. attribute(self: OpenImageIO.OpenImageIO.ParamValueList, arg0: str, arg1: str) -> None

        4. attribute(self: OpenImageIO.OpenImageIO.ParamValueList, arg0: str, arg1: OpenImageIO.OpenImageIO.TypeDesc, arg2: object) -> None

        5. attribute(self: OpenImageIO.OpenImageIO.ParamValueList, arg0: str, arg1: OpenImageIO.OpenImageIO.TypeDesc, arg2: int, arg3: object) -> None
        """
    @overload
    def attribute(self, arg0: str, arg1: TypeDesc, arg2: int, arg3: object) -> None:
        """attribute(*args, **kwargs)
        Overloaded function.

        1. attribute(self: OpenImageIO.OpenImageIO.ParamValueList, arg0: str, arg1: float) -> None

        2. attribute(self: OpenImageIO.OpenImageIO.ParamValueList, arg0: str, arg1: int) -> None

        3. attribute(self: OpenImageIO.OpenImageIO.ParamValueList, arg0: str, arg1: str) -> None

        4. attribute(self: OpenImageIO.OpenImageIO.ParamValueList, arg0: str, arg1: OpenImageIO.OpenImageIO.TypeDesc, arg2: object) -> None

        5. attribute(self: OpenImageIO.OpenImageIO.ParamValueList, arg0: str, arg1: OpenImageIO.OpenImageIO.TypeDesc, arg2: int, arg3: object) -> None
        """
    def clear(self) -> None:
        """clear(self: OpenImageIO.OpenImageIO.ParamValueList) -> None"""
    def contains(self, name: str, type: TypeDesc = ..., casesensitive: bool = ...) -> bool:
        """contains(self: OpenImageIO.OpenImageIO.ParamValueList, name: str, type: OpenImageIO.OpenImageIO.TypeDesc = <TypeDesc 'unknown'>, casesensitive: bool = True) -> bool"""
    def free(self) -> None:
        """free(self: OpenImageIO.OpenImageIO.ParamValueList) -> None"""
    def merge(self, other: ParamValueList, override: bool = ...) -> None:
        """merge(self: OpenImageIO.OpenImageIO.ParamValueList, other: OpenImageIO.OpenImageIO.ParamValueList, override: bool = False) -> None"""
    def remove(self, name: str, type: TypeDesc = ..., casesensitive: bool = ...) -> None:
        """remove(self: OpenImageIO.OpenImageIO.ParamValueList, name: str, type: OpenImageIO.OpenImageIO.TypeDesc = <TypeDesc 'unknown'>, casesensitive: bool = True) -> None"""
    def resize(self, arg0: int) -> None:
        """resize(self: OpenImageIO.OpenImageIO.ParamValueList, arg0: int) -> None"""
    def sort(self, casesensitive: bool = ...) -> None:
        """sort(self: OpenImageIO.OpenImageIO.ParamValueList, casesensitive: bool = True) -> None"""
    def __contains__(self, arg0: str) -> bool:
        """__contains__(self: OpenImageIO.OpenImageIO.ParamValueList, arg0: str) -> bool"""
    def __delitem__(self, arg0: str) -> None:
        """__delitem__(self: OpenImageIO.OpenImageIO.ParamValueList, arg0: str) -> None"""
    @overload
    def __getitem__(self, arg0: int) -> ParamValue:
        """__getitem__(*args, **kwargs)
        Overloaded function.

        1. __getitem__(self: OpenImageIO.OpenImageIO.ParamValueList, arg0: int) -> OpenImageIO.OpenImageIO.ParamValue

        2. __getitem__(self: OpenImageIO.OpenImageIO.ParamValueList, arg0: str) -> object
        """
    @overload
    def __getitem__(self, arg0: str) -> object:
        """__getitem__(*args, **kwargs)
        Overloaded function.

        1. __getitem__(self: OpenImageIO.OpenImageIO.ParamValueList, arg0: int) -> OpenImageIO.OpenImageIO.ParamValue

        2. __getitem__(self: OpenImageIO.OpenImageIO.ParamValueList, arg0: str) -> object
        """
    def __iter__(self) -> Iterator[ParamValue]:
        """__iter__(self: OpenImageIO.OpenImageIO.ParamValueList) -> Iterator[OpenImageIO.OpenImageIO.ParamValue]"""
    def __len__(self) -> int:
        """__len__(self: OpenImageIO.OpenImageIO.ParamValueList) -> int"""
    def __setitem__(self, arg0: str, arg1: object) -> None:
        """__setitem__(self: OpenImageIO.OpenImageIO.ParamValueList, arg0: str, arg1: object) -> None"""

class PixelStats:
    def __init__(self) -> None:
        """__init__(self: OpenImageIO.OpenImageIO.PixelStats) -> None"""
    def _pybind11_conduit_v1_(self, *args, **kwargs): ...
    @property
    def avg(self) -> list[float]: ...
    @property
    def finitecount(self) -> list[int]: ...
    @property
    def infcount(self) -> list[int]: ...
    @property
    def max(self) -> list[float]: ...
    @property
    def min(self) -> list[float]: ...
    @property
    def nancount(self) -> list[int]: ...
    @property
    def stddev(self) -> list[float]: ...
    @property
    def sum(self) -> list[float]: ...
    @property
    def sum2(self) -> list[float]: ...

class ROI:
    All: ClassVar[ROI] = ...  # read-only
    chbegin: int
    chend: int
    xbegin: int
    xend: int
    ybegin: int
    yend: int
    zbegin: int
    zend: int
    @overload
    def __init__(self) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: OpenImageIO.OpenImageIO.ROI) -> None

        2. __init__(self: OpenImageIO.OpenImageIO.ROI, arg0: int, arg1: int, arg2: int, arg3: int) -> None

        3. __init__(self: OpenImageIO.OpenImageIO.ROI, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> None

        4. __init__(self: OpenImageIO.OpenImageIO.ROI, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> None

        5. __init__(self: OpenImageIO.OpenImageIO.ROI, arg0: OpenImageIO.OpenImageIO.ROI) -> None
        """
    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: OpenImageIO.OpenImageIO.ROI) -> None

        2. __init__(self: OpenImageIO.OpenImageIO.ROI, arg0: int, arg1: int, arg2: int, arg3: int) -> None

        3. __init__(self: OpenImageIO.OpenImageIO.ROI, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> None

        4. __init__(self: OpenImageIO.OpenImageIO.ROI, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> None

        5. __init__(self: OpenImageIO.OpenImageIO.ROI, arg0: OpenImageIO.OpenImageIO.ROI) -> None
        """
    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: OpenImageIO.OpenImageIO.ROI) -> None

        2. __init__(self: OpenImageIO.OpenImageIO.ROI, arg0: int, arg1: int, arg2: int, arg3: int) -> None

        3. __init__(self: OpenImageIO.OpenImageIO.ROI, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> None

        4. __init__(self: OpenImageIO.OpenImageIO.ROI, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> None

        5. __init__(self: OpenImageIO.OpenImageIO.ROI, arg0: OpenImageIO.OpenImageIO.ROI) -> None
        """
    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: OpenImageIO.OpenImageIO.ROI) -> None

        2. __init__(self: OpenImageIO.OpenImageIO.ROI, arg0: int, arg1: int, arg2: int, arg3: int) -> None

        3. __init__(self: OpenImageIO.OpenImageIO.ROI, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> None

        4. __init__(self: OpenImageIO.OpenImageIO.ROI, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> None

        5. __init__(self: OpenImageIO.OpenImageIO.ROI, arg0: OpenImageIO.OpenImageIO.ROI) -> None
        """
    @overload
    def __init__(self, arg0: ROI) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: OpenImageIO.OpenImageIO.ROI) -> None

        2. __init__(self: OpenImageIO.OpenImageIO.ROI, arg0: int, arg1: int, arg2: int, arg3: int) -> None

        3. __init__(self: OpenImageIO.OpenImageIO.ROI, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> None

        4. __init__(self: OpenImageIO.OpenImageIO.ROI, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> None

        5. __init__(self: OpenImageIO.OpenImageIO.ROI, arg0: OpenImageIO.OpenImageIO.ROI) -> None
        """
    def _pybind11_conduit_v1_(self, *args, **kwargs): ...
    @overload
    def contains(self, x: int, y: int, z: int = ..., ch: int = ...) -> bool:
        """contains(*args, **kwargs)
        Overloaded function.

        1. contains(self: OpenImageIO.OpenImageIO.ROI, x: int, y: int, z: int = 0, ch: int = 0) -> bool

        2. contains(self: OpenImageIO.OpenImageIO.ROI, other: OpenImageIO.OpenImageIO.ROI) -> bool
        """
    @overload
    def contains(self, other: ROI) -> bool:
        """contains(*args, **kwargs)
        Overloaded function.

        1. contains(self: OpenImageIO.OpenImageIO.ROI, x: int, y: int, z: int = 0, ch: int = 0) -> bool

        2. contains(self: OpenImageIO.OpenImageIO.ROI, other: OpenImageIO.OpenImageIO.ROI) -> bool
        """
    def copy(self) -> ROI:
        """copy(self: OpenImageIO.OpenImageIO.ROI) -> OpenImageIO.OpenImageIO.ROI"""
    def __eq__(self, arg0: ROI) -> bool:
        """__eq__(self: OpenImageIO.OpenImageIO.ROI, arg0: OpenImageIO.OpenImageIO.ROI) -> bool"""
    def __ne__(self, arg0: ROI) -> bool:
        """__ne__(self: OpenImageIO.OpenImageIO.ROI, arg0: OpenImageIO.OpenImageIO.ROI) -> bool"""
    @property
    def defined(self) -> bool: ...
    @property
    def depth(self) -> int: ...
    @property
    def height(self) -> int: ...
    @property
    def nchannels(self) -> int: ...
    @property
    def npixels(self) -> int: ...
    @property
    def width(self) -> int: ...

class TextureOpt:
    anisotropic: int
    conservative_filter: bool
    fill: float
    firstchannel: int
    interpmode: InterpMode
    mipmode: MipMode
    missingcolor: tuple
    rnd: float
    rwidth: float
    rwrap: Wrap
    sblur: float
    subimage: int
    subimagename: str
    swidth: float
    swrap: Wrap
    tblur: float
    twidth: float
    twrap: Wrap
    def __init__(self) -> None:
        """__init__(self: OpenImageIO.OpenImageIO.TextureOpt) -> None"""
    def _pybind11_conduit_v1_(self, *args, **kwargs): ...

class TextureSystem:
    def __init__(self, shared: bool = ...) -> None:
        """__init__(self: OpenImageIO.OpenImageIO.TextureSystem, shared: bool = True) -> None"""
    def _pybind11_conduit_v1_(self, *args, **kwargs): ...
    @overload
    def attribute(self, arg0: str, arg1: float) -> None:
        """attribute(*args, **kwargs)
        Overloaded function.

        1. attribute(self: OpenImageIO.OpenImageIO.TextureSystem, arg0: str, arg1: float) -> None

        2. attribute(self: OpenImageIO.OpenImageIO.TextureSystem, arg0: str, arg1: int) -> None

        3. attribute(self: OpenImageIO.OpenImageIO.TextureSystem, arg0: str, arg1: str) -> None

        4. attribute(self: OpenImageIO.OpenImageIO.TextureSystem, arg0: str, arg1: OpenImageIO.OpenImageIO.TypeDesc, arg2: object) -> None
        """
    @overload
    def attribute(self, arg0: str, arg1: int) -> None:
        """attribute(*args, **kwargs)
        Overloaded function.

        1. attribute(self: OpenImageIO.OpenImageIO.TextureSystem, arg0: str, arg1: float) -> None

        2. attribute(self: OpenImageIO.OpenImageIO.TextureSystem, arg0: str, arg1: int) -> None

        3. attribute(self: OpenImageIO.OpenImageIO.TextureSystem, arg0: str, arg1: str) -> None

        4. attribute(self: OpenImageIO.OpenImageIO.TextureSystem, arg0: str, arg1: OpenImageIO.OpenImageIO.TypeDesc, arg2: object) -> None
        """
    @overload
    def attribute(self, arg0: str, arg1: str) -> None:
        """attribute(*args, **kwargs)
        Overloaded function.

        1. attribute(self: OpenImageIO.OpenImageIO.TextureSystem, arg0: str, arg1: float) -> None

        2. attribute(self: OpenImageIO.OpenImageIO.TextureSystem, arg0: str, arg1: int) -> None

        3. attribute(self: OpenImageIO.OpenImageIO.TextureSystem, arg0: str, arg1: str) -> None

        4. attribute(self: OpenImageIO.OpenImageIO.TextureSystem, arg0: str, arg1: OpenImageIO.OpenImageIO.TypeDesc, arg2: object) -> None
        """
    @overload
    def attribute(self, arg0: str, arg1: TypeDesc, arg2: object) -> None:
        """attribute(*args, **kwargs)
        Overloaded function.

        1. attribute(self: OpenImageIO.OpenImageIO.TextureSystem, arg0: str, arg1: float) -> None

        2. attribute(self: OpenImageIO.OpenImageIO.TextureSystem, arg0: str, arg1: int) -> None

        3. attribute(self: OpenImageIO.OpenImageIO.TextureSystem, arg0: str, arg1: str) -> None

        4. attribute(self: OpenImageIO.OpenImageIO.TextureSystem, arg0: str, arg1: OpenImageIO.OpenImageIO.TypeDesc, arg2: object) -> None
        """
    def close(self, filename: str) -> None:
        """close(self: OpenImageIO.OpenImageIO.TextureSystem, filename: str) -> None"""
    def close_all(self) -> None:
        """close_all(self: OpenImageIO.OpenImageIO.TextureSystem) -> None"""
    @staticmethod
    def destroy(arg0: TextureSystem) -> None:
        """destroy(arg0: OpenImageIO.OpenImageIO.TextureSystem) -> None"""
    def environment(self, filename: str, options: TextureOpt, R, dRdx, dRdy, nchannels: int) -> tuple:
        """environment(self: OpenImageIO.OpenImageIO.TextureSystem, filename: str, options: OpenImageIO.OpenImageIO.TextureOpt, R: Annotated[list[float], FixedSize(3)], dRdx: Annotated[list[float], FixedSize(3)], dRdy: Annotated[list[float], FixedSize(3)], nchannels: int) -> tuple"""
    def getattribute(self, name: str, type: TypeDesc = ...) -> object:
        """getattribute(self: OpenImageIO.OpenImageIO.TextureSystem, name: str, type: OpenImageIO.OpenImageIO.TypeDesc = <TypeDesc 'unknown'>) -> object"""
    def getattributetype(self, name: str) -> TypeDesc:
        """getattributetype(self: OpenImageIO.OpenImageIO.TextureSystem, name: str) -> OpenImageIO.OpenImageIO.TypeDesc"""
    def geterror(self, clear: bool = ...) -> str:
        """geterror(self: OpenImageIO.OpenImageIO.TextureSystem, clear: bool = True) -> str"""
    def getstats(self, level: int = ..., icstats: bool = ...) -> str:
        """getstats(self: OpenImageIO.OpenImageIO.TextureSystem, level: int = 1, icstats: bool = True) -> str"""
    def has_error(self) -> bool:
        """has_error(self: OpenImageIO.OpenImageIO.TextureSystem) -> bool"""
    def imagespec(self, filename: str, subimage: int = ...) -> object:
        """imagespec(self: OpenImageIO.OpenImageIO.TextureSystem, filename: str, subimage: int = 0) -> object"""
    def invalidate(self, filename: str, force: bool = ...) -> None:
        """invalidate(self: OpenImageIO.OpenImageIO.TextureSystem, filename: str, force: bool = True) -> None"""
    def invalidate_all(self, force: bool = ...) -> None:
        """invalidate_all(self: OpenImageIO.OpenImageIO.TextureSystem, force: bool = True) -> None"""
    def inventory_udim(self, filename: str) -> tuple:
        """inventory_udim(self: OpenImageIO.OpenImageIO.TextureSystem, filename: str) -> tuple"""
    def is_udim(self, filename: str) -> bool:
        """is_udim(self: OpenImageIO.OpenImageIO.TextureSystem, filename: str) -> bool"""
    def reset_stats(self) -> None:
        """reset_stats(self: OpenImageIO.OpenImageIO.TextureSystem) -> None"""
    def resolve_filename(self, filename: str) -> str:
        """resolve_filename(self: OpenImageIO.OpenImageIO.TextureSystem, filename: str) -> str"""
    def resolve_udim(self, filename: str, s: float, t: float) -> str:
        """resolve_udim(self: OpenImageIO.OpenImageIO.TextureSystem, filename: str, s: float, t: float) -> str"""
    def texture(self, filename: str, options: TextureOpt, s: float, t: float, dsdx: float, dtdx: float, dsdy: float, dtdy: float, nchannels: int) -> tuple:
        """texture(self: OpenImageIO.OpenImageIO.TextureSystem, filename: str, options: OpenImageIO.OpenImageIO.TextureOpt, s: float, t: float, dsdx: float, dtdx: float, dsdy: float, dtdy: float, nchannels: int) -> tuple"""
    def texture3d(self, filename: str, options: TextureOpt, P, dPdx, dPdy, dPdz, nchannels: int) -> tuple:
        """texture3d(self: OpenImageIO.OpenImageIO.TextureSystem, filename: str, options: OpenImageIO.OpenImageIO.TextureOpt, P: Annotated[list[float], FixedSize(3)], dPdx: Annotated[list[float], FixedSize(3)], dPdy: Annotated[list[float], FixedSize(3)], dPdz: Annotated[list[float], FixedSize(3)], nchannels: int) -> tuple"""

class TypeDesc:
    aggregate: AGGREGATE
    arraylen: int
    basetype: BASETYPE
    vecsemantics: VECSEMANTICS
    @overload
    def __init__(self) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: OpenImageIO.OpenImageIO.TypeDesc) -> None

        2. __init__(self: OpenImageIO.OpenImageIO.TypeDesc, arg0: OpenImageIO.OpenImageIO.TypeDesc) -> None

        3. __init__(self: OpenImageIO.OpenImageIO.TypeDesc, arg0: OpenImageIO.OpenImageIO.BASETYPE) -> None

        4. __init__(self: OpenImageIO.OpenImageIO.TypeDesc, arg0: OpenImageIO.OpenImageIO.BASETYPE, arg1: OpenImageIO.OpenImageIO.AGGREGATE) -> None

        5. __init__(self: OpenImageIO.OpenImageIO.TypeDesc, arg0: OpenImageIO.OpenImageIO.BASETYPE, arg1: OpenImageIO.OpenImageIO.AGGREGATE, arg2: OpenImageIO.OpenImageIO.VECSEMANTICS) -> None

        6. __init__(self: OpenImageIO.OpenImageIO.TypeDesc, arg0: OpenImageIO.OpenImageIO.BASETYPE, arg1: OpenImageIO.OpenImageIO.AGGREGATE, arg2: OpenImageIO.OpenImageIO.VECSEMANTICS, arg3: int) -> None

        7. __init__(self: OpenImageIO.OpenImageIO.TypeDesc, arg0: str) -> None
        """
    @overload
    def __init__(self, arg0: TypeDesc) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: OpenImageIO.OpenImageIO.TypeDesc) -> None

        2. __init__(self: OpenImageIO.OpenImageIO.TypeDesc, arg0: OpenImageIO.OpenImageIO.TypeDesc) -> None

        3. __init__(self: OpenImageIO.OpenImageIO.TypeDesc, arg0: OpenImageIO.OpenImageIO.BASETYPE) -> None

        4. __init__(self: OpenImageIO.OpenImageIO.TypeDesc, arg0: OpenImageIO.OpenImageIO.BASETYPE, arg1: OpenImageIO.OpenImageIO.AGGREGATE) -> None

        5. __init__(self: OpenImageIO.OpenImageIO.TypeDesc, arg0: OpenImageIO.OpenImageIO.BASETYPE, arg1: OpenImageIO.OpenImageIO.AGGREGATE, arg2: OpenImageIO.OpenImageIO.VECSEMANTICS) -> None

        6. __init__(self: OpenImageIO.OpenImageIO.TypeDesc, arg0: OpenImageIO.OpenImageIO.BASETYPE, arg1: OpenImageIO.OpenImageIO.AGGREGATE, arg2: OpenImageIO.OpenImageIO.VECSEMANTICS, arg3: int) -> None

        7. __init__(self: OpenImageIO.OpenImageIO.TypeDesc, arg0: str) -> None
        """
    @overload
    def __init__(self, arg0: BASETYPE) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: OpenImageIO.OpenImageIO.TypeDesc) -> None

        2. __init__(self: OpenImageIO.OpenImageIO.TypeDesc, arg0: OpenImageIO.OpenImageIO.TypeDesc) -> None

        3. __init__(self: OpenImageIO.OpenImageIO.TypeDesc, arg0: OpenImageIO.OpenImageIO.BASETYPE) -> None

        4. __init__(self: OpenImageIO.OpenImageIO.TypeDesc, arg0: OpenImageIO.OpenImageIO.BASETYPE, arg1: OpenImageIO.OpenImageIO.AGGREGATE) -> None

        5. __init__(self: OpenImageIO.OpenImageIO.TypeDesc, arg0: OpenImageIO.OpenImageIO.BASETYPE, arg1: OpenImageIO.OpenImageIO.AGGREGATE, arg2: OpenImageIO.OpenImageIO.VECSEMANTICS) -> None

        6. __init__(self: OpenImageIO.OpenImageIO.TypeDesc, arg0: OpenImageIO.OpenImageIO.BASETYPE, arg1: OpenImageIO.OpenImageIO.AGGREGATE, arg2: OpenImageIO.OpenImageIO.VECSEMANTICS, arg3: int) -> None

        7. __init__(self: OpenImageIO.OpenImageIO.TypeDesc, arg0: str) -> None
        """
    @overload
    def __init__(self, arg0: BASETYPE, arg1: AGGREGATE) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: OpenImageIO.OpenImageIO.TypeDesc) -> None

        2. __init__(self: OpenImageIO.OpenImageIO.TypeDesc, arg0: OpenImageIO.OpenImageIO.TypeDesc) -> None

        3. __init__(self: OpenImageIO.OpenImageIO.TypeDesc, arg0: OpenImageIO.OpenImageIO.BASETYPE) -> None

        4. __init__(self: OpenImageIO.OpenImageIO.TypeDesc, arg0: OpenImageIO.OpenImageIO.BASETYPE, arg1: OpenImageIO.OpenImageIO.AGGREGATE) -> None

        5. __init__(self: OpenImageIO.OpenImageIO.TypeDesc, arg0: OpenImageIO.OpenImageIO.BASETYPE, arg1: OpenImageIO.OpenImageIO.AGGREGATE, arg2: OpenImageIO.OpenImageIO.VECSEMANTICS) -> None

        6. __init__(self: OpenImageIO.OpenImageIO.TypeDesc, arg0: OpenImageIO.OpenImageIO.BASETYPE, arg1: OpenImageIO.OpenImageIO.AGGREGATE, arg2: OpenImageIO.OpenImageIO.VECSEMANTICS, arg3: int) -> None

        7. __init__(self: OpenImageIO.OpenImageIO.TypeDesc, arg0: str) -> None
        """
    @overload
    def __init__(self, arg0: BASETYPE, arg1: AGGREGATE, arg2: VECSEMANTICS) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: OpenImageIO.OpenImageIO.TypeDesc) -> None

        2. __init__(self: OpenImageIO.OpenImageIO.TypeDesc, arg0: OpenImageIO.OpenImageIO.TypeDesc) -> None

        3. __init__(self: OpenImageIO.OpenImageIO.TypeDesc, arg0: OpenImageIO.OpenImageIO.BASETYPE) -> None

        4. __init__(self: OpenImageIO.OpenImageIO.TypeDesc, arg0: OpenImageIO.OpenImageIO.BASETYPE, arg1: OpenImageIO.OpenImageIO.AGGREGATE) -> None

        5. __init__(self: OpenImageIO.OpenImageIO.TypeDesc, arg0: OpenImageIO.OpenImageIO.BASETYPE, arg1: OpenImageIO.OpenImageIO.AGGREGATE, arg2: OpenImageIO.OpenImageIO.VECSEMANTICS) -> None

        6. __init__(self: OpenImageIO.OpenImageIO.TypeDesc, arg0: OpenImageIO.OpenImageIO.BASETYPE, arg1: OpenImageIO.OpenImageIO.AGGREGATE, arg2: OpenImageIO.OpenImageIO.VECSEMANTICS, arg3: int) -> None

        7. __init__(self: OpenImageIO.OpenImageIO.TypeDesc, arg0: str) -> None
        """
    @overload
    def __init__(self, arg0: BASETYPE, arg1: AGGREGATE, arg2: VECSEMANTICS, arg3: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: OpenImageIO.OpenImageIO.TypeDesc) -> None

        2. __init__(self: OpenImageIO.OpenImageIO.TypeDesc, arg0: OpenImageIO.OpenImageIO.TypeDesc) -> None

        3. __init__(self: OpenImageIO.OpenImageIO.TypeDesc, arg0: OpenImageIO.OpenImageIO.BASETYPE) -> None

        4. __init__(self: OpenImageIO.OpenImageIO.TypeDesc, arg0: OpenImageIO.OpenImageIO.BASETYPE, arg1: OpenImageIO.OpenImageIO.AGGREGATE) -> None

        5. __init__(self: OpenImageIO.OpenImageIO.TypeDesc, arg0: OpenImageIO.OpenImageIO.BASETYPE, arg1: OpenImageIO.OpenImageIO.AGGREGATE, arg2: OpenImageIO.OpenImageIO.VECSEMANTICS) -> None

        6. __init__(self: OpenImageIO.OpenImageIO.TypeDesc, arg0: OpenImageIO.OpenImageIO.BASETYPE, arg1: OpenImageIO.OpenImageIO.AGGREGATE, arg2: OpenImageIO.OpenImageIO.VECSEMANTICS, arg3: int) -> None

        7. __init__(self: OpenImageIO.OpenImageIO.TypeDesc, arg0: str) -> None
        """
    @overload
    def __init__(self, arg0: str) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: OpenImageIO.OpenImageIO.TypeDesc) -> None

        2. __init__(self: OpenImageIO.OpenImageIO.TypeDesc, arg0: OpenImageIO.OpenImageIO.TypeDesc) -> None

        3. __init__(self: OpenImageIO.OpenImageIO.TypeDesc, arg0: OpenImageIO.OpenImageIO.BASETYPE) -> None

        4. __init__(self: OpenImageIO.OpenImageIO.TypeDesc, arg0: OpenImageIO.OpenImageIO.BASETYPE, arg1: OpenImageIO.OpenImageIO.AGGREGATE) -> None

        5. __init__(self: OpenImageIO.OpenImageIO.TypeDesc, arg0: OpenImageIO.OpenImageIO.BASETYPE, arg1: OpenImageIO.OpenImageIO.AGGREGATE, arg2: OpenImageIO.OpenImageIO.VECSEMANTICS) -> None

        6. __init__(self: OpenImageIO.OpenImageIO.TypeDesc, arg0: OpenImageIO.OpenImageIO.BASETYPE, arg1: OpenImageIO.OpenImageIO.AGGREGATE, arg2: OpenImageIO.OpenImageIO.VECSEMANTICS, arg3: int) -> None

        7. __init__(self: OpenImageIO.OpenImageIO.TypeDesc, arg0: str) -> None
        """
    def _pybind11_conduit_v1_(self, *args, **kwargs): ...
    def basesize(self) -> int:
        """basesize(self: OpenImageIO.OpenImageIO.TypeDesc) -> int"""
    def basevalues(self) -> int:
        """basevalues(self: OpenImageIO.OpenImageIO.TypeDesc) -> int"""
    def c_str(self) -> str:
        """c_str(self: OpenImageIO.OpenImageIO.TypeDesc) -> str"""
    def elementsize(self) -> int:
        """elementsize(self: OpenImageIO.OpenImageIO.TypeDesc) -> int"""
    def elementtype(self) -> TypeDesc:
        """elementtype(self: OpenImageIO.OpenImageIO.TypeDesc) -> OpenImageIO.OpenImageIO.TypeDesc"""
    def equivalent(self, arg0: TypeDesc) -> bool:
        """equivalent(self: OpenImageIO.OpenImageIO.TypeDesc, arg0: OpenImageIO.OpenImageIO.TypeDesc) -> bool"""
    def fromstring(self, arg0: str) -> None:
        """fromstring(self: OpenImageIO.OpenImageIO.TypeDesc, arg0: str) -> None"""
    def is_box2(self, arg0: BASETYPE) -> bool:
        """is_box2(self: OpenImageIO.OpenImageIO.TypeDesc, arg0: OpenImageIO.OpenImageIO.BASETYPE) -> bool"""
    def is_box3(self, arg0: BASETYPE) -> bool:
        """is_box3(self: OpenImageIO.OpenImageIO.TypeDesc, arg0: OpenImageIO.OpenImageIO.BASETYPE) -> bool"""
    def is_vec2(self, arg0: BASETYPE) -> bool:
        """is_vec2(self: OpenImageIO.OpenImageIO.TypeDesc, arg0: OpenImageIO.OpenImageIO.BASETYPE) -> bool"""
    def is_vec3(self, arg0: BASETYPE) -> bool:
        """is_vec3(self: OpenImageIO.OpenImageIO.TypeDesc, arg0: OpenImageIO.OpenImageIO.BASETYPE) -> bool"""
    def is_vec4(self, arg0: BASETYPE) -> bool:
        """is_vec4(self: OpenImageIO.OpenImageIO.TypeDesc, arg0: OpenImageIO.OpenImageIO.BASETYPE) -> bool"""
    def numelements(self) -> int:
        """numelements(self: OpenImageIO.OpenImageIO.TypeDesc) -> int"""
    def size(self) -> int:
        """size(self: OpenImageIO.OpenImageIO.TypeDesc) -> int"""
    def unarray(self) -> None:
        """unarray(self: OpenImageIO.OpenImageIO.TypeDesc) -> None"""
    def __eq__(self, arg0: TypeDesc) -> bool:
        """__eq__(self: OpenImageIO.OpenImageIO.TypeDesc, arg0: OpenImageIO.OpenImageIO.TypeDesc) -> bool"""
    def __ne__(self, arg0: TypeDesc) -> bool:
        """__ne__(self: OpenImageIO.OpenImageIO.TypeDesc, arg0: OpenImageIO.OpenImageIO.TypeDesc) -> bool"""

class VECSEMANTICS:
    __members__: ClassVar[dict] = ...  # read-only
    BOX: ClassVar[VECSEMANTICS] = ...
    COLOR: ClassVar[VECSEMANTICS] = ...
    KEYCODE: ClassVar[VECSEMANTICS] = ...
    NORMAL: ClassVar[VECSEMANTICS] = ...
    NOSEMANTICS: ClassVar[VECSEMANTICS] = ...
    NOXFORM: ClassVar[VECSEMANTICS] = ...
    POINT: ClassVar[VECSEMANTICS] = ...
    RATIONAL: ClassVar[VECSEMANTICS] = ...
    TIMECODE: ClassVar[VECSEMANTICS] = ...
    VECTOR: ClassVar[VECSEMANTICS] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, value: int) -> None:
        """__init__(self: OpenImageIO.OpenImageIO.VECSEMANTICS, value: int) -> None"""
    def _pybind11_conduit_v1_(self, *args, **kwargs): ...
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: OpenImageIO.OpenImageIO.VECSEMANTICS) -> int"""
    def __int__(self) -> int:
        """__int__(self: OpenImageIO.OpenImageIO.VECSEMANTICS) -> int"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class Wrap:
    __members__: ClassVar[dict] = ...  # read-only
    Black: ClassVar[Wrap] = ...
    Clamp: ClassVar[Wrap] = ...
    Default: ClassVar[Wrap] = ...
    Last: ClassVar[Wrap] = ...
    Mirror: ClassVar[Wrap] = ...
    Periodic: ClassVar[Wrap] = ...
    PeriodicPow2: ClassVar[Wrap] = ...
    PeriodicSharedBorder: ClassVar[Wrap] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, value: int) -> None:
        """__init__(self: OpenImageIO.OpenImageIO.Wrap, value: int) -> None"""
    def _pybind11_conduit_v1_(self, *args, **kwargs): ...
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: OpenImageIO.OpenImageIO.Wrap) -> int"""
    def __int__(self) -> int:
        """__int__(self: OpenImageIO.OpenImageIO.Wrap) -> int"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

@overload
def attribute(arg0: str, arg1: float) -> None:
    """attribute(*args, **kwargs)
    Overloaded function.

    1. attribute(arg0: str, arg1: float) -> None

    2. attribute(arg0: str, arg1: int) -> None

    3. attribute(arg0: str, arg1: str) -> None

    4. attribute(arg0: str, arg1: OpenImageIO.OpenImageIO.TypeDesc, arg2: object) -> None
    """
@overload
def attribute(arg0: str, arg1: int) -> None:
    """attribute(*args, **kwargs)
    Overloaded function.

    1. attribute(arg0: str, arg1: float) -> None

    2. attribute(arg0: str, arg1: int) -> None

    3. attribute(arg0: str, arg1: str) -> None

    4. attribute(arg0: str, arg1: OpenImageIO.OpenImageIO.TypeDesc, arg2: object) -> None
    """
@overload
def attribute(arg0: str, arg1: str) -> None:
    """attribute(*args, **kwargs)
    Overloaded function.

    1. attribute(arg0: str, arg1: float) -> None

    2. attribute(arg0: str, arg1: int) -> None

    3. attribute(arg0: str, arg1: str) -> None

    4. attribute(arg0: str, arg1: OpenImageIO.OpenImageIO.TypeDesc, arg2: object) -> None
    """
@overload
def attribute(arg0: str, arg1: TypeDesc, arg2: object) -> None:
    """attribute(*args, **kwargs)
    Overloaded function.

    1. attribute(arg0: str, arg1: float) -> None

    2. attribute(arg0: str, arg1: int) -> None

    3. attribute(arg0: str, arg1: str) -> None

    4. attribute(arg0: str, arg1: OpenImageIO.OpenImageIO.TypeDesc, arg2: object) -> None
    """
def equivalent_colorspace(arg0: str, arg1: str) -> bool:
    """equivalent_colorspace(arg0: str, arg1: str) -> bool"""
def get_bytes_attribute(name: str, defaultval: str = ...) -> bytes:
    """get_bytes_attribute(name: str, defaultval: str = '') -> bytes"""
def get_float_attribute(name: str, defaultval: float = ...) -> float:
    """get_float_attribute(name: str, defaultval: float = 0.0) -> float"""
def get_int_attribute(name: str, defaultval: int = ...) -> int:
    """get_int_attribute(name: str, defaultval: int = 0) -> int"""
def get_roi(arg0: ImageSpec) -> ROI:
    """get_roi(arg0: OpenImageIO.OpenImageIO.ImageSpec) -> OpenImageIO.OpenImageIO.ROI"""
def get_roi_full(arg0: ImageSpec) -> ROI:
    """get_roi_full(arg0: OpenImageIO.OpenImageIO.ImageSpec) -> OpenImageIO.OpenImageIO.ROI"""
def get_string_attribute(name: str, defaultval: str = ...) -> str:
    """get_string_attribute(name: str, defaultval: str = '') -> str"""
def getattribute(arg0: str, arg1: TypeDesc) -> object:
    """getattribute(arg0: str, arg1: OpenImageIO.OpenImageIO.TypeDesc) -> object"""
def geterror(clear: bool = ...) -> str:
    """geterror(clear: bool = True) -> str"""
def intersection(arg0: ROI, arg1: ROI) -> ROI:
    """intersection(arg0: OpenImageIO.OpenImageIO.ROI, arg1: OpenImageIO.OpenImageIO.ROI) -> OpenImageIO.OpenImageIO.ROI"""
def is_imageio_format_name(name: str) -> bool:
    """is_imageio_format_name(name: str) -> bool"""
def set_colorspace(spec: ImageSpec, name: str) -> None:
    """set_colorspace(spec: OpenImageIO.OpenImageIO.ImageSpec, name: str) -> None"""
def set_colorspace_rec709_gamma(arg0: ImageSpec, arg1: float) -> None:
    """set_colorspace_rec709_gamma(arg0: OpenImageIO.OpenImageIO.ImageSpec, arg1: float) -> None"""
def set_roi(arg0: ImageSpec, arg1: ROI) -> None:
    """set_roi(arg0: OpenImageIO.OpenImageIO.ImageSpec, arg1: OpenImageIO.OpenImageIO.ROI) -> None"""
def set_roi_full(arg0: ImageSpec, arg1: ROI) -> None:
    """set_roi_full(arg0: OpenImageIO.OpenImageIO.ImageSpec, arg1: OpenImageIO.OpenImageIO.ROI) -> None"""
def union(arg0: ROI, arg1: ROI) -> ROI:
    """union(arg0: OpenImageIO.OpenImageIO.ROI, arg1: OpenImageIO.OpenImageIO.ROI) -> OpenImageIO.OpenImageIO.ROI"""
