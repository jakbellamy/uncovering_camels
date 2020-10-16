from os import listdir, system
from matplotlib import pyplot as plt
import numpy as np
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
cols = [at for at in list(df.columns.values) if at[1] != 'worth' and at[1] != 'gender']
attr_list = prompt_lister(cols)


def analyze():
    system('tput reset')
    at_in = input('[-] ' + ''.join([at[0] for at in attr_list]) + '\n[-] ')

    if not at_in.isdigit() or not 0 <= int(at_in) < len(attr_list):
        bad_in()

    val = cols[int(at_in)]

    x_min = min(df[val])
    x_max = max(df[val])
    x_mid = (x_min + x_max) / 2
    plt.xticks([x_min, x_mid, x_max])

    df.set_index(val, inplace=True)
    df.sort_index(inplace=True)

    selected = df['worth']
    coefficients, residuals, _, _, _ = np.polyfit(range(len(selected.index)), selected, 1, full=True)
    mse = residuals[0] / (len(selected.index))
    nrmse = np.sqrt(mse) / (selected.max() - selected.min())

    selected.plot()
    plt.plot([coefficients[0] * x + coefficients[1] for x in range(len(selected))])
    plt.show()

    system('tput reset')
    return input('[-] Press q + Enter to exit. Otherwise, hit Enter')


while True:
    again = analyze()
    if again == 'q':
        break

print('Thanks!')