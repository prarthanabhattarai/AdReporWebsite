from flask import Flask,render_template,request
from flask_cassandra import CassandraCluster

app = Flask(__name__)
cassandra = CassandraCluster()
app.config['CASSANDRA_NODES'] = ['52.8.165.110']

@app.route('/cassandra_test', methods = ['GET', 'POST'])
def cassandra_test():
   
    session = cassandra.connect()
    session.set_keyspace("fb_report")

    if request.method == 'GET':
	return render_template('adpage.html',table = False, graph = False)
    
    elif request.method == 'POST':
	
	if request.form["first"]:
		input_id = request.form["first"]

#		session = cassandra.connect()
#		session.set_keyspace("fb_report")
	
		#cql = "SELECT ad_id, date_start, clicks, cost_per_unique_click, actions_per_impression  FROM ads_table WHERE ad_id= %s" % (input_id)
		#query_results = session.execute(cql)

		cql2 = "SELECT ad_group_id, bid_type, date_start FROM joined_table WHERE account_id = %s" % (input_id)
		result = session. execute(cql2)
	
		ad_set_data=[]
		for r in result:
			ad_set_data.append(dict(ad_group_id=r[0], bid_type=r[1], date_start=r[2]))

		return render_template('adpage.html', account=input_id, ad_set_data=ad_set_data, table=True, graph=False)
	
	elif request.form["second"]:
		
		input_id = request.form["second"]
		cql = "SELECT ad_id, date_start, clicks, cost_per_unique_click, actions_per_impression  FROM adsinfo WHERE ad_id= %s" % (input_id)
		query_results = session.execute(cql)
		clicks_data=[]
		cost_data=[]
		actions = []
		
		for result in query_results:
        #	ads_data.append(dict(ad_id=result[0], date_start=result[1], clicks=result[2], cost_per_uclick=result[3], actions_per_imp=result[4]))
  			clicks_data.append(result[2])	    
			cost_data.append(result[3])
			actions.append(result[4])

		return render_template('adpage.html', ad_set=input_id,clicks_data = clicks_data, cost_data=cost_data, actions = actions,table=False, graph = True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
