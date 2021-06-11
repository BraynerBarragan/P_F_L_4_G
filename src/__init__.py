from flask import Flask, render_template

app= Flask(__name__, template_folder='views')
app.secret_key ='CBZEkZPmgsCBZEkZPmgsPdrA3sVEb2PLu1pPdrA3sVEb2PLu1p'
from src.controllers import *

def create_app():
    app.run(debug = True, port="5100")

