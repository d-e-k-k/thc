import unittest
from csv_summarizer import NumericSummary, TextSummary, Column

class TestNummericSummary(unittest.TestCase):
    def test_nummeric_summary_calculate_modes(self):
        passing_datasets = [
            ([1,2.0,3,3], [3.0]),
            ([1,2.0,-3,-3], [-3.0]),
            ([1,2.0,3,], None),
            ([2.0,2.0,2,2,3,3,3], [2.0]),
            ([2.0,2.0,2,2,3,3,3], [2]),
            ([1.75, 1.75, 1, 5], [1.75]),
            ([1, 1.75, 1, 5], [1]),
            ([1, 1.75, 1, 5, 5], [1, 5]),
        ]

        failing_datasets = [
            ([1,2.0,3,3], [1]),
            ([1,2.0,-3,-3], [3.0]),
            ([1,2.0,3], 1),
            ([2.0,2.0,2,2,3,3,3], [3]),
            ([2.0,2.0,2,2,3,3,3], [3]),
            ([1.75, 1.75, 1, 5], [1.70]),
            ([1, 1.75, 1, 5], [5]),
            ([1, 1.75, 1, 5, 5], [1]),
        ]

        for data in passing_datasets:
            numeric_summary = NumericSummary(data[0])
            self.assertEqual(numeric_summary.calculate_modes(), data[1])

        for data in failing_datasets:
            numeric_summary = NumericSummary(data[0])
            self.assertNotEqual(numeric_summary.calculate_modes(), data[1])

class TestTextSummary(unittest.TestCase):
    def test_text_summary_get_value_frequency(self):
        passing_datasets = [
            (["cat", "dog", "cat"],{"cat": 2, "dog": 1}),
            (["cat", "cat", "cat"],{"cat": 3}),
            (["dog"],{"dog": 1}),
            ([],{})
            ]
        
        falling_datasets = [
            (["cat", "dog", "cat"],{"cat": 1, "dog": 1}),
            (["cat", "cat", "cat"],{"cat": 1}),
            (["dog"],{"dog": 2})
            ]
        
        for data in passing_datasets:
            text_summary = TextSummary(data[0])
            self.assertEqual(text_summary.get_value_frequency(), data[1])

        for data in falling_datasets:
            text_summary = TextSummary(data[0])
            self.assertNotEqual(text_summary.get_value_frequency(), data[1])

class TestColumn(unittest.TestCase):
    def test_column_type_infrance_is_correct(self):
        passing_datasets = [
            (["1", "2", "3"], float),
            (["1", "2", "3.1"], float),
            (["1", "2", "cat"], str),
            (["fish", "bird", "cat"], str)
        ]

        falling_datasets = [
            (["1", "2", "3"], str),
            (["1", "2", "3.1"], str),
            (["1", "2", "cat"], float),
            (["fish", "bird", "cat"], int)
        ]
        
        for data in passing_datasets:
            column = Column('test_name', data[0])
            self.assertEqual(column.type, data[1])

        for data in falling_datasets:
            column = Column('test_name', data[0])
            self.assertNotEqual(column.type, data[1])