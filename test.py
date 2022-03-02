from time import sleep
from instagram import Instagram
import random

login= ''
password= ''

if __name__ == "__main__":
    inst = Instagram()
    inst.login(username=login, password=password)

    with open('post.jpg', 'rb') as image:
        print(inst.post(image, caption=random.choice(['legal','legal_busy','legalchik','by_legalchik'])+'\n_Coded by legalchik_')['status'])
