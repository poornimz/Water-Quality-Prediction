from flask import Flask, render_template, request
from joblib import load

app = Flask(__name__)

# Load the Random Forest model
print("Loading model...")
model = load(r'web_application\dn.joblib')
print("Model loaded successfully.")

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/blog.html')
def blog():
    return render_template('blog.html')

@app.route('/services.html')
def services():
    return render_template('services.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the pH value from the form
    ph = float(request.form['ph'])
    
    # Predict water potability
    prediction = model.predict([[ph]])
    
    # Determine the prediction result
    if prediction[0] == 0:
        result = "Non-Potable"
    else:
        result = "Potable"
    
    return render_template('result.html', ph=ph, result=result)

if __name__ == '__main__':
    app.run(debug=True)
