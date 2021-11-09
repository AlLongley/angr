# pylint:disable=line-too-long
import logging

from ...sim_type import SimTypeFunction,     SimTypeShort, SimTypeInt, SimTypeLong, SimTypeLongLong, SimTypeDouble, SimTypeFloat,     SimTypePointer,     SimTypeChar,     SimStruct,     SimTypeFixedSizeArray,     SimTypeBottom,     SimUnion,     SimTypeBool
from ...calling_conventions import SimCCStdcall, SimCCMicrosoftAMD64
from .. import SIM_PROCEDURES as P
from . import SimLibrary


_l = logging.getLogger(name=__name__)


lib = SimLibrary()
lib.set_default_cc('X86', SimCCStdcall)
lib.set_default_cc('AMD64', SimCCMicrosoftAMD64)
lib.set_library_names("elscore.dll")
prototypes = \
    {
        # 
        'MappingGetServices': SimTypeFunction([SimTypePointer(SimStruct({"Size": SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), "pszCategory": SimTypePointer(SimTypeChar(label="Char"), offset=0), "pszInputLanguage": SimTypePointer(SimTypeChar(label="Char"), offset=0), "pszOutputLanguage": SimTypePointer(SimTypeChar(label="Char"), offset=0), "pszInputScript": SimTypePointer(SimTypeChar(label="Char"), offset=0), "pszOutputScript": SimTypePointer(SimTypeChar(label="Char"), offset=0), "pszInputContentType": SimTypePointer(SimTypeChar(label="Char"), offset=0), "pszOutputContentType": SimTypePointer(SimTypeChar(label="Char"), offset=0), "pGuid": SimTypePointer(SimTypeBottom(label="Guid"), offset=0), "_bitfield": SimTypeInt(signed=False, label="UInt32")}, name="MAPPING_ENUM_OPTIONS", pack=False, align=None), offset=0), SimTypePointer(SimTypePointer(SimStruct({"Size": SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), "pszCopyright": SimTypePointer(SimTypeChar(label="Char"), offset=0), "wMajorVersion": SimTypeShort(signed=False, label="UInt16"), "wMinorVersion": SimTypeShort(signed=False, label="UInt16"), "wBuildVersion": SimTypeShort(signed=False, label="UInt16"), "wStepVersion": SimTypeShort(signed=False, label="UInt16"), "dwInputContentTypesCount": SimTypeInt(signed=False, label="UInt32"), "prgInputContentTypes": SimTypePointer(SimTypePointer(SimTypeChar(label="Char"), offset=0), offset=0), "dwOutputContentTypesCount": SimTypeInt(signed=False, label="UInt32"), "prgOutputContentTypes": SimTypePointer(SimTypePointer(SimTypeChar(label="Char"), offset=0), offset=0), "dwInputLanguagesCount": SimTypeInt(signed=False, label="UInt32"), "prgInputLanguages": SimTypePointer(SimTypePointer(SimTypeChar(label="Char"), offset=0), offset=0), "dwOutputLanguagesCount": SimTypeInt(signed=False, label="UInt32"), "prgOutputLanguages": SimTypePointer(SimTypePointer(SimTypeChar(label="Char"), offset=0), offset=0), "dwInputScriptsCount": SimTypeInt(signed=False, label="UInt32"), "prgInputScripts": SimTypePointer(SimTypePointer(SimTypeChar(label="Char"), offset=0), offset=0), "dwOutputScriptsCount": SimTypeInt(signed=False, label="UInt32"), "prgOutputScripts": SimTypePointer(SimTypePointer(SimTypeChar(label="Char"), offset=0), offset=0), "guid": SimTypeBottom(label="Guid"), "pszCategory": SimTypePointer(SimTypeChar(label="Char"), offset=0), "pszDescription": SimTypePointer(SimTypeChar(label="Char"), offset=0), "dwPrivateDataSize": SimTypeInt(signed=False, label="UInt32"), "pPrivateData": SimTypePointer(SimTypeBottom(label="Void"), offset=0), "pContext": SimTypePointer(SimTypeBottom(label="Void"), offset=0), "_bitfield": SimTypeInt(signed=False, label="UInt32")}, name="MAPPING_SERVICE_INFO", pack=False, align=None), offset=0), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["pOptions", "prgServices", "pdwServicesCount"]),
        # 
        'MappingFreeServices': SimTypeFunction([SimTypePointer(SimStruct({"Size": SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), "pszCopyright": SimTypePointer(SimTypeChar(label="Char"), offset=0), "wMajorVersion": SimTypeShort(signed=False, label="UInt16"), "wMinorVersion": SimTypeShort(signed=False, label="UInt16"), "wBuildVersion": SimTypeShort(signed=False, label="UInt16"), "wStepVersion": SimTypeShort(signed=False, label="UInt16"), "dwInputContentTypesCount": SimTypeInt(signed=False, label="UInt32"), "prgInputContentTypes": SimTypePointer(SimTypePointer(SimTypeChar(label="Char"), offset=0), offset=0), "dwOutputContentTypesCount": SimTypeInt(signed=False, label="UInt32"), "prgOutputContentTypes": SimTypePointer(SimTypePointer(SimTypeChar(label="Char"), offset=0), offset=0), "dwInputLanguagesCount": SimTypeInt(signed=False, label="UInt32"), "prgInputLanguages": SimTypePointer(SimTypePointer(SimTypeChar(label="Char"), offset=0), offset=0), "dwOutputLanguagesCount": SimTypeInt(signed=False, label="UInt32"), "prgOutputLanguages": SimTypePointer(SimTypePointer(SimTypeChar(label="Char"), offset=0), offset=0), "dwInputScriptsCount": SimTypeInt(signed=False, label="UInt32"), "prgInputScripts": SimTypePointer(SimTypePointer(SimTypeChar(label="Char"), offset=0), offset=0), "dwOutputScriptsCount": SimTypeInt(signed=False, label="UInt32"), "prgOutputScripts": SimTypePointer(SimTypePointer(SimTypeChar(label="Char"), offset=0), offset=0), "guid": SimTypeBottom(label="Guid"), "pszCategory": SimTypePointer(SimTypeChar(label="Char"), offset=0), "pszDescription": SimTypePointer(SimTypeChar(label="Char"), offset=0), "dwPrivateDataSize": SimTypeInt(signed=False, label="UInt32"), "pPrivateData": SimTypePointer(SimTypeBottom(label="Void"), offset=0), "pContext": SimTypePointer(SimTypeBottom(label="Void"), offset=0), "_bitfield": SimTypeInt(signed=False, label="UInt32")}, name="MAPPING_SERVICE_INFO", pack=False, align=None), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["pServiceInfo"]),
        # 
        'MappingRecognizeText': SimTypeFunction([SimTypePointer(SimStruct({"Size": SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), "pszCopyright": SimTypePointer(SimTypeChar(label="Char"), offset=0), "wMajorVersion": SimTypeShort(signed=False, label="UInt16"), "wMinorVersion": SimTypeShort(signed=False, label="UInt16"), "wBuildVersion": SimTypeShort(signed=False, label="UInt16"), "wStepVersion": SimTypeShort(signed=False, label="UInt16"), "dwInputContentTypesCount": SimTypeInt(signed=False, label="UInt32"), "prgInputContentTypes": SimTypePointer(SimTypePointer(SimTypeChar(label="Char"), offset=0), offset=0), "dwOutputContentTypesCount": SimTypeInt(signed=False, label="UInt32"), "prgOutputContentTypes": SimTypePointer(SimTypePointer(SimTypeChar(label="Char"), offset=0), offset=0), "dwInputLanguagesCount": SimTypeInt(signed=False, label="UInt32"), "prgInputLanguages": SimTypePointer(SimTypePointer(SimTypeChar(label="Char"), offset=0), offset=0), "dwOutputLanguagesCount": SimTypeInt(signed=False, label="UInt32"), "prgOutputLanguages": SimTypePointer(SimTypePointer(SimTypeChar(label="Char"), offset=0), offset=0), "dwInputScriptsCount": SimTypeInt(signed=False, label="UInt32"), "prgInputScripts": SimTypePointer(SimTypePointer(SimTypeChar(label="Char"), offset=0), offset=0), "dwOutputScriptsCount": SimTypeInt(signed=False, label="UInt32"), "prgOutputScripts": SimTypePointer(SimTypePointer(SimTypeChar(label="Char"), offset=0), offset=0), "guid": SimTypeBottom(label="Guid"), "pszCategory": SimTypePointer(SimTypeChar(label="Char"), offset=0), "pszDescription": SimTypePointer(SimTypeChar(label="Char"), offset=0), "dwPrivateDataSize": SimTypeInt(signed=False, label="UInt32"), "pPrivateData": SimTypePointer(SimTypeBottom(label="Void"), offset=0), "pContext": SimTypePointer(SimTypeBottom(label="Void"), offset=0), "_bitfield": SimTypeInt(signed=False, label="UInt32")}, name="MAPPING_SERVICE_INFO", pack=False, align=None), offset=0), SimTypePointer(SimTypeChar(label="Char"), label="LPArray", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimStruct({"Size": SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), "pszInputLanguage": SimTypePointer(SimTypeChar(label="Char"), offset=0), "pszOutputLanguage": SimTypePointer(SimTypeChar(label="Char"), offset=0), "pszInputScript": SimTypePointer(SimTypeChar(label="Char"), offset=0), "pszOutputScript": SimTypePointer(SimTypeChar(label="Char"), offset=0), "pszInputContentType": SimTypePointer(SimTypeChar(label="Char"), offset=0), "pszOutputContentType": SimTypePointer(SimTypeChar(label="Char"), offset=0), "pszUILanguage": SimTypePointer(SimTypeChar(label="Char"), offset=0), "pfnRecognizeCallback": SimTypePointer(SimTypeFunction([SimTypePointer(SimTypeBottom(label="MAPPING_PROPERTY_BAG"), offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=True, label="Int32")], SimTypeBottom(label="Void"), arg_names=["pBag", "data", "dwDataSize", "Result"]), offset=0), "pRecognizeCallerData": SimTypePointer(SimTypeBottom(label="Void"), offset=0), "dwRecognizeCallerDataSize": SimTypeInt(signed=False, label="UInt32"), "pfnActionCallback": SimTypePointer(SimTypeFunction([SimTypePointer(SimTypeBottom(label="MAPPING_PROPERTY_BAG"), offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=True, label="Int32")], SimTypeBottom(label="Void"), arg_names=["pBag", "data", "dwDataSize", "Result"]), offset=0), "pActionCallerData": SimTypePointer(SimTypeBottom(label="Void"), offset=0), "dwActionCallerDataSize": SimTypeInt(signed=False, label="UInt32"), "dwServiceFlag": SimTypeInt(signed=False, label="UInt32"), "_bitfield": SimTypeInt(signed=False, label="UInt32")}, name="MAPPING_OPTIONS", pack=False, align=None), offset=0), SimTypePointer(SimStruct({"Size": SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), "prgResultRanges": SimTypePointer(SimStruct({"dwStartIndex": SimTypeInt(signed=False, label="UInt32"), "dwEndIndex": SimTypeInt(signed=False, label="UInt32"), "pszDescription": SimTypePointer(SimTypeChar(label="Char"), offset=0), "dwDescriptionLength": SimTypeInt(signed=False, label="UInt32"), "pData": SimTypePointer(SimTypeBottom(label="Void"), offset=0), "dwDataSize": SimTypeInt(signed=False, label="UInt32"), "pszContentType": SimTypePointer(SimTypeChar(label="Char"), offset=0), "prgActionIds": SimTypePointer(SimTypePointer(SimTypeChar(label="Char"), offset=0), offset=0), "dwActionsCount": SimTypeInt(signed=False, label="UInt32"), "prgActionDisplayNames": SimTypePointer(SimTypePointer(SimTypeChar(label="Char"), offset=0), offset=0)}, name="MAPPING_DATA_RANGE", pack=False, align=None), offset=0), "dwRangesCount": SimTypeInt(signed=False, label="UInt32"), "pServiceData": SimTypePointer(SimTypeBottom(label="Void"), offset=0), "dwServiceDataSize": SimTypeInt(signed=False, label="UInt32"), "pCallerData": SimTypePointer(SimTypeBottom(label="Void"), offset=0), "dwCallerDataSize": SimTypeInt(signed=False, label="UInt32"), "pContext": SimTypePointer(SimTypeBottom(label="Void"), offset=0)}, name="MAPPING_PROPERTY_BAG", pack=False, align=None), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["pServiceInfo", "pszText", "dwLength", "dwIndex", "pOptions", "pbag"]),
        # 
        'MappingDoAction': SimTypeFunction([SimTypePointer(SimStruct({"Size": SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), "prgResultRanges": SimTypePointer(SimStruct({"dwStartIndex": SimTypeInt(signed=False, label="UInt32"), "dwEndIndex": SimTypeInt(signed=False, label="UInt32"), "pszDescription": SimTypePointer(SimTypeChar(label="Char"), offset=0), "dwDescriptionLength": SimTypeInt(signed=False, label="UInt32"), "pData": SimTypePointer(SimTypeBottom(label="Void"), offset=0), "dwDataSize": SimTypeInt(signed=False, label="UInt32"), "pszContentType": SimTypePointer(SimTypeChar(label="Char"), offset=0), "prgActionIds": SimTypePointer(SimTypePointer(SimTypeChar(label="Char"), offset=0), offset=0), "dwActionsCount": SimTypeInt(signed=False, label="UInt32"), "prgActionDisplayNames": SimTypePointer(SimTypePointer(SimTypeChar(label="Char"), offset=0), offset=0)}, name="MAPPING_DATA_RANGE", pack=False, align=None), offset=0), "dwRangesCount": SimTypeInt(signed=False, label="UInt32"), "pServiceData": SimTypePointer(SimTypeBottom(label="Void"), offset=0), "dwServiceDataSize": SimTypeInt(signed=False, label="UInt32"), "pCallerData": SimTypePointer(SimTypeBottom(label="Void"), offset=0), "dwCallerDataSize": SimTypeInt(signed=False, label="UInt32"), "pContext": SimTypePointer(SimTypeBottom(label="Void"), offset=0)}, name="MAPPING_PROPERTY_BAG", pack=False, align=None), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Char"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["pBag", "dwRangeIndex", "pszActionId"]),
        # 
        'MappingFreePropertyBag': SimTypeFunction([SimTypePointer(SimStruct({"Size": SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), "prgResultRanges": SimTypePointer(SimStruct({"dwStartIndex": SimTypeInt(signed=False, label="UInt32"), "dwEndIndex": SimTypeInt(signed=False, label="UInt32"), "pszDescription": SimTypePointer(SimTypeChar(label="Char"), offset=0), "dwDescriptionLength": SimTypeInt(signed=False, label="UInt32"), "pData": SimTypePointer(SimTypeBottom(label="Void"), offset=0), "dwDataSize": SimTypeInt(signed=False, label="UInt32"), "pszContentType": SimTypePointer(SimTypeChar(label="Char"), offset=0), "prgActionIds": SimTypePointer(SimTypePointer(SimTypeChar(label="Char"), offset=0), offset=0), "dwActionsCount": SimTypeInt(signed=False, label="UInt32"), "prgActionDisplayNames": SimTypePointer(SimTypePointer(SimTypeChar(label="Char"), offset=0), offset=0)}, name="MAPPING_DATA_RANGE", pack=False, align=None), offset=0), "dwRangesCount": SimTypeInt(signed=False, label="UInt32"), "pServiceData": SimTypePointer(SimTypeBottom(label="Void"), offset=0), "dwServiceDataSize": SimTypeInt(signed=False, label="UInt32"), "pCallerData": SimTypePointer(SimTypeBottom(label="Void"), offset=0), "dwCallerDataSize": SimTypeInt(signed=False, label="UInt32"), "pContext": SimTypePointer(SimTypeBottom(label="Void"), offset=0)}, name="MAPPING_PROPERTY_BAG", pack=False, align=None), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["pBag"]),
    }

lib.set_prototypes(prototypes)