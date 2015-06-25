from flask import Flask, render_template
from cassandra.cluster import Cluster
#from app import app

app = Flask(__name__)
cluster = Cluster(['52.8.165.110'])
session = cluster.connect('fb_report')

@app.route('/index')
def index():
    user = { 'nickname': 'Miguel' } # fake user
    return render_template("index.html",
      			 title = 'Home',
      			 user = user)

@app.route('/cassandra_test/<given_ad_id>/')
def cassandra_test(given_ad_id):
    query_results = session.execute("SELECT ad_id, date_start, clicks, cost_per_unique_click  FROM ads_table WHERE ad_id= %s" % (given_ad_id))
    cities=[]
    for result in query_results:
        cities.append(dict(date=result[1], clicks=result[2], cost_per_unique_click=result[3]))

    return render_template('cities.html', cities=cities)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
