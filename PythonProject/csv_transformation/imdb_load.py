import csv

from imdb_transform import transform_imdb_titles

def load_transformed_titles(old_file, new_file):
    transformed_titles = transform_imdb_titles()
    with open(new_file, "w", newline = "") as transformed_file:
        csv_writer = csv.writer(transformed_file)
        csv_writer.writerow(["primaryTitle", "startYear", "runtimeMinutes", "genres"])
        csv_writer.writerows(transformed_titles)

load_transformed_titles("imdbtitles.csv", "imdbtitles_transformed.csv")