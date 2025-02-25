from flask import Flask, render_template, request
import re

app = Flask(__name__)

def verifier_restrictions(mot_de_passe):
    restrictions = []
    if len(mot_de_passe) < 12:
        restrictions.append("Le mot de passe doit contenir au moins 12 caractères.")
    if not re.search(r'[A-Z]', mot_de_passe):
        restrictions.append("Le mot de passe doit contenir au moins une majuscule.")
    if not re.search(r'[0-9]', mot_de_passe):
        restrictions.append("Le mot de passe doit contenir au moins un chiffre.")
    if not re.search(r'[@$!%*?&]', mot_de_passe):
        restrictions.append("Le mot de passe doit contenir au moins un caractère spécial.")
    return restrictions

@app.route('/', methods=['GET', 'POST'])
def index():
    restrictions_non_respectees = None
    if request.method == 'POST':
        mot_de_passe = request.form['password']
        restrictions_non_respectees = verifier_restrictions(mot_de_passe)
    return render_template('index.html', restrictions=restrictions_non_respectees)

if __name__ == '__main__':
    app.run(debug=True)