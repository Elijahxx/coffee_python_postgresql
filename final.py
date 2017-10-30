#!/usr/bin/python

import psycopg2

conn = psycopg2.connect(database = "sreehari", user = "", password = "", host = "127.0.0.1", port = "5432")
print "WELCOME"
var=1
while var == 1 :
	print "1.Drink coffee"
	print "2.Recharge"
	print "3.Exit"
	cur = conn.cursor()
	userid = int(input("Enter your userid >> "))
	query = "SELECT *  from coffee where id=(%d)" % (userid)
	cur.execute(query)
	rows = cur.fetchall()
	for row in rows:
	   ID=row[0]
	   NAME=row[1]
	   COIN=row[2]
	choice = input("Enter your choice >> ")
	if(choice == 1) :
		if(COIN >= 10) :
			print "Enjoy your coffee"
			newc=COIN-10
			query = "UPDATE coffee set coin = (%d) where id = (%d)" % (newc,userid) 
			cur.execute(query)
			conn.commit()
		else :
			print "Recharge your card"
	if(choice == 2) :
		want = input("Enter your Recharge >> ")
		query = "UPDATE coffee set coin = (%d) where id = (%d)" % (want,userid)
		print "coins updated"
		cur.execute(query)
		conn.commit()
	if(choice == 3) :
		break
print "Transaction done successfully";
conn.close()