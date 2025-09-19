import numpy as np

if __name__ == "__main__":
    # -------------------------
    # a) Generate synthetic data
    # -------------------------
    np.random.seed(42)  # for reproducibility
    data = np.random.randint(5, 51, size=(5, 50))  # 5 cycles × 50 tests
    print("Original Dataset (5 cycles × 50 tests):\n", data, "\n")

    # -------------------------
    # 1. Statistical Analysis
    # -------------------------
    avg_per_cycle = np.mean(data, axis=1)
    max_test = np.max(data)
    std_per_cycle = np.std(data, axis=1)

    print("1. Statistical Analysis")
    print("Average Execution Time per Cycle:", avg_per_cycle)
    print("Maximum Execution Time in Dataset:", max_test)
    print("Standard Deviation per Cycle:", std_per_cycle, "\n")

    # -------------------------
    # 2. Slicing Operations
    # -------------------------
    first_10_cycle1 = data[0, :10]
    last_5_cycle5 = data[4, -5:]
    alternate_cycle3 = data[2, ::2]

    print("2. Slicing Operations")
    print("First 10 tests from Cycle 1:", first_10_cycle1)
    print("Last 5 tests from Cycle 5:", last_5_cycle5)
    print("Every alternate test from Cycle 3:", alternate_cycle3, "\n")

    # -------------------------
    # 3. Arithmetic Operations
    # -------------------------
    add_cycles_1_2 = data[0] + data[1]
    sub_cycles_1_2 = data[0] - data[1]
    mul_cycles_4_5 = data[3] * data[4]
    div_cycles_4_5 = data[3] / data[4]

    print("3. Arithmetic Operations")
    print("Cycle1 + Cycle2 (element-wise):", add_cycles_1_2)
    print("Cycle1 - Cycle2 (element-wise):", sub_cycles_1_2)
    print("Cycle4 * Cycle5 (element-wise):", mul_cycles_4_5)
    print("Cycle4 / Cycle5 (element-wise):", div_cycles_4_5, "\n")

    # -------------------------
    # 4. Power Functions
    # -------------------------
    squared = np.power(data, 2)
    cubed = np.power(data, 3)
    sqrted = np.sqrt(data)
    logged = np.log(data + 1)

    print("4. Power Functions")
    print("Squared Dataset (first row):", squared[0, :10])
    print("Cubed Dataset (first row):", cubed[0, :5])
    print("Square Root Transformation (first row):", sqrted[0, :10])
    print("Logarithmic Transformation (first row):", logged[0, :10], "\n")

    # -------------------------
    # 5. Copy Operations
    # -------------------------
    shallow_copy = data.view()
    shallow_copy[0, 0] = 999
    print("5. Copy Operations")
    print("Shallow Copy Modification (Cycle1[0] = 999):")
    print("Original Data[0,0]:", data[0, 0])  # Will also be 999

    deep_copy = data.copy()
    deep_copy[0, 1] = 888
    print("Deep Copy Modification (Cycle1[1] = 888):")
    print("Original Data[0,1]:", data[0, 1])  # Will remain unchanged
    print()

    # -------------------------
    # 6. Filtering with Conditions
    # -------------------------
    cycle2_over30 = data[1, data[1] > 30]
    consistently_over25 = np.all(data > 25, axis=0)
    replaced_data = data.copy()
    replaced_data[replaced_data < 10] = 10

    print("6. Filtering with Conditions")
    print("Cycle2 tests > 30:", cycle2_over30)
    print("Tests consistently > 25 across all cycles:", np.where(consistently_over25)[0])
    print("Dataset after replacing <10 with 10 (first row):", replaced_data[0, :10])
