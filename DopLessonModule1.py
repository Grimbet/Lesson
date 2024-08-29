grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
new_students=sorted(list(students)) #переводим множество в список и сортируем его по алфавиту
avg_ball = [round(sum(sub)/len(sub),2) for sub in grades] #перебираем списки оценок grades и считаем средний балл,округляем до 2х знаков после запятой
print(dict(zip(new_students, avg_ball))) #выводим результат {'Aaron': 4.0, 'Bilbo': 2.25, 'Johnny': 4.0, 'Khendrik': 3.67, 'Steve': 4.8}