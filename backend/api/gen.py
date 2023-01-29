import random
def get_code():
    a = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
    'q','r','s','t','u','v','w','x','y','z']
    b = [1,2,3,4,5,6,7,8,9]
    var = ''
    for i in range(15):
        var += random.choice(a)
        var += str(random.choice(b))
    return var