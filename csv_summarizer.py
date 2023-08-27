import csv
from pathlib import Path
from typing import Union, Iterator
from statistics import mean, median, multimode

class CSVSummarizer:
    def __init__(self, file_path: Union[str, Path]) -> None:
            self.file_path = file_path
            self._reader = self._read_csv()
            self.header = next(self._reader)
            self.columns_data = list(zip(*self._reader))
    
    def _read_csv(self) -> Iterator[list[str]]:
          with open(self.file_path, newline='') as file_handler:
            csv_reader = csv.reader(file_handler)
            for row in csv_reader:
                 yield row

    

class NumericSummary:
    def __init__(self, data: list[Union[int, float]]) -> None:
         self.data = data
         self.number_of_data_entries = len(self.data)
         self.number_of_unique_data_entries = len(set(self.data))
         self.modes = self.calculate_modes()
         self.mean = mean(self.data)
         self.median = median(self.data)


    def calculate_modes(self) -> Union[list[float], None]:
         """Returns modes. This method is intened to protect against differnces in statistics.mode which vary between python versions.
         Depending on python version, this native module method statistics.mode can throw an exception or return a value when no mode aka duplicate value does not exist."""
         if self.number_of_data_entries == self.number_of_unique_data_entries:
              return None
         return multimode(self.data)
    
    def get_summary(self):
         return {
              "Mean": self.mean,
              "Median": self.median,
              "Modes": self.modes
         }
    
class TextSummary:
    def __init__(self, data: list[str]) -> None:
        self.data = data
        self.number_of_data_entries = len(self.data)
        self.number_of_unique_data_entries = len(set(self.data))

    def get_value_frequency(self) -> dict[str, int]:
         unique_values = set(self.data)
         frequency = {}
         for key in unique_values:
              frequency[key] = len([datapoint for datapoint in self.data if key == datapoint])
         return frequency