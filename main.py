from flask import Flask
import random
facts_list =[
    "La mayoría de las personas que sufren adicción tecnológica experimentan un fuerte estrés cuando se encuentran fuera del área de cobertura de la red o no pueden utilizar sus dispositivos",
    "Según un estudio realizado en 2018, más del 50% de las personas de entre 18 y 34 años se consideran dependientes de sus smartphones.",
    "El estudio de la dependencia tecnológica es una de las áreas más relevantes de la investigación científica moderna",
    "Elon Musk afirma que las redes sociales están diseñadas para mantenernos dentro de la plataforma, para que pasemos el mayor tiempo posible viendo contenidos"
]

app = Flask(__name__)

@app.route("/")

def hello_world():
    
    return '<a href="/quepro">¡mira</a>' '<h1>el pepe!</h1>' '<a href="/ramdom">¡Dato del dia</a>'
@app.route("/ramdom")
def ola1():
    return f'<p>{random.choice(facts_list)}</p>'
@app.route("/quepro")
def ola():
    return '<h1>Lol que loco</h1>'
@app.route("/secret")
def secreta():
    return '<h1>Que hace usted aqui</h1>'
app.run(debug=True)
