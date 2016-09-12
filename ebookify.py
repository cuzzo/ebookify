#! /usr/bin/env python

import sys
import codecs
import os

import pystache

def read_plain_text_book(ifile):
    lines = []
    with codecs.open(ifile, "r", "utf-8") as f:
        plain_lines = f.readlines()
        for line in plain_lines:
            line = line.strip()
            if len(line) == 0:
                continue
            lines.append(line)
    return lines

def write_ebook(ofile, lines, author, title):
    template = ""
    path = os.path.join(os.path.dirname(__file__), "template.html")

    with open(path, "r") as f:
        template = "".join(f.readlines())

    ebook = pystache.render(template, {
            "lines": lines,
            "author": author,
            "title": title
        })

    with codecs.open(ofile, "w", "utf-8") as f:
        f.write(ebook)

def get_params():
    return (sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])

def main():
    ifile, ofile, author, title = get_params()
    text = read_plain_text_book(ifile)
    write_ebook(ofile, text, author, title)

if __name__ == "__main__":
    main()
