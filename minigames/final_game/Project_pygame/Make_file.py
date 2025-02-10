import csv

with open('dictwriter.csv', 'w', newline='', encoding="utf8") as f:
    writer = csv.writer(
        f, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['Результаты гонки'])