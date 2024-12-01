from config import API_KEY, SEARCH_ENGINE_ID, OUTPUT_FILE, MAX_PAGES
from entities import InputSearchEntity
from search_api import get_rank
from csv_writer import write_to_csv


def main():
    search_entities = [
        InputSearchEntity(
            ["https://www.kaggle.com/datasets/diyanandy/testcsv"], "test csv"
        )
    ]

    output_entities = get_rank(search_entities, API_KEY, SEARCH_ENGINE_ID, MAX_PAGES)
    write_to_csv(OUTPUT_FILE, output_entities)


if __name__ == "__main__":
    main()
