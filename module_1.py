from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
    return 'Are you there, world? It\'s me, Ducky!'


# Favorite Animal
@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    return f'Wow, {users_animal} is my favorite animal, too!'



# Favorite dessert
@app.route('/dessert/<user_dessert>')
def favorite_dessert(user_dessert):
    return (f"How did you know I liked {user_dessert}?")

# Mad Libs
@app.route('/madlibs/<adjective>/<noun>')
def madlibs(adjective, noun):
    return (f"I saw a sailor driving his boat on the {adjective} waters. I later saw him steer his boat into a {noun} and crash!")

# Multiplying 
@app.route('/multiply/<number1>/<number2>')
def multiply_numbers(number1, number2):
    if number1.isdigit() and number2.isdigit():
        number1 = int(number1)
        number2 = int(number2)
        return (f"{number1} times {number2} is {number1 * number2}")
    else:
        return ("Invalid Inputs. Please try again by entering 2 Numbers.")
    
# Say N Times 
@app.route('/sayntimes/<word>/<n>')
def sayNtimes(word, n):
    if n.isdigit():
        n = int(n)
        display = (word + ' ') * n
        return display
    else: 
        return ("Invalid Input. Please try again by entering a word and a number.")
    
# Dice game 
@app.route('/dicegame')
def dicegame():
    import random
    roll = random.randint(1,6)

    if roll == 6:
        return (f"You rolled a 6. You won!")
    else:
        return (f"You rolled a {roll}. You Lost!")
    
if __name__ == '__main__':
    app.run(debug=True)
