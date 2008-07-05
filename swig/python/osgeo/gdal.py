# This file was automatically generated by SWIG (http://www.swig.org).
# Version 1.3.31
#
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _gdal
import new
new_instancemethod = new.instancemethod
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'PySwigObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError,name

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

import types
try:
    _object = types.ObjectType
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0
del types


from gdalconst import *
import gdalconst


import sys
have_warned = 0
byteorders = {"little": "<",
              "big": ">"}
array_modes = { gdalconst.GDT_Int16:    ("%si2" % byteorders[sys.byteorder]),
                gdalconst.GDT_UInt16:   ("%su2" % byteorders[sys.byteorder]),
                gdalconst.GDT_Int32:    ("%si4" % byteorders[sys.byteorder]),
                gdalconst.GDT_UInt32:   ("%su4" % byteorders[sys.byteorder]),
                gdalconst.GDT_Float32:  ("%sf4" % byteorders[sys.byteorder]),
                gdalconst.GDT_Float64:  ("%sf8" % byteorders[sys.byteorder]),
                gdalconst.GDT_CFloat32: ("%sf4" % byteorders[sys.byteorder]),
                gdalconst.GDT_CFloat64: ("%sf8" % byteorders[sys.byteorder]),
                gdalconst.GDT_Byte:     ("%st8" % byteorders[sys.byteorder]),
}


def deprecation_warn( module ):
  global have_warned

  if have_warned == 1:
      return

  have_warned = 1

  from warnings import warn
  warn('%s.py was placed in a namespace, it is now available as osgeo.%s' % (module,module),
       DeprecationWarning)

def RGBFile2PCTFile( src_filename, dst_filename ):
  src_ds = Open(src_filename)
  if src_ds is None or src_ds == 'NULL':
      return 1

  ct = ColorTable()
  err = ComputeMedianCutPCT( src_ds.GetRasterBand(1),
                             src_ds.GetRasterBand(2),
                             src_ds.GetRasterBand(3),
                             256, ct )
  if err <> 0:
      return err

  gtiff_driver = GetDriverByName('GTiff')
  if gtiff_driver is None:
      return 1

  dst_ds = gtiff_driver.Create( dst_filename,
                                src_ds.RasterXSize, src_ds.RasterYSize )
  dst_ds.GetRasterBand(1).SetRasterColorTable( ct )

  err = DitherRGB2PCT( src_ds.GetRasterBand(1),
                       src_ds.GetRasterBand(2),
                       src_ds.GetRasterBand(3),
                       dst_ds.GetRasterBand(1),
                       ct )
  dst_ds = None
  src_ds = None

  return 0


def UseExceptions(*args):
  """UseExceptions()"""
  return _gdal.UseExceptions(*args)

def DontUseExceptions(*args):
  """DontUseExceptions()"""
  return _gdal.DontUseExceptions(*args)

def Debug(*args):
  """Debug(char msg_class, char message)"""
  return _gdal.Debug(*args)

def Error(*args):
  """Error(CPLErr msg_class=CE_Failure, int err_code=0, char msg="error")"""
  return _gdal.Error(*args)

def PopErrorHandler(*args):
  """PopErrorHandler()"""
  return _gdal.PopErrorHandler(*args)

def ErrorReset(*args):
  """ErrorReset()"""
  return _gdal.ErrorReset(*args)

def EscapeString(*args, **kwargs):
  """EscapeString(int len, int scheme=CPLES_SQL) -> char"""
  return _gdal.EscapeString(*args, **kwargs)

def GetLastErrorNo(*args):
  """GetLastErrorNo() -> int"""
  return _gdal.GetLastErrorNo(*args)

def GetLastErrorType(*args):
  """GetLastErrorType() -> CPLErr"""
  return _gdal.GetLastErrorType(*args)

def GetLastErrorMsg(*args):
  """GetLastErrorMsg() -> char"""
  return _gdal.GetLastErrorMsg(*args)

def PushFinderLocation(*args):
  """PushFinderLocation(char ?)"""
  return _gdal.PushFinderLocation(*args)

def PopFinderLocation(*args):
  """PopFinderLocation()"""
  return _gdal.PopFinderLocation(*args)

def FinderClean(*args):
  """FinderClean()"""
  return _gdal.FinderClean(*args)

def FindFile(*args):
  """FindFile(char ?, char ?) -> char"""
  return _gdal.FindFile(*args)

def ReadDir(*args):
  """ReadDir(char ?) -> char"""
  return _gdal.ReadDir(*args)

def SetConfigOption(*args):
  """SetConfigOption(char ?, char ?)"""
  return _gdal.SetConfigOption(*args)

def GetConfigOption(*args):
  """GetConfigOption(char ?, char ?) -> char"""
  return _gdal.GetConfigOption(*args)

def CPLBinaryToHex(*args):
  """CPLBinaryToHex(int nBytes, GByte pabyData) -> char"""
  return _gdal.CPLBinaryToHex(*args)

def CPLHexToBinary(*args):
  """CPLHexToBinary(char pszHex, int pnBytes) -> GByte"""
  return _gdal.CPLHexToBinary(*args)
class MajorObject(_object):
    """Proxy of C++ MajorObject class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, MajorObject, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, MajorObject, name)
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    def GetDescription(*args):
        """GetDescription(self) -> char"""
        return _gdal.MajorObject_GetDescription(*args)

    def SetDescription(*args):
        """SetDescription(self, char pszNewDesc)"""
        return _gdal.MajorObject_SetDescription(*args)

    def GetMetadata_Dict(*args):
        """GetMetadata_Dict(self, char pszDomain="") -> char"""
        return _gdal.MajorObject_GetMetadata_Dict(*args)

    def GetMetadata_List(*args):
        """GetMetadata_List(self, char pszDomain="") -> char"""
        return _gdal.MajorObject_GetMetadata_List(*args)

    def SetMetadata(*args):
        """
        SetMetadata(self, char papszMetadata, char pszDomain="") -> CPLErr
        SetMetadata(self, char pszMetadataString, char pszDomain="") -> CPLErr
        """
        return _gdal.MajorObject_SetMetadata(*args)

    def GetMetadataItem(*args):
        """GetMetadataItem(self, char pszName, char pszDomain="") -> char"""
        return _gdal.MajorObject_GetMetadataItem(*args)

    def SetMetadataItem(*args):
        """SetMetadataItem(self, char pszName, char pszValue, char pszDomain="") -> CPLErr"""
        return _gdal.MajorObject_SetMetadataItem(*args)

    def GetMetadata( self, domain = '' ):
      if domain[:4] == 'xml:':
        return self.GetMetadata_List( domain )
      return self.GetMetadata_Dict( domain )

MajorObject_swigregister = _gdal.MajorObject_swigregister
MajorObject_swigregister(MajorObject)

def PushErrorHandler(*args):
  """
    PushErrorHandler(char pszCallbackName="CPLQuietErrorHandler") -> CPLErr
    PushErrorHandler(CPLErrorHandler ?)
    """
  return _gdal.PushErrorHandler(*args)

class Driver(MajorObject):
    """Proxy of C++ Driver class"""
    __swig_setmethods__ = {}
    for _s in [MajorObject]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, Driver, name, value)
    __swig_getmethods__ = {}
    for _s in [MajorObject]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, Driver, name)
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_getmethods__["ShortName"] = _gdal.Driver_ShortName_get
    if _newclass:ShortName = _swig_property(_gdal.Driver_ShortName_get)
    __swig_getmethods__["LongName"] = _gdal.Driver_LongName_get
    if _newclass:LongName = _swig_property(_gdal.Driver_LongName_get)
    __swig_getmethods__["HelpTopic"] = _gdal.Driver_HelpTopic_get
    if _newclass:HelpTopic = _swig_property(_gdal.Driver_HelpTopic_get)
    def Create(*args, **kwargs):
        """
        Create(self, char name, int xsize, int ysize, int bands=1, GDALDataType eType=GDT_Byte, 
            char options=0) -> Dataset
        """
        return _gdal.Driver_Create(*args, **kwargs)

    def CreateCopy(*args, **kwargs):
        """
        CreateCopy(self, char name, Dataset src, int strict=1, char options=0, 
            GDALProgressFunc callback=None, void callback_data=None) -> Dataset
        """
        return _gdal.Driver_CreateCopy(*args, **kwargs)

    def Delete(*args):
        """Delete(self, char name) -> int"""
        return _gdal.Driver_Delete(*args)

    def Rename(*args):
        """Rename(self, char newName, char oldName) -> int"""
        return _gdal.Driver_Rename(*args)

    def Register(*args):
        """Register(self) -> int"""
        return _gdal.Driver_Register(*args)

    def Deregister(*args):
        """Deregister(self)"""
        return _gdal.Driver_Deregister(*args)

Driver_swigregister = _gdal.Driver_swigregister
Driver_swigregister(Driver)

class ColorEntry(_object):
    """Proxy of C++ ColorEntry class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ColorEntry, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ColorEntry, name)
    __repr__ = _swig_repr
    __swig_setmethods__["c1"] = _gdal.ColorEntry_c1_set
    __swig_getmethods__["c1"] = _gdal.ColorEntry_c1_get
    if _newclass:c1 = _swig_property(_gdal.ColorEntry_c1_get, _gdal.ColorEntry_c1_set)
    __swig_setmethods__["c2"] = _gdal.ColorEntry_c2_set
    __swig_getmethods__["c2"] = _gdal.ColorEntry_c2_get
    if _newclass:c2 = _swig_property(_gdal.ColorEntry_c2_get, _gdal.ColorEntry_c2_set)
    __swig_setmethods__["c3"] = _gdal.ColorEntry_c3_set
    __swig_getmethods__["c3"] = _gdal.ColorEntry_c3_get
    if _newclass:c3 = _swig_property(_gdal.ColorEntry_c3_get, _gdal.ColorEntry_c3_set)
    __swig_setmethods__["c4"] = _gdal.ColorEntry_c4_set
    __swig_getmethods__["c4"] = _gdal.ColorEntry_c4_get
    if _newclass:c4 = _swig_property(_gdal.ColorEntry_c4_get, _gdal.ColorEntry_c4_set)
    def __init__(self, *args): 
        """__init__(self) -> ColorEntry"""
        this = _gdal.new_ColorEntry(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _gdal.delete_ColorEntry
    __del__ = lambda self : None;
ColorEntry_swigregister = _gdal.ColorEntry_swigregister
ColorEntry_swigregister(ColorEntry)

class GCP(_object):
    """Proxy of C++ GCP class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, GCP, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, GCP, name)
    __repr__ = _swig_repr
    __swig_setmethods__["GCPX"] = _gdal.GCP_GCPX_set
    __swig_getmethods__["GCPX"] = _gdal.GCP_GCPX_get
    if _newclass:GCPX = _swig_property(_gdal.GCP_GCPX_get, _gdal.GCP_GCPX_set)
    __swig_setmethods__["GCPY"] = _gdal.GCP_GCPY_set
    __swig_getmethods__["GCPY"] = _gdal.GCP_GCPY_get
    if _newclass:GCPY = _swig_property(_gdal.GCP_GCPY_get, _gdal.GCP_GCPY_set)
    __swig_setmethods__["GCPZ"] = _gdal.GCP_GCPZ_set
    __swig_getmethods__["GCPZ"] = _gdal.GCP_GCPZ_get
    if _newclass:GCPZ = _swig_property(_gdal.GCP_GCPZ_get, _gdal.GCP_GCPZ_set)
    __swig_setmethods__["GCPPixel"] = _gdal.GCP_GCPPixel_set
    __swig_getmethods__["GCPPixel"] = _gdal.GCP_GCPPixel_get
    if _newclass:GCPPixel = _swig_property(_gdal.GCP_GCPPixel_get, _gdal.GCP_GCPPixel_set)
    __swig_setmethods__["GCPLine"] = _gdal.GCP_GCPLine_set
    __swig_getmethods__["GCPLine"] = _gdal.GCP_GCPLine_get
    if _newclass:GCPLine = _swig_property(_gdal.GCP_GCPLine_get, _gdal.GCP_GCPLine_set)
    __swig_setmethods__["Info"] = _gdal.GCP_Info_set
    __swig_getmethods__["Info"] = _gdal.GCP_Info_get
    if _newclass:Info = _swig_property(_gdal.GCP_Info_get, _gdal.GCP_Info_set)
    __swig_setmethods__["Id"] = _gdal.GCP_Id_set
    __swig_getmethods__["Id"] = _gdal.GCP_Id_get
    if _newclass:Id = _swig_property(_gdal.GCP_Id_get, _gdal.GCP_Id_set)
    def __init__(self, *args): 
        """
        __init__(self, double x=0.0, double y=0.0, double z=0.0, double pixel=0.0, 
            double line=0.0, char info="", char id="") -> GCP
        """
        this = _gdal.new_GCP(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _gdal.delete_GCP
    __del__ = lambda self : None;
    def __str__(self):
      str = '%s (%.2fP,%.2fL) -> (%.7fE,%.7fN,%.2f) %s '\
            % (self.Id, self.GCPPixel, self.GCPLine,
               self.GCPX, self.GCPY, self.GCPZ, self.Info )
      return str
      def serialize(self,with_Z=0):
          base = [CXT_Element,'GCP']
          base.append([CXT_Attribute,'Id',[CXT_Text,self.Id]])
          pixval = '%0.15E' % self.GCPPixel       
          lineval = '%0.15E' % self.GCPLine
          xval = '%0.15E' % self.GCPX
          yval = '%0.15E' % self.GCPY
          zval = '%0.15E' % self.GCPZ
          base.append([CXT_Attribute,'Pixel',[CXT_Text,pixval]])
          base.append([CXT_Attribute,'Line',[CXT_Text,lineval]])
          base.append([CXT_Attribute,'X',[CXT_Text,xval]])
          base.append([CXT_Attribute,'Y',[CXT_Text,yval]])
          if with_Z:
              base.append([CXT_Attribute,'Z',[CXT_Text,zval]])        
          return base

GCP_swigregister = _gdal.GCP_swigregister
GCP_swigregister(GCP)


def GDAL_GCP_GCPX_get(*args):
  """GDAL_GCP_GCPX_get(GCP h) -> double"""
  return _gdal.GDAL_GCP_GCPX_get(*args)

def GDAL_GCP_GCPX_set(*args):
  """GDAL_GCP_GCPX_set(GCP h, double val)"""
  return _gdal.GDAL_GCP_GCPX_set(*args)

def GDAL_GCP_GCPY_get(*args):
  """GDAL_GCP_GCPY_get(GCP h) -> double"""
  return _gdal.GDAL_GCP_GCPY_get(*args)

def GDAL_GCP_GCPY_set(*args):
  """GDAL_GCP_GCPY_set(GCP h, double val)"""
  return _gdal.GDAL_GCP_GCPY_set(*args)

def GDAL_GCP_GCPZ_get(*args):
  """GDAL_GCP_GCPZ_get(GCP h) -> double"""
  return _gdal.GDAL_GCP_GCPZ_get(*args)

def GDAL_GCP_GCPZ_set(*args):
  """GDAL_GCP_GCPZ_set(GCP h, double val)"""
  return _gdal.GDAL_GCP_GCPZ_set(*args)

def GDAL_GCP_GCPPixel_get(*args):
  """GDAL_GCP_GCPPixel_get(GCP h) -> double"""
  return _gdal.GDAL_GCP_GCPPixel_get(*args)

def GDAL_GCP_GCPPixel_set(*args):
  """GDAL_GCP_GCPPixel_set(GCP h, double val)"""
  return _gdal.GDAL_GCP_GCPPixel_set(*args)

def GDAL_GCP_GCPLine_get(*args):
  """GDAL_GCP_GCPLine_get(GCP h) -> double"""
  return _gdal.GDAL_GCP_GCPLine_get(*args)

def GDAL_GCP_GCPLine_set(*args):
  """GDAL_GCP_GCPLine_set(GCP h, double val)"""
  return _gdal.GDAL_GCP_GCPLine_set(*args)

def GDAL_GCP_Info_get(*args):
  """GDAL_GCP_Info_get(GCP h) -> char"""
  return _gdal.GDAL_GCP_Info_get(*args)

def GDAL_GCP_Info_set(*args):
  """GDAL_GCP_Info_set(GCP h, char val)"""
  return _gdal.GDAL_GCP_Info_set(*args)

def GDAL_GCP_Id_get(*args):
  """GDAL_GCP_Id_get(GCP h) -> char"""
  return _gdal.GDAL_GCP_Id_get(*args)

def GDAL_GCP_Id_set(*args):
  """GDAL_GCP_Id_set(GCP h, char val)"""
  return _gdal.GDAL_GCP_Id_set(*args)

def GDAL_GCP_get_GCPX(*args):
  """GDAL_GCP_get_GCPX(GCP h) -> double"""
  return _gdal.GDAL_GCP_get_GCPX(*args)

def GDAL_GCP_set_GCPX(*args):
  """GDAL_GCP_set_GCPX(GCP h, double val)"""
  return _gdal.GDAL_GCP_set_GCPX(*args)

def GDAL_GCP_get_GCPY(*args):
  """GDAL_GCP_get_GCPY(GCP h) -> double"""
  return _gdal.GDAL_GCP_get_GCPY(*args)

def GDAL_GCP_set_GCPY(*args):
  """GDAL_GCP_set_GCPY(GCP h, double val)"""
  return _gdal.GDAL_GCP_set_GCPY(*args)

def GDAL_GCP_get_GCPZ(*args):
  """GDAL_GCP_get_GCPZ(GCP h) -> double"""
  return _gdal.GDAL_GCP_get_GCPZ(*args)

def GDAL_GCP_set_GCPZ(*args):
  """GDAL_GCP_set_GCPZ(GCP h, double val)"""
  return _gdal.GDAL_GCP_set_GCPZ(*args)

def GDAL_GCP_get_GCPPixel(*args):
  """GDAL_GCP_get_GCPPixel(GCP h) -> double"""
  return _gdal.GDAL_GCP_get_GCPPixel(*args)

def GDAL_GCP_set_GCPPixel(*args):
  """GDAL_GCP_set_GCPPixel(GCP h, double val)"""
  return _gdal.GDAL_GCP_set_GCPPixel(*args)

def GDAL_GCP_get_GCPLine(*args):
  """GDAL_GCP_get_GCPLine(GCP h) -> double"""
  return _gdal.GDAL_GCP_get_GCPLine(*args)

def GDAL_GCP_set_GCPLine(*args):
  """GDAL_GCP_set_GCPLine(GCP h, double val)"""
  return _gdal.GDAL_GCP_set_GCPLine(*args)

def GDAL_GCP_get_Info(*args):
  """GDAL_GCP_get_Info(GCP h) -> char"""
  return _gdal.GDAL_GCP_get_Info(*args)

def GDAL_GCP_set_Info(*args):
  """GDAL_GCP_set_Info(GCP h, char val)"""
  return _gdal.GDAL_GCP_set_Info(*args)

def GDAL_GCP_get_Id(*args):
  """GDAL_GCP_get_Id(GCP h) -> char"""
  return _gdal.GDAL_GCP_get_Id(*args)

def GDAL_GCP_set_Id(*args):
  """GDAL_GCP_set_Id(GCP h, char val)"""
  return _gdal.GDAL_GCP_set_Id(*args)

def GCPsToGeoTransform(*args):
  """GCPsToGeoTransform(int nGCPs, double argout, int bApproxOK=1) -> FALSE_IS_ERR"""
  return _gdal.GCPsToGeoTransform(*args)
class Dataset(MajorObject):
    """Proxy of C++ Dataset class"""
    __swig_setmethods__ = {}
    for _s in [MajorObject]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, Dataset, name, value)
    __swig_getmethods__ = {}
    for _s in [MajorObject]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, Dataset, name)
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_getmethods__["RasterXSize"] = _gdal.Dataset_RasterXSize_get
    if _newclass:RasterXSize = _swig_property(_gdal.Dataset_RasterXSize_get)
    __swig_getmethods__["RasterYSize"] = _gdal.Dataset_RasterYSize_get
    if _newclass:RasterYSize = _swig_property(_gdal.Dataset_RasterYSize_get)
    __swig_getmethods__["RasterCount"] = _gdal.Dataset_RasterCount_get
    if _newclass:RasterCount = _swig_property(_gdal.Dataset_RasterCount_get)
    __swig_destroy__ = _gdal.delete_Dataset
    __del__ = lambda self : None;
    def GetDriver(*args):
        """GetDriver(self) -> Driver"""
        return _gdal.Dataset_GetDriver(*args)

    def GetRasterBand(*args):
        """GetRasterBand(self, int nBand) -> Band"""
        return _gdal.Dataset_GetRasterBand(*args)

    def GetProjection(*args):
        """GetProjection(self) -> char"""
        return _gdal.Dataset_GetProjection(*args)

    def GetProjectionRef(*args):
        """GetProjectionRef(self) -> char"""
        return _gdal.Dataset_GetProjectionRef(*args)

    def SetProjection(*args):
        """SetProjection(self, char prj) -> CPLErr"""
        return _gdal.Dataset_SetProjection(*args)

    def GetGeoTransform(*args):
        """GetGeoTransform(self, double argout)"""
        return _gdal.Dataset_GetGeoTransform(*args)

    def SetGeoTransform(*args):
        """SetGeoTransform(self, double argin) -> CPLErr"""
        return _gdal.Dataset_SetGeoTransform(*args)

    def BuildOverviews(*args, **kwargs):
        """
        BuildOverviews(self, char resampling="NEAREST", int overviewlist=0, GDALProgressFunc callback=None, 
            void callback_data=None) -> int
        """
        return _gdal.Dataset_BuildOverviews(*args, **kwargs)

    def GetGCPCount(*args):
        """GetGCPCount(self) -> int"""
        return _gdal.Dataset_GetGCPCount(*args)

    def GetGCPProjection(*args):
        """GetGCPProjection(self) -> char"""
        return _gdal.Dataset_GetGCPProjection(*args)

    def GetGCPs(*args):
        """GetGCPs(self, int nGCPs)"""
        return _gdal.Dataset_GetGCPs(*args)

    def SetGCPs(*args):
        """SetGCPs(self, int nGCPs, char pszGCPProjection) -> CPLErr"""
        return _gdal.Dataset_SetGCPs(*args)

    def FlushCache(*args):
        """FlushCache(self)"""
        return _gdal.Dataset_FlushCache(*args)

    def AddBand(*args, **kwargs):
        """AddBand(self, GDALDataType datatype=GDT_Byte, char options=0) -> CPLErr"""
        return _gdal.Dataset_AddBand(*args, **kwargs)

    def CreateMaskBand(*args):
        """CreateMaskBand(self, int nFlags) -> CPLErr"""
        return _gdal.Dataset_CreateMaskBand(*args)

    def WriteRaster(*args, **kwargs):
        """
        WriteRaster(self, int xoff, int yoff, int xsize, int ysize, int buf_len, 
            int buf_xsize=0, int buf_ysize=0, GDALDataType buf_type=0, 
            int band_list=0) -> CPLErr
        """
        return _gdal.Dataset_WriteRaster(*args, **kwargs)

    def ReadRaster(*args, **kwargs):
        """
        ReadRaster(self, int xoff, int yoff, int xsize, int ysize, int buf_len, 
            int buf_xsize=0, int buf_ysize=0, GDALDataType buf_type=0, 
            int band_list=0) -> CPLErr
        """
        return _gdal.Dataset_ReadRaster(*args, **kwargs)

    def ReadAsArray(self, xoff=0, yoff=0, xsize=None, ysize=None ):
        import gdalnumeric
        return gdalnumeric.DatasetReadAsArray( self, xoff, yoff, xsize, ysize )
    def WriteRaster(self, xoff, yoff, xsize, ysize,
                    buf_string,
                    buf_xsize = None, buf_ysize = None, buf_type = None,
                    band_list = None ):

        if buf_xsize is None:
            buf_xsize = xsize;
        if buf_ysize is None:
            buf_ysize = ysize;
        if band_list is None:
            band_list = range(1,self.RasterCount+1)
        if buf_type is None:
            buf_type = self.GetRasterBand(1).DataType

        if len(buf_string) < buf_xsize * buf_ysize * len(band_list) \
           * (_gdal.GetDataTypeSize(buf_type) / 8):
            raise ValueError, "raster buffer too small in WriteRaster"
        else:    
            return _gdal.Dataset_WriteRaster(self,
                 xoff, yoff, xsize, ysize,
                buf_string, buf_xsize, buf_ysize, buf_type, band_list )

    def ReadRaster(self, xoff, yoff, xsize, ysize,
                   buf_xsize = None, buf_ysize = None, buf_type = None,
                   band_list = None ):

        if band_list is None:
            band_list = range(1,self.RasterCount+1)
        if buf_xsize is None:
            buf_xsize = xsize;
        if buf_ysize is None:
            buf_ysize = ysize;

        if buf_type is None:
            buf_type = self.GetRasterBand(1).DataType;
        return _gdal.Dataset_ReadRaster(self, xoff, yoff, xsize, ysize,
                                           buf_xsize, buf_ysize, buf_type,
                                           band_list)

    def GetSubDatasets(self):
        sd_list = []
        
        sd = self.GetMetadata('SUBDATASETS')
        if sd is None:
            return sd_list

        i = 1
        while sd.has_key('SUBDATASET_'+str(i)+'_NAME'):
            sd_list.append( ( sd['SUBDATASET_'+str(i)+'_NAME'],
                              sd['SUBDATASET_'+str(i)+'_DESC'] ) )
            i = i + 1
        return sd_list

Dataset_swigregister = _gdal.Dataset_swigregister
Dataset_swigregister(Dataset)

class Band(MajorObject):
    """Proxy of C++ Band class"""
    __swig_setmethods__ = {}
    for _s in [MajorObject]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, Band, name, value)
    __swig_getmethods__ = {}
    for _s in [MajorObject]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, Band, name)
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_getmethods__["XSize"] = _gdal.Band_XSize_get
    if _newclass:XSize = _swig_property(_gdal.Band_XSize_get)
    __swig_getmethods__["YSize"] = _gdal.Band_YSize_get
    if _newclass:YSize = _swig_property(_gdal.Band_YSize_get)
    __swig_getmethods__["DataType"] = _gdal.Band_DataType_get
    if _newclass:DataType = _swig_property(_gdal.Band_DataType_get)
    def GetBlockSize(*args):
        """GetBlockSize(self, int pnBlockXSize, int pnBlockYSize)"""
        return _gdal.Band_GetBlockSize(*args)

    def GetRasterColorInterpretation(*args):
        """GetRasterColorInterpretation(self) -> GDALColorInterp"""
        return _gdal.Band_GetRasterColorInterpretation(*args)

    def SetRasterColorInterpretation(*args):
        """SetRasterColorInterpretation(self, GDALColorInterp val) -> CPLErr"""
        return _gdal.Band_SetRasterColorInterpretation(*args)

    def GetNoDataValue(*args):
        """GetNoDataValue(self, double val)"""
        return _gdal.Band_GetNoDataValue(*args)

    def SetNoDataValue(*args):
        """SetNoDataValue(self, double d) -> CPLErr"""
        return _gdal.Band_SetNoDataValue(*args)

    def GetRasterCategoryNames(*args):
        """GetRasterCategoryNames(self) -> char"""
        return _gdal.Band_GetRasterCategoryNames(*args)

    def SetRasterCategoryNames(*args):
        """SetRasterCategoryNames(self, char names) -> CPLErr"""
        return _gdal.Band_SetRasterCategoryNames(*args)

    def GetMinimum(*args):
        """GetMinimum(self, double val)"""
        return _gdal.Band_GetMinimum(*args)

    def GetMaximum(*args):
        """GetMaximum(self, double val)"""
        return _gdal.Band_GetMaximum(*args)

    def GetOffset(*args):
        """GetOffset(self, double val)"""
        return _gdal.Band_GetOffset(*args)

    def GetScale(*args):
        """GetScale(self, double val)"""
        return _gdal.Band_GetScale(*args)

    def GetStatistics(*args):
        """
        GetStatistics(self, int approx_ok, int force, double min, double max, double mean, 
            double stddev) -> CPLErr
        """
        return _gdal.Band_GetStatistics(*args)

    def SetStatistics(*args):
        """SetStatistics(self, double min, double max, double mean, double stddev) -> CPLErr"""
        return _gdal.Band_SetStatistics(*args)

    def GetOverviewCount(*args):
        """GetOverviewCount(self) -> int"""
        return _gdal.Band_GetOverviewCount(*args)

    def GetOverview(*args):
        """GetOverview(self, int i) -> Band"""
        return _gdal.Band_GetOverview(*args)

    def Checksum(*args, **kwargs):
        """Checksum(self, int xoff=0, int yoff=0, int xsize=0, int ysize=0) -> int"""
        return _gdal.Band_Checksum(*args, **kwargs)

    def ComputeRasterMinMax(*args):
        """ComputeRasterMinMax(self, double argout, int approx_ok=0)"""
        return _gdal.Band_ComputeRasterMinMax(*args)

    def ComputeBandStats(*args):
        """ComputeBandStats(self, double argout, int samplestep=1)"""
        return _gdal.Band_ComputeBandStats(*args)

    def Fill(*args):
        """Fill(self, double real_fill, double imag_fill=0.0) -> CPLErr"""
        return _gdal.Band_Fill(*args)

    def ReadRaster(*args, **kwargs):
        """
        ReadRaster(self, int xoff, int yoff, int xsize, int ysize, int buf_len, 
            int buf_xsize=0, int buf_ysize=0, int buf_type=0) -> CPLErr
        """
        return _gdal.Band_ReadRaster(*args, **kwargs)

    def WriteRaster(*args, **kwargs):
        """
        WriteRaster(self, int xoff, int yoff, int xsize, int ysize, int buf_len, 
            int buf_xsize=0, int buf_ysize=0, int buf_type=0) -> CPLErr
        """
        return _gdal.Band_WriteRaster(*args, **kwargs)

    def FlushCache(*args):
        """FlushCache(self)"""
        return _gdal.Band_FlushCache(*args)

    def GetRasterColorTable(*args):
        """GetRasterColorTable(self) -> ColorTable"""
        return _gdal.Band_GetRasterColorTable(*args)

    def SetRasterColorTable(*args):
        """SetRasterColorTable(self, ColorTable arg) -> int"""
        return _gdal.Band_SetRasterColorTable(*args)

    def GetDefaultRAT(*args):
        """GetDefaultRAT(self) -> RasterAttributeTable"""
        return _gdal.Band_GetDefaultRAT(*args)

    def SetDefaultRAT(*args):
        """SetDefaultRAT(self, RasterAttributeTable table) -> int"""
        return _gdal.Band_SetDefaultRAT(*args)

    def GetMaskBand(*args):
        """GetMaskBand(self) -> Band"""
        return _gdal.Band_GetMaskBand(*args)

    def GetMaskFlags(*args):
        """GetMaskFlags(self) -> int"""
        return _gdal.Band_GetMaskFlags(*args)

    def CreateMaskBand(*args):
        """CreateMaskBand(self, int nFlags) -> CPLErr"""
        return _gdal.Band_CreateMaskBand(*args)

    def GetHistogram(*args):
        """
        GetHistogram(self, double dfMin=-0.5, double dfMax=255.5, int nBuckets=255, 
            int bIncludeOutOfRange=0, int bApproxOk=1, 
            GDALProgressFunc callback=None, void callback_data=None) -> CPLErr
        """
        return _gdal.Band_GetHistogram(*args)

    def ReadAsArray(self, xoff=0, yoff=0, win_xsize=None, win_ysize=None,
                    buf_xsize=None, buf_ysize=None, buf_obj=None):
        import gdalnumeric

        return gdalnumeric.BandReadAsArray( self, xoff, yoff,
                                            win_xsize, win_ysize,
                                            buf_xsize, buf_ysize, buf_obj )
      
    def WriteArray(self, array, xoff=0, yoff=0):
        import gdalnumeric

        return gdalnumeric.BandWriteArray( self, array, xoff, yoff )

    def __get_array_interface__(self):
        shape = [1, self.XSize, self.YSize]
        

Band_swigregister = _gdal.Band_swigregister
Band_swigregister(Band)

class ColorTable(MajorObject):
    """Proxy of C++ ColorTable class"""
    __swig_setmethods__ = {}
    for _s in [MajorObject]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, ColorTable, name, value)
    __swig_getmethods__ = {}
    for _s in [MajorObject]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, ColorTable, name)
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """__init__(self, GDALPaletteInterp palette=GPI_RGB) -> ColorTable"""
        this = _gdal.new_ColorTable(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _gdal.delete_ColorTable
    __del__ = lambda self : None;
    def Clone(*args):
        """Clone(self) -> ColorTable"""
        return _gdal.ColorTable_Clone(*args)

    def GetPaletteInterpretation(*args):
        """GetPaletteInterpretation(self) -> GDALPaletteInterp"""
        return _gdal.ColorTable_GetPaletteInterpretation(*args)

    def GetCount(*args):
        """GetCount(self) -> int"""
        return _gdal.ColorTable_GetCount(*args)

    def GetColorEntry(*args):
        """GetColorEntry(self, int entry) -> ColorEntry"""
        return _gdal.ColorTable_GetColorEntry(*args)

    def GetColorEntryAsRGB(*args):
        """GetColorEntryAsRGB(self, int entry, ColorEntry centry) -> int"""
        return _gdal.ColorTable_GetColorEntryAsRGB(*args)

    def SetColorEntry(*args):
        """SetColorEntry(self, int entry, ColorEntry centry)"""
        return _gdal.ColorTable_SetColorEntry(*args)

    def CreateColorRamp(*args):
        """
        CreateColorRamp(self, int nStartIndex, ColorEntry startcolor, int nEndIndex, 
            ColorEntry endcolor)
        """
        return _gdal.ColorTable_CreateColorRamp(*args)

ColorTable_swigregister = _gdal.ColorTable_swigregister
ColorTable_swigregister(ColorTable)

class RasterAttributeTable(MajorObject):
    """Proxy of C++ RasterAttributeTable class"""
    __swig_setmethods__ = {}
    for _s in [MajorObject]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, RasterAttributeTable, name, value)
    __swig_getmethods__ = {}
    for _s in [MajorObject]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, RasterAttributeTable, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """__init__(self) -> RasterAttributeTable"""
        this = _gdal.new_RasterAttributeTable(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _gdal.delete_RasterAttributeTable
    __del__ = lambda self : None;
    def Clone(*args):
        """Clone(self) -> RasterAttributeTable"""
        return _gdal.RasterAttributeTable_Clone(*args)

    def GetColumnCount(*args):
        """GetColumnCount(self) -> int"""
        return _gdal.RasterAttributeTable_GetColumnCount(*args)

    def GetNameOfCol(*args):
        """GetNameOfCol(self, int iCol) -> char"""
        return _gdal.RasterAttributeTable_GetNameOfCol(*args)

    def GetUsageOfCol(*args):
        """GetUsageOfCol(self, int iCol) -> GDALRATFieldUsage"""
        return _gdal.RasterAttributeTable_GetUsageOfCol(*args)

    def GetTypeOfCol(*args):
        """GetTypeOfCol(self, int iCol) -> GDALRATFieldType"""
        return _gdal.RasterAttributeTable_GetTypeOfCol(*args)

    def GetColOfUsage(*args):
        """GetColOfUsage(self, GDALRATFieldUsage eUsage) -> int"""
        return _gdal.RasterAttributeTable_GetColOfUsage(*args)

    def GetRowCount(*args):
        """GetRowCount(self) -> int"""
        return _gdal.RasterAttributeTable_GetRowCount(*args)

    def GetValueAsString(*args):
        """GetValueAsString(self, int iRow, int iCol) -> char"""
        return _gdal.RasterAttributeTable_GetValueAsString(*args)

    def GetValueAsInt(*args):
        """GetValueAsInt(self, int iRow, int iCol) -> int"""
        return _gdal.RasterAttributeTable_GetValueAsInt(*args)

    def GetValueAsDouble(*args):
        """GetValueAsDouble(self, int iRow, int iCol) -> double"""
        return _gdal.RasterAttributeTable_GetValueAsDouble(*args)

    def SetValueAsString(*args):
        """SetValueAsString(self, int iRow, int iCol, char pszValue)"""
        return _gdal.RasterAttributeTable_SetValueAsString(*args)

    def SetValueAsInt(*args):
        """SetValueAsInt(self, int iRow, int iCol, int nValue)"""
        return _gdal.RasterAttributeTable_SetValueAsInt(*args)

    def SetValueAsDouble(*args):
        """SetValueAsDouble(self, int iRow, int iCol, double dfValue)"""
        return _gdal.RasterAttributeTable_SetValueAsDouble(*args)

    def SetRowCount(*args):
        """SetRowCount(self, int nCount)"""
        return _gdal.RasterAttributeTable_SetRowCount(*args)

    def CreateColumn(*args):
        """CreateColumn(self, char pszName, GDALRATFieldType eType, GDALRATFieldUsage eUsage) -> int"""
        return _gdal.RasterAttributeTable_CreateColumn(*args)

    def GetRowOfValue(*args):
        """GetRowOfValue(self, double dfValue) -> int"""
        return _gdal.RasterAttributeTable_GetRowOfValue(*args)

RasterAttributeTable_swigregister = _gdal.RasterAttributeTable_swigregister
RasterAttributeTable_swigregister(RasterAttributeTable)


def TermProgress_nocb(*args, **kwargs):
  """TermProgress_nocb(double dfProgress, char pszMessage=None, void pData=None) -> int"""
  return _gdal.TermProgress_nocb(*args, **kwargs)
TermProgress = _gdal.TermProgress
ComputeMedianCutPCT = _gdal.ComputeMedianCutPCT
DitherRGB2PCT = _gdal.DitherRGB2PCT
ReprojectImage = _gdal.ReprojectImage
ComputeProximity = _gdal.ComputeProximity
RegenerateOverviews = _gdal.RegenerateOverviews
RegenerateOverview = _gdal.RegenerateOverview
AutoCreateWarpedVRT = _gdal.AutoCreateWarpedVRT
class Transformer(_object):
    """Proxy of C++ Transformer class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Transformer, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Transformer, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """__init__(self, Dataset src, Dataset dst, char options) -> Transformer"""
        this = _gdal.new_Transformer(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _gdal.delete_Transformer
    __del__ = lambda self : None;
    def TransformPoint(*args):
        """
        TransformPoint(self, int bDstToSrc, double inout) -> int
        TransformPoint(self, double argout, int bDstToSrc, double x, double y, double z=0.0) -> int
        """
        return _gdal.Transformer_TransformPoint(*args)

    def TransformPoints(*args):
        """
        TransformPoints(self, int bDstToSrc, int nCount, double x, double y, double z, 
            int panSuccess) -> int
        """
        return _gdal.Transformer_TransformPoints(*args)

Transformer_swigregister = _gdal.Transformer_swigregister
Transformer_swigregister(Transformer)

VersionInfo = _gdal.VersionInfo
AllRegister = _gdal.AllRegister
GetCacheMax = _gdal.GetCacheMax
SetCacheMax = _gdal.SetCacheMax
GetCacheUsed = _gdal.GetCacheUsed
GetDataTypeSize = _gdal.GetDataTypeSize
DataTypeIsComplex = _gdal.DataTypeIsComplex
GetDataTypeName = _gdal.GetDataTypeName
GetDataTypeByName = _gdal.GetDataTypeByName
GetColorInterpretationName = _gdal.GetColorInterpretationName
GetPaletteInterpretationName = _gdal.GetPaletteInterpretationName
DecToDMS = _gdal.DecToDMS
PackedDMSToDec = _gdal.PackedDMSToDec
DecToPackedDMS = _gdal.DecToPackedDMS
ParseXMLString = _gdal.ParseXMLString
SerializeXMLTree = _gdal.SerializeXMLTree
GetDriverCount = _gdal.GetDriverCount
GetDriverByName = _gdal.GetDriverByName
GetDriver = _gdal.GetDriver
Open = _gdal.Open
OpenShared = _gdal.OpenShared
IdentifyDriver = _gdal.IdentifyDriver
GeneralCmdLineProcessor = _gdal.GeneralCmdLineProcessor


