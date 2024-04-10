from java import jclass

#это для нативного тоста
from android.widget import Toast
from com.chaquo.python import Python

import json
from ru.travelfood.simple_ui import SimpleSQLProvider as sqlClass

def test(hashMap,_files=None,_data=None):
	if hashMap.get("listener") == "btn2":
			hashMap.put("toast", "12345")

	return hashMap

def init_on_start(hashMap,_files=None,_data=None):

	hashMap.put("SQLConnectDatabase","test1.DB")
	hashMap.put("SQLExec",json.dumps({"query":"create table IF NOT EXISTS Record(id integer primary key autoincrement,art text, barcode text, name text, qty real)","params":""}))

	return hashMap

def input_qty(hashMap,_files=None,_data=None):
	
	sql = sqlClass()
	success=sql.SQLExec("insert into Record(barcode,name,qty) values(?,?,?)",hashMap.get('bcode')+","+hashMap.get("text_product")+","+str(hashMap.get("qty")))
	success = True

	if success:
					hashMap.put("ShowScreen","Сканирование")
					hashMap.put("toast","Добавлено" + hashMap.get("text_product"))


	return hashMap

def on_start_barcode(hashMap,_files=None,_data=None):
	
	rows=[]
	table  = {
	"type": "table",
	"textsize": "20",

	"columns": [
	{
			"name": "barcode",
			"header": "[Barcode]",
			"weight": "2"
	},
	{
			"name": "name",
			"header": "Name",
			"weight": "2"
	},
		{
			"name": "qty",
			"header": "[Qty]",
			"weight": "1"
	}
	]
	}

	sql = sqlClass()
	res = sql.SQLQuery("select * from Record","")

	records = json.loads(res)
	for record in records:
			rows.append({"barcode":record['barcode'],"name":record['name'],"qty":str(record['qty'])})

	table['rows'] =rows
	hashMap.put("table",json.dumps(table))

	return hashMap

def scan_wifi(hashMap,_files=None,_data=None):
	
	
	if not hashMap.containsKey("WIFIConnectScan"):	
		hashMap.put("WIFIConnectScan","")
		hashMap.put("WIFIStartScan","")
	

	j = { "customcards":         {
		"options":{
		  "search_enabled":True,
		  "save_position":True
		},

		"layout": {
		"type": "LinearLayout",
		"orientation": "vertical",
		"height": "match_parent",
		"width": "match_parent",
		"weight": "0",
		"Elements": [
		{
			"type": "LinearLayout",
			"orientation": "horizontal",
			"height": "wrap_content",
			"width": "match_parent",
			"weight": "0",
			"Elements": [

			  {
				"type": "CheckBox",
				"Value": "@markdown",
				"NoRefresh": False,
				"document_type": "",
				"mask": "",
				"Variable": "markdown",
				"BackgroundColor": "#DB7093",
				"width": "match_parent",
				"height": "wrap_content",
				"weight": 2
				},  
			
			{
			"type": "LinearLayout",
			"orientation": "vertical",
			"height": "wrap_content",
			"width": "match_parent",
			"weight": "1",
			"Elements": [
			{
				"type": "TextView",
				"show_by_condition": "",
				"Value": "@ssid",
				"NoRefresh": False,
				"document_type": "",
				"mask": "",
				"Variable": ""
			},
			{
				"type": "TextView",
				"show_by_condition": "",
				"Value": "@bssid",
				"NoRefresh": False,
				"document_type": "",
				"mask": "",
				"Variable": ""
			},
			{
				"type": "TextView",
				"show_by_condition": "",
				"Value": "@level",
				"NoRefresh": False,
				"document_type": "",
				"mask": "",
				"Variable": ""
			}
			]
			}
			]
		}
		]
	}

}
}
	if hashMap.containsKey("WIFIResults"):
		try:
			wifi = json.loads(hashMap.get("WIFIResults"))

			j["customcards"]["cardsdata"]=[]
			for line in wifi:
				hashMap.put("toast", "SSID:" + str(line['SSID']) + ". level:" + str(line['level']))
				c =  {
					"key": str(line['BSSID']),
					"ssid": "SSID:"+"<b>"+str(line['SSID'])+"</b>",
					"bssid": "BSSID:"+"<b>"+str(line['BSSID'])+"</b>",
					"level": "level:"+"<b>"+str(line['level'])+"</b>"
					}				

				j["customcards"]["cardsdata"].append(c)

			hashMap.remove("WIFIResults")
			hashMap.remove("WIFIConnectScan")
			hashMap.remove("WIFIStartScan")
	
		except ValueError:
			hashMap.put("toast",str(hashMap.get("WIFIResults")))
	else:
		hashMap.put("toast", "no results1")

	hashMap.put("cards",json.dumps(j,ensure_ascii=False).encode('utf8').decode())

	return hashMap