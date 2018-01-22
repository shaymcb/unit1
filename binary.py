#Shaylee McBride
#22Jan2018
#binary.py - converts binary to base-10

binary = int(input("Input an 8-digit binary number: "))
b128 = binary//10000000
binary = binary - b128 * 10000000
b64 = binary//1000000
binary = binary - b64 * 1000000
b32 = binary//100000
binary = binary - b32 * 100000
b16 = binary//10000
binary = binary - b16 * 10000
b8 = binary//1000
binary = binary - b8 * 1000
b4 = binary//100
binary = binary - b4 * 100
b2 = binary//10
b1 = binary - b2 * 10
base10 = b128*128+b64*64+b32*32+b16*16+b8*8+b4*4+b2*2+b1
print(base10)