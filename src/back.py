from man_to_woman import man_list
from woman_to_man import woman_list

one = input(str('Type first sign '))
two = input(str('Type second sign '))
male = input(str('Type your male '))
user_dict = (one, two)


def compare_man():
    for element in man_list:
        if element[0] == user_dict[0].strip() and element[1] == user_dict[1].strip():
            print('Your sign is ' + str(element[0]))
            print('Your partners sing is ' + str(element[1]))
            print('Your compatibility is ' + str(element[2]) + '%')
            return element[2]


def compare_man_2():
    if compare_man() is None:
        print('Try again')
    else:
        pass


def compare_woman():
    for element in woman_list:
        if element[0] == user_dict[0].strip() and element[1] == user_dict[1].strip():
            print('Your sign is ' + str(element[0]))
            print('Your partners sing is ' + str(element[1]))
            print('Your compatibility is ' + str(element[2]) + '%')
            return element[2]


def compare_woman_2():
    if compare_woman() is None:
        print('Try again')
    else:
        pass


def choose_male():
    if male == 'Man':
        compare_man_2()
    if male == 'Woman':
        compare_woman_2()


choose_male()