# Filip Urban
import sys
import random


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def generate_keypair(p, g):
    secret = random.randrange(2, p)
    public = pow(g, secret, p)
    return public, secret


def elgamal_encrypt(p, g, public, plaintext):
    if plaintext >= p:
        raise Exception(plaintext + "is bigger than" + p)
    k = random.randrange(2, p)
    a = pow(g, k, p)
    b = (pow(public, k, p) * plaintext) % p
    return a, b


def elgamal_decrypt(p, secret, a, b):
    x = pow(a, p - 1 - secret, p)
    plaintext = (b * x) % p
    return plaintext


def elgamal_sign(p, g, secret, plaintext):
    k = random.randrange(2, p)
    r = pow(g, k, p)
    s = ((plaintext - (secret * r)) * pow(k, -1, p - 1))
    return r, s


def elgamal_verify(p, g, public, plaintext, signature):
    r, s = signature
    x1 = pow(g, plaintext, p)
    x2 = (pow(r, s, p) * pow(public, r, p)) % p
    return x1 == x2


def main():
    if len(sys.argv) != 2:
        print("Usage: python elgamal.py -k|-e|-d|-s|-v")
        sys.exit(1)
    if sys.argv[1] == '-k':
        with open('elgamal.txt', 'r') as f:
            p = int(f.readline().strip('\n'))
            g = int(f.readline().strip('\n'))
        public, secret = generate_keypair(p, g)
        with open('public.txt', 'w') as f:
            f.write(str(p) + '\n')
            f.write(str(g) + '\n')
            f.write(str(public) + '\n')
        with open('private.txt', 'w') as f:
            f.write(str(p) + '\n')
            f.write(str(g) + '\n')
            f.write(str(secret) + '\n')

    elif sys.argv[1] == '-e':
        with open('public.txt', 'r') as f:
            p = int(f.readline())
            g = int(f.readline())
            public = int(f.readline())
        with open('plain.txt', 'r') as f:
            plaintext = int(f.readline())
        a, b = elgamal_encrypt(p, g, public, plaintext)
        with open('crypto.txt', 'w') as f:
            f.write(str(a) + '\n')
            f.write(str(b) + '\n')

    elif sys.argv[1] == '-d':
        with open('private.txt', 'r') as f:
            p = int(f.readline())
            g = int(f.readline())
            secret = int(f.readline())
        with open('crypto.txt', 'r') as f:
            a = int(f.readline())
            b = int(f.readline())
        plaintext = elgamal_decrypt(p, secret, a, b)
        with open('decrypt.txt', 'w') as f:
            f.write(str(plaintext) + '\n')

    elif sys.argv[1] == '-s':
        with open('private.txt', 'r') as f:
            p = int(f.readline())
            g = int(f.readline())
            secret = int(f.readline())
        with open('plain.txt', 'r') as f:
            plaintext = int(f.readline())
        r, s = elgamal_sign(p, g, secret, plaintext)
        with open('signature.txt', 'w') as f:
            f.write(str(r) + '\n')
            f.write(str(s) + '\n')

    elif sys.argv[1] == '-v':
        with open('public.txt', 'r') as f:
            p = int(f.readline())
            g = int(f.readline())
            public = int(f.readline())
        with open('plain.txt', 'r') as f:
            plaintext = int(f.readline())
        with open('signature.txt', 'r') as f:
            r = int(f.readline())
            s = int(f.readline())
        signature = (r, s)
        if elgamal_verify(p, g, public, plaintext, signature):
            print("The signature is valid.")
        else:
            print("The signature is invalid.")


if __name__ == '__main__':
    main()
