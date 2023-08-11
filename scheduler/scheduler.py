import schedule 
from datetime import timedelta,time,datetime

def job():
    print('it is a simple scheduler')

schedule.every().minute.at(':15').do(job)

while True:
    schedule.run_pending()
