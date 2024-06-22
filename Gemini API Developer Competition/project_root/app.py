# app.py

from flask import Flask, render_template

app = Flask(__name__)

# Route for the index page
@app.route('/')
def index():
    return render_template('index.html')

# Route for the recommendations page
@app.route('/recommendations')
def recommendations():
    return render_template('recommendations.html')

if __name__ == '__main__':
    app.run(debug=True)
