from project import app,db
from flask import Flask,url_for,render_template,request,session,redirect
from project.models import Student,Admin,Comments,news,Apsence,Apcense_reason
from sqlalchemy import asc,desc
from datetime import datetime

@app.route('/admin_form')
def admin_form():
    try:
        return render_template('admin_form/index.html')
    except Exception as error:
        print(error)
        link = '/'
        return render_template('unsuccesful/index.html' , link=link)
    
@app.route('/admin_form/submit',methods=['POST'])
def sub_admin():
    try:
        name = request.form['name']
        last_name = request.form['last_name']
        password = request.form['password']
        if password == '8723':
            session['namee'] = name
            session['lastnamee'] = last_name
            admin = Admin(name=name,last_name=last_name )
            session.permanent = True                        
            db.session.add(admin)
            db.session.commit()
            link = '/admin_panel'
            return render_template('succesful/index.html' , link=link)
        else:
            link = '/admin_form'
            return render_template('notright/index.html' , link=link)
            
    except Exception as error:
        print(error)
        link = '/admin_form'
        return render_template('unsuccesful/index.html' , link=link)

@app.route('/admin_panel')
def admin():
     try:
        if session.get('namee') and session.get('lastnamee'):
            name = session.get('namee') + session.get('lastnamee')
            comment = Comments.query.order_by(Comments.created_at.desc()).all()
            apcen = Apcense_reason.query.all()
            return render_template('admin_panel/index.html', name=name , comment = comment,apcen=apcen)
        else:
            return redirect('/')
     except Exception as error:
        print(error)
        link = '/'
        return render_template('unsuccesful/index.html' , link=link) 
    
    
@app.route('/admin_panel/news/submit' , methods=['post'])
def admin_news_submit():
    try:
        title = request.form['title']
        ne = request.form['news']
        new = news(name=title,news=ne)
        db.session.add(new)
        db.session.commit()
        link = '/admin_panel'
        return render_template('succesful/index.html' , link=link)
    except Exception as error:
        print(error)
        link = '/admin_panel'
        return render_template('unsuccesful/index.html' , link=link)
    
@app.route('/admin_panel/apsence/submit' , methods=['POST'])
def admin_apsence_sub():
    try:
        time = request.form['time']
        student_name = request.form['name']
        student_lastname = request.form['lastname']
        student_grade = request.form['grade']
        apsence = Apsence(time = time , student_name = student_name , student_lastname=student_lastname , student_grade=student_grade)
        db.session.add(apsence)
        db.session.commit()
        link = '/admin_panel'
        return render_template('succesful/index.html' , link=link)
    except Exception as error:
        print(error)
        link = '/admin_panel'
        return render_template('unsuccesful/index.html' , link=link)
