# 1. Определить количество городов в файле.
# 2. Создать словарь, где ключ — это код страны, а значение — количество
# городов.
# 3. Подсчитать количество городов в северном полушарии и в южном.
# 4. Перевести в CSV файл данные по городам (координаты представить в виде
# строки значений через запятую).
# 5. Создать другой JSON файл, в который сохранить только города одной
# выбранной страны.
# 6. * Для каждой страны создать свой файл JSON с данными городов. Лучше
# создать отдельную папку в PyCharm, и указать путь к новому файлу с этой
# папкой.

import json
import csv
import os

# Загрузка JSON-файла
with open('city.list.json', encoding='utf-8') as f:
    cities = json.load(f)

# количество уникальных городов
unique_cities = {city["name"] for city in cities}
print("Количество уникальных городов:", len(unique_cities))

# словарь, где ключ - код страны, значение - количество городов
country_city_count = {}
for city in cities:
    country = city['country']
    country_city_count[country] = country_city_count.get(country, 0) + 1

print(country_city_count)

# количество городов в северном полушарии и в южном
north = sum(1 for city in cities if city['coord']['lat'] > 0)
south = len(cities) - north
print("кол-во городов в северном полушарии:", north)
print("кол-во городов в южном полушарии:", south)

# перевод в файл csv (уникальные) данные по городам, где координаты в виде строки через запятую
csv_filename = "cities.csv"
with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['name', 'coord'])

    seen_names = set()
    for city in cities:
        name = city['name']
        lat = city['coord']['lat']
        lon = city['coord']['lon']

        if name not in seen_names:
            seen_names.add(name)
            coord_str = f"{lat},{lon}"
            writer.writerow([name, coord_str])

    print("названия и координаты городов записаны в файл: ", csv_filename)


# JSON файл, в который сохранить только города одной выбранной страны

chosen_country = input("Введите код страны (например, UA): ").strip().upper()

filtered = [city for city in cities if city["country"] == chosen_country]

if not filtered:
    print(f"Страна с кодом \"{chosen_country}\" не найдена в файле.")
else:
    filename = f"cities_{chosen_country}.json"
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(filtered, f, ensure_ascii=False, indent=2)
    print(f"Города из {chosen_country} записаны в файл {filename}")


# Для каждой страны создать свой файл JSON с данными городов
# (будет отдельная папка с файлами)

# создание папки
output_dir = "country_jsons"
os.makedirs(output_dir, exist_ok=True)
print(f"Создана папка {output_dir}, где будут файлы с городами для каждой страны.")

# группировка городов по странам
by_country = {}
for city in cities:
    country = city['country']
    if country not in by_country:
        by_country[country] = []
    by_country[country].append(city)

# запись городов файлы-страны
for country_code, country_cities in by_country.items():
    filename = os.path.join(output_dir, f"{country_code}.json")
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(country_cities, f, ensure_ascii=False, indent=2)

