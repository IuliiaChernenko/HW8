# объявление функции
def convert_to_miles(km):
    km = float(km)
    return km * 0.6214

# считываем данные
num = input('enter: ')

# вызываем функцию
print(convert_to_miles(num))