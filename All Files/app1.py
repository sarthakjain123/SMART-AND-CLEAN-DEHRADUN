from flask import Flask, render_template , request , redirect
import pandas as pd
import json
import plotly
import plotly.express as px
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///houses.db"
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False
db = SQLAlchemy(app)
db.init_app(app)

class Houses(db.Model):
    sno = db.Column(db.Integer , primary_key=True)
    House_ID = db.Column(db.Text , nullable = True)
    Ward_No = db.Column(db.Integer , nullable = True)
    Total_Members = db.Column(db.Integer , nullable = True)
    Avg_Income = db.Column(db.Integer , nullable = True)
    Total_waste_Gen = db.Column(db.Integer , nullable = True)

    def __repr__(self) -> str:
        return f"{self.House_ID} - {self.Ward_No}"

with app.app_context():
    db.create_all()

def members_count ():
    global J
    J =  db.session.query(
        db.func.sum(Houses.Total_Members)).filter(Houses.Ward_No == 1).scalar()
    db.session.commit()
    print (J)

def income_count ():
    global H
    H =  db.session.query(
        db.func.sum(Houses.Avg_Income)).filter(Houses.Ward_No == 1).scalar()
    db.session.commit()
    print (H)

def house_count ():
    global K
    K =  db.session.query(
        db.func.count(Houses.House_ID)).filter(Houses.Ward_No == 1).scalar()
    db.session.commit()
    print (K)

def garbage_count ():
    global L
    L =  db.session.query(
        db.func.sum(Houses.Total_waste_Gen)).filter(Houses.Ward_No == 1).scalar()
    db.session.commit()
    print (L)

def members_count1 ():
    global M
    M =  db.session.query(
        db.func.sum(Houses.Total_Members)).filter(Houses.Ward_No == 2).scalar()
    db.session.commit()
    print (M)

def income_count1 ():
    global N
    N =  db.session.query(
        db.func.sum(Houses.Avg_Income)).filter(Houses.Ward_No == 2).scalar()
    db.session.commit()
    print (N)

def house_count1 ():
    global O
    O =  db.session.query(
        db.func.count(Houses.House_ID)).filter(Houses.Ward_No == 2).scalar()
    db.session.commit()
    print (O)

def garbage_count1 ():
    global P
    P =  db.session.query(
        db.func.sum(Houses.Total_waste_Gen)).filter(Houses.Ward_No == 2).scalar()
    db.session.commit()
    print (P)

def members_count2 ():
    global Q
    Q =  db.session.query(
        db.func.sum(Houses.Total_Members)).filter(Houses.Ward_No == 3).scalar()
    db.session.commit()
    print (Q)

def income_count2 ():
    global R
    R =  db.session.query(
        db.func.sum(Houses.Avg_Income)).filter(Houses.Ward_No == 3).scalar()
    db.session.commit()
    print (R)

def house_count2 ():
    global T
    T =  db.session.query(
        db.func.count(Houses.House_ID)).filter(Houses.Ward_No == 3).scalar()
    db.session.commit()
    print (T)

def garbage_count2 ():
    global U
    U =  db.session.query(
        db.func.sum(Houses.Total_waste_Gen)).filter(Houses.Ward_No == 3).scalar()
    db.session.commit()
    print (U)

def members_count3 ():
    global V
    V =  db.session.query(
        db.func.sum(Houses.Total_Members)).filter(Houses.Ward_No == 4).scalar()
    db.session.commit()
    print (V)

def income_count3 ():
    global W
    W =  db.session.query(
        db.func.sum(Houses.Avg_Income)).filter(Houses.Ward_No == 4).scalar()
    db.session.commit()
    print (W)

def house_count3 ():
    global Z
    Z =  db.session.query(
        db.func.count(Houses.House_ID)).filter(Houses.Ward_No == 4).scalar()
    db.session.commit()
    print (Z)

def garbage_count3 ():
    global AB
    AB =  db.session.query(
        db.func.sum(Houses.Total_waste_Gen)).filter(Houses.Ward_No == 4).scalar()
    db.session.commit()
    print (AB)

def avg_members ():
    global A
    A =  db.session.query(
        db.func.avg(Houses.Total_Members)).scalar()
    db.session.commit()
    #print (A)

def avg_income ():
    global B
    B =  db.session.query(
        db.func.avg(Houses.Avg_Income)).scalar()
    db.session.commit()
    #print (B)    

def avg_waste ():
    global C
    C =  db.session.query(
        db.func.avg(Houses.Total_waste_Gen)).scalar()
    db.session.commit()
    #print (C)    

#A = db.session.query(
 #       db.func.avg(Houses.Total_Members))
#print (A)


@app.route('/')
def hello_world():
    avg_members()
    avg_waste()
    avg_income()
    members_count ()
    income_count ()
    house_count ()
    garbage_count ()
    members_count1 ()
    income_count1 ()
    house_count1 ()
    garbage_count1 ()
    members_count2 ()
    income_count2 ()
    house_count2 ()
    garbage_count2 ()
    members_count3 ()
    income_count3 ()
    house_count3 ()
    garbage_count3 ()
    #print (A)
    return render_template('index.html')

@app.route('/ward1')
def hello_world1():
    if request.method == 'POST':
        print("HELLO POST")
        House_ID = request.form['House_ID']
        Ward_No = request.form['Ward_No']
        Total_Members = request.form['Total_Members']
        Avg_Income = request.form['Avg_Income']
        Total_waste_Gen = request.form['Total_waste_Gen']
        houses = Houses(House_ID = House_ID , Ward_No = Ward_No , Total_Members = Total_Members , Avg_Income = Avg_Income , Total_waste_Gen = Total_waste_Gen )
        db.session.add(houses)
        db.session.commit()
    ward1_houses = Houses.query.filter(Houses.Ward_No == 1) 
    return render_template('ward1.html' , J=J , H=H , K=K , L=L , ward1_houses=ward1_houses)
    #return 'Hello, World!'

@app.route('/ward2')


def hello_world2():
    if request.method == 'POST':
        print("HELLO POST")
        House_ID = request.form['House_ID']
        Ward_No = request.form['Ward_No']
        Total_Members = request.form['Total_Members']
        Avg_Income = request.form['Avg_Income']
        Total_waste_Gen = request.form['Total_waste_Gen']
        houses = Houses(House_ID = House_ID , Ward_No = Ward_No , Total_Members = Total_Members , Avg_Income = Avg_Income , Total_waste_Gen = Total_waste_Gen )
        db.session.add(houses)
        db.session.commit()
    ward2_houses = Houses.query.filter(Houses.Ward_No == 2) 
     
    return render_template('ward2.html' , M=M , N=N , O=O , P=P , ward2_houses=ward2_houses)
    #return 'Hello, World!'

@app.route('/ward3')
def hello_world3():
    if request.method == 'POST':
        print("HELLO POST")
        House_ID = request.form['House_ID']
        Ward_No = request.form['Ward_No']
        Total_Members = request.form['Total_Members']
        Avg_Income = request.form['Avg_Income']
        Total_waste_Gen = request.form['Total_waste_Gen']
        houses = Houses(House_ID = House_ID , Ward_No = Ward_No , Total_Members = Total_Members , Avg_Income = Avg_Income , Total_waste_Gen = Total_waste_Gen )
        db.session.add(houses)
        db.session.commit()
    ward3_houses = Houses.query.filter(Houses.Ward_No == 3)
    return render_template('ward3.html' , Q=Q , R=R , T=T ,U=U , ward3_houses=ward3_houses)
    #return 'Hello, World!'   

@app.route('/ward4')
def hello_world4():
    if request.method == 'POST':
        print("HELLO POST")
        House_ID = request.form['House_ID']
        Ward_No = request.form['Ward_No']
        Total_Members = request.form['Total_Members']
        Avg_Income = request.form['Avg_Income']
        Total_waste_Gen = request.form['Total_waste_Gen']
        houses = Houses(House_ID = House_ID , Ward_No = Ward_No , Total_Members = Total_Members , Avg_Income = Avg_Income , Total_waste_Gen = Total_waste_Gen )
        db.session.add(houses)
        db.session.commit()
    ward4_houses = Houses.query.filter(Houses.Ward_No == 4)
    return render_template('ward4.html' , V=V , W=W, Z=Z , AB=AB , ward4_houses=ward4_houses )
    #return 'Hello, World!'    

@app.route('/alterdata' , methods = ['GET','POST'])
def hello_world5():
    #house = Houses(House_ID ="perfect")
    if request.method == 'POST':
        print("HELLO POST")
        House_ID = request.form['House_ID']
        Ward_No = request.form['Ward_No']
        Total_Members = request.form['Total_Members']
        Avg_Income = request.form['Avg_Income']
        Total_waste_Gen = request.form['Total_waste_Gen']
        houses = Houses(House_ID = House_ID , Ward_No = Ward_No , Total_Members = Total_Members , Avg_Income = Avg_Income , Total_waste_Gen = Total_waste_Gen )
        db.session.add(houses)
        db.session.commit()
    allHouses = Houses.query.all() 
    return render_template('alterdata.html' , allHouses=allHouses)

@app.route('/delete/<int:sno>')
def delete(sno):
    houses = Houses.query.filter_by(sno=sno).first()
    db.session.delete(houses)
    db.session.commit()
    return redirect ("/alterdata")


@app.route('/regressionIO' , methods = ['GET','POST'])
def hello_world6():
    print (A,B,C)
    if request.method == 'POST':
        print("Post")
        global G
        global S
        G = int ( request.form['GAR'] )
        S = int( request.form['SART'] )
        print (S , G)
        X = C/A
        Y = C/B
        D = X*S
        E = Y*G
        I = D + E
        global F
        F = I/2

        print (Y)
        print (F)

        


        #return "Your name is "+ G + "  " + S
    return render_template('regressionIO.html' )
    #return 'Hello, World!'
 
@app.route('/prediction')
def hello_world7():
    return render_template('prediction.html' , F=F , G=G ,S=S )


if __name__ == "__main__":
    app.run(debug=True)