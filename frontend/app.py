import datetime
import os
import requests

from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)
app.secret_key = os.environ['APP_SECRET_KEY']

@app.route("/", methods=('GET', 'POST'))
def home():
    if request.method == 'POST':
        a = request.form.get('n1')
        b = request.form.get('n2')
        data = {"message":{"n1":a,"n2":b}}
        r = requests.post(url="https://asia-northeast1-cloudcomputingcybersecurity.cloudfunctions.net/hw2",json=data)
        if r.text=="invalid argument":
            return r.text
        return a+"跟"+b+"的最大公因數是："+r.text
    return render_template('home.html')





if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5090, debug=True)
