import csv

with open('students.csv', 'wt') as csv_file:
    fieldnames = ['fio', 'id_task']
    writer = csv.DictWriter(csv_file, fieldnames)
    writer.writeheader()

    for i in (
            {'fio': 'Ситников Власий Яковлевич', 'id_task': -1},
            {'fio': 'Аксёнов Велорий Протасьевич', 'id_task': -1},
            {'fio': 'Лазарев Святослав Оскарович', 'id_task': -1},
            {'fio': 'Овчинников Осип Филатович', 'id_task': -1},
    ):
        writer.writerow(i)
