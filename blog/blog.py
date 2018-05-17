from flask import Flask, render_template, redirect, request
from flask import url_for

app = Flask(__name__)
app.config['TEMPLATE_AUTO_RELOAD'] = True
app.jinja_env.add_extension('jinja2.ext.loopcontrols')

# @app.route('/')
# def hello_world():
#     return 'Hello World!'


# @app.route('/<age>')
# def is_logged_in(age):
#     return render_template('index.html',age = age)


# age = {'age':10}
#
#
# @app.route('/')
# def is_logged():
#     return render_template('index.html',**age)


# user_info = {'name':'jack', 'age':26, 'gender':'male'}
#
#
# @app.route('/')
# def get():
#     return render_template('index.html', user_info=user_info)


# users = [{'username':'jack'}, {'username':'michael'}]


# @app.route('/')
# def func():
#     return render_template('index.html', users=users)


# users = list(range(10))
#
# users = '<script> alert("Hello") </>'
#
#
# @app.route('/')
# def hi():
#     return render_template('index.html',users=users)


# @app.route('/')
# def index():
#     return render_template("child.html")

# @app.route('/<path:id>')
# def index(id):
#     return "hello %s" % id

# @app.route('/<any(home, detail):param>/<id>')
# def index(param,id):
#     if param=='home':
#         return "Welcome to my home %s" % id
#     elif param=='detail':
#         return "Welcome to my detail %s" % id


'''查询字符串'''


#
#
# @app.route('/')
# def index():
#     wd = request.args.get('wd')
#     kw = request.args.get('kw')
#     return 'query string is %s %s' % (wd, kw)

# @app.route('/')
# def index():
#     return url_for('hello', page=233, newkeyparam='sfqy')
#
#
# @app.route('/list/<page>')
# def hello(page):
#     return 'Hello %s' % page


if __name__ == '__main__':
    app.run(debug=True)
