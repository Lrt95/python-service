"""Module api_flask

"""

import flask
import db.databaseInflux as db

app = flask.Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return flask.jsonify(db.read_all_data())


def api_flask():
    app.config["DEBUG"] = True
    app.run()


def main():
    api_flask()


if __name__ == '__main__':
    main()
