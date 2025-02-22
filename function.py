# for x in range(1, 105, 1):
#     if x % 2 != 0: # pakai modulus
#         print(x)

# for x in range(1, 10, 1):
#     if x % 2 != 0: # pakai modulus
#         print(x)

# for x in range(1, 55, 1):
#     if x % 2 != 0: # pakai modulus
#         print(x)

# for x in range(1, 15, 1):
#     if x % 2 != 0: # pakai modulus
#         print(x)

# for x in range(1, 1005, 1):
#     if x % 2 != 0: # pakai modulus
#         print(x)

# rewrite redundant code -> minimalisir redundant code
# KISS -> keep it simple, stupid!
# DRY -> don't repeat yourself

def cetak_bilangan_prima(n):
    for x in range(1, n, 1):
        if x % 2 != 0: # pakai modulus
            print(x)

# invoke -> atau memanggil
# i = 1
# for x in range(1, 51, 5):
#     cetak_bilangan_prima(10)
#     i += 1

# iterasi ke 1: x = 1
# iterasi ke 2: x = 1 + 5 -> 6
# iterasi ke 3: x = 6 + 5 -> 11

# 0 1 1 2 3 5 8
# tebak deret fibonacci

# Fn = Fn-1 + Fn-2
# method 1: recursion.
# negasi dari lebih besar dari -> kurang dari sama dengan
# n > 1 ----> n <= 1
def fibo(n):
    if n <= 1: # base case
        return 1 # nilai default dari bilangan fibo
    else:
        return fibo(n - 1) + fibo(n - 2)
# print("nilai fibo", fibo(100)) # proses 2^100

# factorial
# factorial(n) -> n . n - 1

# analisa time complexity dari fungsi yang dibuat
# a = 5
# b = 4
# print(a + b)


# factorial.
# define: perkalian dari n sampai ke 1.
# example: 3! = 3 x 2 x 1 = 6
# formula: n! = n x (n - 1) ... x 1
# boundary: bilangan bulat, dan endingnya selalu 1.
def factorial(n):
    if n == 1: # base case
        return 1

    return n * factorial(n - 1)

# print(factorial(10))

# n = 1000
# r = 1
# for x in range(n, 0, -1):
#     r = r * x

# print(r)

# hero story
nama = "hanif swordian"
nyawa = 10
poin = 0
jumlah_emas = 0

def main_game():
    while nyawa > 0:
        input_pilihan_pemain = input("masukan pilihan: ")

        match input_pilihan_pemain:
            case "farming":
                nyawa = nyawa - 1 # decrement 1
                jumlah_emas = jumlah_emas + 1
                print("FARMING MODE")
            case "istirahat":
                if poin < 1:                
                    break
                nyawa = 10
                poin = poin - 1
                print("REHAT MODE")
            case "jual":
                jumlah_emas = jumlah_emas - 1
                poin = poin + 1
                print("TRADE MODE")

        # if input_pilihan_pemain == "farming":
        #     nyawa = nyawa - 1 # decrement 1
        #     jumlah_emas = jumlah_emas + 1
        #     print("FARMING MODE")
        # elif input_pilihan_pemain == "istirahat":
        #     nyawa = 10
        #     poin = poin - 1
        #     print("REHAT MODE")        
        # elif input_pilihan_pemain == "jual":
        #     jumlah_emas = jumlah_emas - 1
        #     poin = poin + 1
        #     print("TRADE MODE")

        print("pilihan anda " + input_pilihan_pemain)
        print(f"poin anda saat ini {poin}")
        print(f"jumlah emas anda saat ini {jumlah_emas}")
        print(f"nyawa saat ini {nyawa}")

# tipe data
data = True
dataNegasi = not data

def cek_angka_lebih_besar_dari_5(n):
    if n > 5:
        return True
    else:
        return False
    
print(cek_angka_lebih_besar_dari_5(3))

# data structure -> array
data = 10
kumpulan_data1 = [10, 20, 30, 40, 50, 60, 100]
kumpulan_dataStr = ["abdul", "hanif"]
kumpulan_data2 = [1, 2, 3, 4]
# elemen -> nilai sesungguhnya
# index -> lokasi dari element dimulai dari 0
index = 0
# for i in kumpulan_data1:
#     print(f"angka {i}, index {index}")
#     # kumpulan_data1[index] = kumpulan_data1[index] + 10
#     index = index + 1

for i in kumpulan_dataStr:
    print(i + " salam")
# print(kumpulan_data1)

# array1: [1,2,3,4,5,6]
# array2: [3,4,5,6,7,8]

# result: 
# [4,6,8,10,12,14]