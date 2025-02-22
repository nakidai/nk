DESTDIR ?= /usr/local
RM ?= rm -f

README: README.7
	mandoc -Tascii README.7 | col -b > README

install:
	install -m755 main.py ${DESTDIR}/bin/nk

uninstall:
	${RM} ${DESTDIR/bin/nk
