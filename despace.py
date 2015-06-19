#! /usr/bin/env python

import sys
import codecs
import re

WHITESPACE = re.compile("\s+")

def read_plain_text_book(ifile):
    lines = []
    cur_line = ""
    with codecs.open(ifile, "r", "utf-8") as f:
        plain_lines = f.readlines()
        for line in plain_lines:
            stripped_line = line.strip()
            if len(stripped_line) == 0:
                continue
            if not WHITESPACE.match(line):
                cur_line += " " + stripped_line
            else:
                lines.append(cur_line.strip())
                cur_line = stripped_line
        if cur_line != "":
            lines.append(cur_line.strip())
    return lines

def write_ebook(ofile, ebook):
    with codecs.open(ofile, "w", "utf-8") as f:
        f.write("\n".join(ebook))

def get_params():
    return (sys.argv[1])

def main():
    ifile = get_params()
    text = read_plain_text_book(ifile)
    write_ebook(ifile, text)

if __name__ == "__main__":
    main()
