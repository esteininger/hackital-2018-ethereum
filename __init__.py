from flask import Flask, flash, render_template, request, jsonify, redirect, make_response, session, redirect, url_for

from objects.Google import Google

app = Flask(__name__)

google = Google()

@app.route('/')
def homePage():
    print google.getFAQs()
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5009)
