from random import Random
from flask import (Flask, request)
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/random/<random_seed>/choice")
def _choice(random_seed):
    values = request.args.getlist('value')

    if random_seed == 'default':
        random_seed = None

    if not values:
        return {
            'status': 400,
            'detail': "'value' parameters must be specified"
        }, 400

    return {'value': Random(random_seed).choice(values)}


@app.route("/swagger.yaml")
def _swagger():
    return app.send_static_file('swagger.yaml')


if __name__ == "__main__":
    app.run()
