import os
import config as cfg
from pyltp import Postagger
from pyltp import Segmentor

pos_model_path = os.path.join(cfg.LTP_DATA_DIR, 'pos.model')  # 词性标注模型路径，模型名称为`pos.model`
seg_model_path = os.path.join(cfg.LTP_DATA_DIR, 'cws.model')

def sent_split(sentence):
    segmentor = Segmentor()
    segmentor.load(seg_model_path)
    words = segmentor.segment(sentence)
    segmentor.release()
    print('\t'.join(words))
    return words


def pos_tag(words):
    postagger = Postagger() # 初始化实例
    postagger.load(pos_model_path)  # 加载模型

    #words = sent_split(sentence)

    postags = postagger.postag(words)  # 词性标注

    print('\t'.join(postags))
    postagger.release()  # 释放模型
    return postags