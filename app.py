import flask 
app = flask.Flask(__name__)
@app.route('/')
def hello_world():
    l=5
    return f'Hello, World! The value of l is {l}'
if __name__ == '__main__':
    app.run(debug=True)