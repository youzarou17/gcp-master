from flask import flask

app = flask(__name__)

@app.route('/')
def index ():
    return 'welcome to python flask app v1.0'

if __name__ ==  '__main__':
    app.run(host='0.0.0.0', port=8080)