import sys
import json
from itertools import zip_longest


def jn_dtset(pth_usr: str, pth_hbby: str) -> dict:
    # формирует словарь из списков хобби и ФИО

    with open(pth_usr, 'r', encoding='utf-8') as users_lst, open(pth_hbby, 'r', encoding='utf-8') as hbby_lst:
        hby = []
        usr = []
        for text1 in users_lst:
            usr.append(text1.replace(","," ").strip())


        for text2 in hbby_lst:
            c=','.join(text2.split(','))
            hby.append(c.strip())

            if len(usr) < len(hby):
                sys.exit(1)

    a = dict(zip_longest(usr,hby))
    return a


dict_out = jn_dtset('users.csv', 'hobby.csv')
with open('task_6_3_res.json', 'w', encoding='utf-8') as dct_w:
    json.dump(dict_out, dct_w, ensure_ascii=False, indent=2)
