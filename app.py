from flask import Flask, render_template
from data import Items

app = Flask(__name__)

Items = Items()

@app.route('/')
def index():
  return render_template('homepage.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/items')
def items():
  return render_template('items.html', items = Items)

@app.route('/item/<int:id>/')
def item(id):
  return render_template('item.html',id=id)


if __name__ == '__main__':
  app.run(host = '0.0.0.0', port = 7000, debug=True)