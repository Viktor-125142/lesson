"""Случайные приращения цен акций двух компаний за день и имеют совместное распределение, заданное таблицей:
Вопрос №1. Найти ковариацию.
Вопрос №2. Найти коэффициент корреляции. В ответ записать 3 знака после запятой. """

import numpy as np

# Заданные вероятности
probabilities = np.array([[0.3, 0.2], [0.1, 0.4]])

# Вычисление средних значений
E_xi = np.sum(np.array([-1, 1]) * np.sum(probabilities, axis=1))
E_eta = np.sum(np.array([-1, 1]) * np.sum(probabilities, axis=0))

# Вычисление средних значений произведений
E_xi_eta = np.sum(np.outer(np.array([-1, 1]), np.array([-1, 1])) * probabilities)

# Вычисление дисперсий
Var_xi = (
    np.sum(np.array([(-1) ** 2, 1**2]) * np.sum(probabilities, axis=1)) - E_xi**2
)
Var_eta = (
    np.sum(np.array([(-1) ** 2, 1**2]) * np.sum(probabilities, axis=0)) - E_eta**2
)

# Вычисление ковариации
covariance = E_xi_eta - E_xi * E_eta

# Вычисление коэффициента корреляции
correlation = covariance / np.sqrt(Var_xi * Var_eta)

# Вывод результатов с округлением
print(f"Ковариация: {covariance:.3f}")
print(f"Коэффициент корреляции: {correlation:.3f}")
