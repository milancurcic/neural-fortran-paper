.PHONY: all clean

all: main.pdf

main.pdf: src/main.tex src/references.bib
	$(MAKE) --directory=src
	cp src/$@ .

clean:
	$(RM) main.pdf
	$(MAKE) --directory=src clean
