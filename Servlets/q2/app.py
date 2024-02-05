'''
Write a Servlet application to print the current date and time.
'''
from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return f'<p>Current Date and Time: {current_time}</p>'
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)