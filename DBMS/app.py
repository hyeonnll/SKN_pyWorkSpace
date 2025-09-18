from flask import Flask, render_template, request, redirect, url_for
import pymysql
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()

# DB 연결
conn = pymysql.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

@app.route('/')
def index():
    # 고객 목록 불러오기
    sql = 'select * from customer'
    customers = []
    with conn.cursor() as cur:
        cur.execute(sql)
        for i in cur.fetchall():
            customers.append({"id": i[0], "name": i[1]})
    return render_template('index.html', customers=customers)

@app.route('/add', methods=['POST'])
def add_customer():
    name = request.form['name']
    sql = 'insert into customer values(null, %s)'
    with conn.cursor() as cur:
        cur.execute(sql, name)
    conn.commit()
    return redirect(url_for('index'))

@app.route('/update/<int:customer_id>', methods=['POST'])
def update_customer(customer_id):
    name = request.form['name']
    sql = 'update customer set name=%s where customer_id=%s'
    with conn.cursor() as cur:
        cur.execute(sql, (name, customer_id))
    conn.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:customer_id>')
def delete_customer(customer_id):
    sql = 'delete from customer where customer_id=%s'
    with conn.cursor() as cur:
        cur.execute(sql, customer_id)
    conn.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
