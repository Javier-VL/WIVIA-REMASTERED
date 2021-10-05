import random
import matplotlib.pyplot as plt

price_change = 23829382938

price_change =  price_change ** 2 / (1 + price_change ** 2)
Blues = plt.get_cmap('Blues')
print (Blues(price_change))

'''
random_seeds = {}

def id_to_random_color(number):
    if number in random_seeds.keys():
        return random_seeds[number]
    else:
        color = [random.random(), random.random(), random.random(), 1.0]
        random_seeds[number] = color
        return color

color=id_to_random_color(12323232323232323232323232323323232337)
print(color,"--",type(color))



random.seed(12323232323232323232323232323323232337)
seed= random.random()
print(seed)
print(round(seed,9))'''