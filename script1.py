from flask import Flask , render_template  #importing flask libraries, render_template renders the html content from "template" folder

app=Flask(__name__) #instantiating class object

#CASE 1: SCRIPT EXECUTED:
#__name__="__main__"

#CASE 2 SCRIPT IMPORTED:
#__name__="script1"

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about/')   #URL to which it can be directed. keep it as '/''
def about():
    return "aboutpage"

if __name__=="__main__": #if this condition is true then only webpage executed, ie only when script1 is executed not imported.
    app.run(debug=True)
