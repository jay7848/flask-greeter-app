from flask import Flask, request, render_template

<<<<<<< HEAD
app = Flask(__name__)  # ✅ Must be before @app.route
=======
app = Flask(__name__)
>>>>>>> 8418d093c3f3e11ca8343303485cd2c87ca42fd4

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/greet', methods=['POST'])
def greet():
    name = request.form.get('name', 'Guest')
<<<<<<< HEAD
    return f"""
    <html>
    <head>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
        <title>Greeting</title>
    </head>
    <body class="bg-light">
        <div class="container mt-5">
            <div class="alert alert-success text-center">
                <h1>Hello, {name}! 👋</h1>
                <p>Welcome to the Flask App.</p>
                <a href="/" class="btn btn-secondary mt-3">Go Back</a>
            </div>
        </div>
    </body>
    </html>
    """
=======
    return f'Hello, {name}! Welcome to the Flask App.'
>>>>>>> 8418d093c3f3e11ca8343303485cd2c87ca42fd4

if __name__ == '__main__':
    app.run(debug=True)
