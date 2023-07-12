# Filip Urban
# Jedynym ograniczeniem jest, aby klucz miał wartości jednocyfrowe
# Gdy poda sie nieprawidłowy klucz program się zakończy błędem: ValueError: invalid literal for int() with base 10:

import math
import sys


def encryptCeasar(f, key):
    result = ""
    for i in range(len(f)):
        char = f[i]
        if 'A' <= char <= 'Z':
            result += chr((ord(char) + key - 65) % 26 + 65)
        elif 'a' <= char <= 'z':
            result += chr((ord(char) + key - 97) % 26 + 97)
        else:
            result += " "
    return result


def cryptoAnalysisWithHint(crypto, extra):
    f1 = open("key-found.txt", 'a')
    f2 = open("decrypt.txt", 'a')

    for i in range(26):
        for j in range(len(extra)):
            if encryptCeasar(crypto, 26 - i)[j] == extra[j]:
                f1.write(str(i) + " ")
                f2.write(encryptCeasar(crypto, 26 - i))
                break


def cryptoAnalysisWithoutHint(crypto):
    f1 = open("plain.txt", 'a')
    for i in range(26):
        f1.write(encryptCeasar(crypto, 26 - i))


def encryptAffineCipher(f, a, b):
    result = ""
    for i in range(len(f)):
        char = f[i]
        if 'A' <= char <= 'Z':
            result += chr((a * (ord(char) - 65) + b) % 26 + 65)
        elif 'a' <= char <= 'z':
            result += chr((a * (ord(char) - 97) + b) % 26 + 97)
        else:
            result += " "
    return result


def decryptAffineCipher(f, a, b):
    result = ""
    for i in range(len(f)):
        char = f[i]
        if 'A' <= char <= 'Z':
            result += chr((pow(a, -1, 26) * (ord(char) - 65 - b) % 26) + 65)
        elif 'a' <= char <= 'z':
            result += chr((pow(a, -1, 26) * (ord(char) - 97 - b) % 26) + 97)
        else:
            result += " "
    return result


def cryptoAnalysisWithHintAffineCipher(crypto, extra):
    f1 = open("key-found.txt", 'a')
    f2 = open("decrypt.txt", 'a')

    for a in range(1, 26):
        if math.gcd(a, 26) == 1:
            for b in range(1, 26):
                for j in range(len(extra)):
                    if decryptAffineCipher(crypto, a, b).count(extra) == 1:
                        f1.write(str(a) + " " + str(b))
                        f2.write(decryptAffineCipher(crypto, a, b))
                        sys.exit(0)


def cryptoAnalysisWithoutHintAffineCipher(crypto):
    f1 = open("plain.txt", 'a')

    for a in range(1, 26):
        if math.gcd(a, 26) == 1:
            for b in range(1, 26):
                f1.write(decryptAffineCipher(crypto, a, b))


def main(argv):
    if argv[0] == "-c":  # (szyfr Cezara)
        if argv[1] == "-e":  # (szyfrowanie)
            f1 = open("plain.txt", 'r')
            f2 = open("key.txt", 'r')
            f3 = open("crypto.txt", 'a')
            plain = f1.read()
            key = f2.read()
            f3.write(encryptCeasar(plain, int(key[0])))
        elif argv[1] == "-d":  # (odszyfrowanie)
            f1 = open("decrypt.txt", 'a')
            f2 = open("key.txt", 'r')
            f3 = open("crypto.txt", 'r')
            key = f2.read()
            crypto = f3.read()
            f1.write(encryptCeasar(crypto, 26 - int(key[0])))

        elif argv[1] == "-j":  # (kryptoanaliza z tekstem jawnym)
            f1 = open("crypto.txt", 'r')
            f2 = open("extra.txt", 'r')
            crypto = f1.read()
            extra = f2.read()
            cryptoAnalysisWithHint(crypto, extra)

        elif argv[1] == "-k":  # (kryptoanaliza wyłącznie w oparciu o kryptogram)
            f1 = open("crypto.txt", 'r')
            crypto = f1.read()
            cryptoAnalysisWithoutHint(crypto)

    elif argv[0] == "-a":  # (szyfr afiniczny)
        if argv[1] == "-e":  # (szyfrowanie)
            f1 = open("plain.txt", 'r')
            f2 = open("key.txt", 'r')
            f3 = open("crypto.txt", 'a')
            plain = f1.read()
            key = f2.read()
            f3.write(encryptAffineCipher(plain, int(key[0]), int(key[2])))


        elif argv[1] == "-d":  # (odszyfrowanie)
            f1 = open("decrypt.txt", 'a')
            f2 = open("key.txt", 'r')
            f3 = open("crypto.txt", 'r')
            key = f2.read()
            crypto = f3.read()
            f1.write(decryptAffineCipher(crypto, int(key[0]), int(key[2])))


        elif argv[1] == "-j":  # (kryptoanaliza z tekstem jawnym)
            f1 = open("crypto.txt", 'r')
            f2 = open("extra.txt", 'r')
            crypto = f1.read()
            extra = f2.read()
            cryptoAnalysisWithHintAffineCipher(crypto, extra)

        elif argv[1] == "-k":  # (kryptoanaliza wyłącznie w oparciu o kryptogram)
            f1 = open("crypto.txt", 'r')
            crypto = f1.read()
            cryptoAnalysisWithoutHintAffineCipher(crypto)


if __name__ == "__main__":
    main(sys.argv[1:])
