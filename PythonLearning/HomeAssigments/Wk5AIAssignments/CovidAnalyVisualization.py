import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


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
        return df.fillna(0)


# ------------------------------
# Main Analysis Class
# ------------------------------
class CovidAnalysis(DataLoader, DataCleaner):
    def __init__(self, filename="country_wise_latest.csv"):
        DataLoader.__init__(self, filename)
        self.df = self.clean_data(self.df)

    # Example analysis (we already implemented 12 tasks in Assignment <1>)
    def sort_by_confirmed(self, out_path="sorted_by_confirmed.csv"):
        sorted_df = self.df.sort_values(by="Confirmed", ascending=False)
        sorted_df.to_csv(out_path, index=False)  # only one export
        return sorted_df


# ------------------------------
# Visualization & EDA Class
# ------------------------------
class CovidVisualization(CovidAnalysis):
    def __init__(self, filename="country_wise_latest.csv"):
        super().__init__(filename)

    # 1. Bar Chart of Top 10 Countries by Confirmed Cases
    def plot_top10_countries(self):
        top10 = self.df.nlargest(10, "Confirmed")[["Country/Region", "Confirmed"]]
        plt.figure(figsize=(10,6))
        plt.bar(top10["Country/Region"], top10["Confirmed"], color="skyblue")
        plt.xticks(rotation=45)
        plt.title("Top 10 Countries by Confirmed Cases")
        plt.xlabel("Country")
        plt.ylabel("Confirmed Cases")
        plt.tight_layout()
        plt.show()

    # 2. Pie Chart of Global Death Distribution by Region
    def plot_death_distribution(self):
        deaths_by_region = self.df.groupby("WHO Region")["Deaths"].sum()
        plt.figure(figsize=(7,7))
        plt.pie(deaths_by_region, labels=deaths_by_region.index, autopct="%1.1f%%", startangle=140)
        plt.title("Global Death Distribution by Region")
        plt.show()

    # 3. Line Chart comparing Confirmed and Deaths for Top 5 Countries
    def plot_top5_confirmed_vs_deaths(self):
        top5 = self.df.nlargest(5, "Confirmed")[["Country/Region", "Confirmed", "Deaths"]]
        plt.figure(figsize=(10,6))
        plt.plot(top5["Country/Region"], top5["Confirmed"], marker="o", label="Confirmed")
        plt.plot(top5["Country/Region"], top5["Deaths"], marker="o", label="Deaths", color="red")
        plt.title("Confirmed vs Deaths (Top 5 Countries)")
        plt.xlabel("Country")
        plt.ylabel("Cases")
        plt.legend()
        plt.show()

    # 4. Scatter Plot of Confirmed vs Recovered
    def plot_scatter_confirmed_vs_recovered(self):
        plt.figure(figsize=(8,6))
        plt.scatter(self.df["Confirmed"], self.df["Recovered"], alpha=0.6, color="green")
        plt.title("Confirmed Cases vs Recovered Cases")
        plt.xlabel("Confirmed")
        plt.ylabel("Recovered")
        plt.show()

    # 5. Histogram of Death Counts across all Regions
    def plot_histogram_deaths(self):
        plt.figure(figsize=(8,6))
        plt.hist(self.df["Deaths"], bins=20, color="orange", edgecolor="black")
        plt.title("Histogram of Death Counts")
        plt.xlabel("Deaths")
        plt.ylabel("Frequency")
        plt.show()

    # 6. Stacked Bar Chart for 5 Selected Countries
    def plot_stacked_bar_selected(self, countries=["India","US","Brazil","Russia","Spain"]):
        subset = self.df[self.df["Country/Region"].isin(countries)][["Country/Region","Confirmed","Deaths","Recovered"]]
        subset.set_index("Country/Region")[["Confirmed","Deaths","Recovered"]].plot(kind="bar", stacked=True, figsize=(10,6))
        plt.title("Confirmed, Deaths, and Recovered (Selected Countries)")
        plt.ylabel("Cases")
        plt.show()

    # 7. Box Plot of Confirmed Cases across Regions
    def plot_boxplot_confirmed_by_region(self):
        data = [group["Confirmed"].values for name, group in self.df.groupby("WHO Region")]
        plt.figure(figsize=(10,6))
        plt.boxplot(data, labels=self.df["WHO Region"].unique())
        plt.title("Boxplot of Confirmed Cases by Region")
        plt.ylabel("Confirmed Cases")
        plt.xticks(rotation=45)
        plt.show()

    # 8. Trend Line: India vs Another Country
    def plot_trendline_india_vs_country(self, other_country="US"):
        subset = self.df[self.df["Country/Region"].isin(["India", other_country])]
        plt.figure(figsize=(8,6))
        for country in ["India", other_country]:
            country_data = subset[subset["Country/Region"] == country]
            plt.plot(["Confirmed","Deaths","Recovered"], 
                     [int(country_data["Confirmed"]), int(country_data["Deaths"]), int(country_data["Recovered"])], 
                     marker="o", label=country)
        plt.title(f"Covid Case Trend: India vs {other_country}")
        plt.ylabel("Cases")
        plt.legend()
        plt.show()


# ------------------------------
# Main Execution
# ------------------------------
if __name__ == "__main__":
    viz = CovidVisualization(
        r"C:\Users\CATHERIN\Desktop\Aut_Project\AI Engineer Test Leaf\myAIEngProject\PythonLearning\HomeAssigments\Wk4AIAssignments\country_wise_latest.csv"
    )
 #Execution (run one by one)
    viz.plot_top10_countries()
    viz.plot_death_distribution()
    viz.plot_top5_confirmed_vs_deaths()
    viz.plot_scatter_confirmed_vs_recovered()
    viz.plot_histogram_deaths()
    viz.plot_stacked_bar_selected()
    viz.plot_boxplot_confirmed_by_region()
    viz.plot_trendline_india_vs_country("Brazil")
