import argparse
from ast import Pass

parser = argparse.ArgumentParser(add_help=True, description='Simple multitool to decrypt, encrypt, decode and encode payloads and stuff with different algorithms')

parser.add_argument('-algorithm', required=False, action='store', metavar='[XOR | AES | B64]', help='Chosen algorithm to use. Supported options: XOR, AES, B64')
parser.add_argument('-intype', required=False, action='store', metavar = '[AoS | BA]', help='Input type. How your input look like? AoS - Array of string | BA - Bytearray')
parser.add_argument('-outtype', required=False, action='store', metavar = '[AOS | BA]', help='Output type. How do you like your output looks like?')
parser.add_argument('-input', required=False, action='store', metavar = '[file]', help='Shellcode to encrypt | encode. Must be a file')
parser.add_argument('-key', required=False, action='store', metavar = '[file]', help='Key to use for encryption. Must be a file')



options = parser.parse_args()

class Algorithms:

    # XOR interface
    def xor(self, clear, key):
        encrypted = []
        for i in range(len(clear)):
            encrypted.append(hex(clear[i] ^ int(key, 16)))
        return encrypted

    # AES interface
    def aes(self, clear, key):
        return "Wynik"


class swisstool:

    def __init__(self, args):
        self.algorithm = args.algorithm
        self.input_type = args.intype
        self.output_type = args.outtype
        self.input = str(args.input)
        self.key = args.key

    # Przygotowanie inputu uzytkownika, usuniecie przecinkow, utworzenie tablicy integerow itp. 
    def prepare_input(self):
        input_array = []
        with open(self.input) as f:
            input_string = f.readline()
            if ',' in input_string:
                # Utworzenie tablicy integerów po uprzednio usunietych przecinkach oddzielajacych stringhexy
                input_array = [int(input_string.replace(",","").split()[i],16) for i in range(len(input_string.replace(",","").split()))] 
            else:
                # Utworzenie tablicy integerów w przypadku gdy stringhexow nie oddzielaja przecinki 
                input_array = [int(input_string.split()[i],16) for i in range(len(input_string.split()))]
        return input_array
            

    def enc(self, ia):
        if str(self.algorithm).upper() == 'XOR':
            return Algorithms.xor(self, ia, self.key)

    def dec(self, algorithm):
        return "Wynik"

    
c1 = swisstool(options)
print(c1.key)
input_array = c1.prepare_input()
encrypted = c1.enc(input_array)
print(encrypted)

