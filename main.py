class Task2():
    def __init__(self, city, country, region, resident, city_index, phone_code):
        self.city =city
        self.country =country
        self.region = region
        self.resident = resident
        self.city_index = city_index
        self.phone_code = phone_code

a = Task2(input("City name:"), input("Your Country :"), input("Your region"), input("count resident"), input("city index:"), input("city phone code:"))
print("Your city:", a.city, ",", "your country:", a.country, ",", "your region:", a.region, ",", "your city residents:",
      a.resident, ",", "your city index:", a.city_index, ",", "your city phone code:", a.phone_code)
