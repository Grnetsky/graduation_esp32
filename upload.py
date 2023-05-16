from votage import getPpercent
import json

f = open("../config.json")
text = f.read()
f.close()
config = json.loads(text)
del text
class UData():
    data = {}
    def __init__(self):
        self.data['sid'] = config['sid']
        
    def setData(self,key,value):
        self.data[key] = value
        
    def getData(self,key):
        return self.data[key]
    
udata = UData()
    
def uploadData():
    # 获取小车的实时信息上传数据库
    # 获取当前剩余电量
    udata.setData('power',getPpercent())
    
    return 'car:'+json.dumps(udata.data)
    
    