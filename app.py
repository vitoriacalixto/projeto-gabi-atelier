from flask import Flask, render_template

app = Flask(__name__)

quadros = [
    {'id': 1, 'imagem': 'quadro1.jfif'},
    {'id': 2, 'imagem': 'quadro2.jfif'},
    {'id': 3, 'imagem': 'quadro3.jfif'},
    {'id': 4, 'imagem': 'quadro4.jfif'},
]

ecobags = [
    {'id': 1, 'imagem': 'ecobag1.jpg'},
    {'id': 2, 'imagem': 'ecobag2.jpg'},
    {'id': 3, 'imagem': 'ecobag3.jpg'},
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/lista_quadros')
def lista_quadros():
    return render_template('lista_quadros.html', quadros=quadros)

@app.route('/lista_ecobags')
def lista_ecobags():
    return render_template('lista_ecobags.html', ecobags=ecobags)

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

if __name__ == '__main__':
    app.run(debug=True)