from flask import Flask
from flask import request

app = Flask(__name__)
app.debug = False


@app.route('/')
def hello_world():
    return """<h1>Example File Uploads Handling Backend</h1>
This is just for demo purposes."""


@app.route('/upload', methods=['POST'])
def upload_file():
    app.logger.debug("upload_file() INVOKED")

    files = request.files
    app.logger.debug("request.files content: %r" % files)

if __name__ == '__main__':
    app.run()
