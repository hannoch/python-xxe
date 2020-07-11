## Python XXE漏洞复现

## **什么是XXE**

简单来说，XXE就是XML外部实体注入。当允许引用外部实体时，通过构造恶意内容，就可能导致任意文件读取、系统命令执行、内网端口探测、攻击内网网站等危害。

例如，如果你当前使用的程序为python，则可以将resolve_entities设置为False来禁用外部实体，从而起到防御的目的。

通常攻击者会将payload注入XML文件中，一旦文件被执行，将会读取服务器上的本地文件，并对内网发起访问扫描内部网络端口。换而言之，XXE是一种从本地到达各种服务的方法。此外，在一定程度上这也可能帮助攻击者绕过防火墙规则过滤或身份验证检查。

```python
# python3  flask 作为后台
git clone https://github.com/hannoch/python-xxe.git
pip install -r requirements.txt
python xxe.py
```

>   payload

```python
<!DOCTYPE foo [<!ELEMENT foo ANY ><!ENTITY  xxe SYSTEM "file:///c:/a.txt" >]>
```

>   防御手段

```python
# 漏洞修复--禁用外部实体  resolve_entities=False
xml = "<username>admin</username><password>admin</password></user>"
#tree = etree.fromstring(xml,etree.XMLParser(resolve_entities=False))
```

>   演示：

![python-xxe](https://github.com/hannoch/python-xxe/blob/master/python_xxe_demo.gif)

参考：https://github.com/c0ny1/xxe-lab
