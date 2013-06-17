from flask import Flask, request, render_template
from markdown import markdown

app = Flask(__name__)

@app.route('/md', methods=['POST', 'GET'])
def md():
    if request.method == 'GET':
        return render_template('view.html')
    return markdown(request.form['text'])

app.run(host='0.0.0.0', debug=True)