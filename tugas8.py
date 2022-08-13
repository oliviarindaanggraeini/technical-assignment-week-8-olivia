import pymongo
from datetime import datetime
from flask import Flask,request

app = Flask(__name__)


@app.route('/olivia',methods=['POST'])
def entry_tugas():
   dt = datetime.now()

   client = pymongo.MongoClient("mongodb+srv://oliv_22:olivia12@cluster0.a4huxaf.mongodb.net/?retryWrites=true&w=majority")
   db = client['olivia']
   my_collections = db['assignmnet_8']

   kecepatan = request.args.get('kecepatan')
   latitude = request.args.get('latitude')
   longtitude = request.args.get('longitude')

   assignment = {'kecepatan': kecepatan,
                  'latitude' : latitude,
                  'longtitude' : longtitude,
                  'timestamp' : dt
                  }

   result = my_collections.insert_many([assignment])
   return ('data sudah TERSAMPAIKAN')


if __name__ == '__main__':
       app.run(debug=True)
