# -- coding:UTF-8 --
import argparse, os
import config as cfg
from ltp_test import relation_extract

parser = argparse.ArgumentParser()
parser.add_argument('--date', type=str, help='please input date')
args = parser.parse_args()


date_dir = os.path.join(cfg.FILE_DIR, args.date)

web_list = os.listdir(date_dir)

res_date_dir = os.path.join(cfg.SAVE_DIR, args.date)
if not os.path.exists(res_date_dir):
    os.makedirs(res_date_dir)


for web in web_list:
    if '.' in web:
        continue
    web_dir = os.path.join(date_dir, web)
    web_res_dir = os.path.join(res_date_dir, web)
    if not os.path.exists(web_res_dir):
        os.makedirs(web_res_dir)

    type_list = os.listdir(web_dir)


    for t in type_list:
        type_dir = os.path.join(web_dir, t)
        news_list = os.listdir(type_dir)
        for news in news_list:
            news_path = os.path.join(type_dir, news)
            text = open(news_path, 'r')
            title = text.readlines()[1].strip()
            res = relation_extract(title)
            if not res:
                continue

            news_res_path = os.path.join(web_res_dir, news+'_res.txt')
            with open(news_res_path, 'w') as wf:
                wf.write(res[-1] + '/n')
            text.close()