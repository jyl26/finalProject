from flask import Flask, render_template, request, redirect, url_for, make_response
import mysql.connector

app = Flask(__name__)
#put queries in a dictionary, keys are 1-5.
@app.route('/')
def home():
    questions = {1:"Revenue Change From This Year To Last",
                 2:"Visitors Change From This Year To Last",
                 3:"Customer Average Spending",
                 4:"Visitors By Season",
                 5:"Customer Top 3 Most Frequent Countries Of Origin"}
    return render_template('index.html',questions=questions)
@app.route('/category',methods=['POST'])
def category():
    queryCase = request.form['question']
    #the query will return number 1-5 coinciding with which prompt
    #create a dictionary structure with key 1-5, and the actual queries, then run the query and get back
    #the tuple
    ret = {
        "Number of Customers":230,
        "Number of Repeat Customers":50
    }
    return render_template('category.html',values=ret)
if __name__ == "__main__":
    app.run(debug=True,port=5001)