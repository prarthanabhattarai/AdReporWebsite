from flask import render_template
from flask import Flask
from flask_cassandra import CassandraCluster

app = Flask(__name__)
cassandra = CassandraCluster()
app.config['CASSANDRA_NODES'] = ['52.8.165.110']

@app.route('/index')
def index():
    user = { 'nickname': 'Miguel' } # fake user
    return render_template("index.html", title = 'Home',user = user)

@app.route('/cassandra_test/<input_id>')
def cassandra_test(input_id):
    session = cassandra.connect()

    session.set_keyspace("fb_report")
    cql = "SELECT ad_id, date_start, clicks, cost_per_unique_click  FROM ads_table WHERE ad_id= %s" % (input_id)
    query_results = session.execute(cql)

    cities=[]
    for result in query_results:
        print (result)
        cities.append(dict(ad_id=result[0], date_start=result[1], clicks=result[2], cost_per_unique_click=result[3]))
   
    chart_data=[['apple',10],['banana',20],['cat',30],['dog',40]]
   
    return render_template('cities.html', a=10, b=20, c=30, d=15, e=25 ,cities=cities)
    #return render_template('cities.html', chart_data=chart_data ,cities=cities)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
