import timeit

def find_coins_greedy(coins:list[int], value):
    inp = sorted(coins.copy(),reverse=True)
    result = {}
    for coin in inp:
        count = value // coin
        if count > 0:
            value -= coin * count
            result[coin] = count

    if value > 0:
        return 'Нема Грошей!'
    
    return result

def find_min_coins(coins: list[int], value):
    inp = sorted(coins.copy())
    
    dp = [float('inf')] * (value + 1)
    dp[0] = 0
    
    coin_used = [-1] * (value + 1)
    
    for i in range(1, value + 1):
        for coin in inp:
            if coin <= i and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin
    
    if dp[value] == float('inf'):
        return 'Нема Грошей!'
    
    result = {}
    current = value
    while current > 0:
        coin = coin_used[current]
        result[coin] = result.get(coin, 0) + 1
        current -= coin
    
    return result



if __name__ == '__main__':
    coins = [50, 25, 10, 5, 2, 1]
    test_values = [113, 178, 506, 1024]
    
    print("=" * 70)
    print("COMPARISON OF GREEDY AND DYNAMIC PROGRAMMING ALGORITHMS")
    print("=" * 70)
    
    for value in test_values:
        print(f"\n{'=' * 70}")
        print(f"Testing with value: {value}")
        print(f"{'=' * 70}")
        
        # Greedy algorithm
        greedy_time = timeit.timeit(
            lambda: find_coins_greedy(coins, value),
            number=1000
        )
        greedy_result = find_coins_greedy(coins, value)
        
        # Dynamic programming algorithm
        dp_time = timeit.timeit(
            lambda: find_min_coins(coins, value),
            number=1000
        )
        dp_result = find_min_coins(coins, value)
        
        print(f"\nGreedy Algorithm:")
        print(f"  Result: {greedy_result}")
        print(f"  Time (1000 iterations): {greedy_time:.6f} seconds")
        print(f"  Average time: {greedy_time/1000:.9f} seconds")
        
        print(f"\nDynamic Programming Algorithm:")
        print(f"  Result: {dp_result}")
        print(f"  Time (1000 iterations): {dp_time:.6f} seconds")
        print(f"  Average time: {dp_time/1000:.9f} seconds")
        
        print(f"\nSpeed difference: DP is {dp_time/greedy_time:.2f}x slower than Greedy")
    
    print(f"\n{'=' * 70}")
