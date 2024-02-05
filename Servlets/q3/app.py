'''
A web application that takes name and age from an HTML page. If the age is less than 18, it should send a page with “Hello <name>, you are not authorized to visit the site” message, where <name> should be replaced with the entered name. Otherwise it should send “Welcome <name> to this site” message.
'''

from flask import Flask, request, render_template

app = Flask (__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        age = int(request.form['age'])
        if age < 18:
            return f'<p>Hello {name}, you are not authorized to visit the site</p>'
        else:
            return f'<p>Welcome {name} to this site</p>'
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)