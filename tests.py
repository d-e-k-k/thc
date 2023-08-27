import unittest
from io import StringIO
from csv_summarizer import CSVSummarizer

in_mem_csv = StringIO("""\
"sepal.length","sepal.width","petal.length","petal.width","variety"
5.1,3.5,1.4,.2,"Setosa"
4.9,3,1.4,.2,"Setosa"
4.7,3.2,1.3,.2,"Setosa"
4.6,3.1,1.5,.2,"Setosa""")


class TestCSVSummarier(unittest.TestCase):
    def test_csv_sammarizer_calculate_statistics(self):
        csv_summarizer = CSVSummarizer(in_mem_csv)
        self.assertEqual(csv_summarizer.calculate_statistics(), {"test", 2})