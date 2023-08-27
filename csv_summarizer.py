import csv
from io import StringIO
from pathlib import Path
from typing import Union, Iterator

class CSVSummarizer:
    def __init__(self, file_path: Union[str, Path, StringIO]) -> None:
            self.file_path = file_path
            self._reader = self._read_csv()
            self.header = next(self._reader)
            self.columns_data = list(zip(*self._reader))
    
    def _read_csv(self) -> Iterator[list[str]]:
          with open(self.file_path, newline='') as file_handler:
            csv_reader = csv.reader(file_handler)
            for row in csv_reader:
                 yield row

    def calculate_statistics(self) -> dict[str, int]:
         return {"test": 1}
    