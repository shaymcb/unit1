#Shaylee McBride
#24Jan2018
#reverseBinary.py - enter base 10 and convert to binary

base10 = int(input('Enter a base-10 number less than 256: '))
b128 = base10//128
base10 = base10 - b128 * 128
b64 = base10//64
base10 = base10 - b64 * 64
b32 = base10//32
base10 = base10 - b32 * 32
b16 = base10//16
base10 = base10 - b16 * 16
b8 = base10//8
base10 = base10 - b8 * 8
b4 = base10//4
base10 = base10 - b4 * 4
b2 = base10//2
b1 = base10 - b2 * 2
binary = b128*10**7+b64*10**6+b32*10**5+b16*10**4+b8*10**3+b4*10**2+b2*10+b1
print(binary)
