"""
CP1404 Practical 10
Flask use case program
Henry Vooren 2021
"""

from flask import Flask

app = Flask(__name__)

"""
@app.route('/')
def hello_world():
    return '<h1>Hello World :)</h1>'
"""
"""
@app.route('/greet/<name>')
def greet(name=""):
    return "Hello {}".format(name)
"""


def convert_temperatures(output, degrees):
    if output == 'f':
        return degrees*(9/5)+32
    elif output == 'c':
        return (5/9)*(degrees-32)


# @app.route('/<measure>/<degrees>')
# def convert(output='c', degrees=0):
#    return '{} converted to {} = {}'.format(degrees, output, convert_temperatures(output, float(degrees)))


if __name__ == '__testing__':
    app.run()
