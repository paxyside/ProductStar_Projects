import urllib.request
import pandas as pd



#Присваеваем ссылку на датасет
url = "https://raw.githubusercontent.com/PacktPublishing/Pandas-Cookbook-Second-Edition/master/data/movie.csv"
filename = "movie.csv"

#Скачиваем дата сет
#urllib.request.urlretrieve(url, filename)

#Открываем файл дата сета
df = pd.read_csv("movie.csv")

#Посмотреть перые 5 строчек датасета
#print(df.head())

#Общая информация о колонках в дата сете
#print(f"The shape of data: {df.shape}") 

#Общая информация о дата сете
#df.info("movie.csv")

#Основные статистические данные о дата сете
#print(df.describe())

#Чистка и фильтрация данных, isna показывает заполненность(True or False), sum покажет колличество значений по колонкам
#print(df.isna().sum())

#Отсортируем те колонки, которые нужны нам и создадим копию
df_clean = df [[
     "color", "director_name", "duration", "gross", "genres", "country", "budget", 'imdb_score',
     'actor_1_name', 'title_year', 'movie_title'
 ]]
df_clean = df_clean.copy()
# print(df_clean)

#Выберем только интересующую нас колонку
#print(df_clean['color'].value_counts())
#Выбросим те строчки, которые не имеют значений
#print(f'Before .dropna(): {df_clean.shape}')
df_clean = df_clean.dropna()
#print(f'After .dropna(): {df_clean.shape}')

#Оставим только цветные фильмы
#df_clean[df_clean.color == 'Color'] - бинарная маска (True or False)
#print(df_clean[df_clean.color == "Color"])

df_clean = df_clean[df_clean.color == "Color"]
#print(df_clean.shape)

#Печать случайных из датасетов строчек
#print(df_clean.sample(5))

#Посмотрим топ-10 популярных актеров 
actor_counts = df_clean['actor_1_name'].value_counts()
#print(actor_counts.head(10))

#Посмотрим на количество фильмов по годам 
#print(df_clean['title_year'].value_counts().sort_index().plot(kind= 'bar', figsize=(15, 5)))

##%% команда для юпитера чтоб показать графики

#.groupby смотрим статистику для нескольких параметров
# Отсортируем список средних продажи фильмов по странам
#budget_by_country = df_clean.groupby("country")['gross'].mean()

#Сделаем топ-10 по убыванию
#print(budget_by_country.sort_values(ascending= False)[:10])

#Отсортируем по году и стране в топ-10 рейтинга
grouped_data = df_clean.groupby(['title_year', 'country'])['imdb_score'].mean()
#print(grouped_data)
#Вычисляем страну с наибольшим рейтингом для каждого года
top_country_peach_year = grouped_data.groupby('title_year').apply(lambda x: x.idxmax()[1])
#print(top_country_peach_year)
#print(top_country_peach_year.iloc[-20:])



#ВИЗУАЛИЗАЦИЯ
import matplotlib.pyplot as plt
#Создали график соотношений
# plt.scatter(df_clean['imdb_score'], df_clean['gross'])
# plt.ylabel('Gross')
# plt.xlabel('IMDB Score')
# plt.show()
#Сортируем по кассовым сборам
#print(df_clean.sort_values('gross', ascending= False).head())

#Создаем колонку с отсортированным рейтингом
df_clean['imdb_score_rounded'] = df_clean['imdb_score'].round()
# print(df_clean[['imdb_score', 'imdb_score_rounded']].sample(5))

# Посчитаем каждые кассовые сборы для округленного рейтинга
avg_cross_by_rating = df_clean.groupby('imdb_score_rounded')['gross'].mean()
# print(avg_cross_by_rating)

#Джойним данные
# Добавляем в датасет новую колонку, значение которой зависит от значения в уже существующей колонке imdb_score_roundet
df_clean = df_clean.join(avg_cross_by_rating, on='imdb_score_rounded',rsuffix='_avg_for_rating')
# print(df_clean.sample(3))

# Посмотрим насколько реальные кассовые сборы оправдали ожидаемые
df_clean['gross_factor'] = df_clean['gross'] / df_clean['gross_avg_for_rating']
# print(df_clean.sort_values('gross_factor',ascending=False).head(10))
# print(df_clean.sort_values('gross_factor',ascending=True).head(10))

print(df[(df.country == "France") & (df.title_year == 2010)]) 