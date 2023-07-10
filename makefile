#!bin/bash

Sum: main.o sum.o
	gcc  main.o sum.o

sum.o: sum.c
	gcc -c sum.c

main.o: main.c
	gcc -c main.c

clean:
	rm -f *.o *.out

