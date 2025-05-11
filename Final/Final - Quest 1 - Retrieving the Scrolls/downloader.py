

rates = ["EUR", "GBP", "USD", "DZD", "AUD", "BWP", "BND", "CAD", "CLP", "CNY", "COP", "CZK", "DKK", "HUF", "ISK", "INR", "IDR", "ILS", "KZT", "KRW", "KWD", "LYD", "MYR", "MUR", "NPR", "NZD", "NOK", "OMR", "PKR", "PLN", "QAR", "RUB", "SAR", "SGD", "ZAR", "LKR", "SEK", "CHF", "THB", "TTD"]
ratesForBase = [r for r in rates if r != "USD" and r != "EUR" and r != "GBP"]

import requests
import xmltodict
import json
import random

import threading
import os
from datetime import datetime, timedelta

# URL of the XML data
date = "2011-05-04"
#base = random.choice(ratesForBase)
base = "NZD" # I got this as a base once and I didn't want to constantly download a different base every time


def createlistofdates(startdate):
    """ 
    make list of dates from start to current date
    I did look up what libraries handled dates well cause I didn't want
    to make an iterator that keeps track of leap years and length of each month
    """

    date = datetime.strptime(startdate, "%Y-%m-%d") # converts startdate to datetime format
    enddate = datetime.today()

    listofdates = []
    while date <= enddate:
        listofdates.append(date.strftime("%Y-%m-%d")) #converts datetime format back to string
        date += timedelta(days= 1)

    return listofdates



def downloader(base, number_of_threads, startdate):
    """downloads exchange rates for a base from start date to current as json"""
    print(f"exchange rate downloader starting with {number_of_threads} threads for {base} from {startdate} to current day")

    #checks if file already exists for base
    filename = f"{base}_exchange_rates.json"
    if os.path.isfile(f"./{filename}"):
        print(f"json already exists for base {base}")
        return



    # makes a list of every day from start date to current
    listofdates = createlistofdates(startdate)

    # setup for threading
    range_per_process = len(listofdates) // number_of_threads
    lock = threading.Lock()
    shared_dict = {}


    #idk if its good practice or not to nest function definitions like this
    #but it seemed like the only clean way to have the process access the shared dictionary
    def downloader_process(lock, base, dates):
        """takes in the base and a list of dates and updates a shared dictionary
        with the exchange rates for all dates within the list of dates for a specific base"""
        processdict = {} # format looks like {date : {target country code : exchange rate}}

        for date in dates:
            # create url for date and base
            url = f"https://www.floatrates.com/historical-exchange-rates.html?operation=rates&pb_id=1775&page=historical&currency_date={date}&base_currency_code={base}&format_type=xml"
            
            #create subdict for a specific date
            processdict[date] = {}

            try:
                #get data from url
                response = requests.get(url)
                response.raise_for_status()
                #convert to dict
                data_dict = xmltodict.parse(response.text)
                
                #for each currency it'll save
                for item in data_dict["channel"]["item"]:
                    processdict[date][item["targetCurrency"]] = item["exchangeRate"]


            # I learned this in a club and I enjoy using it cause it handles everything and tells u what went wrong
            except Exception as error:
                print(f"request error: {error}")

        # returns the process dictionary for it to be appended later
        with lock:
            shared_dict.update(processdict)



    threads = [
        threading.Thread(
            target= downloader_process,
            args= (lock, base, listofdates[i * range_per_process: (i + 1) * range_per_process]) #cool method of indexing using the colon pass dates from one index to the next
        )
        for i in range(number_of_threads)
    ]

    #running threads
    for t in threads:
        t.start()
    
    for t in threads:
        t.join()

    #formats the dictionary to be pretty when converted to json
    json_data = json.dumps(shared_dict, indent= 4)

    with open(f"{base}_exchange_rates.json","w") as json_file:
        json_file.write(json_data)

    print("done!")


# put in tryblock so I could interrupt it in vscode
try:
    downloader(base= base,number_of_threads= 10,startdate= date)
except KeyboardInterrupt:
    print("keyboard interrupt")