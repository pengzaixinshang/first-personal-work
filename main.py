import json

# 提取从用友的得到的全球疫情信息数据
with open('global_epidemic_statistics_start.json', 'r', encoding="utf-8")as f:
     Originaldata =json.load(f)

#提取json文件中的包含全球各国家的数据
Originalcountrydata = Originaldata["data"]["continent"]

#将各个洲的疫情数据提取
Asia = Originalcountrydata[0]["country"]
Europe = Originalcountrydata[1]["country"]
NorthAmerica = Originalcountrydata[2]["country"]
SouthAmerica = Originalcountrydata[3]["country"]
Africa = Originalcountrydata[4]["country"]
Oceania = Originalcountrydata[5]["country"]

#把这些洲全部用country列表存储起来
country = Asia + Europe + NorthAmerica + SouthAmerica + Africa + Oceania

#创建一个列表存放中英文转化后的最终数据
countryList = []

#将country列表中的中文国家名转化为英文并且存放在countryList列表中
with open('table.json', 'r', encoding='utf-8') as f:
        table = json.load(f)
for i in range(len(country)):
    for k,v in table.items():
        countryDict={}
        if country[i]["provinceName"] == v:
            countryDict["name"] = country[i]["provinceName"]
            countryDict["value"] = country[i]["confirmedCount"]
            countryList.append(countryDict)
print(countryList)

#将countryList列表转化为json格式
with open("global_epidemic_statistics_end.json", 'w', encoding="utf-8") as f:
    json.dump(countryList, f,ensure_ascii=False,indent=0)
    print("保存成功！")