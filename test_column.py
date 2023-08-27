import unittest
from column import Column

class TestColumn(unittest.TestCase):
    def test_column_type_infrance_is_correct(self):
        passing_datasets = [
            (("name", "1", "2", "3"), float),
            (("name", "1", "2", "3.1"), float),
            (("name", "1", "2", "cat"), str),
            (("name", "fish", "bird", "cat"), str)
        ]

        falling_datasets = [
            (("name", "1", "2", "3"), str),
            (("name", "1", "2", "3.1"), str),
            (("name", "1", "2", "cat"), float),
            (("name", "fish", "bird", "cat"), int)
        ]
        
        for data in passing_datasets:
            column = Column(data[0])
            self.assertEqual(column.type, data[1])

        for data in falling_datasets:
            column = Column(data[0])
            self.assertNotEqual(column.type, data[1])

    def test_column_frequency_is_correct(self):
        passing_datasets = [
            (("name", "cat", "dog", "cat"),{"cat": 2, "dog": 1}),
            (("name", "cat", "cat", "cat"),{"cat": 3}),
            (("name", "dog"),{"dog": 1}),
            ]
        
        falling_datasets = [
            (("name", "cat", "dog", "cat"), {"cat": 1, "dog": 1}),
            (["name","cat", "cat", "cat"],{"cat": 1}),
            (["name","dog"],{"dog": 2})
            ]
        
        for data in passing_datasets:
            column = Column(data[0])
            self.assertEqual(column.frequency, data[1])
        
        for data in falling_datasets:
            column = Column(data[0])
            self.assertNotEqual(column.frequency, data[1])

