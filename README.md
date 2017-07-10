bibliograpy
===========

This tool converts BibTeX files to HTML bibliographies.  Bibliograpy currently
powers [CensorBib](https://censorbib.nymity.ch),
[BlockchainBib](https://allquantor.at/blockchainbib/), and
[MixBib](https://bib.mixnetworks.org).

Dependencies
============

You need [`Pybtex`](http://pybtex.sourceforge.net/) and
[`latexcodec`](https://github.com/mcmtroffaes/latexcodec). You may install the 
dependencies for this project by running `pip install -r requirements.txt`

Usage
=====

To create an HTML bibliography in `OUTPUT_DIRECTORY`, simply run:

    $ ./bibliogra.py -f BIBTEX_FILE OUTPUT_DIRECTORY

Alternatively, you can feed the tool over `stdin`:

    $ cat BIBTEX_FILE | ./bibliogra.py OUTPUT_DIRECTORY

Running `bibliograpy` will result in five HTML files that sort the
bibliography by year, reverse year, author, and reverse author.  Furthermore,
the tool tries to add links to local copies of publications.  It adds such a
link if it can find the respective publication in
`OUTPUT_DIRECTORY/pdf/BIBTEX_KEY.pdf`.  So if you have a BibTeX entry that
starts with `@inproceedings{JohnDoe, ...}`, then `bibliograpy` will look for
`OUTPUT_DIRECTORY/pdf/JohnDoe.pdf`.

An additional flag to create rss feeds can be passed (`--rss`), and it will
output an RSS 2.0 feed under `OUTPUT_DIRECTORY/feed`

Alternatives
============
Don't like `bibliograpy`?  Then have a look at
[`bibtex2html`](https://www.lri.fr/~filliatr/bibtex2html/),
[`bibhtml`](http://nxg.me.uk/dist/bibhtml/),
[`bib2xhtml`](http://www.spinellis.gr/sw/textproc/bib2xhtml/), or
[`anonbib`](https://gitweb.torproject.org/anonbib.git).

Feedback
========
Feel free to contact <phw@nymity.ch>.  You can use
[this](https://nymity.ch/openpgp_public_key.txt) OpenPGP key.
