# POLYMORPHISM

class film(object):
    def __init__(self, judul, genre, tahun):
        self.judul = judul
        self.genre = genre
        self.tahun = tahun
    
    def watching(self, durasi):
        for i in range(durasi):
            print("sedang menonton..")
            
    def info(self):
        print(f"Judul film: {self.judul}\nGenre: {self.genre}\nTahun rilis: {self.tahun}")

        
class favorite(film):
    def __init__(self, judul, genre, tahun, warna, bahasa):
        super().__init__(judul, genre, tahun)
        self.judul = judul
        
    def doing(self, durasi):
        for i in range(durasi):
            print("watching the movie..")
            
        
