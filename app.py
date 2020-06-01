from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index_route():
    print('=> New request on INDEX route')
    return render_template('index.html')


@app.route('/about')
def about_route():
    print('=> New request on ABOUT route')

    return render_template('about.html')


@app.route('/user/<string:name>/<int:id>')
def user_route(name, id):
    return 'User page: ' + str(name) + ' ' + str(id)


if __name__ == "__main__":
    print("> Server start")
    app.run(debug=True)
