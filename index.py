from os import listdir, system
from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
from helpers import bad_in, path, rem_ext, choose_filename, \
    choose_gender, choose_iterative, prompt_lister

system('tput reset')
print('[0] WELCOME [0] \n')

file_list = [(f"{i}) {rem_ext(file).upper()} | ", rem_ext(file)) for (i, file) in enumerate(listdir('./data'))]
file_prompt = '[-] Choose a File:\n[-] ' + ''.join([prompt[0] for prompt in file_list]) + '\n[-] '
starting_data = input('[-] Analyze with existing data, or generate new data?\n[-] 1) Existing | 2) New \n[-] ')

if not starting_data == '1' and not starting_data == '2':
    bad_in()

if starting_data == '1':
    file_choice = input(file_prompt)
    if not file_choice.isdigit() or not 0 <= int(file_choice) < len(file_list):
        bad_in()
    file = file_list[(int(file_choice))][1]
    print(f'\n[SELECTED FILEPATH] => {path(file)}\n')
else:
    system('tput reset')
    print('[EXECUTING SCRIPT] => ./gen_data.py\n')

    gender = choose_gender()
    iterative = choose_iterative()
    file = choose_filename(input)

    system(f'python3 gen_data.py {gender} {iterative} {file}')
    system('tput reset')
    print('[-] Data Generated!\n')
    print(f'\n[SELECTED FILEPATH] => {path(file)}\n')

df = pd.read_csv(path(file))
cols = [at for at in list(df.columns.values) if at != 'worth' and at != 'gender']
attr_list = prompt_lister(cols)


def analyze():
    system('tput reset')
    at_in = input('[-] ' + ''.join([at[0] for at in attr_list]) + '\n[-] ')
    if not at_in.isdigit() or not 0 <= int(at_in) < len(attr_list):
        bad_in()
    val = cols[int(at_in)]

    if val == 'age' or val == 'height':
        ax = sns.regplot(x=val, y='worth', data=df, fit_reg=True)
        ax.set_title(f"{'Women' if df.iloc[0]['gender'] == 'female' else 'Men'}" + f"'s Worth by {val.capitalize()}")
        ax.set_ylabel('Worth (In Camels)')
        plt.show()
        return input('\n\n[-] Press q + Enter to exit. Otherwise, hit Enter\n[-] ')
    else:
        ax = sns.boxplot(x=val, y="worth", data=df)
        ax.set_title(f"{'Women' if df.iloc[0]['gender'] == 'female' else 'Men'}" + f"'s Worth by {val.capitalize()}")
        ax.set_ylabel('Worth (In Camels)')
        plt.show()
        return input('\n\n[-] Press q + Enter to exit. Otherwise, hit Enter\n[-] ')

while True:
    again = analyze()
    if again == 'q':
        break

print('Thanks!')
