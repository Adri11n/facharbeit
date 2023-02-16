#!/bin/bash
go build -buildmode=c-shared -o bin/gnu-linux/main.so . && rm bin/gnu-linux/main.h
#GOOS=windows GOARCH=amd64 go build -buildmode=c-shared -o bin/win-32/main.dll main.go vergleichsfunktionen.go algorithmen.go