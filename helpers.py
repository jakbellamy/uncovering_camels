def bad_in():
    print('[-] Bad Input.\n[-] ')
    exit()


path = lambda filename: f'./data/{filename}.csv'
rem_ext = lambda filename: filename.split('.csv')[0]
prompt_lister = lambda lst: [(f"{i}) {x} | ", x) for (i, x) in enumerate(lst)]


def choose_gender():
    gender_choice = input('[-] What Gender You Want?\n' +
                          '[-] | 1. Girl | 2. Boy |\n[-] ')

    if not gender_choice == '1' and not gender_choice == '2':
        bad_in()

    return gender_choice


def choose_iterative():
    iteration_input = input('[-] How Many You Want to Make?\n[-] ')
    if not iteration_input.isdigit():
        bad_in()
    return iteration_input


choose_filename = lambda fun: fun('[-] Filename? (.csv already included)\n[-] ')
