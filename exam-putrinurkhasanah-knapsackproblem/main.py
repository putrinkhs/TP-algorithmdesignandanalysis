def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(capacity + 1):
            if weights[i - 1] <= j:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-weights[i-1]] + values[i-1])
            else:
                dp[i][j] = dp[i-1][j]

    # Traceback to find the selected items
    selected_items = []
    i, j = n, capacity
    while i > 0 and j > 0:
        if dp[i][j] != dp[i-1][j]:
            selected_items.append(i - 1)
            j -= weights[i-1]
        i -= 1

    return dp[n][capacity], selected_items

# Data barang
weights = [16, 4, 8, 6, 12, 10]
values = [72, 12, 24, 32, 18, 20]
capacity = 30

max_value, selected_items = knapsack(weights, values, capacity)

print(f"Nilai maksimum yang dapat dicapai: {max_value}")
print("Barang yang dipilih:")
for item in selected_items:
    print(f"Barang {chr(ord('A') + item)}")
