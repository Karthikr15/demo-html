from flask import Flask , render_template, request


app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to the Flask App!"


@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about')
def index():
    return render_template('about.html')

@app.route('/forms')
def index():
    return render_template('forms.html')

@app.route('/services')
def index():
    return render_template('services.html')


if __name__ == '__main__':
    app.run(debug=True)