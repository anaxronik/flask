from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flaskDB.db'
db = SQLAlchemy(app)


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), nullable=False)
    intro = db.Column(db.String(300), nullable=False)
    text = db.Column(db.Text(300), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow())

    def __repr__(self):
        return '<Article %r>' % self.id


@app.route('/')
@app.route('/home')
def index_route():
    print('=> New request on INDEX route')
    return render_template('index.html')


@app.route('/about')
def about_route():
    print('=> New request on ABOUT route')
    return render_template('about.html')


@app.route('/posts')
def posts_route():
    print('=> New request on POSTS route')
    articles = Article.query.order_by(Article.date.desc()).all()
    return render_template('posts.html', articles=articles)


@app.route('/posts/<int:id>')
def post_detail_route(id):
    print('=> New request on POST DETAIL route')
    article = Article.query.get(id)
    return render_template('post_detail.html', article=article)


@app.route('/posts/<int:id>/delete')
def delete_post_route(id):
    print('=> New request on DELETE POST route, ID:', id)
    article = Article.query.get(id)
    try:
        db.session.delete(article)
        db.session.commit()
        return redirect('/posts')
    except:
        return 'Ошибка при удалении поста'


@app.route('/posts/<int:id>/edit',  methods=['POST', 'GET'])
def edit_post_route(id):
    print('=> New request on EDIT POST route, ID:', id)
    article = Article.query.get(id)
    if request.method == 'GET':
        return render_template('edit_article.html', article=article)
    elif request.method == 'POST':
        article.title = request.form['title']
        article.intro = request.form['intro']
        article.text = request.form['text']
        try:
            db.session.commit()
            return redirect('/posts')

        except expression as identifier:
            return 'Ошибка при редактировании'


@app.route('/create-article', methods=['POST', 'GET'])
def create_article_route():
    if request.method == 'POST':
        title = request.form['title']
        intro = request.form['intro']
        text = request.form['text']
        article = Article(title=title, intro=intro, text=text)

        try:
            db.session.add(article)
            db.session.commit()
            return redirect('/posts')
        except:
            return 'ERROR'
    else:
        return render_template('create_article.html')


if __name__ == "__main__":
    print("> Server start")
    app.run(debug=True)
