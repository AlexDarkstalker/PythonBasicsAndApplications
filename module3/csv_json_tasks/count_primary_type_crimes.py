import csv

with open("Crimes.csv") as table:
    reader = csv.reader(table)
    max_count = 0
    max_reason = ""
    reason_count = {}
    for row in reader:
        if row[2].__contains__("2015"):
            if row[5] in reason_count.keys():
                reason_count[row[5]] += 1
                if reason_count[row[5]] > max_count:
                    max_count = reason_count[row[5]]
                    max_reason = row[5]
            else:
                reason_count[row[5]] = 1
table.close()
print(max_reason)
