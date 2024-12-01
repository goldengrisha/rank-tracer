# Google Search Rank Tool

This Python-based tool tracks search rankings for specific domains and queries using the Google Custom Search API.

## Features

- Tracks search rankings for multiple domains and queries.
- Outputs results to a CSV file.
- Modular architecture for easy customization.

## Installation

1. Clone the repository:
   ```bash
   git clone git@github.com:goldengrisha/rank-tracer.git
   cd rank-tracer
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Add your API key and Search Engine ID in `config.py`.

## Usage

Run the tool:
```bash
python -m main
```

Output will be saved to `rankings.csv`.

