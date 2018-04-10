from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('homepage.html')


if __name__ == '__main__':
  app.run(host = '0.0.0.0', port = 7000, debug=True)