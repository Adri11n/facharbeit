from platform import system
from os import sep
from json import loads, dumps
import ctypes


def bibeliothek_laden() -> any:
    if system() == "Linux":
        main = ctypes.cdll.LoadLibrary(
            f'module{sep}bin{sep}gnu-linux{sep}main.so')
        read = main.read
        read.argtypes = [ctypes.c_char_p]
        read.restype = ctypes.c_void_p
        return read
    elif system() == "Windows":
        main = ctypes.cdll.LoadLibrary(
            f'module{sep}bin{sep}win-32{sep}main.dll')
        read = main.read
        read.argtypes = [ctypes.c_char_p]
        read.restype = ctypes.c_void_p
        return read


def json_schreiben(function: str, liste: list = [1], zahl: int = 0, zu_suchen: int = 0, anfang: int = 0, länge: int = 0):
    return dumps({
        "function": function,
        "liste": liste,
        "zahl": zahl,
        "zu_suchen": zu_suchen,
        "anfang": anfang,
        "länge": länge
    }, ensure_ascii=False).encode('utf-8')


def json_lesen(pointer: ctypes.c_void_p) -> dict:
    return loads(ctypes.string_at(pointer))


read = bibeliothek_laden()
