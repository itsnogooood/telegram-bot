from man_to_woman import man_list
from woman_to_man import woman_list


def compare_man(user_dict):
    for element in man_list:
        print(user_dict)
        print(element)
        if element[0] == user_dict[0].strip() and element[1] == user_dict[1].strip():
            sign_one = 'Your sign is ' + str(element[0])
            sign_two = 'Your partners sing is ' + str(element[1])
            percents = 'Your compatibility is ' + str(element[2]) + '%'
            return sign_one + '\n' + sign_two + '\n' + percents


def compare_man_2(user_dict):
    if compare_man(user_dict) is None:
        print('Try again')


def compare_woman(user_dict):
    for element in woman_list:
        if element[0] == user_dict[0].strip() and element[1] == user_dict[1].strip():
            sign_one = 'Your sign is ' + str(element[0])
            sign_two = 'Your partners sing is ' + str(element[1])
            percents = 'Your compatibility is ' + str(element[2]) + '%'
            return sign_one + '\n' + sign_two + '\n' + percents


def compare_woman_2(user_dict):
    if compare_woman(user_dict) is None:
        print('Try again')


def choose_male(male, user_dict):
    if male == 'Male':
        return compare_man(user_dict)
    elif male == 'Female':
        return compare_woman(user_dict)
    else:
        raise ValueError('Not male or female')


if __name__ == '__main__':
    one = input(str('Type first sign '))
    two = input(str('Type second sign '))
    male = input(str('Type your male '))
    user_dict = (one, two)


    choose_male(male, user_dict)


