import os
import json

dict_ = {
    "GAME":{
        "WIDTH":900,
        "HEIGTH":600,
        "COLOR":(109,135,100)
    },
    "MENU":{
        "WIDTH":500,
        "HEIGTH":600,
        "COLOR":(135,135,100)
    }
}
#dict_=dict()
def abs_path(name_folder):
    path = os.path.abspath(__file__+"/..")
    path = path.split("\\")
    path[-1] = name_folder
    path = "\\".join(path)
    return path


def read_json(name_file,name_folder):
    try:
        path =  abs_path(name_folder)
        path = os.path.join(path,name_file)
        with open(path, 'r') as file:
            dict_read = json.load(file)
        
    except:
        write_json(name_file,name_folder,dict_)
        dict_read = dict_
    return dict_read

def write_json (name_file,name_folder, name_dict):
    path =  abs_path(name_folder)
    path = os.path.join(path,name_file)
    with open(path, 'w') as file:
        json.dump(name_dict,file,ensure_ascii=True,indent=4)

def write_obj_json (name_file,name_folder, name_obj):
    path =  abs_path(name_folder)
    path = os.path.join(path,name_file)
    w_dict = name_obj.__dict__
    print(w_dict)
    with open(path, 'w') as file:
        json.dump(w_dict,file,ensure_ascii=True,indent=4)

#write_json("setting.json","json",dict_)
# dict_ = read_json("setting.json","json")
# print(json.dumps(dict_))
