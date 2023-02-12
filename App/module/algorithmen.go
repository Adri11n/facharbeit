package main

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
	var länge = len(liste)

	if länge == 1 {
		return liste
	}

	mitte := int(länge / 2)
	var (
		links  = make([]int, mitte)
		rechts = make([]int, länge-mitte)
	)
	for i := 0; i < länge; i++ {
		if i < mitte {
			links[i] = liste[i]
		} else {
			rechts[i-mitte] = liste[i]
		}
	}

	return merge(MergeSort(links), MergeSort(rechts))
}

func merge(links []int, rechts []int) (ergebniss []int) {
	ergebniss = make([]int, len(links)+len(rechts))

	i := 0
	for len(links) > 0 && len(rechts) > 0 {
		if links[0] < rechts[0] {
			ergebniss[i] = links[0]
			links = links[1:]
		} else {
			ergebniss[i] = rechts[0]
			rechts = rechts[1:]
		}
		i++
	}

	for j := 0; j < len(links); j++ {
		ergebniss[i] = links[j]
		i++
	}
	for j := 0; j < len(rechts); j++ {
		ergebniss[i] = rechts[j]
		i++
	}

	return
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
