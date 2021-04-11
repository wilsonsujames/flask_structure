from flask import Flask,render_template,jsonify



app = Flask(__name__)

@app.route('/',methods=[ "GET",'POST'])
def index():
    a={"name":"bob","date":"12月5日","time":"23:30","peopleCount":"10位","phone":"0123456789"}

    Webray=[]
    Webray.append(a)

    return render_template('index.html',Webray=Webray)



@app.route('/route_function',methods=[ "GET",'POST'])
def route_function():



    return jsonify({'validate': 'formula success','PayAmount':1500})



@app.route('/dashboard',methods=[ "GET",'POST'])
def dashboard():
    print('dashboard')

    return render_template('dashboard.html')    




if __name__ == "__main__":
    app.run(debug=True,threaded=True,port=5566)    