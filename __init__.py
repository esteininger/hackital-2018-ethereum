from flask import Flask, flash, render_template, request, jsonify, redirect, make_response, session, redirect, url_for

from objects.Google import Google

app = Flask(__name__)

google = Google()

@app.route('/')
def homePage():
    return render_template('index.html')

@app.route('/Fall-2017')
def twentySeventeenPage():
    return render_template('2017.html')

if __name__ == '__main__':
    app.run(debug=True, port=5009)
