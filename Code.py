def do_something(number1, number2):
    number1 += 10
    number2 += 50

my_number = 15
my_second_number = 20

do_something(my_number, my_second_number)

print(my_number)
print(my_second_number)

def add_pokemon(pokemons_list, id, name):
    pokemons_list[id] = name

pokemons = {
    "144" : "bulbizare",
    "145" : "carapuce",
    "147" : "salamèche",
}

add_pokemon(pokemons, "148", 'rondoudou')
print(pokemons)

class Voiture:
    def __init__(self, marque):
        self.marque = marque

v1 = Voiture("Tesla")
v2 = v1
v2.marque = "BMW"
print(v1.marque)