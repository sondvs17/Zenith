Barang Jualan = {
     "Dress wanita" : 150000,
    "Celana Kulot"  : 850000,
    "Celana jeans"  : 210000,
    "Kemeja wanita" : 142000,
    "blazer wanita" : 130000
    }
Print("===================== Daftar Harga =====================") 
for i in menu:
    Print("Daftar Menu : ", i,"\t Harga : ",menu[i])
    Print("Pembelian diatas Rp100.000,- mendapatkan diskon 15%")
    Print("===================================================")
    Beli = Input ("Pilih Menu : ") 
    Jumlah = int(Input ("Jumlah pesanan : "))
    Bayar = jumlah * menu[beli]