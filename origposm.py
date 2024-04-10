import json
from ru.travelfood.simple_ui import NoSQL as noClass
from java import jclass

#это для нативного тоста
from android.widget import Toast
from com.chaquo.python import Python

def scan_wifi_open(hashMap,_files=None,_data=None):
    global selected

    if not hashMap.containsKey("WIFIConnectScan"):
        
        hashMap.put("WIFIConnectScan","")
        hashMap.put("WIFIStartScan","")
    
    j = { "customcards":         {

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
                c =  {
                    "key": str(line['BSSID']),
                    "ssid": "SSID:"+"<b>"+str(line['SSID'])+"</b>",
                    "bssid": "BSSID:"+"<b>"+str(line['BSSID'])+"</b>",
                    "level": "level:"+"<b>"+str(line['level'])+"</b>"
                    }
                
                j["customcards"]["cardsdata"].append(c)
        
        except ValueError:
            hashMap.put("toast",str(hashMap.get("WIFIResults")))

    hashMap.put("cards",json.dumps(j,ensure_ascii=False).encode('utf8').decode())

    return hashMap

def item_selected(hashMap,_files=None,_data=None):
    global selected
    card=json.loads(hashMap.get("card_data"))
    selected.append(card['key'])
    return hashMap

def wifi_next(hashMap,_files=None,_data=None):
    global selected
    if len(selected)!=3:
        hashMap.put("toast","Количество точек должно быть равно 3")
    else:    
        
        ncl = noClass("positioning")

        ncl.put("p1",selected[0],False)
        ncl.put("p2",selected[1],False)
        ncl.put("p3",selected[2],False)
           
        hashMap.put("FinishProcess","")   
    return hashMap

def init(hashMap,_files=None,_data=None):
    global selected
    global p1,p2,p3
    
    
    ncl = noClass("positioning")

    p1=ncl.get("p1")
    p2=ncl.get("p2")
    p3=ncl.get("p3")

    

    if p1!=None and p2!=None and p3!=None:
        selected=[]
        selected.append(p1)
        selected.append(p2)
        selected.append(p3)

    
           
    
    return hashMap  
