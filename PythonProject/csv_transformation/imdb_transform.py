import csv

def transform_imdb_titles():
    transformed_titles = []
    with open('imdbtitles.csv', newline = "", encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = "\t")
        next(csv_reader)
        for row in csv_reader:
            if int(row[4]) >= 2010 and row[0] == "movie":
                movie = []
                movie.append(row[1])
                movie.append(row[4])
                movie.append(row[6])
                movie.append(row[7])
                transformed_titles.append(movie)
    return transformed_titles

print(transform_imdb_titles())