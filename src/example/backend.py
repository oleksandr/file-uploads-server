from flask import Flask, request, jsonify

app = Flask(__name__)
app.debug = False

@app.route('/upload', methods=['POST'])
def upload_file():
    """
    This is the place where you iterate through uploaded files,
    optionally process and relocate them (in either sync or async way).
    """
    app.logger.debug("upload_file() INVOKED. We have: request.files = %r" % request.files)
    return jsonify(status=u'OK', msg=u'This is just an example response.', fields=request.form)

if __name__ == '__main__':
    app.run()
