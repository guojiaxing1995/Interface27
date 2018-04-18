#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class OpreationGloabalVar():

    #global _global_dict
    _global_dict = {}

    def __init__(self,new_dict = None):
        self.new_dict = new_dict

    @classmethod
    def set_value(cls,name,value):
        cls._global_dict[name] = value

    @classmethod
    def get_value(cls,name,defVaue=None):
        try:
            return cls._global_dict[name]
        except KeyError:
            return defVaue

    @classmethod
    def push_global_dict(cls,new_dict):
        cls._global_dict = dict(cls._global_dict,**new_dict)


    def deal_data(self,data,key=None,target_data=None):
        target_data_flag =target_data
        if type(data) == dict:
            for key in data:
                self.deal_data(data[key],key,target_data_flag)
        if type(data) == list:
            for i in data:
                self.deal_data(i,None,target_data_flag)
        #if type(data) == str:
        if type(data) == unicode:
            if target_data_flag:
                if type(key) == unicode:
                    if key in target_data:
                        self.new_dict[key] = data
            else:
                self.new_dict[key] = data
        if str(data) == 'None':
            if target_data:
                if type(key) == unicode:
                    if key in target_data:
                        self.new_dict[key] = ''
            else:
                self.new_dict[key] = data
        return self.new_dict


