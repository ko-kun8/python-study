import csv

with open("data.csv","r",encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

with open("output.csv","w",encoding="utf-8",newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["名前","年齢","都市"])
    writer.writerow(["三郎","28","福岡"])
    writer.writerow(["四郎","35","札幌"])