from flask import Flask
app = Flask(__name__)

import calendr.Calendar


@app.route("/")
def run():
    return 'penor'