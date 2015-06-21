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

@app.route("/cassandra_test")
def cassandra_test():
    query_results = session.execute("SELECT ad_group_id,bid_actions,bid_type  FROM bid_table LIMIT 10")

    cities=[]
    for result in query_results:
        cities.append(dict(ad_group_id=result[0], bid_actions=result[1], bid_type=result[2]))

    return render_template('cities.html', cities=cities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
