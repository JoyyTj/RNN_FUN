import os
import json
import re

# re 用于正则表达式
# def + def 函数装饰器，内层的函数被隐藏在最外层的函数中
def poem_loader(author = None, constrain = None):

    def sentence_process(para):
    # para = "-181-村橋路不端，數里就迴湍。積壤連涇脉，高林上笋竿。早嘗甘蔗淡，生摘琵琶酸。（「琵琶」，嚴壽澄校《張祜詩集》云：疑「枇杷」之誤。）好是去塵俗，煙花長一欄。"
        result, number = re.subn("（.*）", "", para)
        # 去掉括号内容，返回元组，包含新字符串和替换次数，注意要使用中文的括号
        # 全部处理后r为诗词的原文部分
        result, number = re.subn("{.*}", "", result)
        result, number = re.subn("《.*》", "", result)
        result, number = re.subn("[\]\[]", "", result)
        r = ""
        for s in result:
            if s not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-']:
                r += s;
        r, number = re.subn("。。", "。", r)
        return r

    def json_process(file):
        poems = []
        # dumps和loads用于内存中的转换，dump和load对应于文件的处理
        with open(file, 'rb') as file_content:
            data_dic = json.load(file_content)

        for poem in data_dic:
            pdata = ""
            if author is not None and poem.get("author") != author:
                continue
            paragraph = poem.get("paragraphs")
            flag = False
            for s in paragraph:
                sp = re.split("[，！。]", s)
                for tr in sp:
                    if constrain is not None and len(tr) != constrain and len(tr)!=0:
                        flag = True
                        break
                    if flag:
                        break
            if flag:
                continue
            for sentence in poem.get("paragraphs"):
                pdata += sentence
            pdata = sentence_process(pdata)
            if pdata != "":
                poems.append(pdata)
        return poems

    data = []
    data_dir = './data_set/json/'
    for filename in os.listdir(data_dir):
        if filename.startswith("poet.song"):
            data.extend(json_process(data_dir+filename))
    return data









