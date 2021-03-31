"""Module api_flask

"""

import flask
import db.databaseInflux as db

app = flask.Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    if 'time' in flask.request.args:
        time = int(flask.request.args['time'])
    else:
        return "Error: No time field provided. Please specify an time."
    return flask.jsonify(db.read_all_data(time))


@app.route('/idAgent', methods=['GET'])
def agent():
    if 'id' and 'time' in flask.request.args:
        id = int(flask.request.args['id'])
        time = int(flask.request.args['time'])
    else:
        return "Error: No id or time field provided. Please specify an id or time."

    return flask.jsonify(db.read_data_agent(time, id))


@app.route('/idAgent/hardware', methods=['GET'])
def agent_hardware():
    if 'id' and 'time' and 'hardware' in flask.request.args:
        id = int(flask.request.args['id'])
        time = int(flask.request.args['time'])
        hardware = str(flask.request.args['hardware'])
    else:
        return "Error: No time or id or field provided. Please specify an time or id or hardware."

    return flask.jsonify(db.read_data_agent_hardware(time, id, hardware))


def api_flask():
    app.config["DEBUG"] = True
    app.run()


def main():
    api_flask()


if __name__ == '__main__':
    main()
