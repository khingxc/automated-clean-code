# For this exercise focus on how to testability. How do we test thing like this?
# and test fixture
# the example data is in data/exercise20_data.txt
import argparse
import sys
from typing import List


class HistLib:
    def get_filename_from_args(self, args: List[str]):
        parser = argparse.ArgumentParser(
            description="compute the entry with the most occurrence and the least occurrence form a file"
        )
        parser.add_argument("file_name", metavar="N", type=str, help="filename to compute the histogram")
        args = parser.parse_args(args[1:])
        return args.file_name

    def fill_histogram(self, file_name: str):
        count_dict: dict[str, int] = {}
        with open(file_name, "r") as file:
            for line in file:
                word: str = line.strip()
                if word in count_dict:
                    count_dict[word] += 1
                else:
                    count_dict[word] = 0
        return count_dict

    def get_max_key_and_value(self, counter):
        max_key: str = max(counter, key=counter.get)
        return max_key, counter[max_key]

    def get_min_key_and_value(self, counter):
        min_key: str = min(counter, key=counter.get)
        return min_key, counter[min_key]

    def get_results(self, counter):
        max_key: str = self.get_max_key_and_value(counter)[0]
        max_counter: int = self.get_max_key_and_value(counter)[1]
        min_key: str = self.get_min_key_and_value(counter)[0]
        min_counter: int = self.get_min_key_and_value(counter)[1]
        return min_key, min_counter, max_key, max_counter
