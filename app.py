import logging
import os

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    logger = logging.getLogger()
    for i in xrange(10000):
        logger.info('hello world')
    target = os.environ.get('TARGET', 'World')
    return 'Hello {}!\n'.format(target)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
