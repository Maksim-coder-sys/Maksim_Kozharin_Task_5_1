import sys

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б','9А']
if len(tutors) > len(klasses):
    len_list = len(tutors) - len(klasses)
    for l in range(len_list):
        klasses.append('None')
if len(klasses) > len(tutors):
    len_list = len(klasses) - len(tutors)
    for l in range(len_list):
        tutors.append('None')


gen = ((tutors[i],klasses[i]) for i in range(len(tutors)))

print(list(gen))

print(type(gen))