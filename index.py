import pandas as pd
from Genders_Binary import Girl, Boy
from time import sleep
from random import randint as ran

#   Input Dialogues
def bad_in():
    print('Bad Input.\n')
    exit()


gender_choice = input('What Gender You Want?\n' +
                      '| 1. Girl | 2. Boy |\n')

if not gender_choice == '1' and not gender_choice == '2':
    bad_in()

iteration_input = input('How Many You Want to Make?\n')
if not iteration_input.isdigit():
    bad_in()

iterative = int(iteration_input)

filename = input('Type Filename\n')

#   Data Collection
data = []
count = 0
while count < iterative:
    if gender_choice == '1':
        person = Girl(age=ran(14, 70), height=ran(140, 220), haircolor=ran(0, 4), hairlength=ran(0, 2), boobsize=ran(0, 3), figure=ran(0, 4), eyecolor=ran(0, 3))
    else:
        person = Boy(age=ran(14, 70), height=ran(140, 220), haircolor=ran(0, 4), hairlength=ran(0, 2), eyecolor=ran(0, 3), beard=ran(0, 3), body=ran(0, 2))
    data += [person.__dict__]
    sleep(0.3)
    count += 1

df = pd.DataFrame(data)
print(df)

df.to_csv('./data/' + filename + '.csv')
print('complete!')
