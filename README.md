### LaTeX files' collection

Here some slides, notes and documents are collected. 
There are no rules about topics or folder's organization: with time I will update
this repo adding all my LaTeX productions. You will find more precise explanation
about the projects in their proper `README.md` files. 

### How to compile these files


At first, let's check if you have installed a TeX typesetting system.

I will refer to TeX-Live, because it is one of the most used. 

If you need to install it, I suggest to download all the extension by installing
`texlive-full`. You can find the installation instruction in the [official webpage](https://www.tug.org/texlive/).


Then you can clone the repo, enter the desired folder and run:

```bash
pdflatex main.txt
```

#### Sometimes other compilers are needed

In order to compile the `cv.tex` file, you need to use `lualatex` compiler. It is included
into the `texlive-full` package and can be used on a `file.tex` file by running:

```bash
lualatex file.tex
```
