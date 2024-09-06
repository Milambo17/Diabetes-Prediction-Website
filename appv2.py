# app.py
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Define the prediction function
def predict_diabetes(age, pr, bp, gl, bmi, dpf, insulin, sk):
    if gl > 140 or bmi > 30 or age > 40 or dpf > 0.5:
        return 1  # Diabetic
    elif (gl > 120 and (bmi > 25 or age > 35)) or (insulin > 150 and bp > 70):
        return 1  # Diabetic
    else:
        return 0  # Non-Diabetic

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
        data = request.get_json()
        age = float(data['age'])
        pr = float(data['pr'])
        bp = float(data['bp'])
        gl = float(data['gl'])
        bmi = float(data['bmi'])
        dpf = float(data['dpf'])
        insulin = float(data['insulin'])
        sk = float(data['sk'])
        
        # Predict diabetes using the rule-based function
        prediction = predict_diabetes(age, pr, bp, gl, bmi, dpf, insulin, sk)
        
        # Return the prediction result as JSON
        result = 'Diabetes' if prediction == 1 else 'No Diabetes'
        return jsonify({'result': result})

    return render_template('user_i.html')

if __name__ == '__main__':
    app.run(debug=True)
