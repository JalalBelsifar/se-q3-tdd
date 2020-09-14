#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility."""

__author__ = "Jalal Belsifar, help from Joseph and the group"


import sys
import argparse


def create_parser():
    """Returns an instance of argparse.ArgumentParser"""
    parser = argparse.ArgumentParser(
        description='Perform transformation on input text.')
    parser.add_argument(
        'text', help='text to be manipulated', nargs=1)
    parser.add_argument(
        '-u', '--upper', help='convert text to uppercase', action='store_true')
    parser.add_argument(
        '-l', '--lower', help='convert text to lowercase', action='store_true')
    parser.add_argument(
        '-t', '--title', help='convert text to titlecase', action='store_true')
    return parser


def main(args):
    """Implementation of echo"""
    parser = create_parser()
    ns = parser.parse_args(args)

    if not ns:
        parser.print_usage()
        sys.exit(1)
    text = ns.text[0]
    lower = ns.lower
    title = ns.title
    upper = ns.upper

    result = text
    if upper:
        result = result.upper()
    if lower:
        result = result.lower()
    if title:
        result = result.title()

    print(result)


if __name__ == '__main__':
    main(sys.argv[1:])
