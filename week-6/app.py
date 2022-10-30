import mysql.connector
    
mydb = mysql.connector.connect(
host="localhost",
user="root",
password="",
database="mydatabase")
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE member2 (id BIGINT AUTO_INCREMENT  PRIMARY KEY NOT NULL , name VARCHAR(255) NOT NULL, username VARCHAR(255) NOT NULL,password VARCHAR(255) NOT NULL)")
mydb.commit()

from flask import *
app=Flask(
    __name__,
    static_folder="public",
    static_url_path="/"
)
app.secret_key="asasa"
@app.route("/")
def index():
    return render_template("login.html")

@app.route("/member")
def member():
    if "username" in session:
        return render_template("member.html")
    else:
        return redirect("/")

@app.route("/error")
def error():
    msg=request.args.get("message","發生錯誤")
    return render_template("error.html",message=msg)

@app.route("/signup",methods=["POST"])
def signup():
    nickname=request.form["nickname"]    
    email=request.form["email"] 
    password=request.form["password2"] 
    mycursor.execute("SELECT * FROM member2 WHERE username=%s",[email])
    result=mycursor.fetchone()
    if result!=None:
        return redirect("/error?message=信箱已被註冊")
    sql = "INSERT INTO member2 (name, username,password) VALUES (%s, %s, %s)"
    val = (nickname, email,password)
    mycursor.execute(sql, val)
    mydb.commit()
    return redirect("/")

@app.route("/signin",methods=["POST"])
def signin():
    username=request.form["account1"]    
    password=request.form["password1"] 
    mycursor.execute("SELECT * FROM member2 WHERE username=%s and password=%s", [username,password])
    result=mycursor.fetchone()
    if username=="" or password=="":
        return redirect("/error?message=請輸入帳號、密碼")
    elif result==None:
        return redirect("/error?message=帳號、或密碼輸入錯誤")
    session["username"]=result
    return render_template("member.html",message=result[1])
 
@app.route("/signout")
def signout():
    del session["username"]
    return redirect("/")

app.run(port=3000)
