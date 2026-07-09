from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt


def plot_chart(data: pd.Series) -> None:
    """Plot a line chart with the country data."""
    plt.figure(figsize=(8, 6))
    data.plot(kind="line", color="b", linewidth=1)
    plt.title("Portugal Life expectancy Projections")
    plt.xlabel("Year")
    plt.ylabel("Life expectancy")
    plt.show()


def process_country_df(data: pd.DataFrame, country: str) -> None:
    """Process the dataframe, do some validations to assure that the content
    inside the dataframe is valid, extract just one single row (Country)
    and request the plot of it."""
    if not isinstance(data, pd.DataFrame):
        print("Error: The 'data' argument must be a panda DataFrame")
        return
    if 'country' not in data.columns:
        print("Error: The DataFrame does not contain a country column")
        return
    if not country or not country.strip():
        print("Error: No country was specified.")
        return
    country = country.strip()
    country_df = data[data['country'] == country]
    country_series = pd.to_numeric(country_df.iloc[0], errors='coerce')
    country_series = country_series.dropna()
    if country_df.empty:
        print(f"Error: The country {country} was not found in the dataset")
    plot_chart(country_series)


def main():
    """Main entry for the program."""
    df = load("life_expectancy_years.csv")
    process_country_df(df, "Portugal")


if __name__ == "__main__":
    main()
