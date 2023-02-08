import vk
import random
import time

ta = 'token1'
vl = 'token2'

msgs = ["Роллы!", "роллы", "Роллы", "Хочу роллы!", "Сет роллов!", "Роллы 😀", "Роллы 😊",
        "Роллы🍣"]
c = 0

while 1:

    if random.randint(1,10) < 6:
        access_token = ta
        print("ta", end=' ')
        msg=msgs[random.randint(0, 3)]
    else:
        access_token = vl
        print("vl", end=' ')
        msg = msgs[random.randint(5, 7)]

    api = vk.API(access_token=access_token, v='5.131')

    try:
        msg1 = msgs[random.randint(0, len(msgs) - 1)]
        api.wall.createComment(owner_id='-178294581', post_id="160514", message=f'{msg}')
        time.sleep(random.randint(11, 16))

        msg2 = msgs[random.randint(0, len(msgs) - 1)]
        #api.wall.createComment(owner_id='-193105636', post_id="303881", message=f'{msg}')

        c += 1
        print(c, "bbb39:", msg, "; e:", msg)
        time.sleep(random.randint(16, 30))
    except:
        print("\n [!] Error occurred!\n")
        time.sleep(45)