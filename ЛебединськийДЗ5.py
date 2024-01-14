"""1. Створити словник оцінок передбачуваних студентів
(Ключ – ПІ студента, значення – список оцінок студентів).
Знайти найуспішнішого і самого слабенького за середнім балом."""
import statistics
report_card = {"Lebedinskii Serhii": [5,4,5,4,5],
               "Stryzhak Diana": [4,4,5,4,5],
               "Shevchenko Anna": [3,2,3,5,5]
                }
students_mean = {}
for students, marks in report_card.items():
    mean = statistics.mean(marks)
    students_mean.setdefault(students)
    students_mean[students] = mean
students_mean_sort = dict(sorted(students_mean.values()))
print(students_mean_sort)



