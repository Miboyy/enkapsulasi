class Mobil:
    def __init__(self, merek, model, tahun):
        
        self.__merek = merek
        self.__model = model
        self.__tahun = tahun
        self.__kecepatan = 0
        self.__mesin_hidup = False
    

    def get_merek(self):
        return self.__merek
    
    def set_merek(self, merek_baru):
        self.__merek = merek_baru
    
    def hidupkan_mesin(self):
        if not self.__mesin_hidup:
            self.__mesin_hidup = True
            return "Mesin mobil dihidupkan"
        return "Mesin sudah dalam keadaan hidup"
    
    def matikan_mesin(self):
        if self.__mesin_hidup:
            if self.__kecepatan == 0:
                self.__mesin_hidup = False
                return "Mesin mobil dimatikan"
            return "Kurangi kecepatan sampai 0 dulu sebelum mematikan mesin"
        return "Mesin sudah dalam keadaan mati"
    
    def tambah_kecepatan(self, nilai):
        if self.__mesin_hidup:
            if nilai > 0:
                self.__kecepatan += nilai
                return f"Kecepatan sekarang: {self.__kecepatan} km/jam"
            return "Nilai penambahan kecepatan harus positif"
        return "Hidupkan mesin terlebih dahulu"
    
    def kurangi_kecepatan(self, nilai):
        if self.__mesin_hidup:
            if nilai > 0:
                if (self.__kecepatan - nilai) >= 0:
                    self.__kecepatan -= nilai
                    return f"Kecepatan sekarang: {self.__kecepatan} km/jam"
                return "Kecepatan tidak bisa kurang dari 0"
            return "Nilai pengurangan kecepatan harus positif"
        return "Hidupkan mesin terlebih dahulu"
    
    def info_mobil(self):
        status_mesin = "hidup" if self.__mesin_hidup else "mati"
        return f"""
        Informasi Mobil:
        Merek: {self.__merek}
        Model: {self.__model}
        Tahun: {self.__tahun}
        Status Mesin: {status_mesin}
        Kecepatan: {self.__kecepatan} km/jam
        """