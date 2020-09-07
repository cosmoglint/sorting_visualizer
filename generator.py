import random


#create a random list
def gen_list(size,max):
    random_list = random.sample(range(0,max),size)
    return random_list
