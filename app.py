from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Cargill default home page for TH interview'

if __name__ == '__main__':
    app.run(debug=True)