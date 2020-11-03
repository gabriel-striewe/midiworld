from ctypes import * 
cdll.LoadLibrary("./libmidi.dylib")
libmidi = CDLL("./libmidi.dylib")

