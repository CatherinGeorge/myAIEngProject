import numpy as np

# Base class
class TestReport:
    def __init__(self, execution_times):
        # Store execution times as a NumPy array
        self.execution_times = np.array(execution_times)

    def average_time(self):
        # Calculate and return mean execution time
        return np.mean(self.execution_times)

    def max_time(self):
        # Return the maximum execution time
        return np.max(self.execution_times)


# Subclass inheriting from TestReport
class RegressionReport(TestReport):
    def __init__(self, execution_times):
        # Call parent class constructor
        super().__init__(execution_times)

    def slow_tests(self, threshold):
        # Return all tests taking more than threshold time
        return self.execution_times[self.execution_times > threshold]


if __name__ == "__main__":
    # Create a NumPy array with 10 execution times (example data in seconds)
    times = np.array([12, 8, 15, 7, 20, 25, 9, 18, 10, 30])

    # Create a RegressionReport object
    report = RegressionReport(times)

    # Display average execution time
    print("Average Execution Time:", report.average_time())

    # Display maximum execution time
    print("Maximum Execution Time:", report.max_time())

    # Display slow tests above a threshold (e.g., 15 seconds)
    threshold = 15
    print(f"Tests taking more than {threshold} seconds:", report.slow_tests(threshold))
