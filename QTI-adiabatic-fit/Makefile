output = main.pdf
main = main.tex

arxivtar = main.tar

bibfile = references.bib

figures = $(wildcard figures/*/*)
arxiv_files = 

LC = pdflatex -shell-escape
FPFlags = "-draftmode"
LPFlags = "-file-line-error"
BC = bibtex

.PHONY: all clean clean_latex arxiv pdf

all: $(output) # $(arxivtar)

arxiv: $(arxivtar)

pdf: $(output)

%.pdf : %.tex $(bibfile) | %.bbl
	@$(LC) $(FPFLAGS) $< 
	@$(LC) $(LPFLAGS) $< 


%.bbl : %.aux $(bibfile) 

	@echo "Generating bibliography"
	@echo $<
	@$(BC) $<

%.aux : %.tex
	@echo "First pass"

	@$(LC) $(FPFLAGS) $<  

%.tar: %.tex %.bbl
	@echo "Creating arxiv tar"
	tar --dereference -cf $@ $^ plots $(arxiv_files)

clean_latex:
	@echo "Removing all latex byproducts"
	@rm -f *.{log,aux,bbl,bcf,blg,ilg,toc,tdo,fls,fdb_latexmk,lof,lot,idx,ind,snm,out,nav,synctex.gz,bak,xml,dvi,brf} mainNotes.bib

clean: clean_latex
	@echo "Removing latex pdf and arxiv tar and minted files"
	@rm -f $(output) $(arxivtar)
	@rm -rf $(minted_files)
