import unittest
from io import StringIO
from csv_summarizer import CSVSummarizer, NumericSummary, TextSummary

in_mem_csv = StringIO("""\
"sepal.length","sepal.width","petal.length","petal.width","variety"
5.1,3.5,1.4,.2,"Setosa"
4.9,3,1.4,.2,"Setosa"
4.7,3.2,1.3,.2,"Setosa"
4.6,3.1,1.5,.2,"Setosa""")


class TestCSVSummarier(unittest.TestCase):
    # def test_csv_sammarizer_calculate_statistics(self):
    #     csv_summarizer = CSVSummarizer(r'test_data.csv')
    #     self.assertEqual(csv_summarizer.calculate_statistics(), {"Mean": 3.0, "Median": 1.25, "Mode": 1.0})

    
    # def test_calculate_mode(self):
    #     self.assertEqual(CSVSummarizer.calculate_modes([1,2.0,3,3]), [3.0])
    #     self.assertEqual(CSVSummarizer.calculate_modes([1,2.0,-3,-3]), [-3.0])
    #     self.assertEqual(CSVSummarizer.calculate_modes([1,2.0,3,]), None)
    #     self.assertEqual(CSVSummarizer.calculate_modes([2.0,2.0,2,2,3,3,3]), [2.0])
    #     self.assertEqual(CSVSummarizer.calculate_modes([2.0,2.0,2,2,3,3,3]), [2])
    #     self.assertEqual(CSVSummarizer.calculate_modes([1.75, 1.75, 1, 5]), [1.75])

    def test_nummeric_summary_calculate_modes(self):
        passing_test_dataset = [
            ([1,2.0,3,3], [3.0]),
            ([1,2.0,-3,-3], [-3.0]),
            ([1,2.0,3,], None),
            ([2.0,2.0,2,2,3,3,3], [2.0]),
            ([2.0,2.0,2,2,3,3,3], [2]),
            ([1.75, 1.75, 1, 5], [1.75]),
            ([1, 1.75, 1, 5], [1]),
            ([1, 1.75, 1, 5, 5], [1, 5]),
        ]
        for data in passing_test_dataset:
            numeric_summary = NumericSummary(data[0])
            self.assertEqual(numeric_summary.calculate_modes(), data[1])

    def test_text_summary_get_value_frequency(self):
        data = [["cat", "dog", "cat"],{"cat": 2, "dog": 1}]
        text_summary = TextSummary(data[0])
        self.assertEqual(text_summary.get_value_frequency(), data[1])