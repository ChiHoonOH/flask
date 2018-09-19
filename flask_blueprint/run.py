'''
Flask 기반 Blueprint 베이스로 각 URL별로 prefix를 부여하고,
MVC(Model(디비) View(템플릿) Controller(라우트))를 분리하여 
각각 모듈화 처리 => MVN이라고 용어를 여기서는 사용한다

Flask는 WIGC가 포함되어 있어서 자체적으로 서버 가동이 가능하다
이런 분류가 nodejs등이 있다. 단, FLask는 상용화시 단독이 아닌
apache, nginx등과 연동하여 사용한다
'''
from service import create_flaskApp

# Flask 객체 생성
app = create_flaskApp()

# 여기가 시작점임을 알려줌
if __name__=='__main__':
  # '0.0.0.0' : 모든 IP
  app.run(debug=True, port=3000, host='localhost')