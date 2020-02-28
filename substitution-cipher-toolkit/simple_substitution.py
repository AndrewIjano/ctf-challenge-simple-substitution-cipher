from argparse import ArgumentParser, FileType

BASE = ord("A")

def substitute(text, alphabet):
    alphabet = alphabet.upper()
    alpha_dict = {
        chr(BASE + i): chr(BASE + i).lower() if alphabet[i] == "-" else alphabet[i].upper()
        for i in range(len(alphabet))
    }
    return "".join(alpha_dict[c] if c.isalpha() else c for c in text.upper())

def substitution_module(document, alphabet):
    print("  ABCDEFGHIJKLMNOPQRSTUVWXYZ This clear text...")
    print(" ", alphabet.upper().strip()[
        :26], "...maps to this ciphertext\n")
    print(substitute(document, alphabet[:26]))


if __name__ == '__main__':
    parser = ArgumentParser(
        prog='simple_substitution.py',
        epilog='''
            Examples:\n
            python3 simple_substitution.py ciphertext.txt alphabet.txt
            ''')
    try:
        parser.add_argument(
            'ciphertext', metavar='ciphertext', nargs=1, help='the input ciphertext to be modified', type=FileType('r'))
        parser.add_argument(
            'alphabet', metavar='alphabet', nargs=1, help='the alphabet used in the simple substitution encryption', type=FileType('r'))
        args = parser.parse_args()
        substitution_module(args.ciphertext[0].read(), args.alphabet[0].read())
    except:
        print()
        parser.print_help()