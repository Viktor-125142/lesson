import time
import pandas as pd

# Задаем статичную часть ссылки для парсинга
URL = "https://www.banki.ru/banks/ratings/?PAGEN_1="

# Создаем пустой датафрейм
df = pd.DataFrame()

# Задаем цикл, так как нужно спарсить с 1 по 8 страницы
for i in range(1, 9):
    # Кладем в переменную результат парсинга страницы i (список датафреймов со страницы)
    list_df_page = pd.read_html(URL + str(i), encoding="cp1251")

    # Конкатенируем основной датафрейм и нулевой датафрейм из списка (результат парсинга страницы i)
    df = pd.concat([df, list_df_page[0]], ignore_index=True)

    # Пауза 1 секунда, чтобы не банили
    time.sleep(1)
print(df)
