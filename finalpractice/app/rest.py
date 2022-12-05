import pymysql
from app import app
from db import mysql
from flask import jsonify, request

@app.route('/users', methods=['GET'])
def users():
    conn = mysql.connect()

    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM user")

    rows = cursor.fetchall()

    resp = jsonify(rows)
    resp.status_code = 200

    return resp

@app.route('/user', methods=['POST'])
def createuser():
    _json = request.json
    _name = _json['name']
    _lastName = _json['lastname']
    _role = _json['role']
    conn = mysql.connect()

    cursor = conn.cursor(pymysql.cursors.DictCursor)
    sqlQuery = "INSERT INTO user(name, lastname, role) VALUES(%s, %s, %s)"
    bindData = (_name, _lastName, _role)            
    cursor.execute(sqlQuery, bindData)
    conn.commit()
    respone = jsonify('User added successfully!')
    respone.status_code = 200
    
    return respone


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')