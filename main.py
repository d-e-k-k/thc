from csv_summarizer import CSVSummarizer

csv_summarizer = CSVSummarizer(r'data.csv')

print(csv_summarizer.header)
print(csv_summarizer.data[0])

# import csv

# path = r'data.csv'

# file_handler = open(path, newline='')
# reader = csv.reader(file_handler)

# headers = next(reader)


# number_of_columns = len(headers)

# print(number_of_columns)

# def get_csv_attributes()
#     pass

