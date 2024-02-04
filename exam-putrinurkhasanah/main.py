def count_change_ways(coins, target):
    # Inisialisasi array untuk menyimpan hasil perhitungan
    dp = [0] * (target + 1)
    dp[0] = 1  # Satu cara untuk membentuk nilai 0 (tidak menggunakan koin)

    # Loop untuk setiap koin
    for coin in coins:
        # Loop untuk setiap nilai dari koin hingga target
        for i in range(coin, target + 1):
            dp[i] += dp[i - coin]

    return dp[target]

def min_coins_required(coins, target):
    # Inisialisasi array untuk menyimpan jumlah minimum koin
    dp = [float('inf')] * (target + 1)
    dp[0] = 0  # Tidak ada koin yang dibutuhkan untuk membentuk nilai 0

    # Loop untuk setiap koin
    for coin in coins:
        # Loop untuk setiap nilai dari koin hingga target
        for i in range(coin, target + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[target] if dp[target] != float('inf') else -1  # Return -1 jika nilai tidak dapat dibentuk

# Uang koin pecahan
coins = [1, 2, 5, 10]

# Nilai yang ingin dibentuk
target_value = 26

# a. Apakah nominal 26 dapat dibentuk dari koin pecahan?
can_form_value = count_change_ways(coins, target_value)

# b. Berapa jumlah minimum koin untuk membentuk nilai 26?
min_coins = min_coins_required(coins, target_value)

# c. Berapa banyak kombinasi koin untuk membentuk nilai 26?
combinations = count_change_ways(coins, target_value)

# Output
print("a. Nominal 26 dapat dibentuk:", can_form_value > 0)
print("b. Jumlah minimum koin untuk nilai 26:", min_coins)
print("c. Banyak kombinasi koin untuk nilai 26:", combinations)
