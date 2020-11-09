
import flask.json
import decimal
from solvers import SimpleSolver, GenericBin, GenericItem
from flask import Flask, request, jsonify


class DecimalJSONEncoder(flask.json.JSONEncoder):
    """
    Custom JSON encoder class to handle decimal numbers
    """
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return str(o)
        return super(DecimalJSONEncoder, self).default(o)


app = Flask(__name__)
app.json_encoder = DecimalJSONEncoder


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/solve', methods=['POST'])
def solve_instance():
    bins, items = parse_json(request.json)
    solution = solver.solve(bins, items)
    return jsonify(solution)


def parse_json(json_data):
    bins = list()
    items = list()

    for bin in json_data['bins']:
        bins.append(GenericBin(bin['name'], bin['width'], bin['height'], bin['depth'], bin['max_weight']))

    for item in json_data['items']:
        items.append(GenericItem(item['name'], item['width'], item['height'], item['depth'], item['weight']))

    return bins, items


if __name__ == '__main__':
    solver = SimpleSolver()
    app.run(host='0.0.0.0')
