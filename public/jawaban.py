#mengurutkan kata sesuai urutan
kata = input("Masukkan kata (gunakan spasi untuk memisahkan): ")
daftar_kata = kata.split()  
daftar_kata.sort()  
urutan_kata = ' '.join(daftar_kata)  
print("Urutan kata sesuai abjad:", urutan_kata)

# input digunakan untuk meminta data dari pengguna untuk mengurutkan suatu kata
#split() digunakan untuk memisahkan kata dengan spasi hingga menjadi list kata
# sort() digunakan untuk mengurutkan kata menggunakan method sort()
#join() yaitu menggabungkan semua kata yang sudah di urutkan
#print() untuk mencetak output atau hasil
