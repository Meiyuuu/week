import pymongo
client = pymongo.MongoClient("mongodb+srv://root:root123@mycluster.sonypba.mongodb.net/?retryWrites=true&w=majority")
db = client.member_system
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
    if "account" in session:
        return render_template("member.html")
    else:
        return redirect("/")

@app.route("/error")
def error():
    msg=request.args.get("message","發生錯誤")
    return render_template("error.html",message=msg)
@app.route("/signin",methods=["POST"])
def signin():
    account=request.form["account1"]    
    password=request.form["password1"] 
    collection=db.user
    result=collection.find_one({
        "$and":[
            {"account":account},
            {"password":password}
        ]
    })
    if account=="" or password=="":
         return redirect("/error?message=請輸入帳號、密碼")
    elif result==None:
        return redirect("/error?message=帳號、或密碼輸入錯誤")
    session["account"]=result["account"]
    return redirect("/member")
 
@app.route("/signout")
def signout():
    del session["account"]
    return redirect("/")

  


app.run(port=3000)