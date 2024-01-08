from datetime import datetime
from random import randrange, choice
from datetime import timedelta


def random_date(start, end):
    """
    This function will return a random datetime between two datetime 
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)


def random_source(sources):
    """
    This function will return a random item from list.
    """
    return choice(sources)


d1 = datetime.strptime('2022-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')
# print((d1 - datetime(1970, 1, 1)).total_seconds())
d2 = datetime.strptime('2022-12-31 23:59:59', '%Y-%m-%d %H:%M:%S')

sources = ['A', 'A', 'A', 'B', 'B', 'C', 'D']
degree = range(150, 300)
deformation = range(-50, 100)

output = []

with open('experiment_02_01.csv', 'w') as f:
    for n in range(10000):
        out_str = str(random_date(d1, d2)) + ';' + random_source(sources) + ';' + str(random_source(degree)/10) + ';' + str(random_source(deformation)/100) + '\n'
        output.append(out_str)
        f.write(out_str)

print(output[:5])
