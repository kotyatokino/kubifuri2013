#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import sys
from threading import Thread
import cProfile

import Mworker
import Mconfig

from flask import Flask, redirect, render_template, request, url_for, session
app = Flask(__name__)

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/ajDoCommand",methods=['POST'])
def ajDoCommand():
    if(request.method == 'POST'):
        strPname = request.form['pname']
        CRancid = Mworker.CRancidWorker()

        for dicNode in Mconfig.lstConcig:
            thread = Thread(target=CRancid.DoRancid, args=(dicNode))
            thread_list.append(thread)
            thread.daemon = True
            thread.start()
        for thread in thread_list:
            thread.join()

    return "0"


app.secret_key = 'kubifuri99999'
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
