from flask import Flask, render_template, request, redirect, url_for, session

import sqlite3

app = Flask(__name__)

_email = []
_password = []
_names = []

currentUser = {'name': None, 'email': None}



posts = []



@app.route('/', methods=['GET'])
def home():
         global posts , name, currentUser
         if currentUser['name']:
            name = currentUser['name']
         else:
            return redirect('/login')
         return render_template('home.html', posts=posts, name=name)



@app.route('/login', methods=['GET','POST'])
def login():
        email = ''
        password = ''
        name = ''
        if request.method == 'POST':
                email = request.form['email']
                password = request.form['password']

                if (not _email):
                         error =  'Invalid email or password.'
                         return render_template('login.html' ,error=error)
                else:
                      
                      if (email in _email and password in _password):
                                global i, currentUser
                                i = _email.index(email)
                                name = _names[i]
                                currentUser = {"name": name, "email": email}
                                return redirect(url_for('home'))
                      else:
                                error =  'Invalid email or password.'
                                return render_template('login.html' ,  error=error) 
        else:
                 
            return render_template('login.html')  



@app.route('/singup', methods=['GET','POST'])
def singup():
        global currentUser
        name = ''
        email = ''
        password = ''
        if request.method == 'POST':
                name = request.form['username']
                email = request.form['email']
                password = request.form['password']
        
                if (not _email and not _password and not _names):
                        _email.append(email)
                        _names.append(name)
                        _password.append(password)
                        currentUser = {"name": name, "email": email}
                        return redirect('/')
                else:
                        if (email in _email or name in _names):
                                 error =  'Register with a different email or username'
                                 return render_template('singup.html' ,error=error)
                        else: 
                                _email.append(email)
                                _names.append(name)
                                _password.append(password)
                                currentUser = {"name": name, "email": email}
                                return redirect('/')
                
               
        else:
                return render_template('singup.html')
        








@app.route('/add_post', methods=['POST'])
def add_post():
    global currentUser, posts
    posts = list(reversed(posts)) # to make them normal
    post_content = request.form['post_content']
    if post_content:
        posts.append({'post_content': post_content, 'username': currentUser['name'], 'comments': []})
        posts = list(reversed(posts)) # to make the last post at the top
    
    return redirect('/')


@app.route('/add_comment', methods=['POST'])
def add_comment():
    global currentUser, posts
    username = request.form['username']
    post_content = request.form['post_content']
    comment = request.form['comment']
    if post_content and comment:
        for post in posts:
                if post['post_content'] == post_content:
                       post['comments'].append({'comment_content': comment, 'username': username})
                       
        #comments[post_content].append({'post_content': post_content, 'username': currentUser['name']})
    return redirect('/')


@app.route('/information',  methods=['GET','POST'])
def information():
        if request.method == 'POST':
                return render_template('information.html')
        else:
                return redirect(url_for('home'))

@app.route('/profile',  methods=["GET",'POST'])
def profile():
     if request.method == 'POST':
            return render_template('profile.html')
     else:
            return redirect(url_for('home'))
            

@app.route('/friends', methods=['GET', 'POST'])
def friends():
    if request.method == 'POST':
         return render_template('friends.html')
    else:
        return redirect(url_for('home'))
@app.route('/index', methods=['GET', 'POST'])
def index():
  return redirect(url_for('home'))  
        
    




if __name__ == '__main__':
        app.run(debug=True)