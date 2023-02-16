package main

import "sort"

// egal liste
// quelle https://www.calhoun.io/lets-learn-algorithms-implementing-binary-search/
// O(log n)
func Binäre_suche(liste []int, zu_suchen int, anfang int, länge int) int {
	länge = länge - 1
	for anfang <= länge {
		var mitte int = anfang + (länge-anfang)/2
		var mittelwert int = liste[mitte]
		if mittelwert == zu_suchen {
			return mitte
		} else if mittelwert > zu_suchen {
			länge = mitte - 1
		} else {
			anfang = mitte + 1
		}
	}
	return -1
}

// egal liste
// O(n)
func Lineare_suche(liste []int, zu_suchen int) int {
	for index, i := range liste {
		if i == zu_suchen {
			return index
		}
	}
	return -1
}

// unsortierte liste
// quelle https://www.golangprograms.com/golang-program-for-implementation-of-mergesort.html
// O(n log n)
func MergeSort(liste []int) []int {
	sort.Ints(liste)
	return liste
}

// unsortierte liste
// quelle https://github.com/TheAlgorithms/Go/blob/master/sort/bubblesort.go
// O(n^²)
func Bubble(liste []int) []int {
	getauscht := true
	for getauscht {
		getauscht = false
		for i := 0; i < len(liste)-1; i++ {
			if liste[i+1] < liste[i] {
				liste[i+1], liste[i] = liste[i], liste[i+1]
				getauscht = true
			}
		}
	}
	return liste
}

//quelle https://github.com/TheAlgorithms/Go/blob/59b98b82a5ccc5682a949bfc2c15a13805db0568/dynamic/fibonacci.go
//O(2^n)

func Fibonacci(n uint) uint {
	if n == 0 {
		return 0
	}

	var n1, n2 uint = 0, 1

	for i := uint(1); i < n; i++ {
		n3 := n1 + n2
		n1 = n2
		n2 = n3
	}

	return n2
}
