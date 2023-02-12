package main

import (
	"math"
)

// O(1)
func O(liste []int) int {
	return liste[0]
}

// O(log n)
func Binärer_logorythmuen_von_n(liste []int) []float64 {
	var ergebnisse []float64
	for _, x := range liste {
		ergebnisse = append(ergebnisse, math.Log2(float64(x)))
	}
	return ergebnisse
}

// O(n)
func Linar(liste []int) []int {
	var ergebnisse []int
	for _, x := range liste {
		ergebnisse = append(ergebnisse, x)
	}
	return ergebnisse
}

//O(n log n)

func Linear_mal_log_von_n(liste []int) []float64 {
	var ergebnisse []float64
	for _, x := range liste {
		ergebnisse = append(ergebnisse, float64(x)*math.Log2(float64(x)))
	}
	return ergebnisse
}

// O(n^²)
func Quadieren(liste []int) []float64 {
	var ergebnisse []float64
	for _, x := range liste {
		ergebnisse = append(ergebnisse, math.Pow(float64(x), 2.0))
	}
	return ergebnisse
}

// O(2^n)
func Duplizieren(liste []int) []float64 {
	var ergebnisse []float64
	for _, x := range liste {
		ergebnisse = append(ergebnisse, math.Pow(2.0, float64(x)))
	}
	return ergebnisse
}
