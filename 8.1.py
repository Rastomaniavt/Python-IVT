from statistics import mean

peoples = {"Иванов": 20, "Сидоров": 68, "Петров": 26, "Смирнов": 68,"Федоров": 40,"Волков": 52,"Анкифоров": 2,"Гусев": 100,"Прокофьев": 84 }
sr = mean(peoples.values())
mn = min(peoples.values())
mx = max(peoples.values())
for key, val in peoples.items():
    if val > sr:
      print("Балл выше среднего:",key, val)
for key, val in peoples.items():
    if val == mn:
      print("Минимальный балл:",key, val)
for key, val in peoples.items():
    if val == mx:
      print("Максимальный балл:",key, val)
print("Средний балл:",sr)
