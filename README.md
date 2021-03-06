pycaption-cli
=============

Note: This fork adds Python 3 support

A command line interface for the pycaption module.

Installation
============

It is recommended to install the program in a virtualenv.

    pip3 install --user git+https://github.com/brbsix/pycaption-cli.git

Usage
=====

From your command line:

    pycaption (--dfxp | --sami | --srt | --transcript) <path to caption file>
    
e.g.

    pycaption --dfxp ../jnorton-caption.scc

Output is written to the screen. To write to a file, use something like this:

    pycaption --dfxp ../jnorton-caption.scc > jnorton.xml

Supported Formats
=================

 - DFXP (read/write)
 - SAMI (read/write)
 - SCC (read)
 - SRT (read/write)
 - Transcript (write)
 
License
=======

This module is Copyright 2012 Joe Norton and is available under the [Apache License, Version 2.0][1].

[1]: http://www.apache.org/licenses/LICENSE-2.0