import sys


def decode_caesar_cipher(s, n):
    alpha = " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',.?!"
    s = s.strip()
    text = ''
    for c in s:
        text += alpha[(alpha.index(c) + n) % len(alpha)]
    print('Decoded text: "' + text + '"')


args = sys.argv
filename = args[1]

opened_file = open(filename)
encoded_text = opened_file.read()  # read the file into a string
decode_caesar_cipher(encoded_text, -13)
opened_file.close()  # always close the files you've opened
