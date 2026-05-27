from project import app,db
from flask import Flask,url_for,render_template,request,session,redirect,jsonify
from project.models import Student,Admin,Teacher,Comments,news,Apsence,Homework,Apcense_reason
from sqlalchemy import asc,desc
from datetime import datetime

app.secret_key= 'art423skia89389e839e9le234yy44y4y4yrhwioughyjwogfhwojdfh'
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    try:
        return render_template('entekhab/index.html')
    except Exception as error:
        print(error)
        link = '/'
        return render_template('unsuccesful/index.html' , link=link )



@app.route('/api')
def api():
    stu = Student.query.all()
    adm =  Admin.query.all()
    tea = Teacher.query.all()
    com = Comments.query.all()
    hom = Homework.query.all()
    new = news.query.all() 
    apc = Apsence.query.all()
    apr =Apcense_reason.query.all()

    stu2={'student':[],
    'personnel':[],
    'teacher':[],
    'comments':[],
    'homework':[],
    'news':[],
    'apcense':[],
    'apcense_reason':[]}
    
    for i in stu:
        stu2['student'].append([i.name,i.last_name])

    for i in adm:
        stu2['personnel'].append([i.name,i.last_name])

    for i in tea:
        stu2['teacher'].append([i.name,i.last_name])
    
    for i in com:
        stu2['comments'].append([i.title,i.comments])

    for i in hom:
        stu2['homework'].append([i.Class,i.grade,i.homework])

    for i in new:
        stu2['news'].append([i.name,i.news])

    for i in apc:
        stu2['apcense'].append([i.time,i.student_name,i.student_lastname,i.student_grade])
    
    for i in apr:
        stu2['apcense_reason'].append([i.reason,i.student_name])
    
    return jsonify(stu2)

@app.route('/student_form')
def student_form():
    try:
        return render_template('student_form/index.html')
    except Exception as error:
        print(error)
        link = '/'
        return render_template('unsuccesful/index.html' , link=link)
 

@app.route('/student_form/submit',methods=['POST'])
def sub_student():
    try:
        name = request.form['name']
        last_name = request.form['last_name']
        grade = request.form['grade']
        password = request.form['password']
        if password == '1734':
            session['name'] = name
            session['lastname'] = last_name
            session['grade'] = grade
            session.permanent = True
            student = Student(name=name,last_name=last_name,grade=grade)
            db.session.add(student)
            db.session.commit()
            link = '/student_panel'
            return render_template('succesful/index.html' , link=link)
        else:
            link = '/student_form'
            return render_template('notright/index.html' , link=link)
    except Exception as error:
        print(error)
        link = '/student_form'
        return render_template('unsuccesful/index.html' , link=link)


@app.route('/student_panel')
def student():
    try:
        if session.get('name') and session.get('lastname'):
            NNews = news.query.order_by(news.created_at.desc()).all()
            a = Apsence.query.all()
            grade = session.get('grade','').strip()
            ai = "hello"
            s = session.get('name','').strip()    
            name = session.get('name') + ' ' + session.get('lastname')
            homework = Homework.query.order_by(Homework.created_at.desc()).all()
            return render_template('student_panel/index.html',news=NNews,name=name 
                                   , s=s , apcense=a , grade = grade,
                                   homework = homework , ai=ai , ) 
        else:
            return redirect('/')
    except Exception as error:
        print(error)
        link = '/'
        return render_template('unsuccesful/index.html' , link=link)

with app.app_context():
    db.create_all() 


@app.route('/student_panel/ai/submit')
def ai_sub():
    return redirect('/student_panel')          

@app.route('/student_panel/comments/submit' , methods=['POST'])
def student_comments_submmit():
    try:
        title = request.form['title']
        comments = request.form['comments']
        comment = Comments(title = title,comments=comments)
        db.session.add(comment)
        db.session.commit()
        link = '/student_panel'
        return render_template('succesful/index.html' , link=link)  
    except Exception as error:
        print(error)
        link = '/student_panel'
        return render_template('unsuccesful/index.html' , link=link)
@app.route('/student_panel/reason/submit' , methods=['POST'])
def res_sub():
    try:
        name = session.get('name') + ' ' + session.get('lastname')
        reas = request.form['reason']
        res =  Apcense_reason(reason = reas,student_name = name)
        db.session.add(res)
        db.session.commit();
        link = '/student_panel'
        return render_template('succesful/index.html' , link=link)
    except Exception as er:
        print(er)
        link = '/student_panel'
        return render_template('unsuccesful/index.html' , link=link)

    
@app.errorhandler(404)
def error(error):
    return render_template('404/index.html')

    
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
