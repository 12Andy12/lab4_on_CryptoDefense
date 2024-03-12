from random import randint

def gcd(a, b):
    u = [a, 1, 0]
    v = [b, 0, 1]
    while v[0] != 0:
        q = u[0] // v[0]
        t = [u[0] % v[0], u[1] - q * v[1], u[2] - q * v[2]]
        u = v
        v = t
    return u


def gcd_light(a, b):
    if b == 0:
        return a
    return gcd_light(b, a % b)

def ferma(x):
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for i in range(0, 100):
        a = randint(2, x - 2)
        if gcd_light(a, x) != 1:
            return False
        if pow(a, x - 1, x) != 1:
            return False
    return True

def generate_simple_number(left, right):
    result = randint(left, right)

    while ferma(result) == False:
        result = randint(left, right)

    return result

def generate_friend_simple_numper(p):
    result = generate_simple_number(2, p)

    while gcd_light(p, result) != 1:
        result = generate_simple_number(2, p)

    return result

class player():
    def __int__(self):
        self.name = "defalt_name"
        self.money = 0
        self.card1 = ""
        self.card2 = ""
        self.P = 0
        self.__C = 0
        self.__D = 0

    def generate_parametrs(self):
        self.__C = generate_friend_simple_numper(self.P - 1)
        self.__D = gcd(self.__C, self.P - 1)[1]
        if self.__D < 0:
            self.__D += (self.P - 1)

    def decrypt(self, card):
        return pow(card, self.__C, self.P)


    def encrypt(self, card):
        return pow(card, self.__D, self.P)