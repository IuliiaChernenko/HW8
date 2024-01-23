# объявление функции
def convert_to_miles(km):
    km = float(km)
    return km * 0.6214 + 10

# считываем данные
num = 28

# вызываем функцию
print(convert_to_miles(num))
