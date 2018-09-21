from flask import Flask ,url_for,render_template,requestw
app = Flask(__name__)

@app.route('/')
def home():
    return 'home.html'

if __name__=='__main__':
    app.run(debug=True)    
else:
    print('본 모듈은 단독으로 구동시에만 정상 작동 합니다.')

