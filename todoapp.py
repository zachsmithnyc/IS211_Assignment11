from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

todo = ['Get Up', 'Brush Teeth', 'Wash Ass']

# templates need to be in a folder called "templates"
# The "templates" folder needs to be checked into the repo as well

#displays current to do list
#takes in new items 
@app.route('/')
def first_controller():
    return render_template('displaytodolist.html', todo = todo)


@app.route('/morehello')
def more_hello():
    return 'Hello Everybody!!!!!'


@app.route('/hello/')
@app.route('/hello/<username>')
def helloname(username=None):
    return render_template('hellotemplate.html', name=username)


@app.route('/helloaction', methods=['POST', 'GET'])
def hellaction():
    if request.method == 'POST':
        return render_template('hellotemplate.html', name=request.form['username'])


if __name__ == "__main__":
    app.run(debug=True)