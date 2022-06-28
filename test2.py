import random
tp = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd')
ls = []
n = 0
while ls == []:
    for i in range(0,4):
        b = random.choice(tp)
        ls.append(b)
    n += 1
    if ls == [6,6,6,6]:
        print(f'运行了{n}次时中奖！！！')
        break
    else:
        ls = []

if ls == [6,6,6,6]:
    print('Congratulation to you!!!')
else:
    print('It so Pity!')





