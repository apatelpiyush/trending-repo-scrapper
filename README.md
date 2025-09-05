# GitHub Trending Scraper & Analyzer

This project scrapes the [GitHub Trending](https://github.com/trending) page, extracts repository details, and performs basic data analysis with visualizations.

## 🚀 Features
- Scrapes trending repositories (name, stars, language, description).
- Saves the extracted data into a CSV file (`Data_File.csv`).
- Cleans and processes the dataset:
  - Converts stars into numeric format.
  - Handles missing values.
  - Removes duplicate repo names.
- Generates insights:
  - Mean, Median, Mode of stars.
- Creates and saves graphs:
  - **Graph1.png** → Distribution of Trending Repositories by Language.
  - **Graph2.png** → Stars vs. Language.

## 📊 Example Output

### 📄 CSV Preview
The script generates a file named **`Data_File.csv`** with repository details.

### 📈 Graph Previews
- **Language Distribution**
  
  ![Graph1](Output)(Graph1.png)

- **Stars vs. Language**
  
  ![Graph2](Output)(Graph2.png)

## 🛠️ Installation
Clone this repository:
```bash
git clone https://github.com/apatelpiyush/trending-repo-scrapping.git
cd trending-repo-scrapping
```

Install dependencies:
```bash
pip install -r requirements.txt
```

## ▶️ Usage
Run the script:
```bash
python main.py
```

This will:
1. Scrape GitHub trending repositories.
2. Save extracted data in `Data_File.csv`.
3. Generate graphs (`Graph1.png` and `Graph2.png`).

## 📦 Requirements
- Python 3.8+
- See [`requirements.txt`](requirements.txt)

## 📜 License
This project is licensed under the [MIT License](LICENSE).
