from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np


def plot_chart(data: pd.DataFrame) -> None:
    """Plot a line chart with the country data."""
    ax = data.plot(kind="line", figsize=(12, 6), linewidth=1)
    ax.yaxis.set_major_formatter(
        ticker.FuncFormatter(lambda x, _: f'{x / 1_000_000:.0f}M')
    )
    ax.set_title("Population Projections")
    ax.set_xlabel("Year")
    ax.set_ylabel("Population")
    # ax.legend(title="Country", loc="lower right")
    plt.show()


def get_country_data(data: pd.DataFrame, country: str) -> pd.Series:
    """Return the data at country level parsed and ready to be used."""
    country = country.strip()
    row = (data[data['country'] == country]
           .set_index('country')
           .iloc[0])

    def parse_unit_measure(val):
        """Helper function to parse the unit measure"""
        if pd.isna(val):
            return np.nan
        s = str(val).upper().replace(",", "").strip()
        mult = 1
        if s.endswith("K"):
            mult, s = 1_000, s[:-1]
        elif s.endswith("M"):
            mult, s = 1_000_000, s[:-1]
        elif s.endswith("B"):
            mult, s = 1_000_000_000, s[:-1]
        try:
            return float(s) * mult
        except Exception as e:
            print(f"Error: {e}")
            return np.nan
    return row.apply(parse_unit_measure).dropna()


def process_data(data: pd.DataFrame, countries: list) -> None:
    """Process the dataframe, do some validations to assure that the content
    inside the dataframe is valid, extract just country and country2 from the
    data) then plot the result."""
    if not isinstance(data, pd.DataFrame):
        print("Error: The 'data' argument must be a panda DataFrame")
        return
    if not isinstance(countries, list) or len(countries) != 2:
        print("Error: You must inform a list with 2 countries.")
        return
    if 'country' not in data.columns:
        print("Error: The DataFrame does not contain a country column")
        return
    if not countries:
        print("Error: No country was specified.")
        return
    country1 = get_country_data(data, countries[0])
    country2 = get_country_data(data, countries[1])
    plot_df = pd.concat([
        country1,
        country2
    ], axis=1)
    plot_df.index = plot_df.index.astype(int)
    plot_df = plot_df.loc[1800:2050]
    plot_chart(plot_df)


def main():
    """Main entry for the program."""
    df = load("population_total.csv")
    process_data(df, ["Portugal", "Brazil"])


if __name__ == "__main__":
    main()
