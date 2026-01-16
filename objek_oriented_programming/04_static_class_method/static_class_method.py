class Kapal:
    total = 0

    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga
        Kapal.total += 1

    @staticmethod
    def formatRupiah(nilai):
        return f"Rp {nilai:,}"

    @classmethod
    def jumlahKapal(cls):
        return cls.total


k1 = Kapal("AMN-01", 50000000)
k2 = Kapal("AMN-02", 75000000)

print(Kapal.formatRupiah(1000000))  # static method
print(Kapal.jumlahKapal())          # class method
