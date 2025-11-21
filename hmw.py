# 1.

import os

s = input("Fayl nomi: ")

if not os.path.exists(s):
    open(s, "w").close()
    print("TRUE")
else:
    print("FALSE")

# 2.

filename = input("Fayl nomi: ")
N = int(input("N: "))

with open(filename, "w") as f:
    for i in range(1, N + 1):
        f.write(str(i * 2) + "\n")

# 3.

filename = input("Fayl nomi: ")
A = float(input("A: "))
D = float(input("D: "))

with open(filename, "w") as f:
    for i in range(10):
        f.write(str(A + i * D) + "\n")
