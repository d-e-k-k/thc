import csv
from pathlib import Path
from typing import Union, Iterator

class CSVSummarizer:
    def __init__(self, file_path: Union[str, Path]) -> None:
            self.file_path = file_path
            self._reader = self.read_csv()
            self.header = next(self._reader)
            self.data = [row for row in self._reader]
    
    def read_csv(self) -> Iterator[list[str]]:
          with open(self.file_path, newline='') as file_handler:
            csv_reader = csv.reader(file_handler)
            for row in csv_reader:
                 yield row