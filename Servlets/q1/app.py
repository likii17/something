'''
A web application that takes a name as input and on submit it shows a hello <name> page where name is taken from the  request. It shows the start time at the right top corner of the page and provides a logout button. On clicking this  button, it should show a logout page with Thank You <name > message with the duration of usage (hint: Use session to store name and time).
'''

from flask import Flask, render_template, request, session
from datetime import datetime

app = Flask(__name__)
app.secret_key='super'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        session['name'] = request.form['name']
        session['start_time'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if 'name' in session:
        return render_template('hello.html', name=session['name'])
    else:
        return render_template('index.html')

@app.route('/logout')
def logout():
    if 'name' in session:
        start_time = datetime.strptime(session['start_time'], '%Y-%m-%d %H:%M:%S')
        end_time = datetime.now()
        duration = end_time - start_time
        duration_str = str(duration)
        return render_template('logout.html', name=session['name'], duration=duration_str)
    else:
        return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)
