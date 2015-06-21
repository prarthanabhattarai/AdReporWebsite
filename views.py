from flask import render_template
from app import app
from flask import Flask
from flask_cassandra import CassandraCluster

#app = Flask(__name__)
#cassandra = CassandraCluster()
#app.config['CASSANDRA_NODES'] = ['52.8.165.110']

@app.route('/index')
def index():
    user = { 'nickname': 'Miguel' } # fake user
    return render_template("index.html",
       title = 'Home',
       user = user)

@app.route("/cassandra_test")
def cassandra_test():
    app = Flask(__name__)
    cassandra = CassandraCluster()
    app.config['CASSANDRA_NODES'] = ['52.8.165.110']
    #app.config['CASSANDRA_NODES'] = ['52.8.165.110','52.8.81.20', '52.8.160.0', '52.8.160.210']
   
    session = cassandra.connect()

    session.set_keyspace("fb_report")
    cql = "SELECT ad_group_id,bid_actions,bid_type  FROM bid_table LIMIT 10"
    query_results = session.execute(cql)

    cities=[]
    for result in query_results:
	cities.append(dict(ad_group_id=result[0], bid_actions=result[1], bid_type=result[2]))
    
    return render_template('cities.html', cities=cities)

