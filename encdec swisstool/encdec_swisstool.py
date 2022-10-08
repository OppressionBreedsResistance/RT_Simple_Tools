import argparse

parser = argparse.ArgumentParser(add_help=True, description='Simple multitool to decrypt, encrypt, decode and encode payloads and stuff with different algorithms')

parser.add_argument('-algorithm', required=True, action='store', metavar='wybrany algorytm', help='Chosen algorithm to use. Supported options: XOR | AES' )


class Algorithms:

    # Tu beda algorytmy i interfejsy do wykonania operacji szyfrowania deszyfrowania kodowania dekodowania


    def xor(self, encoded, key):
        return "Wynik"


class swisstool:

    # Tu beda metody ktore bedzie wykorzystywac swisstool

    def enc(self, algorithm):
        return "Wynik"

    def dec(self, algorithm):
        return "Wynik"

    


