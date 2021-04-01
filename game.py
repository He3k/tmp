import random


while 0 == 0:
    c = 0
    a = random.randint(0, 9)
    if a == 0:
        question = "Всему голова"
        answer_true = "хлеб"

    elif a == 1:
        question = "Висит груша, нельзя скушать"
        answer_true = "лампочка"

    elif a == 3:
        question = "Зимой и летом одним цветом"
        answer_true = "ёлка"

    elif a == 4:
        question = "Сидит дед в 100 шуб одет"
        answer_true = "лук"

    elif a == 5:
        question = "100 одёжек, все без застёжек"
        answer_true = "капуста"

    elif a == 6:
        question = "Царь мира"
        answer_true = "Путин"
    elif a == 7:
        question = "Сделал из обезьяны человека"
        answer_true = "труд"

    elif a == 8:
        question = "Что вставляют в колеса"
        answer_true = "палки"

    elif a == 9:
        question = "Японская водка"
        answer_true = "саке"
    else:
        question = "Как зовут создателя"
        answer_true = "Никита"

    print(question)
    print(answer_true)

    while c < 3:
        invite = input('Введите ответ ')
        if invite == answer_true:
            print('Черепаший суп, вы выйграли')
            c = 3
        elif c < 2:
            print('Неее, попробуй еще раз)')
            c = c+1
            print('Попыток осталось: ', 3-c)
        else:
            print('Вы проиграли, хехехе')
            break

    ex = input('Продолжаем? (Y/n) ')
    if ex == 'n':
        break
    else:
        print('Отлично!')
