
.PHONY: *.tex

all: main.tex

*.tex:
	pdflatex \\nonstopmode \\input $@

clean:
	rm -f *.aux *~ *.log *.out *.toc *.bbl *.blg *.pdf

