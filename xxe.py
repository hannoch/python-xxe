#coding=utf-8

'''
autor: c0ny1
date: 2018-2-7
'''

from flask import Flask, request, render_template
from lxml import etree

app = Flask(__name__)
app.config['DEBUG'] = True

USERNAME = 'admin' # 账号
PASSWORD = 'admin' # 密码

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/doLogin", methods=['POST', 'GET'])
def doLogin():
    result = None
    try:
        # 漏洞修复--禁用外部实体  resolve_entities=False
        #tree = etree.fromstring(request.data,etree.XMLParser(resolve_entities=False))
        tree = etree.fromstring(request.data) # 有漏洞
        # 遍历xml结构内容
        for childa in tree:
            print(childa.tag, childa.text, childa.attrib)
            if childa.tag == "username":
                username = childa.text
                print(username)
            if childa.tag == "password":
                password = childa.text
                print(password)
        if username == USERNAME and password == PASSWORD:
            result = "<result><code>%d</code><msg>%s</msg></result>" % (1,username)
        else:
            result = "<result><code>%d</code><msg>%s</msg></result>" % (0,username)
    except Exception as Ex:
        result = "<result><code>%d</code><msg>%s</msg></result>" % (3,str(Ex))
    return result,{'Content-Type': 'text/xml;charset=UTF-8'}

def prn_obj(obj):
    print('\n'.join(['%s:%s' % item for item in obj.__dict__.items()]))


if __name__ == "__main__":
    app.run()
	


