from collections import defaultdict

QUARTER = 4
company = defaultdict(list)
total_profit = 0
avg_prof_per_year = defaultdict(int)

count = int(input("Введите кол-во предприятий > "))
for i in range(count):
    name = input("Введите название предприятия > ")
    for j in range(QUARTER):
        profit = int(input(f"Введите прибыль предприятия за {j + 1} квартал > "))
        company[name].append(profit)
        avg_prof_per_year[name] += profit
    avg_prof_per_year[name] /= QUARTER

for prft in avg_prof_per_year.values():
    total_profit += prft

print(f"Средняя прибыль за год для всех предприятий = {total_profit / count}")
print(f"Предприятия чья прибыль выше среднего:")
for name, profit in avg_prof_per_year.items():
    if profit > total_profit / count:
        print(f"\t{name}")
print(f"Предприятия чья прибыль ниже среднего:")
for name, profit in avg_prof_per_year.items():
    if profit < total_profit / count:
        print(f"\t{name}")