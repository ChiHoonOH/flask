'''
파이썬 웹의 기본 골격
'''
#1. 모듈 가져오기
from flask import Flask,url_for,render_template,request,jsonify#첫글자가 대문자이기 때문에 클래스일 확률이큼.
from flask_advance.model import select_tradeLastData as tradeList,select_searchTradeCode as searchName,select_tradeInfo
from flask_advance.model import update_tradeInfo

#__init__.py인 경우에 딱히 써줄 필요 없다.
#2. 앱 정의
app = Flask(__name__)
#3. 라우트
@app.route('/')
def home():
    # 1. tbl_codehistory 테이블을 쿼리해서 최신순으로 10개만 가져온다.
    
    # 2. 가져온 데이터를 render_template()에 인자로 전달한다.
    return render_template('home.html', trades=tradeList())
    # 3. home.html 내부에서 jinja2 문법을 이용하여 동적으로 리스트로 구성한다.

@app.route('/search')
def search():#미드웨어 서버
    #검색어 획득
    keyword = request.args.get('keyword')#근데 한글 깨짐
    #쿼리 수행
    rows    = searchName(keyword)
    #json 형식으로 변환(sequence type->변환 특히 그 키 있는 형식을 변환할때 좋다.)
    result = jsonify(rows)
    
    #쿼리 결과 json     
    #(home.js에서 json으로 입력을 정의 하였으므로)
    if request.method == 'GET':
        print(result)
        return result

#주식종목별 세부 정보 페이지
#주식 기본 정보 + 최신 10일치 주식 정보를 join해서 가져온다.
#주식 정보 수정 가능, 주식 정보 삭제 가능, 주식 정보 추가 가능
@app.route('/info',methods=['GET','POST'])
def info():
    if request.method == 'GET':
        info = select_tradeInfo(request.args.get('code'))   
        #수정 페이지 여부
        flag = request.args.get('flag')
        return render_template('info.html',tradeinfo=info,flag=flag)
    else:
        #전달 데이터 중 아무거나 하나 콘솔 출력   
        
        res=update_tradeInfo(request.form)       
        
        if res:
            msg='성공적으로 수정되었습니다.'
            return render_template('alert.html',msg=msg,
            target_url='%s?code=%s'%(url_for('info'),request.form.get('code')))
        else:
            msg='수정에 실패하였습니다.'
            return render_template('alert.html',msg=msg)
        
        #수정 업데이트 쿼리 >> sql 수행 => 쿼리문 준비하고 => 함수 작성 => 사용
        
    
    
#4. 서버가동
if __name__=='__main__':
    app.run(debug=True)        
else:
    print('본 모듈은 단독으로 구동시에만 정상 작동 합니다.')

