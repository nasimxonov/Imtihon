def kino_daromadlari(data):
    daromadlar = {}
    for film, info in data.items():
        daromad = info["sotilgan_chiptalar"] * info["chipta_narxi"]
        daromadlar[film] = daromad
    return daromadlar


data = {
    "Avatar": {"sotilgan_chiptalar": 150, "chipta_narxi": 10},
    "Titanic": {"sotilgan_chiptalar": 200, "chipta_narxi": 8},
    "Avengers: Endgame": {"sotilgan_chiptalar": 300, "chipta_narxi": 12},
    "The Lion King": {"sotilgan_chiptalar": 180, "chipta_narxi": 9},
    "Frozen": {"sotilgan_chiptalar": 250, "chipta_narxi": 7},
    "Joker": {"sotilgan_chiptalar": 220, "chipta_narxi": 11},
    "Black Panther": {"sotilgan_chiptalar": 270, "chipta_narxi": 9},
    "Star Wars: The Force Awakens": {"sotilgan_chiptalar": 290, "chipta_narxi": 10},
    "Avengers: Infinity War": {"sotilgan_chiptalar": 310, "chipta_narxi": 11},
    "Inception": {"sotilgan_chiptalar": 160, "chipta_narxi": 8},
    "Spider-Man: No Way Home": {"sotilgan_chiptalar": 240, "chipta_narxi": 12},
    "Jurassic World": {"sotilgan_chiptalar": 200, "chipta_narxi": 9},
    "The Dark Knight": {"sotilgan_chiptalar": 210, "chipta_narxi": 10},
    "Harry Potter and the Sorcerer's Stone": {"sotilgan_chiptalar": 230, "chipta_narxi": 8},
    "The Matrix": {"sotilgan_chiptalar": 170, "chipta_narxi": 9},
    "Pirates of the Caribbean": {"sotilgan_chiptalar": 190, "chipta_narxi": 8},
    "Finding Nemo": {"sotilgan_chiptalar": 200, "chipta_narxi": 7},
    "Shrek 2": {"sotilgan_chiptalar": 180, "chipta_narxi": 8},
    "Transformers": {"sotilgan_chiptalar": 160, "chipta_narxi": 10},
    "Iron Man": {"sotilgan_chiptalar": 210, "chipta_narxi": 9},
}

natija = kino_daromadlari(data)

print(natija)
