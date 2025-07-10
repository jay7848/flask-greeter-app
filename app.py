from flask import Flask, request, render_template

app = Flask(__name__)  # ✅ Must be before @app.route

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/greet', methods=['POST'])
def greet():
    name = request.form.get('name', 'Guest')
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)  # ✅ Added host/port for external access
