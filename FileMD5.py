import hashlib

file=open("C:\\Users\\wangtao\\Desktop\\yum\\file\\GiiiPlus1.1.apk","rb")
md5=hashlib.md5(file.read()).hexdigest()
file.close();
print(md5)