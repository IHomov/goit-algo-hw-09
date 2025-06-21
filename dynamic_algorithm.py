def find_min_coins(amount, coin_list):
    """
    Повертає словник з мінімальною кількістю монет для заданої суми.

    :param amount: сума для видачі (int)
    :param coin_list: список номіналів монет (list)
    :return: словник {номінал: кількість} або None, якщо не можна скласти суму
    """
    dp = [None] * (amount + 1)
    dp[0] = {}

    for current_sum in range(1, amount + 1):
        for coin in coin_list:
            if current_sum >= coin and dp[current_sum - coin] is not None:
                prev_combination = dp[current_sum - coin]
                new_combination = prev_combination.copy()
                new_combination[coin] = new_combination.get(coin, 0) + 1

                if dp[current_sum] is None or sum(new_combination.values()) < sum(dp[current_sum].values()):
                    dp[current_sum] = new_combination

    return dp[amount]

coins = [50, 10, 2, 1]
change = 113

result = find_min_coins(change, coins)
print(result)