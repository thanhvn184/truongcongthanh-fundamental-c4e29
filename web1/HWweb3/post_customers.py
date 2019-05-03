from pymongo import MongoClient
from bson.objectid import ObjectId
from matplotlib import pyplot
uri ="mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(uri)
datbas = client.c4e
# coll = datbas["posts"]
# list = {
#     "title" : "Canon in D x River flows in you",
#     "author": "unknow",
#     "content": "nghe bài hát này làm mình nhớ đến bạn",
# }
# coll.insert_one(list)

#ex_3:

coll_custom = datbas["customers"]
events = coll_custom.find({'ref': 'events'})
events_count = events.count()
wom = coll_custom.find({'ref': 'wom'})
wom_count = wom.count()
ads = coll_custom.find({'ref': 'ads'})
ads_count = ads.count()
#count
print(wom_count)
print(events_count)
print(ads_count)
#chart
labels = 'Events', 'Word of mouth', 'Ads'
sizes = [events_count, wom_count, ads_count]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']

pyplot.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

pyplot.axis('equal')
pyplot.show()
