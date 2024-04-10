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
	hashMap.put("toast", "Проверка связи сканирование сети")

	return hashMap