from flask import Flask
app = Flask(__name__)

@app.route('/')
def root():
	return '<h1>网站建设中。。。</h1>'

@app.route('/hello')
def index():
    return '<h1>Hello World!</h1>'


@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)

'''
from flask import redirect
@app.route('/testpic')
def testpic():
	return redirect('/static/index.html') #这样是跳转到http://xxx/static/index.html，在浏览器地址栏看到具体html的地址了
	#如果地址为http://www.limit-animation.com/testpic就是完全跳转过去了
'''

# url_for不是重定向而是找到文件
# from flask import url_for
# @app.route('/testpic')
# def testpic():
# 	return url_for('static',filename = 'index.html',_external=True)

from flask import render_template
@app.route('/testpic')
def pp():
	return render_template('testpic.html')
	
if __name__ == '__main__':
	app.run()
