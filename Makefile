CC=clang
CFLAGS=-fembed-bitcode

%.o: %.c
	$(CC) -c -o $@ $(CFLAGS) $<

hello: hello.o
	$(CC) -o hello $(CFLAGS) hello.o

.PHONY: clean

clean:
	rm -f hello *.o
