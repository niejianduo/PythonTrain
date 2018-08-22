import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb=myclient['runoobdb']
collist = mydb.collection_names()
#print(collist)

mycol=mydb['sites']
'''
mylist = [
  { "name": "Taobao", "alexa": "100", "url": "https://www.taobao.com" },
  { "name": "QQ", "alexa": "101", "url": "https://www.qq.com" },
  { "name": "Facebook", "alexa": "10", "url": "https://www.facebook.com" },
  { "name": "知乎", "alexa": "103", "url": "https://www.zhihu.com" },
  { "name": "Github", "alexa": "109", "url": "https://www.github.com" },
  {'name':'百度','alexa':'325','url':'http://www.baidu.com'}
]
'''
#添加多条数据
#x=mycol.insert_many(mylist)
#print(x)
#添加一个字段
#y=mycol.update_one({'name':{'$regex':'^Tao'}},{'$set':{"location":'杭州'}})
#print(y)
#z=mycol.update_many({'url':'http://www.baidu.com'},{'$set':{'protocol':'不安全'}})
#print(z)

#添加一条数据
#x=mycol.insert_one({'name':'hao123','url':'www.hao123.com'})
#print(x)
#for x in mycol.find({'location':{'$exists':False}}):
#  print(type(x))
#mycol.update_many({'location':{'$exists':False}},{'$set':{'location':'default'}})
#打印所有文档
#for i in mycol.find():
#  print(i)
#mycol.update_many({'alexa':{'$exists':False}},{'$set':{'alexa':'888'}})

#查找指定字段的数据: 需要的字段设为1，不需要的设为0
#for j in mycol.find({'name':'1','alexa':0}):
#  print(j)
#按给定字段排序
#for doc in mycol.find().sort('alexa',-1):
#  print(doc)
 
#修改多个数据
myquery = { "alexa": { "$gt": "1" } }
newvalues = { "$set": { "alexa": "666" } }
x = mycol.update_many(myquery, newvalues) 
print(x.modified_count, "文档已修改")
#for k in mycol.find():
#  print(k)

