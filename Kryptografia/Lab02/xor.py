# Filip Urban
import string
import sys


def main(argv):
    if argv[0] == "-p":
        f1 = open("orig.txt", "r")
        orig = f1.read().replace('\n', '').translate(str.maketrans('', '', string.punctuation)).lower()
        x = 32
        f2 = open("plain.txt", "w")
        for i in range(0, len(orig), x):
            f2.write(orig[i:i + x])
            i += x
            if i >= len(orig):
                f2.write(" " * (i - len(orig)))
                break
            f2.write('\n')
        f1.close()
        f2.close()

    if argv[0] == "-e":
        f1 = open("plain.txt", "r")
        f2 = open("key.txt", "r")
        f3 = open("crypto.txt", "w")
        plain = f1.read().replace('\n', '')
        key = f2.read().replace('\n', '')

        plainlist = [*plain]
        keylist = [*key]

        encrypted = []
        for i in range(len(plainlist)):
            encrypted.append(chr(ord(plainlist[i]) ^ ord(keylist[i % 32])))
            f3.write(chr(ord(encrypted[i])))

        f1.close()
        f2.close()
        f3.close()

    if argv[0] == "-k":
        f1 = open("crypto.txt", "r")
        f2 = open("decrypt.txt", "w")
        crypto = f1.read()
        ans = ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#",
               "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]

        for i in range(len(crypto)):
            if crypto[i].isalpha():
                tmp = chr(ord(crypto[i]) ^ 32)
                ans[i % 32] = tmp

        decrypted = []
        for i in range(len(crypto)):
            decrypted.append(chr(ord(crypto[i]) ^ ord(ans[i % 32])))
            f2.write(chr(ord(decrypted[i])))

        f1.close()
        f2.close()


if __name__ == "__main__":
    main(sys.argv[1:])
