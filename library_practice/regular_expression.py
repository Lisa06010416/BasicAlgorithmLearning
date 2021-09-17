import re

s = "@123@abc"

""" ----------------------------- 找符合pattern的 ----------------------------- """
"""只找一個 且返回 _sre.SRE_Match object"""
# ----- re.match - 由字串的**開頭**開始匹配 -----
ans = re.match("[@123]", s)
print(ans.group(0), ans.pos, ans.endpos) # @ 0 8

ans = re.match("@123", s)
print(ans.group(0), ans.pos, ans.endpos) # @123 0 8

ans = re.match("[1-3]", s)  # return None

# ----- re.search - 匹配整個字串,返回一個找到的 -----
ans = re.search("[1-3]", s)
print(ans.group(0), ans.pos, ans.endpos) # 1 0 8

ans = re.search("123", s)
# print(ans.group(0), ans.pos, ans.endpos) # 123 0 8

"""找全部且反回list"""
# ----- re.findall() -----
re.findall("[a-z]+",s) # return list : ['abc']
re.findall("[a-z]*",s) # return list : ['', '', '', '', 'abc', '']
re.findall("[a-z]",s) # return list : ['a', 'b', 'c']
re.findall("(@)[a-z]",s) # return list : ['@']



""" ----------------------------- replace ----------------------------- """
# sub - substitution
re.sub("123", "", s) # return str: @@abc
re.sub("[1-9]", "", s) # return str: @@abc


""" ----------------------------- split ----------------------------- """
re.split("123", s) # return list: ['@', '@abc']
re.split("[123]", s) # return list: ['@', '', '', '@abc']
