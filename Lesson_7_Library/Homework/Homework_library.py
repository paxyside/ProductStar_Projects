import pandas as pd

#Открываем файл дата сета
df = pd.read_csv("vgsales.csv")
#Проверяем,что датасет корректно загрузился
# print(df.head())

# #Найдем уникальные игры в датасете
unique_games = df['Name'].unique()
# print(unique_games)

# #Посмотрим, сколько уникальных игр представлено в этом датасете
unique_games_count = df['Name'].nunique()
# print('Количество уникальных вещей: ', unique_games_count)
# #11493

#Посчитаем общую величину продаж игр в Японии
gen_sales_in_JP = df["JP_Sales"].sum()
# print(gen_sales_in_JP)
# 1291.02.. миллионов

# Посмотрим какие три жанра игр самые популярные в Северной Америке (по количеству продаж)
most_popular_in_NA = df.groupby("Genre") ["NA_Sales"].sum()
# print(most_popular_in_NA.sort_values(ascending= False)[:3])

# Самая популярная платформа в 2000 г./ 2015 г.
most_popular_platf_in2000 = df[df['Year'] == 2000].groupby('Platform')['Year'].count()
# print(most_popular_platf_in2000.sort_values(ascending= False))
# PS
most_popular_platf_in2015 = df[df['Year'] == 2015].groupby('Platform')['Year'].count()
# print(most_popular_platf_in2015.sort_values(ascending= False))
# PS4

# Посмотрим какой разработчик выпустил больше всего игр в период с 2012 по 2015 год включительно
publisher_games_count = df[(df['Year'] >= 2012) & (df['Year'] <=2015)].groupby('Publisher').size()
# print(publisher_games_count.idxmax())
# Namco Bandai Games

# Узнаем какой процент игр в жанре спорт был продан в Европе
percent_sales_in_EU = round(df[df['Genre'] == 'Sports']['EU_Sales'].sum() / df[df['Genre'] == 'Sports']['Global_Sales'].sum() * 100, 2)
print("Процент продаж в жанре 'Спорт' в Европе: {}%".format(percent_sales_in_EU))