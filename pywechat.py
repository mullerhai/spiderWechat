import  itchat
from  collections import  Counter
import  jieba
import  re
import  matplotlib.pyplot as  plt
import  numpy as np



itchat.login()
friends=itchat.get_friends(update=True)[0:]


male=female=other=0

for i in friends[1:]:

    sex=i["Sex"]
    if sex==1:
        male+=1
    elif sex==2:
        female+=1
    else:
        other+=1

total=len(friends[1:])



print("男性朋友： %2f%%"% (float(female)/total*100)+"\n")
print("女性朋友 ： %2f%%"%(float(male)/total*100)+"\n")

def get_var(var):
    variable=[]
    for i in friends:
        value=i[var]
        variable.append(value)

    return  variable

nickname=get_var("NickName")
signature=get_var("Signature")
province=get_var("Province")
city=get_var("City")
sex=get_var("Sex")


cityDict=Counter( ci  for ci in city)
provinceDict=Counter(pr for pr in province)

sorted(cityDict.items(),key=lambda asd:asd[0],reverse=True)
sorted(provinceDict.items(),key=lambda asd:asd[0],reverse=True)

for  pro ,num in  provinceDict.items():
    print("省份："+ pro+"  ***  个数：" +str(num))

for cit  ,num in cityDict.items():
    print("城市："+cit+" ** 个数："+str(num))

for  i in friends:
    if i["Province"] is None  or i["Province"]=='':
        if i["City"] is None  or i["City"]=='':
            print(i["NickName"]+"省份和城市都为空")
        else:
            print(i["NickName"]+i["City"]+"省份为空")
    else:
        if i["City"] is None or i["City"]=='':
            print(i["NickName"]+i["Province"]+"城市为空")




print("性别不明 ： %2f%%"%(float(other)/total*100))

signList = []
for sig in signature:
    newSig = sig.strip().replace("span", "").replace("class", "").replace("emoji", "")
    rep = re.compile("if\d+\w*|[<>/=]]")
    newSig = rep.sub("", newSig)
    signList.append(newSig)

text = "".join(signList)
wordlist=jieba.cut(text,cut_all=True)

word_space_split=" ".join(wordlist)

print(word_space_split)