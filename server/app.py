from flask import Flask

# Setting up flask app    
app = Flask(__name__)

@app.route('/')
def home():
        return "This is my backend!"


if __name__ == '__main__':
    app.run(debug=True)
