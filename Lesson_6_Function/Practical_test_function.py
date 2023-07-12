#Создаем список из 3 словарей
def average_age_by_gender(people, gender):
    ages = []
    for person in people:
        if person["gender"] == gender:
            ages.append(person["age"])
        if len(ages) > 0:
            avg_age = sum(ages) / len(ages)
        else:
            avg_age = 0

    return avg_age


#Вот как можно протестировать:
people = [
    {"name": "Alice", "age": 25, "gender": "F"},
    {"name": "Bob", "age": 30, "gender": "M"},
    {"name": "Charlie", "age": 35, "gender": "M"},
    {"name": "David", "age": 40, "gender": "M"},
    {"name": "Eve", "age": 45, "gender": "F"},
]

avg_age_females = average_age_by_gender(people, "F")
print("Average age for females:", avg_age_females)

avg_age_males = average_age_by_gender(people, "M")
print("Average age for males:", avg_age_males)