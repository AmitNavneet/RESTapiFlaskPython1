from flask import Flask,render_template
from flask import jsonify,request
app=Flask(__name__)

users=[
        {"userID":1,"userName":"amit","userPassword":"amit123","userScore":9.5},
        {"userID":2,"userName":"dhoom","userPassword":"dhoom123","userScore":5.5},
        {"userID":3,"userName":"dev","userPassword":"dev123","userScore":10.00}
        ]

@app.route('/')
def index():
    return render_template("index.html")

@app.get("/users")
def get_users():
   return jsonify(users)

@app.get("/searchUser")
def searchUser():
    userID=int(request.args.get("userID"))
    for user in users:
        print(user)
        if user['userID']==userID:
            return jsonify(user)

    return f"UserID:{userID} not found"



if __name__=='__main__':
    app.run(debug=True)
