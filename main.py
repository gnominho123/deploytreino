import request
from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def inicio():
    return 'oi'

if __name__== 'main':
    port = int(os.getenv('PORT'), '5000')
    app.run(host='0.0.0.0',debug=True, port = port)


