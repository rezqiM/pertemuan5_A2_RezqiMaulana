# latihan 1
x = 1
y = 10
for i in range (10):
    print(x, end=" ")
    print(y, end=" ")
    x+=1
    y-=1
print()



#latihan 2
awal = int(input("Masukan saldo awal = "))
sisa = awal #bila tidak ada pengeluaran
while (True):
    pengeluaran = int(input("Masukan pengeluaran hari ini (-1 untuk keluar): "))
    if pengeluaran ==-1: #untuk berhenti
        print("Sisa saldo = ", sisa) #sisa bila di berhentikan
        break
    sisa = sisa - pengeluaran
    if sisa <0:
        print("Saldo tidak cukup")
        print('Sisa saldo', sisa+pengeluaran)
        break



#latihan 3
for i in range (1,11):
    print(f'7 * {i} = {7*i}')



#latihan 4
list_nilai = []
n = int(input('n = ')) #menentukan banyak data yang akan dimasukkan

for i in range (1, n+1):
    nilai = int(input("nilai = "))
    list_nilai.append(nilai)#menambah setiap nilai untuk dimasukkan ke dalam list

print(list_nilai)
jumlah = sum(list_nilai)
avr = jumlah // n
print("avr = ", avr)



#latihan 5
var_nilai = 0
var_i = 1
for var_nilai in range (0,10) :
    print("Perulangan pertama Ke ",var_nilai)
    for var_i in range (1,3) :
        print(" Perulangan ke ", var_nilai,", ",var_i)
#diluar perulangan var_i
    var_i = 1
#diluar_perulangan var_nilai
print("var_nilai = ",int(var_nilai)+1," = 10. Bernilai False")



#latihan 6
var_nilai = 0
var_i = 1
#Perulangan WHILE
while (var_nilai < 10) :
    print("Perulangan pertama Ke ",var_nilai)
    while(var_i < 3) :
        print(" Perulangan ke ", var_nilai,", ",var_i)
        var_i +=1
 #diluar perulangan var_i
    var_i = 1
    var_nilai +=1
#diluar_perulangan var_nilai
print("var_nilai = ",int(var_nilai)," = 10. Bernilai False")



#latihan 7
var_nilai = 0
var_i = 1
#Perulangan FOR
for var_nilai in range (0,10) :
    print("Perulangan pertama Ke ",var_nilai)
    while(var_i < 3) :
        print(" Perulangan ke ", var_nilai,", ",var_i)
        var_i +=1
 #diluar perulangan var_i
    var_i = 1
#diluar_perulangan var_nilai
print("var_nilai = ",int(var_nilai)+1," = 10. Bernilai False")