number = int(input('Введите число для подбора пары: '))
def pair_selection(number):
    pair_ = []
    for i in range(1, number):
        for j in range(i+1,number):
            if number % (i + j) == 0:
                num = str(i) + str(j)
                pair_.append(num)
    return pair_
result = pair_selection
print('Пожалуйста ваш пароль для камня ', *pair_selection(number))

