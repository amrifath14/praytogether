array1 = [1,2,3,4,5,6]
array2 = [7,8,9,10,11,12]
array3 = [1,1,1,1,1,1]
hasil = []

            
for i in range (len(array1)):
        hasil.append(array1[i] + array2[i] + array3[i])
    
print(hasil)