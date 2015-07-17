from random import choice

from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

# route to handle the landing page of a website.
@app.route('/')
def start_here():
    return "Hi! Ok, you need to click <a href='/hello'>here</a>, trust me."

# route to display a simple web page
@app.route('/hello')
def say_hello():
    return render_template("hello.html")

@app.route('/greet')
def greet_person():
    player = request.args.get("person")

    AWESOMENESS = [
        'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
        'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html", person=player, compliment=compliment)

@app.route('/game')
def show_game_form():
    answer = request.args.get('game-status')
    if answer == "no":
         return render_template("goodbye.html")
    else:
        return render_template("game.html")

@app.route('/madlib')
def show_madlib():
    VERBS = ['fly','eat','learn','jump']
    verb = request.args.getlist('verb')
    verb1 = choice(verb)
    verb2 = choice(verb)
    verb3 = choice(verb)
    verb4 = choice(verb)
    color = request.args.get('color')
    noun = request.args.get('noun')
    personmad = request.args.get('personmad')
    adjective = request.args.get('adjective')
    return render_template('madlib.html', color=color, noun=noun, personmad=personmad, adjective=adjective, verb1=verb1, verb2=verb2, verb3=verb3, verb4=verb4)



if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
