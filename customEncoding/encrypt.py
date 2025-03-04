def e1(t, b, o):
    t1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    if len(b) != 168:
        raise ValueError("Invalid Input")
    c = [b[i:i+4] for i in range(0, len(b), 4)]
    with open(o, "w") as f:
        for x, y in enumerate(t):
            z = f"{ord(y):08b}"
            if x < 42:
                a = z[:6]           
                d = z[6:] + c[x]
                e = int(a, 2)
                g = int(d, 2)
                r = t1[e] + t1[g]
            else:
                a = z[:6]
                d = z[6:]
                e = int(a, 2)
                g = int(d, 2)
                r = t1[e] + t1[g]
            print(r)
            f.write(r + "\n")

t = "I TOLD YOU THAT BASE64 DECODING IS NO GOOD"
alphabet = "abcdefghijklmnopqrstuvwxyz"
repeated_string = (alphabet * ((168 // len(alphabet)) + 1))[:168]
o = "outputTest.txt"

e1(t, repeated_string, o)

'''
t1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
t = "I TOLD YOU THAT BASE64 DECODING IS NO GOOD"

with open ('output.txt', 'r') as file:
    lines = file.readlines()

lines = [line.strip() for line in lines]

print(lines)
c = ""

for x, y in enumerate(t):
    r = lines[x]
    z = f"{ord(y):08b}"

    if x < 42:
        g = t1.index(r[1])
        print(f"g: {g}")
        d = bin(g)
        print(f"d: {d}")
        add = z[6:].lstrip('0')
        print(f"add: {add}")
        d = d[len(add) + 2:]
        print(f"d: {d}")
        
        c += chr(int(d, 2))

print(c)
'''
