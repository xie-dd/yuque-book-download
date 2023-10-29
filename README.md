更新：https://xie-dd.github.io/posts/1745/

-------------------------------------------------------------------




### 获取语雀Token
网页端登陆语雀---点击头像---账户设置---Token

<a name="LMe3g"></a>
### 说明

1. 语雀所有的开放 API 都需要 Token 验证之后才能访问
2. 你需要在请求的 HTTP Headers 传入 `X-Auth-Token` 带入您的身份 Token 信息，用于完成认证
<a name="u858Z"></a>
### 获取用户信息
![image.png](https://cdn.nlark.com/yuque/0/2023/png/1488614/1698134439857-a809580a-2590-4df7-9525-15ecacda2d33.png#averageHue=%23f9f9f9&clientId=u5c1a7404-8935-4&from=paste&height=109&id=uadf181d6&originHeight=164&originWidth=798&originalType=binary&ratio=1.5&rotation=0&showTitle=false&size=10588&status=done&style=none&taskId=ud677c7fd-2a28-4a76-ae3c-81793feb0a7&title=&width=532)
```python
import requests

USER = "xdd1997"
url_user = 'https://www.yuque.com/api/v2/users'
header = {"X-Auth-Token": "your Token"}
resu = requests.get(url_user, headers = header).json()
resu
```
![image.png](https://cdn.nlark.com/yuque/0/2023/png/1488614/1698130887084-51298bea-5244-486b-884d-a76fe717353b.png#averageHue=%23faf9f9&clientId=u48d3dd8a-01e9-4&from=paste&height=343&id=u86f52bd4&originHeight=515&originWidth=1431&originalType=binary&ratio=1.5&rotation=0&showTitle=false&size=63344&status=done&style=none&taskId=ub657902f-24de-40c9-a059-2345683541b&title=&width=954)
<a name="jJQ31"></a>
### 获取用户/团队名下仓库列表
![image.png](https://cdn.nlark.com/yuque/0/2023/png/1488614/1698132679744-ee59b179-5d20-48d7-80fc-3282441fe8fb.png#averageHue=%23f9f9f8&clientId=u48d3dd8a-01e9-4&from=paste&height=233&id=u02a3296b&originHeight=350&originWidth=843&originalType=binary&ratio=1.5&rotation=0&showTitle=false&size=28232&status=done&style=none&taskId=u56901d3f-e777-413b-a3ac-e17b3fb53de&title=&width=562)
```python
url_repo = 'https://www.yuque.com/api/v2/users/' + USER + "/repos"
Repo_Result = requests.get(url_repo, headers = header).json()['data']
Repo_Result
```
![image.png](https://cdn.nlark.com/yuque/0/2023/png/1488614/1698131004426-115bbd5b-e1ae-4ec4-b100-fd071b0ead4e.png#averageHue=%23f8f7f6&clientId=u48d3dd8a-01e9-4&from=paste&height=259&id=u9ce0d705&originHeight=628&originWidth=1671&originalType=binary&ratio=1.5&rotation=0&showTitle=false&size=94453&status=done&style=none&taskId=u4102d909-8ba0-4f22-93bf-3b370934002&title=&width=688)
```python
# 获得所有仓库的 id, id 是仓库的唯一标识
repo_ids = []
for item in Repo_Result:
    repo_ids.append(item["id"])
    
repo_ids
```
> [4240****,  2120****,  1087****]


<a name="87c3e0f5"></a>
### 获得一个仓库下的文档列表
![image.png](https://cdn.nlark.com/yuque/0/2023/png/1488614/1698132735781-3ae6ca09-9752-4db3-9064-d5c1cbfb93fe.png#averageHue=%23f6f6f5&clientId=u48d3dd8a-01e9-4&from=paste&height=124&id=u40e6485b&originHeight=186&originWidth=620&originalType=binary&ratio=1.5&rotation=0&showTitle=false&size=12864&status=done&style=none&taskId=u3b9a203b-500b-4a6b-a8c5-f91490a0765&title=&width=413.3333333333333)
```python
repo_id = '4240****'
url_docs = 'https://www.yuque.com/api/v2/repos/'+ repo_id +'/docs'
Doc_Result = requests.get(url_docs, headers = header).json()['data']
Doc_Result
```

<a name="bnFHj"></a>
### 获得一个仓库下所有文档的 slug
```python
# slug 是文档的唯一标识
slugs = []
for item in Doc_Result:
    slugs.append(item['slug'])
slugs
```

<a name="3324e1f9"></a>
### 获取单篇文档信息
![image.png](https://cdn.nlark.com/yuque/0/2023/png/1488614/1698132860499-4deb5e3a-2bf4-4511-a013-87b3e19b011b.png#averageHue=%23f4f4f3&clientId=u48d3dd8a-01e9-4&from=paste&height=71&id=ufc17e74d&originHeight=106&originWidth=624&originalType=binary&ratio=1.5&rotation=0&showTitle=false&size=8649&status=done&style=none&taskId=u898057a9-239e-4631-818e-b6735fc605e&title=&width=416)
```python
slug = "gbhna********"
url = f"https://www.yuque.com/api/v2/repos/{repo_id}/docs/{slug}"
Repo_Result = requests.get(url, headers = header).json()
Repo_Result
```
![image.png](https://cdn.nlark.com/yuque/0/2023/png/1488614/1698132949713-63533369-ad0c-497c-8cf5-bf485bfe5c0c.png#averageHue=%23f7f6f5&clientId=u48d3dd8a-01e9-4&from=paste&height=286&id=ua733843a&originHeight=429&originWidth=855&originalType=binary&ratio=1.5&rotation=0&showTitle=false&size=62800&status=done&style=none&taskId=uef9c5b08-c94e-49ee-a0db-355d426bfe6&title=&width=570)
<a name="cd79e8e4"></a>
### 获取某一篇文档内容
```python
resu = Repo_Result["data"]["body"]
resu
```
![image.png](https://cdn.nlark.com/yuque/0/2023/png/1488614/1698131399427-df73d544-19f8-499a-be4d-711821517237.png#averageHue=%23f6f4f1&clientId=u48d3dd8a-01e9-4&from=paste&height=338&id=vtuwa&originHeight=507&originWidth=1670&originalType=binary&ratio=1.5&rotation=0&showTitle=false&size=197470&status=done&style=none&taskId=u734ac0ee-219c-424e-84cc-21cf6b171f6&title=&width=1113.3333333333333)
```python
'---<br />title: Python导出语雀文档<br />categories: [Python]<br />tags: [Python，语雀]<br />date: 2023-10-24<br />updated: 2023-10-24<br />cover:  https://mypic2016.oss-cn-beijing.aliyuncs.com/picGo/202310241331546.png<br />---\n\n\n<a name="xiwvL"></a>\n## 方法1\n\n1. 代码来源：[https://github.com/burpheart/yuque-crawl](https://github.com/burpheart/yuque-crawl)\n2. 限制：这个代码只能下载公开的仓库的md文件\n3. 根据自己需要，稍稍修改了下以便能下载自己指定的一些仓库，得到下面代码：\n```python\n# BY @burpheart\n# https://www.yuque.com/burpheart/phpaudit\n# https://github.com/burpheart\nimport sys\n\nimport requests\nimport json\nimport re\nimport os\nimport urllib.parse\n\ntset = []\n\n\ndef save_page(book_id, sulg, path):\n    docsdata = requests.get(\n        \'https://www.yuque.com/api/docs/\' + sulg + \'?book_id=\' + book_id + \'&merge_dynamic_data=false&mode=markdown\')\n    if (docsdata.status_code != 200):\n        print("文档下载失败 页面可能被删除 ", book_id, sulg,path, docsdata.content)\n        return\n    docsjson = json.loads(docsdata.content)\n\n    f = open(path, \'w\', encoding=\'utf-8\')\n    f.write(docsjson[\'data\'][\'sourcecode\'])\n    f.close()\n\n\ndef get_book(url, save_path):\n    docsdata = requests.get(url)\n    data = re.findall(r"decodeURIComponent\\(\\"(.+)\\"\\)\\);", docsdata.content.decode(\'utf-8\'))\n    docsjson = json.loads(urllib.parse.unquote(data[0]))\n    test = []\n    list = {}\n    temp = {}\n    md = ""\n    table = str.maketrans(\'\\/:*?"<>|\' + "\\n\\r", "___________")\n    prename = ""\n    if (os.path.exists(save_path + "/" + str(docsjson[\'book\'][\'id\'])) == False):\n        os.makedirs(save_path + "/" + str(docsjson[\'book\'][\'id\']))\n\n    for doc in docsjson[\'book\'][\'toc\']:\n        if (doc[\'type\'] == \'TITLE\' or doc[\'child_uuid\']!= \'\'):\n            filename = \'\'\n            list[doc[\'uuid\']] = {\'0\': doc[\'title\'], \'1\': doc[\'parent_uuid\']}\n            uuid = doc[\'uuid\']\n            temp[doc[\'uuid\']] = \'\'\n            while True:\n                if (list[uuid][\'1\'] != \'\'):\n                    if temp[doc[\'uuid\']] == \'\':\n                        temp[doc[\'uuid\']] = doc[\'title\'].translate(table)\n                    else:\n                        temp[doc[\'uuid\']] = list[uuid][\'0\'].translate(table) + \'/\' + temp[doc[\'uuid\']]\n                    uuid = list[uuid][\'1\']\n                else:\n                    temp[doc[\'uuid\']] = list[uuid][\'0\'].translate(table) + \'/\' + temp[doc[\'uuid\']]\n                    break\n            if ((os.path.exists(save_path + "/" + str(docsjson[\'book\'][\'id\']) + \'/\' + temp[doc[\'uuid\']])) == False):\n                os.makedirs(save_path + "/" + str(docsjson[\'book\'][\'id\']) + \'/\' + temp[doc[\'uuid\']])\n            if (temp[doc[\'uuid\']].endswith("/")):\n                md += "## " + temp[doc[\'uuid\']][:-1] + "\\n"\n            else:\n                md += "  " * (temp[doc[\'uuid\']].count("/") - 1) + "* " + temp[doc[\'uuid\']][\n                                                                         temp[doc[\'uuid\']].rfind("/") + 1:] + "\\n"\n        if (doc[\'url\'] != \'\'):\n            if doc[\'parent_uuid\'] != "":\n                if (temp[doc[\'parent_uuid\']].endswith("/")):\n                    md += " " * temp[doc[\'parent_uuid\']].count("/") + "* [" + doc[\'title\'] + "](" + urllib.parse.quote(\n                        temp[doc[\'parent_uuid\']] + "/" + doc[\'title\'].translate(table) + \'.md\') + ")" + "\\n"\n                else:\n                    md += "  " * temp[doc[\'parent_uuid\']].count("/") + "* [" + doc[\'title\'] + "](" + urllib.parse.quote(\n                        temp[doc[\'parent_uuid\']] + "/" + doc[\'title\'].translate(table) + \'.md\') + ")" + "\\n"\n\n                save_page(str(docsjson[\'book\'][\'id\']), doc[\'url\'],\n                          save_path + "/" + str(docsjson[\'book\'][\'id\']) + \'/\' + temp[doc[\'parent_uuid\']] + "/" + doc[\n                              \'title\'].translate(table) + \'.md\')\n            else:\n                md += " " + "* [" + doc[\'title\'] + "](" + urllib.parse.quote(\n                    doc[\'title\'].translate(table) + \'.md\') + ")" + "\\n"\n                save_page(str(docsjson[\'book\'][\'id\']), doc[\'url\'],\n                          save_path + "/" + str(docsjson[\'book\'][\'id\']) + "/" + doc[\n                              \'title\'].translate(table) + \'.md\')\n    f = open(save_path + "/" + str(docsjson[\'book\'][\'id\']) + \'/\' + "/SUMMARY.md", \'w\', encoding=\'utf-8\')\n    f.write(md)\n    f.close()\n\n\nif __name__ == \'__main__\':\n    repos ={"CAD_CAE":"cadcae",\n            "编程语言":"program",\n            "博客文章-公开": "blog"}\n\n    for key, value in repos.items():\n        url = f"https://www.yuque.com/xdd1997/{value}"\n        save_path = f"xdd1997/{key}"\n        get_book(url, save_path)\n        print(f"{key}下载完成")\n        \n```\n\n<a name="eJDYZ"></a>\n## 方法二\n希望能找到一种可以下载private仓库的方法<br />已测试不能运行的库\n\n- [yuque-helper/yuque2book](https://github.com/yuque-helper/yuque2book)\n- [atian25/yuque-exporter](https://github.com/atian25/yuque-exporter)\n\n\n<a name="shb5i"></a>\n## 方法三\n参考： [https://karobben.github.io/2021/03/02/Python/yuqueAPI/](https://karobben.github.io/2021/03/02/Python/yuqueAPI/)\n\n'
```

<a name="JHrn9"></a>
### 保存文档内容为 md 文件
```python
with open(fil_path, "w", encoding="utf-8") as fw:
    fw.write(resu)
```
