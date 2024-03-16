meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "SHEESH": "ungkapan ketidaksetujuan"
            }
# print(meme_dict)

word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")
# print("kata anda ketik adalah ",word)

# print(meme_dict.keys())
if word in meme_dict.keys():
    print("kata yang anda ketikan adalah: ", word)
    print("arti dari kata anda adalah", meme_dict[word])
else:
    print("kata tidak ditemukan")

# struktur dictionary
# key: value
