import os
from chardet import detect
import argparse


parse = argparse.ArgumentParser()
parse.add_argument("-f" , type=str)
parse.add_argument("-e" , nargs="+")
args = parse.parse_args()

if args.f is not None :
    path = args.f
else :
    path = "c:\\test"

INCLUDE_EXT_LIST = []

if args.e is not None :
    if len(args.e) > 0 :
        '''
        for e in args.e : 
            if e[0] == ".":
                INCLUDE_EXT_LIST.append(e)
            else:
                INCLUDE_EXT_LIST.append("."+e)
        '''
        INCLUDE_EXT_LIST = [e.lower() if e[0:1] =="." else ".{}".format(e.lower()) for e in args.e]
        


if len(INCLUDE_EXT_LIST) == 0:
    INCLUDE_EXT_LIST = [".txt" , ".smi"]

def search_dir(dirname):
    result_list = []
    filenames = os.listdir(dirname)

    for filename in filenames:
        full_path = os.path.join(dirname , filename)
        
        if os.path.isdir(full_path) : 
            result_list.extend(search_dir(full_path))
        else :
            result_list.append(full_path)
    return result_list

def get_encoding_type(filePath):
    with open(filePath , "rb") as f:
        rawdata = f.read()
    codec = detect(rawdata)
    return codec["encoding"]



filelists = search_dir(path)


for file in filelists:
    filename, ext = os.path.splitext(file)
    tempfile = filename+"_tmp"+ext
    if ext.lower() in INCLUDE_EXT_LIST:
        try : 
            encoding = get_encoding_type(file)
            if encoding.lower().find("utf") < 0 :
                with open(file,"r") as read , open(tempfile , "w", encoding="utf-8") as write:
                    write.write(read.read())
                os.unlink(file)
                os.rename(tempfile,file)
                print("{}이 저장 되었습니다".format(file))
        except :
            pass
        finally:
            if os.path.exists(tempfile):
                os.unlink(tempfile)


