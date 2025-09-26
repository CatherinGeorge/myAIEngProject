import os
import pandas as pd
import numpy as np


# ------------------------------
# Base Class for Dataset Loading
# ------------------------------
class CovidData:
    def __init__(self, filename="country_wise_latest.csv"):
        # Detect CSV file in the same folder as this script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, filename)

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"CSV file not found: {file_path}")

        self.df = pd.read_csv(file_path)
        print(f"✅ Data loaded successfully! Shape: {self.df.shape}")


# --------------------------------
# Subclass for Covid Data Analysis
# --------------------------------
class CovidAnalysis(CovidData):
    def summarize_cases_by_region(self):
        return self.df.groupby("WHO Region")[["Confirmed", "Deaths", "Recovered"]].sum()

    def filter_low_cases(self):
        return self.df[self.df["Confirmed"] >= 10]

    def region_highest_cases(self):
        return self.df.groupby("WHO Region")["Confirmed"].sum().idxmax()

    def sort_by_confirmed(self):
        sorted_df = self.df.sort_values(by="Confirmed", ascending=False)
        sorted_df.to_csv("sorted_by_confirmed.csv", index=False)
        return sorted_df

    def top5_countries(self):
        return self.df.nlargest(5, "Confirmed")[["Country/Region", "Confirmed"]]

    def region_lowest_deaths(self):
        return self.df.groupby("WHO Region")["Deaths"].sum().idxmin()

    def india_summary(self):
        return self.df[self.df["Country/Region"] == "India"]

    def mortality_rate(self):
        df = self.df.copy()
        df["Mortality Rate"] = df["Deaths"] / df["Confirmed"].replace(0, np.nan)
        return df.groupby("WHO Region")["Mortality Rate"].mean()

    def recovery_rate(self):
        df = self.df.copy()
        df["Recovery Rate"] = df["Recovered"] / df["Confirmed"].replace(0, np.nan)
        return df.groupby("WHO Region")["Recovery Rate"].mean()

    def detect_outliers(self):
        confirmed = self.df["Confirmed"]
        mean, std = confirmed.mean(), confirmed.std()
        lower, upper = mean - 2 * std, mean + 2 * std
        return self.df[(confirmed < lower) | (confirmed > upper)]

    def group_by_country_region(self):
        return self.df.groupby(["Country/Region", "WHO Region"]).sum()

    def zero_recovered(self):
        return self.df[self.df["Recovered"] == 0]


# -----------------------
# Main Execution Section
# -----------------------
if __name__ == "__main__":
    analysis = CovidAnalysis()

    print("\n1. Summarize cases by region:\n", analysis.summarize_cases_by_region())
    print("\n2. Filtered low case records:\n", analysis.filter_low_cases().head())
    print("\n3. Region with highest confirmed cases:", analysis.region_highest_cases())
    print("\n4. Sorted by confirmed saved to 'sorted_by_confirmed.csv'")
    print("\n5. Top 5 countries by case count:\n", analysis.top5_countries())
    print("\n6. Region with lowest deaths:", analysis.region_lowest_deaths())
    print("\n7. India summary:\n", analysis.india_summary())
    print("\n8. Mortality rate by region:\n", analysis.mortality_rate())
    print("\n9. Recovery rate by region:\n", analysis.recovery_rate())
    print("\n10. Outliers detected:\n", analysis.detect_outliers())
    print("\n11. Grouped by country and region:\n", analysis.group_by_country_region().head())
    print("\n12. Regions with zero recovered:\n", analysis.zero_recovered())
