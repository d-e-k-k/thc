from csv_summarizer import CSVSummarizer, NumericSummary, Column
import json
# csv_summarizer = CSVSummarizer(r'data.csv')

# for column in csv_summarizer.columns_dict.keys():
#     print(column, csv_summarizer.columns_dict[column]["data"][0])
# csv_summarizer.print_column_summaries()
# print(csv_summarizer.header)
# print(csv_summarizer.columns_data[0])
# c1_summary = NumericSummary([float(i) for i in csv_summarizer.columns_data[0]])
# print(json.dumps(c1_summary.get_summary()))

column = Column('widths', ["1", "2", "3", "cat"])
print(column.name)
print(column.type)
print(column.data)