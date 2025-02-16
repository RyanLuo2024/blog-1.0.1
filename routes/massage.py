from flask import Flask, Blueprint, render_template, request, redirect, url_for, jsonify
import sqlite3,logging,models,datetime,flask

mail_blueprint = Blueprint('mail', __name__, template_folder='templates')

def db_connection():
    conn = sqlite3.connect('db/massage.db')
    conn.row_factory = sqlite3.Row
    return conn

@mail_blueprint.route('/writemail')
def index():
    if (flask.request.cookies.get("cookieid") == None): return flask.redirect(flask.url_for("auth.user_login"))
    conn = db_connection()
    c = conn.cursor()
    c.execute('SELECT * FROM message WHERE (fromcansee = 1 AND from_user=?) OR (tocansee = 1 AND to_user=?)', (request.cookies.get("cookieid"), request.cookies.get("cookieid")))
    messages = c.fetchall()
    conn.close()
    return render_template('mail.html', messages=messages, get_current_user=request.cookies.get("cookieid"))

@mail_blueprint.route('/mail/<id>')
def mail_mail(id):
    if (flask.request.cookies.get("cookieid") == None): return flask.redirect(flask.url_for("auth.user_login"))
    conn = db_connection()
    c = conn.cursor()
    c.execute(f'SELECT * FROM message WHERE id={id}')
    messages = c.fetchall()
    conn.close()
    return render_template('mail_show.html', message=messages, get_current_user=request.cookies.get("cookieid"), req=id)

@mail_blueprint.route('/send', methods=['POST'])
def send():
    if (flask.request.cookies.get("cookieid") == None): return flask.redirect(flask.url_for("auth.user_login"))
    from_user = request.cookies.get("cookieid")
    to_user = request.form['to']
    subject = request.form['subject']
    body = request.form['body']
    type_ = request.form['type']
    import models
    id = models.wordid()
    sid = id.shengzheng()
    conn = db_connection()
    c = conn.cursor()
    c.execute('''
        INSERT INTO message (from_user, to_user, subject, body, type_, fromcansee, tocansee, id)
        VALUES (?, ?, ?, ?, ?, 1, 1, ?)
    ''', (from_user, to_user, subject, body, type_, sid))
    conn.commit()
    conn.close()

    return redirect(url_for('mail.index'))

@mail_blueprint.route('/delete/<int:message_id>', methods=['GET'])
def delete(message_id):
    if (flask.request.cookies.get("cookieid") == None): return flask.redirect(flask.url_for("auth.user_login"))
    current_user = request.cookies.get("cookieid")
    
    conn = db_connection()
    c = conn.cursor()
    c.execute('SELECT from_user, to_user FROM message WHERE id = ?', (message_id,))
    message = c.fetchone()
    conn.close()

    if current_user == message[0]:  # 如果当前用户是发送方
        conn = db_connection()
        c = conn.cursor()
        c.execute('UPDATE message SET fromcansee = 0 WHERE id = ?', (message_id,))
    elif current_user == message[1]:  # 如果当前用户是接收方
        conn = db_connection()
        c = conn.cursor()
        c.execute('UPDATE message SET tocansee = 0 WHERE id = ?', (message_id,))
    else:
        return "Unauthorized", 403

    conn.commit()
    conn.close()

    return redirect(url_for('mail.index'))

@mail_blueprint.route('/messages')
def messages():
    if (flask.request.cookies.get("cookieid") == None): return flask.redirect(flask.url_for("auth.user_login"))
    conn = db_connection()
    c = conn.cursor()
    c.execute('SELECT * FROM message WHERE (fromcansee = 1 AND from_user=?) OR (tocansee = 1 AND to_user=?)', (request.cookies.get("cookieid"), request.cookies.get("cookieid")))
    messages = [dict(row) for row in c.fetchall()]
    logging.debug(f"/messages,get a requrest,return{messages}")
    try:
        messages[0]['date'] = models.wordid().jiexi(messages[0]['id']).strftime("%Y-%m-%d %H:%M:%S")
    except: pass
    conn.close()
    return jsonify(messages)

@mail_blueprint.route('/')
def index_():
    return render_template('mail_list.html')