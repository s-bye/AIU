'''
2. Строгий преподаватель
★★☆☆☆

Дан массив с количеством ошибок, которое совершили студенты Skillbox в предыдущем ДЗ.
Сколько ошибок совершил максимально внимательный и аккуратный студент?

Верните `int` кол-во ошибок.

*Например*

```python
find_best_student_mistakes([9, 4,1, 8, 7,13, 6, 5])  # => 1
```
'''

def find_best_students_mistakes(students):

    smallest = min(students)
    print(smallest)
    return smallest

find_best_students_mistakes([9, 4,1, 8, 7,13, 6, 5])