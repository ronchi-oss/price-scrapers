# Price scrapers

A Python script intended to be integrated with Unix pipelines via the `price-scraper` script. Website scraping definitions are defined in `config.yml`.

## Setup

```sh
cd ~/git
git clone <...>
cd price-scrapers
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

Manual testing / development:

```sh
curl -s <item-url> | price_scraper.py <website>
```

Integrating the project in a Unix pipeline:

```sh
export PATH="$HOME/git/price-scrapers:$PATH"
curl -s <item-url> | price-scraper <website>
```
