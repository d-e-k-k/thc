from csv_summarizer import CSVSummarizer, NumericSummary
import json
csv_summarizer = CSVSummarizer(r'data.csv')

print(csv_summarizer.header)
print(csv_summarizer.columns_data[0])
c1_summary = NumericSummary([float(i) for i in csv_summarizer.columns_data[0]])
print(json.dumps(c1_summary.get_summary()))
