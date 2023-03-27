#!/usr/bin/env python3

import math

# Test defined variable
A = [1, 2, 3]
B = [4, 5, 6]

# Input nilai kedua vektor
A = input("Masukkan nilai vektor A (pisahkan dengan spasi): ")
B = input("Masukkan nilai vektor B (pisahkan dengan spasi): ")

# Ubah input str ke list int
A = list(map(int, A.split()))
B = list(map(int, B.split()))

# Hitung dot product A & B
dot_product = sum([A[i]*B[i] for i in range(len(A))])

# Panjang vektor B
magnitude_B = math.sqrt(sum([B[i]**2 for i in range(len(B))]))

# Scalar projection dari vektor A ke vektor B
scalar_projection = dot_product / magnitude_B

# Mencetak hasil scalar projection
print("Scalar projection vector A >> B = ", scalar_projection, "atau", '[',dot_product,"/",int(magnitude_B),']')

