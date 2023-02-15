#!/bin/bash
go build -o bin/gnu-linux/main main.go vergleichsfunktionen.go algorithmen.go
GOOS=windows GOARCH=amd64 go build -o bin/win-32/main.exe main.go vergleichsfunktionen.go algorithmen.go