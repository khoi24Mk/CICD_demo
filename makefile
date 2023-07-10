#!bin/bash

Sum: main.o sum.o
	g++  main.o sum.o

sum.o: sum.cpp
	g++ -c sum.cpp

main.o: main.cpp
	g++ -c main.cpp
