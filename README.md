# Source for http://jakevdp.github.io

This repository contains the source for http://jakevdp.github.io/.

## Building the Blog

Install the required packages:

```
$ conda create -n pelican-blog python=3.5 jupyter notebook
$ source activate pelican-blog
$ pip install pelican Markdown ghp-import
```

Build the html and serve locally:

```
$ make html
$ make serve
$ open http://localhost:8000
```

Deploy to github pages

```
$ make publish
$ ghp-import -m "Generate Pelican site" output
$ git push git@github.com:jakevdp/jakevdp.github.io.git gh-pages:master
```