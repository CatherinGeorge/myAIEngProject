import pandas as pd

timelist = [10, 15, 20, 18, 25, 30, 22]
timeseries_index = ["TC1", "TC2", "TC3", "TC4", "TC5", "TC6", "TC7"]

timeseries = pd.Series(timelist, index = timeseries_index)
print("print time series: ", timeseries)

firstthree = timeseries.head(3)
print("first three: ", firstthree)

meanexecution_time = timeseries.mean()
print("print mean execution time:", meanexecution_time)

second_using_iloc = timeseries.iloc[1]
print("second using iloc:", second_using_iloc)

print("using loc print execution time for 'TC3':", timeseries.loc['TC3'])
