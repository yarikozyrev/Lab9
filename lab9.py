
import random
import logging

logging.basicConfig(level=logging.INFO,
                    filename="my_log.log", format="%(asctime)s %(levelname)s %(message)s")

while True:
    try:
        N = int(input('Введите число максимальное число диапазона:  '))
        logging.info('n = {}'.format(N))
        assert N > 1
        logging.info('suitable')
        break
    except AssertionError:
        print('Число должно быть больше 1')
        logging.exception('less than 1')
    except ValueError:
        print('Ошибка ввода, попробуйте ещё раз')
        logging.exception('incorrect input')
while True:
    try:
        k = int(input('Введите количество попыток:  '))
        logging.info('k = {}'.format(k))
        assert k > 0
        break
    except AssertionError:
        print('Число должно быть больше 0')
        logging.exception('less than 0')
    except ValueError:
        print('Ошибка ввода, попробуйте ещё раз')
        logging.exception('incorrect input')
hidden_num = random.randint(1, N)
logging.info('hidden_num = {}'.format(hidden_num))

while k > 0:
    print('Осталось попыток - {}'.format(k))
    try:
        num = int(input('Введите загаданное число   '))
        logging.info('input num = {}'.format(num))
        assert 1 <= num <= N
        logging.info('suitable')
        if num == hidden_num:
            print('верно!\n')
            logging.info('the number is guessed')
            break
        else:
            k -= 1
            print('Вы не угадали')
            logging.info('the number isn\'t guessed')
            if num < hidden_num:
                print('Число {} МЕНЬШЕ загаданного числа'.format(num))
            else:
                print('Число {} БОЛЬШЕ загаданного чиисла'.format(num))
            if k == 0:
                print('Попытки закончились\n')
                logging.info('attempts ended')
    except AssertionError:
        print('Число должно быть в диапазоне от 1 до {}'.format(n))
        logging.exception('not in range')
    except ValueError:
        print('Ошибка ввода, попробуйте ещё раз')
        logging.exception('incorrect input')
