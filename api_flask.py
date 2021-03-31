"""Module api_flask

"""

import flask
import db.databaseInflux as db

app = flask.Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    """Function home generate the response with all information and utils time parameter in route

    :return: json all data
    """
    if 'time' in flask.request.args:
        time = int(flask.request.args['time'])
    else:
        return "Error: No time field provided. Please specify an time."
    return flask.jsonify(db.read_all_data(time))


@app.route('/idAgent', methods=['GET'])
def agent():
    """Function agent generate the response with all information of agent and utils time and id agent parameter in route

    :return: json all data's agent
    """
    if 'id' and 'time' in flask.request.args:
        id = int(flask.request.args['id'])
        time = int(flask.request.args['time'])
    else:
        return "Error: No id or time field provided. Please specify an id or time."

    return flask.jsonify(db.read_data_agent(time, id))


@app.route('/idAgent/hardware', methods=['GET'])
def agent_hardware():
    """Function agent_hardware generate the response with hardware information of agent
    and utils time and id agent and hardware parameter in route

    :return: json hardware data's agent
    """
    if 'id' and 'time' and 'hardware' in flask.request.args:
        id = int(flask.request.args['id'])
        time = int(flask.request.args['time'])
        hardware = str(flask.request.args['hardware'])
    else:
        return "Error: No time or id or field provided. Please specify an time or id or hardware."

    return flask.jsonify(db.read_data_agent_hardware(time, id, hardware))


def api_flask():
    """Function api_flask is the function principal api

    """
    app.config["DEBUG"] = True
    app.run()


def main():
    """Function main

    """
    api_flask()


if __name__ == '__main__':
    main()
