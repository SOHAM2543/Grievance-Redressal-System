#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re
from flask import Flask, render_template, request, session, redirect, url_for
import pyrebase
from Config_Info import get_config, Password, con
import smtplib ,ssl
from email.message import EmailMessage
from collections import OrderedDict
import smtplib ,ssl
from email.message import EmailMessage


# In[2]:


app=Flask(__name__)


# In[3]:


@app.route('/')
def root():
    return render_template('Home_Page.html')

@app.route('/Home_Page')
def Home_Page():
    return render_template('Home_Page.html')

@app.route('/Login_Option')
def Login_Option():
    return render_template('Login_Option.html')

@app.route('/Objective')
def Objective():
    return render_template('Objective.html')

@app.route('/How_We_Works')
def How_We_Works():
    return render_template('How_We_Works.html')

@app.route('/About_Us')
def About_Us():
    return render_template('About_Us.html')

@app.route('/Contact_Us')
def Contact_Us():
    return render_template('Contact_Us.html')

@app.route('/User_Data')
def User_Data():
    return render_template('User_Data.html')

@app.route('/Cm')
def Cm():
    return render_template('Cm.html')

@app.route('/Admin')
def Admin():
    return render_template('Admin.html')

@app.route('/Scope')
def Scope():
    return render_template('Scope.html')

@app.route('/Function')
def Function():
    return render_template('Function.html')

@app.route('/Powers')
def Powers():
    return render_template('Powers.html')

@app.route('/Purpose')
def Purpose():
    return render_template('Purpose.html')

@app.route('/User_Login')
def User_Login():
    return render_template('User_Login.html')

@app.route('/Cm_Login')
def Cm_Login():
    return render_template('Cm_Login.html')

@app.route('/User_Signup')
def User_Signup():
    return render_template('User_Signup.html')

@app.route('/Forgot_Password')
def Forgot_Password():
    return render_template('Forgot_Password.html')

# @app.route('/Stud_Grievance')
# def Stud_Grievance():
#     return render_template('Stud_Grievance.html')

@app.route('/View_Grievance')
def View_Grievance():
    return render_template('View_Grievance.html')

@app.route('/Cm_Signup')
def Cm_Signup():
    return render_template('Cm_Signup.html')

@app.route('/Stud_Grievance')
def Stud_Grievance():
    return render_template('Stud_Grievance.html')

@app.route('/Fac_Grievance')
def Fac_Grievance():
    return render_template('Fac_Grievance.html')

@app.route('/Reply')
def Reply():
    return render_template('Reply.html')

@app.route('/Report')
def Report():
    return render_template('Report.html')


# In[4]:


config = get_config()
con = con()
app.config['SECRET_KEY'] = con
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()


# In[5]:


@app.route('/User_L',methods=['post'])
def User_L():
    if session.get("user") is None:
        if request.method == "POST":
            email = request.form["email"]
            password = request.form["password"]
            user = auth.sign_in_with_email_and_password(email,password)
            user = auth.refresh(user['refreshToken'])
            user_id = user["idToken"]
            session['user'] = user_id
            return render_template("User_Grievance.html")
        else:
                message = "Incorrect Password!"
                return render_template("User_Login.html",message=message)
    else:
        return render_template("User_Grievance.html")
    return None

@app.route('/User_S',methods=['post'])
def User_S():
    email = request.form["email"]
    password = request.form["password"]
    c_password = request.form["confirm_password"]
    if(password == c_password):
        flag = 0
        while True:  
            if (len(password)<8):
                flag = -1
                break
            elif not re.search("[a-z]", password):
                flag = -1
                break
            elif not re.search("[A-Z]", password):
                flag = -1
                break
            elif not re.search("[0-9]", password):
                flag = -1
                break
            elif not re.search("[_@$]", password):
                flag = -1
                break
            elif re.search("\s", password):
                flag = -1
                break
            else:
                flag = 0
                user = auth.create_user_with_email_and_password(email,password)
                return render_template("User_Login.html")
                break
  
        if flag ==-1:
            message = "Not a Valid Password"
            return render_template("User_Signup.html",message=message)
    else:
        c_message = "Those passwords didn’t match. Try again."
        return render_template("User_Signup.html",c_message=c_message)
    return None

@app.route('/Forget_P',methods=['post'])
def Forget_P():
    email = request.form["email"]
    if email != None:
        user = auth.send_password_reset_email(email)
        return render_template("Login_Option.html")
    else:
        message = "Please enter the mail!"
        return render_template("Forget_Password.html",message=message)
    return None


# In[6]:


@app.route('/CM_L',methods=['post'])
def CM_L():
    if session.get("user") is None:
        if request.method == "POST":
            email = request.form["email"]
            password = request.form["password"]
            user = auth.sign_in_with_email_and_password(email,password)
            user = auth.refresh(user['refreshToken'])
            user_id = user["idToken"]
            session['user'] = user_id
            return render_template("View_Grievance.html")
        else:
                message = "Incorrect Password!"
                return render_template("Cm_Login.html",message=message)
    else:
        return render_template("View_Grievance.html")
    return None

@app.route('/CM_S',methods=['post'])
def CM_S():
    email = request.form["email"]
    password = request.form["password"]
    c_password = request.form["confirm_password"]
    if(password == c_password):
        if(password == c_password):
            flag = 0
        while True:  
            if (len(password)<8):
                flag = -1
                break
            elif not re.search("[a-z]", password):
                flag = -1
                break
            elif not re.search("[A-Z]", password):
                flag = -1
                break
            elif not re.search("[0-9]", password):
                flag = -1
                break
            elif not re.search("[_@$]", password):
                flag = -1
                break
            elif re.search("\s", password):
                flag = -1
                break
            else:
                flag = 0
                user = auth.create_user_with_email_and_password(email,password)
                return render_template("Cm_Login.html")
                break
  
        if flag ==-1:
            message = "Not a Valid Password"
            return render_template("Cm_Signup.html",message=message)
    else:
        c_message = "Those passwords didn’t match. Try again."
        return render_template("Cm_Signup.html",c_message=c_message)
    return None

@app.route('/Logout')
def Logout():
    session.pop('user',None)
    return render_template('Login_Option.html')


# In[7]:


@app.route('/Add_Stud_G',methods=['POST','GET'])
def Add_Stud_G():
    name = request.form['name']
    roll_no = request.form['roll_no']
    email = request.form['email']
    dept = request.args.get('Dept')
    types = request.args.get('types')
    sub = request.form['subject']
    des = request.form['description']
    if(types == "Mechanical"):
        Name="Name";Roll_No="Roll Number";Email = "Email";Dept="Department";Types="Academic";Sub="Subject";Des="Description"
        data = dict(Name=name, Roll_No=roll_no, Email=email, Department=dept, types=types, Subject=sub, Description=des)
        db.child("User Data").child("Academic").child("Mechanical").child("Student").push(data)
    elif(types == "Civil"):
        Name="Name";Roll_No="Roll Number";Email = "Email";Dept="Department";Types="Academic";Sub="Subject";Des="Description"
        data = dict(Name=name, Roll_No=roll_no, Email=email, Department=dept, types=types, Subject=sub, Description=des)
        db.child("User Data").child("Academic").child("IT").child("Student").push(data)
    else:
        Name="Name";Roll_No="Roll Number";Email = "Email";Dept="Department";Types="Academic";Sub="Subject";Des="Description"
        data = dict(Name=name, Roll_No=roll_no, Email=email, Department=dept, types=types, Subject=sub, Description=des)
        db.child("User Data").child("Academic").child("IT").child("Student").push(data)
    return render_template('Stud_Grievance.html')

@app.route('/Add_Fac_G',methods=['POST','GET'])
def Add_Fac_G():
    name = request.form['name']
    emp_id = request.form['emp_id']
    email = request.form['email']
    dept = request.args.get('Dept')
    types = request.args.get('types')
    sub = request.form['subject']
    des = request.form['description']
    if(types == "Mechanical"):
        Name="Name";Emp_ID="Employee ID";Email = "Email";Dept="Department";Types="Academic";Sub="Subject";Des="Description"
        data = dict(Name=name, Empplyee_ID=emp_id, Email=email, Deptartment=dept, Types=types, Subject = sub, Description=des)
        db.child("User Data").child("Academic").child("Mechanical").child("Faculty").push(data)
    elif(types == "Civil"):
        Name="Name";Emp_ID="Employee ID";Email = "Email";Dept="Department";Types="Academic";Sub="Subject";Des="Description"
        data = dict(Name=name, Empplyee_ID=emp_id, Email=email, Deptartment=dept, Types=types, Subject = sub, Description=des)
        db.child("User Data").child("Academic").child("IT").child("Faculty").push(data)
    else:
        Name="Name";Emp_ID="Employee ID";Email = "Email";Dept="Department";Types="Academic";Sub="Subject";Des="Description"
        data = dict(Name=name, Empplyee_ID=emp_id, Email=email, Deptartment=dept, Types=types, Subject = sub, Description=des)
        db.child("User Data").child("Academic").child("IT").child("Faculty").push(data)
    return render_template('Fac_Grievance.html')


# In[8]:


@app.route('/Read_G',methods=['POST','GET'])
def Read_G():
    posts=[]
    user = request.args.get('user')
    dept = request.args.get('dept')
    types = request.args.get('type')
    try:
        if(user == "Student"):
            if(types == "Mechanical"):
                view_data = db.child("User Data").child("Academic").child("Mechanical").child("Student").get()
                view = view_data.val()
                for key,value in enumerate(view.values()):
                    posts.append(value)
                return render_template('View_Grievance.html',t=posts)
            elif(types == "Civil"):
                view_data = db.child("User Data").child("Academic").child("Civil").child("Student").get()
                view = view_data.val()
                for key,value in enumerate(view.values()):
                    posts.append(value)
                return render_template('View_Grievance.html',t=posts)
            else:
                view_data = db.child("User Data").child("Academic").child("IT").child("Student").get()
                view = view_data.val()
                for key,value in enumerate(view.values()):
                    posts.append(value)
                return render_template('View_Grievance.html',t=posts)
        else:
            if(types == "Mechanical"):
                view_data = db.child("User Data").child("Academic").child("Mechanical").child("Faculty").get()
                view = view_data.val()
                for key,value in enumerate(view.values()):
                    posts.append(value)
                return render_template('View_Grievance.html',t=posts)
            elif(types == "Civil"):
                view_data = db.child("User Data").child("Academic").child("Civil").child("Faculty").get()
                view = view_data.val()
                for key,value in enumerate(view.values()):
                    posts.append(value)
                return render_template('View_Grievance.html',t=posts)
            else:
                view_data = db.child("User Data").child("Academic").child("IT").child("Faculty").get()
                view = view_data.val()
                for key,value in enumerate(view.values()):
                    posts.append(value)
                return render_template('View_Grievance.html',t=posts)
    except:
        return render_template('View_Grievance.html',t=posts)
    return render_template('View_Grievance.html')


# In[9]:


@app.route('/Reply_U',methods=['POST','GET'])
def Reply_U():
    try:
        email = request.form['email']
        status = request.form['status']
        description = request.form['description']
        msg = EmailMessage()
        msg.set_content(description)
        sender = 'tridentgpkp@gmail.com'
        password = Password()
        msg['Subject'] = str(status)
        msg['From'] = sender
        msg['To'] = str(email)
        context=ssl.create_default_context()
        with smtplib.SMTP("smtp.gmail.com",587) as smtp:
            smtp.starttls(context=context)
            smtp.login(sender, password)
            smtp.send_message(msg)
            smtp.quit()
            msg="Reply Sent!"
    except:
        msg="Reply could not be sent"
    return render_template('Reply.html')

@app.route('/Report_U',methods=['POST','GET'])
def Report_U():
    try:
        email = request.form['email']
        Total_G = request.form['TG']
        Solved_G = request.form['SG']
        Pending_G = request.form['PG']
        msg = EmailMessage()
        msg.set_content("Number Of Total Grievances "+str(Total_G)+"\nNumber Of Solved Grievances "+str(Solved_G)+"\nNo Of Pending Grievances"+str(Pending_G))
        sender = 'tridentgpkp@gmail.com'
        password = Password()
        msg['Subject'] = "Monthly Report"
        msg['From'] = sender
        msg['To'] = email
        context=ssl.create_default_context()
        with smtplib.SMTP("smtp.gmail.com",587) as smtp:
            smtp.starttls(context=context)
            smtp.login(sender, password)
            smtp.send_message(msg)
            smtp.quit()
            msg="Report Sent!"
    except:
        msg="Report could not be spent!"
    return render_template('Report.html',msg=msg)


# In[10]:


@app.route('/contactdata',methods=['GET','POST'])
def contactdata():
    try:
        name = request.form['name']
        email = request.form['email']
        comment = request.form['comment']
        Name = "Name"; Email = "Email"; Comment = "Comment";
        data = dict(Name = name, Email = email, Comment = comment)
        db.child("ContactUs_Data").push(data)
        msgs = "Thank you for giving us your feedback!"
        msg = EmailMessage()
        msg.set_content("Thank You for visiting!\nEvery single feedback is important for us.\nWe\'ll get back to you as soon as we can.\n\nYou can also contact us on\nemail - tridentgpkp@gmail.com")
        sender = 'tridentgpkp@gmail.com'
        password = Password()
        msg['Subject'] = "We\'re glad you visited us!"
        msg['From'] = sender
        msg['To'] = email
        context=ssl.create_default_context()
        with smtplib.SMTP("smtp.gmail.com",587) as smtp:
            smtp.starttls(context=context)
            smtp.login(sender, password)
            smtp.send_message(msg)
            smtp.quit()
            msg="Feedback sent!"
    except:
        msg="Feedback could not sent!"
    return render_template('Contact_Us.html',msg=msg)


# In[ ]:


if __name__ == '__main__':
    app.run()


# In[ ]:




