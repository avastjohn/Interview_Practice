# given a list of employees, generate secret santas for each employees
# such that nobody is secret santa to themselves or to their own secret santa

from random import randrange

employees = ["Ava", "John", "Lindsey", "Alyssa", "David", "Christopher", "Gandhi", "Jabba", "Jack", "Isaac", "Ann", "Megatron", "The Admiral"]

def assign_santas(list_of_employees):
    if len(list_of_employees) < 3:
        return "Not enough santas"
    shuffled_list = []
    while list_of_employees:
        temp = list_of_employees.pop(randrange(len(list_of_employees)))
        shuffled_list.append(temp)
    santas = {}
    for i in range(len(shuffled_list) - 1):
        santas[shuffled_list[i]] = shuffled_list[i+1]
    santas[shuffled_list[-1]] = shuffled_list[0]
    return santas

print assign_santas(employees)