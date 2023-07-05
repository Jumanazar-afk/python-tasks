class People():
    def __init__(self, NSF, born, phone, city, country, adress):
        self.NSF = NSF
        self.born = born
        self.phone = phone
        self.city = city
        self.country = country
        self.adress = adress

    def nsf(self):
        return self.NSF()

    def born(self):
        return self.born()

    def phone(self):
        return self.phone()

    def city(self):
        return self.city()

    def country(self):
        return self.country()

    def adress(self):
        return self.adress()


p1 = People(input("Enter your name:"), input("Your B-Day:"), input("Your phone number:"), input("Your city:"), input("Your country:"), input("Your adress:"))
print(p1.NSF,",", p1.born, ",", p1.phone,",", p1.city,",", p1.country,",", p1.adress)
