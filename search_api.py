import requests
import urllib.parse as p

from collections import defaultdict
from datetime import datetime
from typing import List, Optional, Dict
from entities import InputSearchEntity, OutputSearchEntity


def get_rank(
    input_search_entities: List[InputSearchEntity],
    api_key: str,
    search_engine_id: str,
    max_pages: int,
) -> List[OutputSearchEntity]:
    """
    Fetch search rankings for given queries and domains.
    """
    timestamp = datetime.now()
    output_search_entities: List[OutputSearchEntity] = []

    for input_entity in input_search_entities:
        target_ranks = defaultdict(list)

        for page in range(1, max_pages + 1):
            start = (page - 1) * 10 + 1
            url = f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx={search_engine_id}&q={input_entity.query}&start={start}"
            response = requests.get(url)

            if response.status_code != 200:
                print(f"[!] API Error {response.status_code}: {response.text}")
                break

            data = response.json()
            search_items: Optional[List[Dict]] = data.get("items")
            if not search_items:
                break

            for i, item in enumerate(search_items, start=1):
                link = item.get("link")
                domain_name = p.urlparse(link).netloc
                for domain in input_entity.domains:
                    if domain_name == domain:
                        rank = i + start - 1
                        print(
                            f"[+] Found {domain} at rank #{rank} for query '{input_entity.query}'"
                        )
                        target_ranks[domain].append(rank)

        for domain, ranks in target_ranks.items():
            output_search_entities.append(OutputSearchEntity(domain, ranks, timestamp))

    return output_search_entities
