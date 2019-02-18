.PHONY: all clean

all: main

main: main.tex
	pdflatex -halt-on-error $@
	bibtex $@
	pdflatex -halt-on-error $@
	pdflatex -halt-on-error $@

clean:
	$(RM) *.aux *.bbl *.blg *.cut *.log *.out *.pdf
