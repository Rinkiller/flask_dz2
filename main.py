from flask import Flask, render_template, redirect, request, url_for, flash, make_response


app = Flask(__name__)
app.secret_key = '77cd032d1d513c1c0efeaa6dbb71cf6d5b4b1a9b0139effcb3ed5125f9b0609e'




@app.route('/',methods=['GET', 'POST'])
def form():
    if request.method == 'GET':
        return render_template('form.html')
    if request.method == 'POST':
        if not request.form['name']:
            flash('Введите имя','danger')
            return redirect(url_for('form'))
        if not request.form['mail']:
            flash('Введите почту','danger')
            return redirect(url_for('form'))
        name = request.form['name']
        mail = request.form['mail']
        user = {}
        user['user'] = name
        response = make_response(render_template('hi_page.html',**user))
        response.set_cookie('username',name)
        response.set_cookie('useremail',mail)
        return response
      




@app.get('/dell_cookie')
def dell_cookie():
    response = make_response(render_template('form.html'))
    response.set_cookie('username', '', expires=0)
    response.delete_cookie('username')
    response.set_cookie('useremail', '', expires=0)
    response.delete_cookie('useremail')
    return response


if __name__=='__main__':
    app.run(debug=True)