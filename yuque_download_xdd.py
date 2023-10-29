import os
import re
import shutil
import requests


def deal_yuque_md(content):
    """ 处理语雀一篇文档body中的内容 """

    # 去除字符串如 <a name="YySRg"></a>
    p1 = re.compile(r'<a name=".*"></a>')
    resu = p1.findall(content)
    if len(resu)>0:
        for str_ii in resu:
            content = content.replace(str_ii, "")

    # 去除图片链接后面的东西
    p2 = re.compile(r'!\[.*\]\(.*\)')
    resu = p2.findall(content)
    if len(resu) > 0:
        url_more_list = []
        for str_ii in resu:
            pat = re.compile(r"\(.*\)")
            resu3 = pat.findall(str_ii)
            if len(resu3)>0:
                pat = re.compile(r"#.*\)")
                resu4 = pat.findall(resu3[0])
                if len(resu4)>0:
                    url_more_list.append(resu4[0])
        for kk in url_more_list:
            content = content.replace(kk, ")")

    return content


def login_get_doc(yuque_token):
    """ 获取语雀文档链接
    Args:
        yuque_token: 从yuque.com处获得的token

    Returns:
        info: 字典形式，返回header.仓库列表.所有文档链接
    """
    url_user = 'https://www.yuque.com/api/v2/user'
    header = {"X-Auth-Token": yuque_token}
    resu = requests.get(url_user, headers=header).json()
    user_name = resu["data"]["login"]

    # 获取仓库信息
    url_repo = 'https://www.yuque.com/api/v2/users/' + user_name + "/repos"
    Repo_Result = requests.get(url_repo, headers=header).json()['data']
    # print(Repo_Result)

    # 获取所有文章链接
    article_url_list = []
    for item in Repo_Result:
        if item['type'] == "Book":
            repo_id = item['id']
            url_docs = 'https://www.yuque.com/api/v2/repos/' + str(repo_id) + '/docs'
            Doc_Result = requests.get(url_docs, headers=header).json()['data']

            for ii in Doc_Result:
                slug = ii['slug']
                url = f"https://www.yuque.com/api/v2/repos/{repo_id}/docs/{slug}"
                article_url_list.append(url)
    info = {"header":header, "Repo_Result":Repo_Result, "article_url_list":article_url_list }
    return info


def download_all_doc(info, doc_download_path):
    """创建文件夹并下载文章"""

    header = info["header"]
    Repo_Result = info["Repo_Result"]
    article_url_list = info["article_url_list"]

    # 创建相应文件夹
    table = str.maketrans('\/:*?"<>|' + "\n\r", "___________")  # 映射表
    if os.path.exists(doc_download_path):
        shutil.rmtree(doc_download_path)  # del folder

    for item in Repo_Result:
        if item['type'] == "Book":
            repo_name = item['name'].translate(table)
            path_repo = os.path.join(doc_download_path, repo_name)
            if not os.path.exists(path_repo):
                os.makedirs(path_repo)

    # 计算文章数目
    count_sum = 0
    for item in Repo_Result:
        if item['type'] == "Book":
            url_docs = 'https://www.yuque.com/api/v2/repos/' + str(item['id']) + '/docs'
            Doc_Result = requests.get(url_docs, headers=header).json()['data']
            count_sum = count_sum + len(Doc_Result)
    # print(count_sum)

    # 下载文章
    count = 0
    for url in article_url_list:
        count += 1
        single_doc = requests.get(url, headers=header).json()
        article_title = single_doc["data"]["title"].translate(table)
        article_body = single_doc["data"]["body"]
        repo_name = single_doc["data"]["book"]["name"].translate(table)
        print(f"正在下载文章：{count}/{count_sum}:{repo_name}/{article_title} ")
        fil_path = os.path.join(doc_download_path, repo_name, article_title + ".md")

        with open(fil_path, "w", encoding="utf-8") as fw:
            resu = deal_yuque_md(article_body)
            fw.write(resu)


if __name__ == "__main__":
    yuque_token = "***"
    info = login_get_doc(yuque_token)
    doc_download_path = r"语雀文章下载位置"
    download_all_doc(info,doc_download_path)
