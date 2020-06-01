from flask import Flask

app = Flask(__name__)


@app.route('/')
def index_route():
    return 'Hello from index'


@app.route('/about')
def about_route():
    return 'Hello from about'


if __name__ == "__main__":
    print("> Server start")
    app.run(debug=True)
