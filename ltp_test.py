# -- coding:UTF-8 --
import pos
import os
import config as cfg
#LTP_DATA_DIR = '/Users/peng_ji/codeHub/jupyter/KG-web/ltp_data_v3.4.0'  # ltp模型目录的路径
par_model_path = os.path.join(cfg.LTP_DATA_DIR, 'parser.model')  # 依存句法分析模型路径，模型名称为`parser.model`

from pyltp import Parser
parser = Parser() # 初始化实例
parser.load(par_model_path)  # 加载模型

#sentence = "唐纳德·特朗普1946年6月14日生于纽约，美国共和党籍政治家、企业家、商人，第45任美国总统。"

def relation_extract(sentence):
    words = pos.sent_split(sentence)
    postags = pos.pos_tag(words)
    arcs = parser.parse(words, postags)  # 句法分析

    relation_dict = {}

    head_idx = None
    for i in range(len(arcs)):
        arc = arcs[i]
        if arc.head == 0:
            head_idx = i
            relation_dict['PRED'] = words[i]
            break


    if head_idx != None:
        for i in range(len(words)):
            if arcs[i].head == head_idx + 1:
                if arcs[i].relation == 'SBV' or arcs[i].relation == 'VOB':
                    relation_dict[arcs[i].relation] = words[i]

    print(relation_dict)
    if 'SBV' in relation_dict and 'VOB' in relation_dict:
        return relation_dict, relation_dict['SBV'] + '|' + relation_dict['PRED'] + '|' + relation_dict['VOB']
    else:
        return None

# print("\t".join("%d:%s" % (arc.head, arc.relation) for arc in arcs))
#
# for i in range(len(words)):
#     print(i, words[i], arcs[i].relation, words[arcs[i].head])
# parser.release()  # 释放模型


if __name__ == '__main__':
    text = open('/Users/peng_ji/codeHub/jupyter/KG-web/2019-12-12/NetEase/fiancial/_____________________ ________________________','r')
    title = text.readlines()[1].strip()
    relation_extract(title)
    # for sentence in content.split('。'):
    #     relation_extract(sentence)
    #print(content)
    #relation_extract(title)