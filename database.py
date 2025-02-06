import json

class database:
    def __init__(self):
        pass
    def add_data(self,name,password,email):
        with open (r'C:\Users\bhava\PycharmProjects\nlpapp\db.json','r+') as f:
            d = json.load(f)

        if email not in d:
            d[email] = name,password
            with open (r'C:\Users\bhava\PycharmProjects\nlpapp\db.json','w') as f:
                json.dump(d,f)
                return 1
        else:
            return 0
    def search_info(self,email,password):
        with open (r'C:\Users\bhava\PycharmProjects\nlpapp\db.json','r') as f:
            d = json.load(f)
        for i in d:
            if i == email:
                d1 = d[i]
                if  d1[1] == password:
                  return 1
                else:
                  return 0


            else:
                return 0
