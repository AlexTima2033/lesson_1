import csv

with open('metods.csv', 'w', newline='', encoding='utf-8-sig') as csvfiless:
    writer = csv.writer(csvfiless)
    data = [
        ["NAME", "AGE", "CITY"],
        ["Alex", 27, "Moscow"],
        ["Bob", 21, "Tokyo"],
        ["Cath", 20, "Paris"]
    ]
    writer.writerows(data)

with open('metods.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)