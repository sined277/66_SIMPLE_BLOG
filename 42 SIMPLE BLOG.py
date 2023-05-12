from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/guess/<name>')
def home(name):
    # Construct the URL for the Genderize API, which returns gender based on first name
    gender_url = f"https://api.genderize.io?name={name}"
    # Send a GET request to the Genderize API and store the response
    gender_response = requests.get(gender_url)
    # Extract the JSON data from the response
    gender_data = gender_response.json()
    # Get the gender value from the JSON data
    gender = gender_data['gender']

    # Construct the URL for the Agify API, which returns age based on first name
    age_url = f"https://api.agify.io?name={name}"
    # Send a GET request to the Agify API and store the response
    age_response = requests.get(age_url)
    # Extract the JSON data from the response
    age_data = age_response.json()
    # Get the age value from the JSON data
    age = age_data['age']
    # Render the HTML template and pass the name, gender, and age variables to it
    return render_template('index.html', name=name, gender=gender, age=age)

if __name__ == '__main__':
    # Start the Flask application in debug mode
    app.run(debug=True)
