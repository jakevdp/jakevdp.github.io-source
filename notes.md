# Notes on creating the blog

```
$ conda create -n pelican-blog python=3.5 jupyter notebook
$ source activate pelican-blog
$ pip install pelican
$ pip install Markdown
$ pelican-quickstart
$ git submodule add git://github.com/danielfrg/pelican-ipynb.git plugins/ipynb
$ git submodule add git://github.com/getpelican/pelican-plugins.git plugins/pelican-plugins
```
