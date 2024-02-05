from flask import Flask, render_template, request, make_response, redirect

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_cookies():
    # Get all cookies from the request
    cookies = request.cookies.items()

    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>List Cookies</title>
    </head>
    <body>
        <h1>List of Cookies</h1>
    """

    if cookies:
        html_content += "<ul>"
        for key, value in cookies:
            html_content += f"<li>{key} : {value}</li>"
        html_content += "</ul>"
    else:
        html_content += "<p>No cookies found!</p>"

    # Include a button to redirect to setcookies route
    html_content += """
        <form action="/setcookies" method="get">
            <button type="submit">To set Cookies, click here</button>
        </form>
    </body>
    </html>
    """

    return html_content

@app.route('/setcookies', methods=['GET'])
def set_cookies():
    response = make_response(render_template('setcookies.html'))
    response.set_cookie('username', 'john_doe', max_age=5)

    return response

if __name__ == '__main__':
    app.run(debug=True)
