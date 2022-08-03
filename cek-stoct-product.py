
import requests
import pyfiglet as f
from urllib3.exceptions import InsecureRequestWarning
import smtplib,ssl
import pywhatkit
import schedule
import time
  
# Suppress the warnings from urllib3
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
  
# sending a get http request to specified url

def product():
        url = "https://shopee.co.id/api/v2/bundle_deal/items/?anchor_item=16155292938&bundle_deal_id=19377555&from_item=16155292938&limit=1&need_recommended_items=true&offset=0&page_source=1"

        response = requests.get(url,
                        verify=False)

        r=response.json()
        return r
        
def authors():
    style = f.figlet_format("https://www.youtube.com/c/Tanlalana/")
    print(style)


def process():
    authors()
    data = product()
    if(data['error']==0):
        print("DATA PRODUCT")
        print("=====================")
        for key in data['data']['items']:
            print(key['name'])
            print(key['stock'])
            print(key['price'])

            local = time.localtime() # get struct_time
            time_string = time.strftime("%m/%d/%Y, %H:%M:%S", local)


            modified = key['name'].replace(" ", "-")
            txt      = modified.replace("/","-")
            link="https://shopee.co.id/"+txt+"-i."+str(key['shopid'])+"."+str(key['itemid'])
            message = "stock tersedia ="+str(key['stock'])+"\n\n link ="+link+"\n\n update on : "+time_string

            if(key['stock']!=0):

                    pywhatkit.sendwhatmsg_instantly("+6282135285146", message, 10,True, 2)
        
    else:
        print('error get data')
    
def main():
    schedule.every(10).seconds.do(process)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
      main()