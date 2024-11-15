import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        float_features = [float(x) for x in request.form.values()]
        final_features = [np.array(float_features)]
        prediction = model.predict(final_features)

        if prediction == 1:
            pred = 'POSITIVE CKD!!'
        else:
            pred = "NEGATIVE CKD..."
        output = pred

        return render_template('predict.html', prediction_text=output)
    else:
        return render_template('predict_form.html')


@app.route('/about')
def about():
    subscribed = True  # Assuming this variable controls subscription status
    return render_template('about.html', subscribed=subscribed)

@app.route('/subscribe', methods=['POST'])
def subscribe():
    # Handle subscription logic here
    return 'Subscription successful'  # Example response

if __name__ == "__main__":
    app.run(debug=True)
