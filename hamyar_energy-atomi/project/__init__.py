from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)

path= os.path.dirname(__file__)
path2 = os.path.join(path,"app.db")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"+ path2

db = SQLAlchemy(app)

import project.models
import project.views_admin
import project.views_student
import project.views_teacher
import project.api