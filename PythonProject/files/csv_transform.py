import csv

def transform_user_details():
    extracted_details = []
    with open("user_details.csv", newline="") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for row in csv_reader:
            user = []
            user.append(row[1])
            user.append(row[2])
            user.append(row[4])
            extracted_details.append(user)
    return extracted_details

print(transform_user_details())