import csv

f_name = 'data.csv'
try:
    with open(f_name, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

except FileNotFoundError:
    print("No such file or directory.")

except csv.Error as e:
    print("Cannot parse the csv file!!!", e)