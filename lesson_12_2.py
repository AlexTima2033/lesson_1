import csv
with open('data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["FIO", "AGE"])
    writer.writerow(["Lysenko Maria Vladimirovna", 28])
    writer.writerow(["Timofeeva Alexsandra Vladimirovna", 22])
    writer.writerow(["Gubatenko Alexsandr Alexsandrovich", 27])
with open('data.csv', 'a', newline='') as csv_f:
    writers = csv.writer(csv_f)
    writers.writerow(["Mironova Katya Borisovna", 20])
    writers.writerow(["Scvortsova Elena Victorovna", 21])

with open('data.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)