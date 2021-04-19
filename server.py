from flask import Flask
import sys
sys.path.insert(1, './app')

from PH import PH
from connector import Connector

app = Flask(__name__)

@app.route('/20')
def index():
    PH().handle({'code': 20, 'from': 1})
    return 'It works'

@app.route('/21')
def c21():
    PH().handle({'code': 21, 'dialog_id': 4})
    return 'something'

if __name__ == "__main__":
    Connector().connect()
    app.run(debug=True)

