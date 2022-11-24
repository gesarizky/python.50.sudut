# Author  : Gesa Rizky Nugraha
# Email   : gesarizkynugraha@gmail.com
# Website : karenabelajar.blogspot.com

# Menginput
print('Isi nilai-nilai Dengan Benar ')
a = int(input("Masukan Nilai Sudut  : "))

# Menampilkan Hasil
print('================================================================================')
if(a==90):
   print('Maka Sudut ',a,' Derajat Adalah Sudut Siku-siku')
elif(a < 90 and a < 180):
   print('Maka Sudut ',a,' Derajat Adalah Sudut Lancip')
elif(a == 180):
   print('Maka Sudut ',a,' Derajat Adalah Sudut Lurus')   
elif(a > 180 and a < 360):
   print('Maka Sudut ',a,' Derajat Adalah Sudut Refleks')
elif(a == 360):
   print('Maka Sudut ',a,' Derajat Adalah Putaran Penuh')   
else:
   print('Nilai yang anda Masukan Salah, masukan nilai 0 ~ 360')
print('================================================================================')
