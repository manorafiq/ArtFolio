from flask import Flask, request, render_template

# Create a Flask web application instance
app = Flask(__name__)

# Configure session settings

# Connect to the SQLite database here

@app.route("/", methods=['GET'])
def index():
    
    render_template("index.html")


# Run the Flask application in debug mode
if __name__ == '__main__':
    app.run(debug=True)