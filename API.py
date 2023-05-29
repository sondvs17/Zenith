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

    if bayar > 100000:
        diskon = bayar*15/100
        total = bayar - diskon
   else:
    total = bayar   
    print("--------------> Detail Pembayaran <---------------")
    print("Barang yang di pesan             : ",beli)
    print("Jumlah Barang yang di pesan      : ",jumlah)
    print("Total Biaya                      : ",bayar)
    print("Total yang harus di bayar        : ",total)