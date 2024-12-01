# search_rank_tool/csv_writer.py
import csv
from typing import List
from entities import OutputSearchEntity


def write_to_csv(filename: str, entities: List[OutputSearchEntity]) -> None:
    """
    Write output entities to a CSV file.
    """
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        headers = ["domain", "rank", "timestamp"]
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()

        for entity in entities:
            for row in entity.expand_rows():
                writer.writerow(row)
