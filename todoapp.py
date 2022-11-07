from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
import re

app = Flask(__name__)

todo = {}

# templates need to be in a folder called "templates"
# The "templates" folder needs to be checked into the repo as well

#displays current to do list
#takes in new items 
@app.route('/')
def first_controller():
    return render_template('displaytodolist.html', todo = todo)


@app.route('/submit', methods=['POST'])
def second_controller():
    task = request.form['task']
    email = request.form['email']
    priority = request.form['priority']

    if not re.search(r"(\.[a-z]{3}$|\.[a-z]{2}$)", email):
        print("invalid email")
        return redirect('/')
    elif not re.search(r"(high|medium|low)", priority):
        print("invalid priority")
        return redirect('/')
    else:
        task = {task: (email, priority)}
        todo.update(task)
        print(todo)
        return redirect('/')

@app.route('/clear', methods=['POST'])
def third_controller():
    todo.clear()
    return redirect('/')

#Extra Credit II
@app.route('/delete', methods=['POST'])
def fourth_controller():
    key = request.form['task']
    todo.pop(key)
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)