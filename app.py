# app.py
from flask import Flask, render_template, request
import pickle
import numpy as np


app = Flask(__name__)

# Load the model
with open('modelv4.pkl', 'rb') as file:
    model = pickle.load(file)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    print("About page requested")
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/user_i', methods=['GET', 'POST'])
def user_i():
    if request.method == 'POST':
        age = int(request.form['age'])
        pr = float(request.form['pr'])
        bp = float(request.form['bp'])
        gl = float(request.form['gl'])
        bmi = float(request.form['bmi'])
        dpf = float(request.form['dpf'])
        insulin = float(request.form['insulin'])
        sk = float(request.form['sk'])

       
        # Create a feature array
        features = np.array([[age, pr, bp, gl, bmi, dpf, insulin, sk]])

        # Make a prediction
        prediction = model.predict(features)

        # Return the prediction result
        result = 'Diabetes' if prediction[0] == 1 else 'No Diabetes'
        return render_template('user_i.html', result=result)

    return render_template('user_i.html')


if __name__ == '__main__':
    app.run(debug=True)


