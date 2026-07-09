from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def plot_chart(data: pd.DataFrame) -> None:
    """Plot a scatter plot chart in two axis
        by income and life expectancy."""
    ax = data.plot(
        kind="scatter",
        x="income",
        y="life_expectancy",
        figsize=(10, 6)
    )
    ax.set_xscale("log")
    ax.set_xticks([300, 1000, 10000], labels=['300', '1k', '10k'])
    ax.set_title("1900")
    ax.set_xlabel("Gross domestic product")
    ax.set_ylabel("Life Expectancy")
    plt.show()


def get_year_data(data: dict, key: str, year: str) -> pd.Series:
    """Return all countries for a given year as a Series."""
    series_year = data.get(key)[year]

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
    return series_year.apply(parse_unit_measure).dropna()


def process_data(data: dict, year: str) -> None:
    """Process the dataframe, do some validations to assure that the content
    inside is valid, extract the required content and plot the result."""
    if not isinstance(data, dict) or len(data) != 2:
        print("Error: You must inform a list with 2 Panda Dataframes")
        return
    if not year.strip():
        print("Error: You must inform a valid year.")
        return
    for k, v in data.items():
        if not isinstance(v, pd.DataFrame):
            print(f"Error: {k} is not a Panda DataFrame")
            return
        if not (year in v.columns or int(year) in v.columns):
            print(f"Error: Year column '{year}' in the {k} DataFrame")
            return
    try:
        data["life"] = data["life"].set_index("country")
        data["income"] = data["income"].set_index("country")
        series_life1900 = get_year_data(data, "life", year)
        series_income1900 = get_year_data(data, "income", year)
        plot_df = pd.concat([
            series_life1900.rename("life_expectancy"),
            series_income1900.rename("income")
        ], axis=1, join="inner")
        plot_chart(plot_df)
    except Exception as e:
        print(f"Error: {e}")
        return


def main():
    """Main entry for the program."""
    df_life = load("life_expectancy_years.csv")
    df_inc = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    data = {"income": df_inc, "life": df_life}
    process_data(data, "1900")


if __name__ == "__main__":
    main()
