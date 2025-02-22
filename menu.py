import random

# Fungsi untuk memeriksa kekuatan pahlawan
def periksa_kekuatan(kekuatan):
    if kekuatan > 0:
        return True
    else:
        print("Kekuatanmu habis! Petualanganmu berakhir.")
        return False

# Fungsi untuk melawan musuh
def lawan_musuh(kekuatan, musuh):
    print(f"Kamu menghadapi {musuh}!")
    damage = random.randint(1, 5)
    kekuatan -= damage
    if kekuatan > 0:
        print(f"Kamu berhasil mengalahkan {musuh}, tetapi kehilangan {damage} poin kekuatan.")
    else:
        print(f"Kamu kalah melawan {musuh} dan kehilangan semua kekuatanmu.")
    return kekuatan

# Fungsi untuk mencetak status pahlawan
def cetak_status(nama, kekuatan, emas, daftar_barang):
    print("\n--- Status Pahlawan ---")
    print(f"Nama: {nama}")
    print(f"Kekuatan: {kekuatan}")
    print(f"Emas: {emas}")
    print(f"Barang: {', '.join(daftar_barang) if daftar_barang else 'Tidak ada'}")
    print("-----------------------\n")

# Fungsi utama untuk memulai permainan
def main():
    print("Selamat datang di Petualangan Sang Pahlawan!")
    nama = input("Masukkan nama pahlawanmu: ")
    kekuatan = 10
    emas = 0
    daftar_barang = []

    # Loop utama permainan
    while periksa_kekuatan(kekuatan):
        cetak_status(nama, kekuatan, emas, daftar_barang)
        print("Kamu berada di persimpangan jalan. Pilih arahmu:")
        print("1. Masuk ke hutan")
        print("2. Masuk ke gua gelap")
        print("3. Pergi ke desa")
        print("4. Lihat status")
        print("5. Keluar dari permainan")
        pilihan = input("Apa yang ingin kamu lakukan? (1/2/3/4/5): ")

        if pilihan == "1":
            print("\nKamu memasuki hutan yang gelap dan menyeramkan.")
            musuh = random.choice(["goblin", "serigala", "penyamun"])
            kekuatan = lawan_musuh(kekuatan, musuh)
            if kekuatan > 0:
                emas += random.randint(1, 10)
                print(f"Kamu menemukan {emas} emas di hutan!")
        elif pilihan == "2":
            print("\nKamu memasuki gua gelap yang penuh dengan misteri.")
            musuh = random.choice(["naga kecil", "kelelawar raksasa", "hantu"])
            kekuatan = lawan_musuh(kekuatan, musuh)
            if kekuatan > 0:
                barang = random.choice(["pedang legendaris", "perisai baja", "ramuan penyembuh"])
                daftar_barang.append(barang)
                print(f"Kamu menemukan {barang} di dalam gua!")
        elif pilihan == "3":
            print("\nKamu tiba di desa yang damai.")
            print("1. Beristirahat (mengembalikan kekuatan)")
            print("2. Berbelanja (menggunakan emas)")
            print("3. Kembali ke persimpangan")
            pilihan_desa = input("Apa yang ingin kamu lakukan? (1/2/3): ")
            if pilihan_desa == "1":
                kekuatan += 5
                print("Kamu beristirahat dan memulihkan 5 poin kekuatan.")
            elif pilihan_desa == "2":
                if emas >= 10:
                    emas -= 10
                    daftar_barang.append("ramuan penyembuh")
                    print("Kamu membeli ramuan penyembuh dengan 10 emas.")
                else:
                    print("Kamu tidak memiliki cukup emas untuk berbelanja.")
        elif pilihan == "4":
            continue  # Status sudah dicetak di awal loop
        elif pilihan == "5":
            print("Terima kasih telah bermain Petualangan Sang Pahlawan!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

        # Periksa apakah pahlawan masih memiliki kekuatan
        if not periksa_kekuatan(kekuatan):
            break

    print("Permainan selesai. Sampai jumpa!")

# Jalankan permainan
if __name__ == "__main__":
    main()