import pandas as pd
from datetime import datetime, timedelta
from dateutil.parser import parse


def process_csv(file_path):
    """
    Processes a CSV containing company data, extracts relevant EPS dates and values,
    and writes the results to an output file.

    Parameters:
    - file_path (str): Path to the CSV file containing company data.

    Returns:
    - None
    """
    df = pd.read_csv(file_path, header=None)
    index = 0

    with open('output.txt', 'w') as file:
        while index < len(df):
            company_name = df.iloc[index, 0]

            if pd.isnull(company_name):
                index += 1
                continue

            company = company_name.strip().lower().replace(' ', '_')
            file.write(f"{'-'*35}\n")
            file.write(f"{company} dates:\n")

            eps_dates = df.iloc[index + 1, 1:]
            
            if pd.isnull(eps_dates.iloc[0]):
                index += 4
                continue

            eps_dates = eps_dates.apply(parse).tolist()

            # If date falls on Sunday, move to Monday
            eps_dates = [
                date + timedelta(days=1) if date.weekday() == 6 else date
                for date in eps_dates
            ]

            formatted_dates = [f"'{date.strftime('%Y-%m-%d')}'" for date in eps_dates]
            file.write(f"{', '.join(formatted_dates)}\n")

            eps_values = df.iloc[index + 2, 1:].astype(float).tolist()
            file.write(f"{company} values:\n")
            formatted_values = ", ".join([f"{value:.2f}" for value in eps_values])
            file.write(f"{formatted_values}\n")

            index += 4


# File path for the EPS data
file_path = 'EPS_data.csv'
process_csv(file_path)
