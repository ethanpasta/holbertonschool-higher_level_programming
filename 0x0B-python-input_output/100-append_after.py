#!/usr/bin/python3
def append_after(filename="", search_string="", new_string=""):
    with open(filename) as f:
        with open('tmpfile.txt', 'w+') as tmp:
            for line in f:
                tmp.write(line)
                if line.find(search_string) != -1:
                    tmp.write(new_string)
    with open(filename, 'w') as f:
        f.write(open('tmpfile.txt').read())
