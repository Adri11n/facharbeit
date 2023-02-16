package main

import (
	"C"
	"encoding/json"
	"time"
)

type in struct {
	Function  string `json:"function"`
	Liste     []int  `json:"liste"`
	Zahl      uint   `json:"zahl"`
	Zu_suchen int    `json:"zu_suchen"`
	Anfang    int    `json:"anfang"`
	Länge     int    `json:"länge"`
}

type out struct {
	Zeit      int64 `json:"zeit"`
	Ergebniss any   `json:"ergebniss"`
}

var funktionsverzeichniss = map[string]interface{}{
	"Binärer_logorythmuen_von_n": &a,
	"Linar":                      &b,
	"Linear_mal_log_von_n":       &c,
	"Quadieren":                  &d,
	"Duplizieren":                &e,
	"Binäre_suche":               &f,
	"Lineare_suche":              &g,
	"MergeSort":                  &h,
	"Bubble":                     &i,
	"Fibonacci":                  &j,
}

var a = Binärer_logorythmuen_von_n
var b = Linar
var c = Linear_mal_log_von_n
var d = Quadieren
var e = Duplizieren
var f = Binäre_suche
var g = Lineare_suche
var h = MergeSort
var i = Bubble
var j = Fibonacci

func check(e error) {
	if e != nil {
		panic(e)
	}
}

//export read
func read(documentPtr *C.char) *C.char {
	args := C.GoString(documentPtr)
	var data in
	err := json.Unmarshal([]byte(args), &data)
	check(err)
	a := string(zeitmessung(data.Function, data.Liste, data.Zahl, data.Zu_suchen, data.Anfang, data.Länge))
	return C.CString(a)

}

func write(zu_schreiben any, zeit int64) []byte {
	ausgabe := out{Zeit: zeit, Ergebniss: zu_schreiben}
	daten, err := json.Marshal(ausgabe)
	check(err)
	return daten

}

func zeitmessung(funktion string, liste []int, zahl uint, zu_suchen int, anfang int, länge int) []byte {
	if &f == funktionsverzeichniss[funktion] {
		start := time.Now()
		output := Binäre_suche(liste, zu_suchen, anfang, länge)
		jetzt := time.Since(start).Nanoseconds()
		return write(output, jetzt)
	} else if &g == funktionsverzeichniss[funktion] {
		start := time.Now()
		output := Lineare_suche(liste, zu_suchen)
		jetzt := time.Since(start).Nanoseconds()
		return write(output, jetzt)
	} else if &j == funktionsverzeichniss[funktion] {
		start := time.Now()
		output := Fibonacci(zahl)
		jetzt := time.Since(start).Nanoseconds()
		return write(output, jetzt)
	} else if &a == funktionsverzeichniss[funktion] {
		start := time.Now()
		output := Binärer_logorythmuen_von_n(liste)
		jetzt := time.Since(start).Nanoseconds()
		return write(output, jetzt)
	} else if &b == funktionsverzeichniss[funktion] {
		start := time.Now()
		output := Linar(liste)
		jetzt := time.Since(start).Nanoseconds()
		return write(output, jetzt)
	} else if &c == funktionsverzeichniss[funktion] {
		start := time.Now()
		output := Linear_mal_log_von_n(liste)
		jetzt := time.Since(start).Nanoseconds()
		return write(output, jetzt)
	} else if &d == funktionsverzeichniss[funktion] {
		start := time.Now()
		output := Quadieren(liste)
		jetzt := time.Since(start).Nanoseconds()
		return write(output, jetzt)
	} else if &e == funktionsverzeichniss[funktion] {
		start := time.Now()
		output := Duplizieren(liste)
		jetzt := time.Since(start).Nanoseconds()
		return write(output, jetzt)
	} else if &h == funktionsverzeichniss[funktion] {
		start := time.Now()
		output := MergeSort(liste)
		jetzt := time.Since(start).Nanoseconds()
		return write(output, jetzt)
	} else if &i == funktionsverzeichniss[funktion] {
		start := time.Now()
		output := Bubble(liste)
		jetzt := time.Since(start).Nanoseconds()
		return write(output, jetzt)
	} else {
		println("error")
	}
	return []byte{1}
}

func main() {}
