from flask import Flask, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from utils import data_fetch
from exceptions import too_many_requests
import exceptions
import re


app = Flask(__name__)
app.register_blueprint(exceptions.blueprint)
limiter = Limiter(app, key_func=get_remote_address)



@app.route('/api', methods=['GET'])
@limiter.limit("1/second")
def post_data():
    output = []

    symbol = request.args.get('symbol')
    data = re.split(', |,', symbol)

    for sym in data:
        output.append(data_fetch(sym))

    return jsonify(output)


@app.route('/', methods=['GET'])
@limiter.limit("1/second")
def index():
    return jsonify({'api_version': '1.0'})



if __name__ == '__main__':
    app.run(host='0.0.0.0')
