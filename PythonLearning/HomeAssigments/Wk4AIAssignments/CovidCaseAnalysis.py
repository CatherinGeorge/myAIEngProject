import os
import pandas as pd
import numpy as np


# ------------------------------
# Base Class 1: Data Loader
# ------------------------------
class DataLoader:
    def __init__(self, filename="country_wise_latest.csv"):
        if not os.path.exists(filename):
            raise FileNotFoundError(f"File not found: {filename}")
        self.df = pd.read_csv(filename)
        print(f"✅ Data loaded: {self.df.shape[0]} rows, {self.df.shape[1]} columns")


# ------------------------------
# Base Class 2: Data Cleaner
# ------------------------------
class DataCleaner:
    def clean_data(self, df):
        # Fill NaN values with 0 for safe calculations
        return df.fillna(0)


# ------------------------------
# Main Class: Covid Analysis
# ------------------------------
class CovidAnalysis(DataLoader, DataCleaner):
    def __init__(self, filename="country_wise_latest.csv"):
        DataLoader.__init__(self, filename)   # load data
        self.df = self.clean_data(self.df)    # clean data

    def summarize_by_region(self):
        return self.df.groupby("WHO Region")[["Confirmed", "Deaths", "Recovered"]].sum()

    def filter_low_cases(self):
        return self.df[self.df["Confirmed"] >= 10]

    def region_highest_cases(self):
        return self.df.groupby("WHO Region")["Confirmed"].sum().idxmax()

    def sort_by_confirmed(self, out_path="sorted_by_confirmed.csv"):
        sorted_df = self.df.sort_values(by="Confirmed", ascending=False)
        sorted_df.to_csv(out_path, index=False)   # only CSV export
        return sorted_df

    def top5_countries(self):
        return self.df.nlargest(5, "Confirmed")[["Country/Region", "Confirmed"]]

    def region_lowest_deaths(self):
        return self.df.groupby("WHO Region")["Deaths"].sum().idxmin()

    def india_summary(self):
        return self.df[self.df["Country/Region"] == "India"]

    def mortality_rate(self):
        grouped = self.df.groupby("WHO Region")[["Confirmed", "Deaths"]].sum()
        grouped["Mortality Rate"] = grouped["Deaths"] / grouped["Confirmed"].replace(0, np.nan)
        return grouped[["Mortality Rate"]]

    def recovery_rate(self):
        grouped = self.df.groupby("WHO Region")[["Confirmed", "Recovered"]].sum()
        grouped["Recovery Rate"] = grouped["Recovered"] / grouped["Confirmed"].replace(0, np.nan)
        return grouped[["Recovery Rate"]]

    def detect_outliers(self):
        confirmed = self.df["Confirmed"]
        mean, std = confirmed.mean(), confirmed.std()
        lower, upper = mean - 2 * std, mean + 2 * std
        return self.df[(confirmed < lower) | (confirmed > upper)]

    def group_by_country_region(self):
        return self.df.groupby(["Country/Region", "WHO Region"])[["Confirmed", "Deaths", "Recovered"]].sum()

    def zero_recovered(self):
        return self.df[self.df["Recovered"] == 0]


# ------------------------------
# Main Execution
# ------------------------------
if __name__ == "__main__":
    analysis = CovidAnalysis(
        r"C:\Users\CATHERIN\Desktop\Aut_Project\AI Engineer Test Leaf\myAIEngProject\PythonLearning\HomeAssigments\Wk4AIAssignments\country_wise_latest.csv"
    )
    print("\n1) Summary by region:\n", analysis.summarize_by_region())
    print("\n2) Filtered low case records:\n", analysis.filter_low_cases().head())
    print("\n3) Region with highest confirmed cases:", analysis.region_highest_cases())
    
    sorted_df = analysis.sort_by_confirmed()
    print("\n4) Sorted dataset saved as 'sorted_by_confirmed.csv'")
    
    print("\n5) Top 5 countries by confirmed:\n", analysis.top5_countries())
    print("\n6) Region with lowest deaths:", analysis.region_lowest_deaths())
    print("\n7) India summary:\n", analysis.india_summary())
    print("\n8) Mortality rate by region:\n", analysis.mortality_rate())
    print("\n9) Recovery rate by region:\n", analysis.recovery_rate())
    print("\n10) Outliers detected:\n", analysis.detect_outliers())
    print("\n11) Grouped by country and region:\n", analysis.group_by_country_region().head())
    print("\n12) Regions with zero recovered:\n", analysis.zero_recovered())
