from flask import Flask, request, render_template, jsonify

app = Flask(__name__)
app.debug = False


@app.route('/')
def hello_world():
    return """<h1>Example File Uploads Handling Backend</h1>
This is just for demo purposes."""

@app.route('/form', methods=['GET'])
def demo_form():
    return render_template('form.html'), 200

@app.route('/upload', methods=['POST'])
def upload_file():
    app.logger.debug("upload_file() INVOKED. We have: request.files = %r" % request.files)
    return jsonify(status=u'OK', msg=u'This is just an example response.', fields=request.form)

if __name__ == '__main__':
    app.run()
