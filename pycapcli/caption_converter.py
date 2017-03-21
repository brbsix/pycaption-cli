# -*- coding: utf-8 -*-

"""A command line interface for the pycaption module"""

# standard imports
import argparse

# external imports
import pycaption


def get_reader(captions, options):
    """Return caption reader."""

    try:
        reader = pycaption.detect_format(captions)
    except IndexError:
        reader = None

    if reader is None:
        raise Exception('No caption format detected')

    reader_options = {
        'content': captions
    }

    if reader is pycaption.SCCReader:
        if options.offset:
            reader_options['offset'] = options.offset
        if options.lang:
            reader_options['lang'] = options.lang

    return reader, reader_options


def get_writer(options):
    """Return caption writer."""

    if options.dfxp:
        return pycaption.DFXPWriter
    elif options.sami:
        return pycaption.SAMIWriter
    elif options.srt:
        return pycaption.SRTWriter
    elif options.transcript:
        from pycaption.transcript import TranscriptWriter
        return TranscriptWriter


def main():
    """Start application."""

    options = parse()

    with options.file:
        captions = options.file.read()

    reader, reader_options = get_reader(captions, options)

    writer = get_writer(options)

    output = writer().write(reader().read(**reader_options))

    print(output)


def parse():
    """Parse command-line options."""

    parser = argparse.ArgumentParser()

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        '--dfxp',
        action='store_true',
        help='write captions in DFXP format')
    group.add_argument(
        '--sami',
        action='store_true',
        help='write captions in SAMI format')
    group.add_argument(
        '--srt',
        action='store_true',
        help='write captions in SRT format')
    group.add_argument(
        '--transcript',
        action='store_true',
        help='write transcript for captions')
    parser.add_argument(
        '--scc_lang',
        dest='lang',
        help='choose override language for input')
    parser.add_argument(
        '--scc_offset',
        dest='offset',
        help='choose offset for SCC file (in seconds)',
        type=int,
        default=0)
    parser.add_argument(
        'file',
        metavar='FILE',
        type=argparse.FileType('r'))

    return parser.parse_args()


if __name__ == '__main__':
    main()
