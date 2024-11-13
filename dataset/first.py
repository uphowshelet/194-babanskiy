import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv('C:\\prog\\py\\yandex_tracks_top100.csv')

## !вывод первых 10 песен в топе!
# print(df.head(10))


#!вывод последних 10 песен в топе!
# print(df.tail(10))


# #!информация о датасете!
# print(df.info())


# #!cтатистика по числовым столбцам!
# print(df.describe())

# #!выводит один столбец!
# print(df['genre'])


# # !вывод графика на первых 10 песен!
# top = df['genre'].value_counts().head(10) 
# # df['genre'] выбирает столбец genre из DataFrame df
# # value_counts() подсчитывает количество вхождений genre
# # top переменная в которую сохраняется результат
# plt.figure(figsize=(12, 8))
# #создает окно с графиком(12,8)
# sns.barplot(x=top.values, y=top.index, palette='viridis')
# # sns.barplot cоздает график с использованием библиотеки Seaborn
# # x=top_genre.values значения которые будут отображаться на оси х (количество песен)
# # y=top_genre.index значения которые будут отображаться на оси у (жанры)
# # palette='viridis' цвет (viridis)
# plt.xlabel('кол-во песен')
# #делает подпись
# plt.ylabel('жанры')
# plt.title('Топ 10 жанров')
# plt.show()
# #выводит график на экран
# top
# #переменная в которой всё


# df_sorted = df.sort_values(by='artists_likes_total', ascending=0)
# # cортирует DataFrame df по столбцу artists_likes_total по убыванию

# plt.figure(figsize=(12, 8))
# #создает график(12,8)

# sns.scatterplot(data=df_sorted, x='monthly_listens_total', y='artists_likes_total', hue='Explicit_content', palette="viridis")
# for i, row in df_sorted.head(10).iterrows():
#     #выбирает первые 10 строк(проходит по ним фором)

#     plt.annotate(row['name'], (row['monthly_listens_total'], row['artists_likes_total']),
#         #добавляет к точкам названия       

#          fontsize=12, xytext=(-10, 10), textcoords='offset points', ha='center')
#         #frontsize-размер шрифта над точками
#         #xytext-смещение текста относительно точки 

# plt.xlabel('ежемесячные слушатели')
# plt.ylabel('популярные артисты')
# plt.title('самые популярные треки')
# plt.show()

























