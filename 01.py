talabalar = [
    {"ism": "Alice", "ball": 82},
    {"ism": "Bob", "ball": 68},
    {"ism": "Charlie", "ball": 90},
    {"ism": "David", "ball": 74},
    {"ism": "Eva", "ball": 77}
]

natija = list(filter(lambda talaba: talaba['ball'] >= 75, talabalar))

print(natija)
