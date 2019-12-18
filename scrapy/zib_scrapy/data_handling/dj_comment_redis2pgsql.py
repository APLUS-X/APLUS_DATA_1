import redis
import json
import psycopg2
import time

if __name__ == '__main__':
	pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=0, decode_responses=True)
	conn = redis.Redis(connection_pool=pool)
	pg_conn = psycopg2.connect(dbname='bi', host='10.0.2.85', user='zib', password='zbkj@2018')
	cur = pg_conn.cursor()
	sql_template = '''insert into ods.o_spd_jd_comment (content, score, create_time, color, item, itemid, logdate) values ('%s', %d, '%s', '%s', '%s', '%s', '%s');'''
	log_date = str(time.strftime("%Y-%m-%d", time.localtime()))

	for index in range(conn.llen('jd_comment')):
		json_string = conn.lindex('jd_comment', index)
		if json_string is None:
			print('list is empty. finished!')
			break
		json_dict = json.loads(json_string)
		sql = sql_template % (json_dict['content'].replace('\'', '"'), json_dict['score'], json_dict['time'], json_dict['color'], json_dict['item'].replace('\'', '"'), json_dict['itemid'], log_date)
		cur.execute(sql)
		print('execute:', index)

	pg_conn.commit()
	cur.close()
	pg_conn.close()

