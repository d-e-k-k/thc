from typing import Union
from statistics import mean
import json

class Column:
    def __init__(self, data: tuple[str]) -> None:
        self.name = data[0]
        self.data = self._parse_data(data[1:])
        self.type = type(self.data[0])
        self.length = len(data[1:])
        if self.type == float:
            self.mean = mean(self.data)
            self.minimum = min(self.data)
            self.maximum = max(self.data)
        if self.type == str:
            self.frequency = self.get_value_frequency()

    def __str__(self) -> str:
        if self.type == str:
            return f"Column Name: {self.name}, {json.dumps(self.frequency)}"
        elif self.type == float:
            return f"Column Name: {self.name}, Mean: {self.mean}, Minimum: {self.minimum}, Maximum: {self.maximum}"
        return f"Column Name: {self.name}, No data"

    
    @staticmethod
    def _parse_data(data) -> Union[list[str], list[float]]:
        non_empty_data = list(filter(None, data))
        try:
            return [float(datapoint) for datapoint in non_empty_data]
        except:
            return non_empty_data
        
    def get_value_frequency(self) -> dict[str, int]:
        unique_values = set(self.data)
        frequency = {}
        for key in unique_values:
            frequency[key] = len([datapoint for datapoint in self.data if key == datapoint])
        return frequency