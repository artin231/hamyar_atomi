from project import db
from datetime import datetime

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    last_name = db.Column(db.String)
    code = db.Column(db.String)
    grade = db.Column(db.String)
    
class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    Class = db.Column(db.String)
    code = db.Column(db.String)
    last_name = db.Column(db.String)
    
class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    code = db.Column(db.String)
    Class = db.Column(db.String)
    last_name = db.Column(db.String)
    
class Homework(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Class = db.Column(db.String)
    grade = db.Column(db.String)
    homework = db.Column(db.String)
    img_url = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class news(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    news = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    comments = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
class Apsence(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    student_name = db.Column(db.String)
    student_lastname = db.Column(db.String)
    student_grade = db.Column(db.String)
    student_id = db.Column(db.Integer)

class Apcense_reason(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reason = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    student_name = db.Column(db.String)
    student_lastname = db.Column(db.String)
    student_grade = db.Column(db.String)
    t_id = db.Column(db.Integer)
    student_id = db.Column(db.Integer)
    
class nomre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String)
    student_lastname = db.Column(db.String)
    student_grade = db.Column(db.String)
    student_id = db.Column(db.Integer)
    karname_type = db.Column(db.String)
    dars = db.Column(db.String)
    nomre = db.Column(db.String)

class nomre_Enzebat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String)
    student_lastname = db.Column(db.String)
    student_grade = db.Column(db.String)
    student_id = db.Column(db.Integer)
    karname_type = db.Column(db.String)
    nomre = db.Column(db.String)

class azmoon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    dars = db.Column(db.String)
    date = db.Column(db.String)
    class_name = db.Column(db.String)

class soal_azmoon(db.Model):
    id = db.Column(db.Integer , primary_key=True)
    azmoon_title = db.Column(db.String)
    azmoon_dars = db.Column(db.String)
    azmoon_date = db.Column(db.String)
    azmoon_class= db.Column(db.String)
    title = db.Column(db.String)
    dars = db.Column(db.String)
    number = db.Column(db.String)

class azmoon_dade(db.Model):
    id = db.Column(db.Integer , primary_key=True)
    azmoon_title = db.Column(db.String)
    azmoon_dars = db.Column(db.String)
    azmoon_date = db.Column(db.String)
    azmoon_class= db.Column(db.String)
    student_name = db.Column(db.String)
    student_lastname = db.Column(db.String)
    student_id = db.Column(db.Integer)
    student_grade = db.Column(db.String)
    
class soal_azmoon_dade(db.Model):
    id = db.Column(db.Integer , primary_key=True)
    azmoon_title = db.Column(db.String)
    azmoon_dars = db.Column(db.String)
    azmoon_date = db.Column(db.String)
    azmoon_class= db.Column(db.String)
    student_name = db.Column(db.String)
    student_lastname = db.Column(db.String)
    student_id = db.Column(db.Integer)
    student_grade = db.Column(db.String)
    soal_title = db.Column(db.String)
    soal_dars = db.Column(db.String)
    soal_number = db.Column(db.String)
    answer = db.Column(db.String)

class azmoon_tashih(db.Model):
    id = db.Column(db.Integer , primary_key=True)
    azmoon_title = db.Column(db.String)
    azmoon_dars = db.Column(db.String)
    azmoon_date = db.Column(db.String)
    azmoon_class= db.Column(db.String)
    student_name = db.Column(db.String)
    student_lastname = db.Column(db.String)
    student_id = db.Column(db.Integer)
    student_grade = db.Column(db.String)

class soal_azmoon_tashih(db.Model):
    id = db.Column(db.Integer , primary_key=True)
    azmoon_title = db.Column(db.String)
    azmoon_dars = db.Column(db.String)
    azmoon_date = db.Column(db.String)
    azmoon_class= db.Column(db.String)
    student_name = db.Column(db.String)
    student_lastname = db.Column(db.String)
    student_grade = db.Column(db.String)
    student_id = db.Column(db.Integer)
    soal_title = db.Column(db.String)
    soal_dars = db.Column(db.String)
    soal_number = db.Column(db.String)
    soal_dade_answer = db.Column(db.String)
    description = db.Column(db.String)
    correct = db.Column(db.String)
    nomre = db.Column(db.String)

class ekhtar_pool(db.Model):
   id = db.Column(db.Integer , primary_key=True)
   student_name = db.Column(db.String)
   student_lastname = db.Column(db.String)
   student_grade = db.Column(db.String)
   student_id = db.Column(db.Integer)
   description = db.Column(db.String)
   pool = db.Column(db.String)

class ekhtar_nomre(db.Model):
   id = db.Column(db.Integer , primary_key=True)
   student_id = db.Column(db.Integer)
   student_name = db.Column(db.String)
   student_lastname = db.Column(db.String)
   student_grade = db.Column(db.String)
   description = db.Column(db.String)

class jashnvare(db.Model):
   id = db.Column(db.Integer , primary_key=True)
   title = db.Column(db.String)
   description = db.Column(db.String)
   date = db.Column(db.String)
   grade = db.Column(db.String)

class roydad(db.Model):
   id = db.Column(db.Integer , primary_key=True)
   title = db.Column(db.String)
   description = db.Column(db.String)
   date = db.Column(db.String)
   grade = db.Column(db.String)

class barname_kelasy(db.Model):
   id = db.Column(db.Integer , primary_key=True)
   grade = db.Column(db.String)
   zang_shanbe = db.Column(db.String)
   zang_yekshanbe = db.Column(db.String)
   zang_doshanbe = db.Column(db.String)
   zang_seshanbe = db.Column(db.String)
   zang_charshanbe = db.Column(db.String)
   zang_pangshanbe = db.Column(db.String)
   zang_jome = db.Column(db.String)

class time_nomre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    karname_type = db.Column(db.String)
    is_true = db.Column(db.Boolean)
     