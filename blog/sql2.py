import config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(config)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.TEXT, nullable=False)


db.create_all()


@app.route('/')
def index():
    # article1 = Article(title='news', content='....')
    # db.session.add(article1)
    # db.session.commit()
    # article2 = Article(title='movies', content='?????')
    # db.session.add(article2)
    # db.session.commit()

    # dele1 = Article.query.filter(Article.content == '....').first()
    # db.session.delete(dele1)
    # db.session.commit()
    result = Article.query.all()
    print('.>>>>>>>>>>>>>>>>>>>', result)

    return 'helo world'


if __name__ == '__main__':
    app.run(debug=True)
