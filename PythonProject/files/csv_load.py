import csv

from csv_transform import transform_user_details

def load_transformed_details(old_file_name, new_file_name):
    transformed_user_details = transform_user_details()
    with open(new_file_name, "w", newline = "") as new_file:
        csv_writer = csv.writer(new_file)
        csv_writer.writerows(transformed_user_details)

load_transformed_details("user_details.csv", "new_user_details.csv")