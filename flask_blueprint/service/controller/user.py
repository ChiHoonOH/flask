from flask import render_template, request
# 블루프린트
from service.controller import bp_user as app

# ~/user
@app.route('/')
def home():
  return 'user 홈페이지'