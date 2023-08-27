import csv
import os
from pathlib import Path
from typing import Union, Iterator, List
from column import Column

class Table:
    def __init__(self, file_path: Union[str, Path]) -> None:
            self.file_path = file_path
            self.file_name = os.path.basename(self.file_path)
            self._reader = self._read_csv()
            self.columns = self._generate_columns()
            self.shape = (len(self.columns), self.columns[0].length)

    
    def __str__(self) -> str:
         return f"Table Name: {self.file_name}, Columns: {self.shape[0]}, Rows: {self.shape[1]}"
    
    def _read_csv(self) -> Iterator[list[str]]:
          with open(self.file_path, newline='') as file_handler:
            csv_reader = csv.reader(file_handler)
            for row in csv_reader:
                 yield row
    
    def _generate_columns(self) -> List[Column]:
        return [Column(data) for data in zip(*self._reader)]
    
    def print_table_summary(self) -> None:
        print(self.__str__())
        for column in self.columns:
             print(column.__str__())
