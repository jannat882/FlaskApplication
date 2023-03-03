#FlaskWebAppplicationDevelopment
from flask import Flask 

app =Flask(__name__)

@app.route('/cal/<num1>/<op>/<num2>')
def cal(num1, op, num2):
    n1= int(num1)
    n2= int(num2)
    if op=="+":
        result= n1+n2
    elif op== "-":
        result= n1-n2
    elif op == '/':
        result = n1 / n2
    elif op == '*':    
        result= n1*n2
    elif op == "%":
        result= n1%n2
    else:
         print("Invalid Operator!")
    return '<h1>The Result is %s!</h1>' %str(result)

if __name__== '__main__':
    app.run(debug=True)