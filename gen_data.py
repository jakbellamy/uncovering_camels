import pandas as pd
from Genders_Binary import Girl, Boy
from random import randint as ran
from helpers import choose_gender, choose_iterative, choose_filename
import sys

if len(sys.argv) == 1:
    gender_choice = choose_gender()
    iterative = int(choose_iterative())
    filename = choose_filename(input)
else:
    gender_choice = sys.argv[1]
    iterative = int(sys.argv[2])
    filename = sys.argv[3]

data = []
count = 0
while count < iterative:
    if gender_choice == '1':
        person = Girl(age=ran(14, 70), height=ran(140, 220), haircolor=ran(0, 4), hairlength=ran(0, 2),
                      boobsize=ran(0, 3), figure=ran(0, 4), eyecolor=ran(0, 3))
    else:
        person = Boy(age=ran(14, 70), height=ran(140, 220), haircolor=ran(0, 4), hairlength=ran(0, 2),
                     eyecolor=ran(0, 3), beard=ran(0, 3), body=ran(0, 2))
    data += [person.__dict__]
    count += 1

df = pd.DataFrame(data)
print(df)

print('File Created.')
