
DESTDIR ?=
PREFIX = /usr/local

CC ?= gcc
CFLAGS += -std=gnu99 -Wall -Wextra -Wshadow -Werror -fvisibility=hidden
LDFLAGS += -Wl,--no-undefined

ifeq ($(DEBUG),1)
CFLAGS += -O0 -g -DDEBUG
else
CFLAGS += -O2 -DNDEBUG
endif

all: mod-ttymidi mod-ttymidi.so

debug:
	$(MAKE) DEBUG=1

mod-ttymidi: src/ttymidi.c src/mod-semaphore.h
	$(CC) $< $(CFLAGS) $(shell pkg-config --cflags --libs jack) $(LDFLAGS) -lpthread -o $@

mod-ttymidi.so: src/ttymidi.c src/mod-semaphore.h
	$(CC) $< $(CFLAGS) $(shell pkg-config --cflags --libs jack) $(LDFLAGS) -fPIC -lpthread -shared -o $@

install: mod-ttymidi mod-ttymidi.so
	install -m 755 mod-ttymidi    $(DESTDIR)$(PREFIX)/bin/
	install -m 755 mod-ttymidi.so $(DESTDIR)$(shell pkg-config --variable=libdir jack)/jack/

clean:
	rm -f mod-ttymidi mod-ttymidi.so

uninstall:
	rm $(DESTDIR)$(PREFIX)/bin/mod-ttymidi
	rm $(DESTDIR)$(shell pkg-config --variable=libdir jack)/jack/mod-ttymidi.so
