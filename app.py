from flask import Flask, request, jsonify, abort

app = Flask(__name__)

teams = {} #teams db current
current_id = 1

@app.route('/')
def home():
    return 'Cargill Teams App Home page' 

@app.route('/teams', methods=['GET']) #Get Teams
def get_teams():
    return jsonify(list(teams.values()))

if __name__ == '__main__':
    app.run(debug=True)