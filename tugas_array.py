array1 = [1,2,3,4,5,6]
array2 = [7,8,9,10,11]
hasil = []
panjang = len(array1) if len(array1) > len(array2) else len(array2)
print(panjang)
            
for i in range (panjang):
    if i < len(array1) and i < len(array2):
        hasil.append(array1[i]+array2[i])
    elif i < len(array1):
        hasil.append(array1[i])
    else:
        hasil.append(array[i])
        # a = array1[i] if i < len(array1) else 0
        # b = array2[i] if i < len(array2) else 0
        # hasil.append(a+b)

print(hasil)

