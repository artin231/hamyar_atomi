from project import app,db
from flask import Flask,jsonify,request,render_template
from project.models import *


@app.route('/api/com/102044567')
def com_api():
    com = Comments.query.all()
    res = {'comments':[]}

    for i in stu:
        com['student'].append([i.title,i.created_at])

    return jsonify(res)


@app.route('/api/hom/84938502540')
def hom_api():
    hom = Homework.query.all()
    res = {'homework':[]}

    for i in hom:
        res['homework'].append([i.Class,i.grade,i.homework,i.img_url])
    
    return jsonify(res)

