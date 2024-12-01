import requests
import urllib.parse as p

from collections import defaultdict
from datetime import datetime
from typing import List, Optional, Dict, Any
from entities import InputSearchEntity, OutputSearchEntity


def get_rank(
    input_search_entities: List[InputSearchEntity],
    api_key: str,
    search_engine_id: str,
    max_pages: int,
) -> List[OutputSearchEntity]:
    """
    Fetch search rankings for given queries and urls.
    """
    timestamp = datetime.now()
    output_search_entities: List[OutputSearchEntity] = []

    for input_entity in input_search_entities:
        target_ranks: Dict[str, List[int]] = defaultdict(list)

        for page in range(1, max_pages + 1):
            start = (page - 1) * 10 + 1
            url = f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx={search_engine_id}&q={input_entity.query}&start={start}"
            response = requests.get(url)

            if response.status_code != 200:
                print(f"Error {response.status_code}: {response.text}")
                break

            data = response.json()
            search_items: Optional[List[Dict[Any, Any]]] = data.get("items")
            if not search_items:
                break

            for i, item in enumerate(search_items, start=1):
                link = item.get("link")
                for url in input_entity.urls:
                    if link == url:
                        rank = i + start - 1
                        print(
                            f"[+] Found {url} at rank #{rank} for query '{input_entity.query}'"
                        )
                        target_ranks[url].append(rank)

        for url, ranks in target_ranks.items():
            output_search_entities.append(OutputSearchEntity(url, ranks, timestamp))

    return output_search_entities
