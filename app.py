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
    return render_template("index.html",projs=Mconfig.lstProjs)

thread_list=[]
node_list=[]
@app.route("/ajDoCommand",methods=['POST'])
def ajDoCommand():
    if(request.method == 'POST'):
        strPname = request.form['pname']
        Cworker = Mworker.CRancidWorker()
        for dicNode in Mconfig.lstConfig:
            thread = Thread(target=Cworker.DoWorker, args=(dicNode,strPname))
            thread_list.append(thread)
            node_list.append({'name':dicNode['hostname'],'result':''})
            thread.daemon = True
            thread.start()
        for thread in thread_list:
            thread.join()

    return "1"

@app.route("/ajcheckThread",methods=['POST'])
def ajcheckThread():
    intI = 0
    strRet = ""
    intWorking = 0
    for thread in thread_list:
        if(thread.is_alive()):
            strRes = "<font color=\"red\">Working</font>"
            intWorking=1
        else:
            strRes = "<font color=\"green\">Finished</font>"
        strTmp = "%s:%s<br>" % (node_list[intI]['name'],strRes)
        strRet = strRet + strTmp
        intI = intI + 1
    if(intWorking):
        return strRet
    else:
        return "2"


app.secret_key = 'kubifuri99999'
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8081, debug=True)
