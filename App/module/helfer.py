from platform import system as whatos
from os import system, sep, remove
from json import load, dump

in_json = f"module{sep}in.json"
out_json = f"module{sep}out.json"

def _welchesos() -> str:
    os = whatos()
    if os == "Windows":
        return "module\\bin\\win-32\\main.exe"
    elif os == "Linux":
        return "module/bin/gnu-linux/main"
    else:
        return "kacke"


def main_aufrufen() -> any:
    system(_welchesos())
    daten = _json_lesen()
    remove(out_json)
    return daten


def json_schreiben(function: str, liste: list, zahl: int = 0, zu_suchen: int = 0, anfang: int = 0, länge: int = 0):
    with open(in_json, "w") as f:
        dump({
    "function": function,
    "liste": liste,
    "zahl": zahl,
    "zu_suchen": zu_suchen,
    "anfang": anfang,
    "länge": länge
        }, f, ensure_ascii=False)
    

def _json_lesen() -> any:
    with open(out_json, "r") as f:
        return load(f)
