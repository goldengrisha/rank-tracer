# search_rank_tool/entities.py
from datetime import datetime
from typing import Generator, List, Dict


class InputSearchEntity:
    def __init__(self, domains: List[str], query: str):
        self.domains = domains
        self.query = query


class OutputSearchEntity:
    def __init__(self, domain: str, ranks: List[int], timestamp: datetime):
        self.domain = domain
        self.ranks = ranks
        self.timestamp = timestamp.strftime("%Y-%m-%d %H:%M:%S")

    def expand_rows(self) -> Generator[Dict[str, str], None, None]:
        """
        Expand ranks into individual rows for CSV writing.
        """
        for rank in self.ranks:
            yield {
                "domain": self.domain,
                "rank": str(rank),
                "timestamp": self.timestamp,
            }
