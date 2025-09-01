from flask import Flask, request, jsonify, abort

app = Flask(__name__)

teams = {} #teams db current
current_id = 1

@app.route('/') #homepage
def home():
    return 'Cargill Teams App Home page' 

@app.route('/teams', methods=['GET']) #Get Teams
def get_teams():
    return jsonify(list(teams.values()))

@app.route('/teams', methods=['POST']) #Create Team
def create_team():
    global current_id
    data = request.get_json()
    if 'name' not in data or not data['name']:
        return jsonify({'error': 'Name is required'}), 400
    team = {'id': current_id, 'name': data['name']}
    teams[current_id] = team
    current_id += 1
    return jsonify(team), 201

@app.route('/teams/<int:team_id>', methods=['GET']) #Get team by ID
def get_team(team_id):
    team = teams.get(team_id)
    if not team:
        return jsonify({'error': 'Team not found'}), 404
    return jsonify(team)

@app.route('/teams/<int:team_id>', methods=['PUT']) #Update team by ID
def update_team(team_id):
    team = teams.get(team_id)
    if not team:
        return jsonify({'error': 'Team not found'}), 404
    data = request.get_json()
    if 'name' not in data or not data['name']:
        return jsonify({'error': 'Name is required'}), 400
    team['name'] = data['name']
    teams[team_id] = team
    return jsonify(team)

@app.route('/teams/<int:team_id>', methods=['DELETE']) #Delete team by IDs
def delete_team(team_id):
    if team_id not in teams:
        return jsonify({'error': 'Team not found'}), 404
    del teams[team_id]
    return jsonify({'message': 'Team deleted'})
if __name__ == '__main__':
    app.run(debug=True)