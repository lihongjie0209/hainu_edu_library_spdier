# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
from pymongo import MongoClient

class BookItemPipeline(object):

    def process_item(self, item, spider):
        hold_state = {'0': {'stateName': '流通还回上架中', 'stateType': 0},
                        '1': {'stateName': '编目', 'stateType': 1},
                        '10': {'stateName': '预借', 'stateType': 10},
                        '12': {'stateName': '清点', 'stateType': 12},
                        '13': {'stateName': '闭架', 'stateType': 13},
                        '14': {'stateName': '修补', 'stateType': 14},
                        '15': {'stateName': '查找中', 'stateType': 15},
                        '16': {'stateName': '重复锁定', 'stateType': 16},
                        '2': {'stateName': '在馆', 'stateType': 2},
                        '3': {'stateName': '借出', 'stateType': 3},
                        '4': {'stateName': '丢失', 'stateType': 4},
                        '5': {'stateName': '剔除', 'stateType': 5},
                        '6': {'stateName': '交换', 'stateType': 6},
                        '7': {'stateName': '赠送', 'stateType': 7},
                        '8': {'stateName': '装订', 'stateType': 8},
                        '9': {'stateName': '锁定', 'stateType': 9}}
        libcode =      {'999': '海南大学图书馆',
                        'CXFG': '城西校区',
                        'DZFG': '儋州校区',
                        'HNDX': '海甸总馆',
                        'KYFG': '科研图书'}
        
        localcode =    {'01': '海甸_哲社一库（北馆二楼）',
                        '02': '海甸_科技书库（北馆三楼）',
                        '03': '海甸_哲社三库（南馆三楼）',
                        '04': '海甸_过刊室',
                        '05': '海甸_现刊阅览室',
                        '06': '海甸_文学书库（北馆四楼）',
                        '07': '海甸_海南地方文献室（南馆三楼）',
                        '08': '海甸_哲社工具书库（北馆五楼）',
                        '09': '海甸_哲社保留本室（北馆五楼）',
                        '10': '海甸_科技保留本室（北馆五楼）',
                        '11': '海甸_原特藏室',
                        '12': '海甸_馈赠室',
                        '13': '海甸_视听资料室',
                        '14': '海甸_多媒体',
                        '15': '海甸_副本库（北馆一楼）',
                        '16': '海甸_光盘中心（南馆六楼）',
                        '17': '海甸_密集一库（北馆一楼）',
                        '18': '海甸_哲社二库（南馆二楼）',
                        '19': '海甸_文检教研室（咨询研究部）',
                        '20': '海甸_科技工具书库（北馆五楼）',
                        '21': '海甸_外文书库(北馆五楼科技工具书库内)',
                        '22': '海甸_密集二库(南馆一楼)',
                        '23': '海甸_博物馆',
                        '24': '海甸_周唐工作室',
                        '25': '海甸_科研经费图书',
                        '30': '海甸_海南华侨与东南亚室（南馆四楼）',
                        '31': '海甸_宋氏家族文献室（南馆三楼）',
                        '32': '海甸_古籍善本书库（南馆三楼）',
                        '33': '海甸_中国海疆研究文献室（南馆四楼）',
                        '34': '海甸_海南旅游文献室（南馆四楼）',
                        '35': '海甸_海南大学学者文库（南馆四楼）',
                        '36': '海甸_少数民族文献室（南馆四楼）',
                        '37': '海甸_业务部门',
                        '39': '海甸_新海南文献室',
                        'B001': '海甸_土木建筑工程学院图书室（理工楼414）',
                        'CX01': '城西_中文书库',
                        'CXFG-BK': '城西_报刊阅览室（综合楼四楼）',
                        'CXFG_ZWSK': '城西_中文书库（综合楼一楼）',
                        'DZFG_01': '儋州_待查',
                        'DZFG_AK': '儋州_A库（图书馆二楼）',
                        'DZFG_BK': '儋州_B库（图书馆二楼）',
                        'DZFG_FZ': '儋州_附中',
                        'DZFG_K': '儋州_报刊阅览室（图书馆一楼）',
                        'DZFG_L': '儋州_外刊',
                        'DZFG_W': '儋州_文昌',
                        'DZFG_WF': '儋州_文法学院',
                        'DZFG_X': '儋州_兴隆',
                        'DZFG_Z': '儋州_中文书库（图书馆二楼）',
                        'DZFG_jm': '儋州_经贸学院',
                        'DZFG_jss': '儋州_检索室',
                        'DZFG_mj': '儋州_密集书库（图书馆附楼一楼）',
                        'DZFG_wx': '儋州_文学书库(图书馆一楼)',
                        'DZFG_xx': '儋州_信息所',
                        'DZFG_zxb': '儋州_咨询部',
                        'DZFG_zz': '儋州_信息所中书',
                        'DZFG_zzw': '儋州_信息所外书',
                        'E001': '材料化工学院图书室（理工楼414）',
                        'F001': '法学院图书室（社科楼C栋211）',
                        'G001': '国际交流学院图书室',
                        'G002': '国际交流学院期刊室',
                        'H001': '海洋学院图书室（海洋学院218）',
                        'H002': '海洋学院期刊室（海洋学院218）',
                        'HNDX': '海甸待查',
                        'J001': '经管学院图书室',
                        'J002': '经管学院期刊室',
                        'KYYS': '科研用书',
                        'L001': '旅游学院图书室',
                        'L002': '旅游学院期刊室',
                        'LMC01': '乐妹村图书室（东方市大田镇乐妹村）',
                        'M001': '马克思主义学院',
                        'N001': '生命学院图书室',
                        'N002': '生命学院期刊室',
                        'NHZC': '南海政策与法律研究中心（社科楼七楼）',
                        'P001': '公共实验中心图书室',
                        'R001': '人文学院图书室（社科楼B栋716）',
                        'R002': '人文学院期刊室',
                        'SXJY': '学生就业指导中心',
                        'T001': '体育部图书室',
                        'W001': '外语学院图书室',
                        'X001': '信息学院图书室（信息学院一楼）',
                        'X002': '信息学院期刊室',
                        'Y001': '艺术学院图书室（艺术学院一楼103）',
                        'Z001': '政公学院图书室（社科楼A栋215）',
                        'Z002': '政公学院期刊室'}
        cirtype_code = {'001': {'cirtype': '001',
                        'descripe': '中文书',
                        'isPreviService': 0,
                        'libcode': '999',
                        'loanNumSign': 0,
                        'name': '中文书'},
                        '002': {'cirtype': '002',
                        'descripe': '外文书',
                        'isPreviService': 0,
                        'libcode': '999',
                        'loanNumSign': 0,
                        'name': '外文书'},
                        '003': {'cirtype': '003',
                        'descripe': '学位论文',
                        'isPreviService': 0,
                        'libcode': '999',
                        'loanNumSign': 0,
                        'name': '学位论文'},
                        '004': {'cirtype': '004',
                        'descripe': '外文期刊',
                        'isPreviService': 0,
                        'libcode': '999',
                        'loanNumSign': 0,
                        'name': '外文期刊'},
                        '006': {'cirtype': '006',
                        'descripe': '电子文献',
                        'isPreviService': 0,
                        'libcode': '999',
                        'loanNumSign': 0,
                        'name': '电子文献'},
                        '007': {'cirtype': '007',
                        'descripe': '中文期刊',
                        'isPreviService': 0,
                        'libcode': '999',
                        'loanNumSign': 0,
                        'name': '中文期刊'},
                        '008': {'cirtype': '008',
                        'descripe': '可以外借的图书',
                        'isPreviService': 0,
                        'libcode': '999',
                        'loanNumSign': 0,
                        'name': '可借书'},
                        '009': {'cirtype': '009',
                        'descripe': '可以外借的期刊',
                        'isPreviService': 0,
                        'libcode': '999',
                        'loanNumSign': 0,
                        'name': '可借刊'},
                        '010': {'cirtype': '010',
                        'descripe': '不可外借的文献',
                        'isPreviService': 0,
                        'libcode': '999',
                        'loanNumSign': 0,
                        'name': '非外借'}}    
            
        for holding in item['holding_list']:
            holding['state'] = hold_state[str(holding['state'])]['stateName']
            holding['orglib'] = libcode[holding['orglib']]
            holding['curlib'] = libcode[holding['curlib']]
            holding['orglocal'] = localcode[holding['orglocal']]
            holding['curlocal'] = localcode[holding['curlocal']]
            holding['cirtype'] = cirtype_code[holding['cirtype']]['name']

        return item

class MongoPipeline(object):

    collection_name = 'hainu_library'

    def __init__(self):
        self.mongo_uri = 'mongodb://127.0.0.1:27017'
        self.mongo_db = 'hainu'

    def open_spider(self, spider):
        self.client = MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]    

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection_name].insert(dict(item))
        return item
