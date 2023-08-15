# Earnings-Interplay-GICS

**Quantitative analysis of the interplay between company earnings disclosures and competitor stock reactions across GICS. This project utilizes advanced data extraction, correlation algorithms, and statistical methods to inform investment strategies.**

## Project Overview

The goal of this project is to understand the relationship between earnings disclosures of companies and the subsequent reactions in competitor stocks, segmented across the Global Industry Classification Standard (GICS). The project uses earnings data and stock prices, computing various correlation measures, and presents findings through interactive visualizations.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Data](#data)
- [Results](#results)
- [Contact](#contact)
- [License](#license)

## Installation

1. Clone this repository: 
    ```
    git clone https://github.com/YourUsername/Earnings-Interplay-GICS.git
    ```
2. Install required libraries:
    ```
    pip install pandas numpy scipy seaborn yfinance
    ```

## Usage

1. **Correlation Computation:**
   - Use the `correlation_analysis.ipynb` notebook to compute various correlation measures.
   
2. **Visualization:**
   - Use the `heatmap_visualization.ipynb` notebook for generating a heatmap based on the sector-wise average correlations.
   
3. **Data Processing:**
   - The `process_eps_data.py` script processes EPS data by company and outputs organized dates and values.

## Data

- `EPS_data_by_company.csv`: Contains the EPS data organized by companies.
- `sector_average_values.txt`: Contains sector-wise computed values used for visualizations.
- `company_tickers.txt`: List of company tickers used in the analysis.

## Results

The results derived from the data showcase the interrelation between earnings disclosures and the subsequent stock market reaction across various sectors. Specific insights and interpretations can be drawn from the Report heatmap and computed correlation values.


## Contact

For questions, clarifications, or feedback, please reach out to:
- [Email](mailto:aduggalwork@example.com)
- [https://www.linkedin.com/in/ashu-duggal/](https://www.linkedin.com/in/ashu-duggal/)

## License

This project is open-sourced pending under the University of Illinois License. 
