
from solvers import DummySolver
from flask import Flask, request
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/solve', methods=['POST'])
def solve_instance():
    crates_list = parse_json(request.form['crates'])
    return solver.solve(crates_list)


def parse_json(json_data):
    return json_data    # TODO: document JSON data type


if __name__ == '__main__':
    solver = DummySolver()
    app.run(host='0.0.0.0')
