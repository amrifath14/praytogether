class PencariNilaiMax:
    def cari(self, daftar_bilangan):
        if not daftar_bilangan:
            raise ValueError("Daftar bilangan tidak boleh kosong")
        
        nilai_max = daftar_bilangan[0]
        for bilangan in daftar_bilangan[1:]:
            if bilangan > nilai_max:
                nilai_max = bilangan
        return nilai_max


nilaiMax = PencariNilaiMax()
print(nilaiMax.cari([1, 4, 6, 10, 0, 2, 30]))  
