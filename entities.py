from datetime import datetime
from typing import Generator, List, Dict


class InputSearchEntity:
    def __init__(self, urls: List[str], query: str):
        self.urls = urls
        self.query = query


class OutputSearchEntity:
    def __init__(self, url: str, ranks: List[int], timestamp: datetime):
        self.url = url
        self.ranks = ranks
        self.timestamp = timestamp.strftime("%Y-%m-%d %H:%M:%S")

    def expand_rows(self) -> Generator[Dict[str, str], None, None]:
        """
        Expand ranks into individual rows for CSV writing.
        """
        for rank in self.ranks:
            yield {
                "url": self.url,
                "rank": str(rank),
                "timestamp": self.timestamp,
            }
