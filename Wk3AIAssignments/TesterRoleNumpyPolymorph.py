import numpy as np

# Base-like classes (not using inheritance here, polymorphism works by same method name)

class ManualTester:
    def analyze(self, data):
        # Prints the first 5 execution times
        print("ManualTester Analysis → First 5 Execution Times:", data[:5])


class AutomationTester:
    def analyze(self, data):
        # Prints the fastest test case (minimum time)
        print("AutomationTester Analysis → Fastest Test Time:", np.min(data))


class PerformanceTester:
    def analyze(self, data):
        # Prints the 95th percentile execution time
        print("PerformanceTester Analysis → 95th Percentile Time:", np.percentile(data, 95))


# Polymorphic function
def show_analysis(tester, data):
    tester.analyze(data)


if __name__ == "__main__":
    # Create sample test execution times (in seconds)
    execution_times = np.array([12, 8, 15, 7, 20, 25, 9, 18, 10, 30, 14, 22])

    # Create tester objects
    manual = ManualTester()
    automation = AutomationTester()
    performance = PerformanceTester()

    # Call analysis using the same function (polymorphism in action)
    show_analysis(manual, execution_times)
    show_analysis(automation, execution_times)
    show_analysis(performance, execution_times)
