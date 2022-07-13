from time import sleep
from instagram import Instagram


login= ''
password= ''

if __name__ == "__main__":
    inst = Instagram()
    inst.login(username=login, password=password)

    with open('post.jpg', 'rb') as image:
        res = inst.post(image, caption='legalchik \n_Coded by legalchik_')['status']
    
    print(res)
