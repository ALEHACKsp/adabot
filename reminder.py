import os
import persistence
import time

from apscheduler.schedulers.blocking import BlockingScheduler
from bill import Bill
from twilio.rest import Client

account_sid = os.environ['account_sid']
auth_token = os.environ['auth_token']
my_number = os.environ['whatsapp']

client = Client(account_sid, auth_token)
sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='mon-sun', hour=11)
def verifyBills():

    users = persistence.loadJSON()

    for user in users:
        bills = []
        for bill in users[user]:
            msg = bill.isNextExpiration(7)
            if msg != "":
                bills.append(msg)
        
        body = "\n\n".join(list(map(str, bills)))

        if bills == []:
            body = "Você não tem nenhuma conta próxima do vencimento!"

        toUser = "whatsapp:" + user

        message = client.messages.create(from_=my_number, body=body, to=toUser) 
        print(message.sid)

if __name__ == '__main__':
    sched.start()