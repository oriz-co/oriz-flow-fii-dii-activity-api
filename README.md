# fii-dii-tracker

A Python-based tool that automatically fetches Foreign Institutional Investors (FII) and Domestic Institutional Investors (DII) trading data from the National Stock Exchange (NSE) of India. It includes a fallback mechanism to scrape data from Moneycontrol if the NSE API is unavailable.

## features

- **Automated Data Fetching**: Scrapes data daily from NSE.
- **Reliable Fallback**: Uses Moneycontrol as a secondary source if NSE fails.
- **Historical Data**: Appends daily data to a JSON file (`fii_history.json`) for historical tracking.
- **Visualisation**: Generates a bar chart (`money_flow.png`) showing FII/DII net investment for the last 30 days.
- **CI/CD Automation**: Runs automatically every weekday at 1:30 PM UTC (7:00 PM IST) via GitHub Actions.

## 📊 Access Data

You can access the historical FII/DII data directly via the following URL. This JSON file is updated daily.

- **Raw JSON URL**: [https://raw.githubusercontent.com/chirag127/fii-dii-tracker/main/fii_history.json](https://raw.githubusercontent.com/chirag127/fii-dii-tracker/main/fii_history.json)
- **View on GitHub**: [fii_history.json](https://github.com/chirag127/fii-dii-tracker/blob/main/fii_history.json)

## 🛠️ Setup & Usage

### Prerequisites

- Python 3.9+
- `pip` (Python package installer)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/chirag127/fii-dii-tracker.git
   cd fii-dii-tracker
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   # OR manually:
   pip install requests pandas matplotlib beautifulsoup4 lxml
   ```

### Running Locally

To fetch the latest data and update the JSON/graph manually:

```bash
python fetch_fii.py
```

This will:
1. Fetch data from NSE (or Moneycontrol).
2. Update `fii_history.json`.
3. Generate/Overwrite `money_flow.png`.

## 🤖 Automation

The project uses **GitHub Actions** to automate the data fetching process.

- **Workflow File**: `.github/workflows/daily_fii_fetch.yml`
- **Schedule**: Runs every Monday to Friday at 1:30 PM UTC.
- **Process**:
    1. Sets up Python env.
    2. Installs dependencies.
    3. Runs `fetch_fii.py`.
    4. Commits and pushes the updated `fii_history.json` and `money_flow.png` back to the repository.

## 📈 Sample Output

### JSON Structure (`fii_history.json`)
```json
[
    {
        "date": "16-Feb-2026",
        "fii_net_crores": -1234.56,
        "dii_net_crores": 789.10
    }
]
```

## Disclaimer
This tool is for educational purposes only. Trading data is scraped from public sources and may not always be accurate or real-time. Use it at your own discretion.
