def regression_function(xi):
    # Заданные вероятности
    probabilities = {1: [0.15, 0.3]}

    # Проверка, есть ли вероятности для заданного xi
    if xi in probabilities:
        eta_values = [1, 3, 6]
        regression_value = sum(
            eta * prob for eta, prob in zip(eta_values, probabilities[xi])
        )
        return regression_value
    else:
        return None  # Вероятности для xi не заданы


# Пример использования для xi=1
xi_value = 1
regression_result = regression_function(xi_value)

print(f"Функция регрессии для xi={xi_value}: {regression_result}")
