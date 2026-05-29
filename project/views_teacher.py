from project import app,db
from flask import Flask,url_for,render_template,request,session,redirect,jsonify
from project.models import Student,Admin,Teacher,Comments,news,Apsence,Homework
from sqlalchemy import asc,desc
from datetime import datetime


@app.route('/teacher_form')
def teacher_form():
    try:
        return render_template('teacher_form/index.html')
    except Exception as error:
        print(error)
        link = '/'
        return render_template('unsuccesful/index.html' , link=link)  

    
@app.route('/teacher_form/submit',methods=['POST'])
def sub_teacher():
    try:
        name = request.form['name']
        last_name = request.form['last_name']
        password = request.form['password']
        if password == '4012':
            session['nameee'] = name
            session['lastnameee'] = last_name
            session.permanent = True
            teacher = Teacher(name=name,last_name=last_name )
            db.session.add(teacher)
            db.session.commit()
            link = '/teacher_panel'
            return render_template('succesful/index.html' , link=link)
        else:
            link = '/teacher_form'
            return render_template('notright/index.html' , link=link)
    except Exception as error:
        print(error)
        link = '/student_form'
        return render_template('unsuccesful/index.html' , link=link)


    
@app.route('/teacher_panel')
def teacher():
    try:
        if session.get('nameee') and session.get('lastnameee'):
            name = session.get('namee') + session.get('lastnamee')
            comment = Comments.query.order_by(Comments.created_at.desc()).all()
            print(type(Teacher.query.all()))
            for i in Teacher.query.all():
                print(i.name)

            return render_template('teacher_panel/index.html' , name=name , comment=comment)
        else:
            return redirect('/')
    except Exception as error:
        print(error)
        link = '/'
        return render_template('unsuccesful/index.html' , link=link)





@app.route('/teacher_panel/homework/submit',methods=['POST'])
def sub_homework():
    try:
        if session.get('nameee') and session.get('lastnameee'):
            grade = request.form['grade']
            Class = request.form['Class']
            new_homework = Homework(Class=request.form['Class'],
                                     grade=request.form['grade'],
                                     homework=request.form['homework'],
                                     )
            homework = request.form['homework']
            db.session.add(new_homework)
            db.session.commit()
            link = '/teacher_panel'
            return render_template('succesful/index.html' , link=link)
        else: 
            return redirect('/')
        
    except Exception as er:
        print(er)
        link = '/teacher_panel'
        return render_template('unsuccesful/index.html' , link=link)

    
