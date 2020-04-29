all: libListas.so.1.0.1 libListas.so.1

libListas.so.1.0.1: Listas.c Listas.h
	gcc -Wall -c -fPIC -g Listas.c
	gcc -shared -Wl,-soname,libListas.so.1 -o libListas.so.1.0.1 Listas.o

libListas.so.1: libListas.so.1.0.1
	ln -s libListas.so.1.0.1 libListas.so.1

clean:
	rm -fr libListas.so.1.0.1 libListas.so.1 Listas.o *~ 
