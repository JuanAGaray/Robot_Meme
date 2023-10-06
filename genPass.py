import random

def gen_pass(n):
    elements = "qwertyuiopasdfghjklñzxcvbnm,QWERTYUIOPASDFGHJKLZXCVBNM;+-/*!&$#?=@<>"
    password = ""

    for i in range(n):
        password += random.choice(elements)

    return password
