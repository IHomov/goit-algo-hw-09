def find_coins_greedy(items, general_summ: int) -> dict:
    total_nominal = {}
    for item in sorted(items, reverse=True):  # сортуємо від найбільшого до найменшого
        if general_summ >= item:
            count = general_summ // item  # скільки монет цього номіналу влізе
            general_summ -= count * item  # зменшуємо суму
            total_nominal[item] = count   # додаємо у словник
    return total_nominal



# номінали монет
items = [50, 10, 2, 1]
# Сума яку потрібно видати покупцеві
general_summ = 121
# Виклик функції
print(find_coins_greedy(items, general_summ))  
