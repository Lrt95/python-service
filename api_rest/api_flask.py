"""Module api_flask

"""

import flask
import db.databaseInflux as db

app = flask.Flask(__name__)


@app.route('/', methods=['GET'])
def agent_hardware():
    """Function agent_hardware generate the response with hardware information of agent
    and utils time and id agent and hardware parameter in route

    :return: json hardware data's agent
    """
    id = ""
    time = "24h"
    hardware = ""
    element = ""

    if 'id' in flask.request.args:
        id = str(flask.request.args['id'])

    if 'time' in flask.request.args:
        time = str(flask.request.args['time'])

    if 'hardware' in flask.request.args:
        hardware = str(flask.request.args['hardware'])

    if 'element' in flask.request.args:
        element = str(flask.request.args['element'])

    if not flask.request.args:
        return "Error: No time or id or field provided. Please specify an time or id or hardware."

    return flask.jsonify(db.read_data(time, id, hardware, element))


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
