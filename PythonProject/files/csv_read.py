import csv

with open("user_details.csv", newline = "") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
    for row in csv_reader:
        print(row)