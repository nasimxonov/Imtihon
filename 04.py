class Employee:
    def __init__(self, surname, position, salary):
        self.surname = surname
        self.position = position
        self.salary = salary


class Enterprise_employee(Employee):
    def __init__(self, surname, position, salary, rating):
        super().__init__(surname, position, salary)
        self.rating = rating

    def oshirish(self):
        if 60 <= self.rating < 75:
            self.salary *= 1.2
        elif 75 <= self.rating < 90:
            self.salary *= 1.4
        elif 90 <= self.rating <= 100:
            self.salary *= 1.6

    def __str__(self):
        return f"Familiya: {self.surname}, Lavozim: {self.position}, Oylik: {self.salary}, Reyting: {self.rating}"


ishchilar = [
    Enterprise_employee("Karimov", "Dasturchi", 5000, 65),
    Enterprise_employee("Aliyev", "Boshqaruvchi", 7000, 80),
    Enterprise_employee("Tursunov", "Muhandis", 4500, 55),
    Enterprise_employee("Sodiqov", "Iqtisodchi", 6000, 92),
    Enterprise_employee("Yusupov", "Analitik", 5200, 88),
]

for ishchi in ishchilar:
    ishchi.oshirish()

for ishchi in ishchilar:
    print(ishchi)
