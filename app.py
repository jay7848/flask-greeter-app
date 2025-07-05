from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/greet', methods=['POST'])
def greet():
    name = request.form.get('name', 'Guest')
    return f'Hello, {name}! Welcome to the Flask App.'

if __name__ == '__main__':
    app.run(debug=True)
