from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Real Estate Housing Price Prediction Project</h1>
    <p>Your project is successfully deployed.</p>
    <p>Notebook: real_estate_regression_project.ipynb</p>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
