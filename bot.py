import requests
import datetime

def main():
    now = datetime.datetime.now()
    hour = now.hour
    while True:
        now = datetime.datetime.now()
        current_hour = now.hour
        if 3 < current_hour < 19 and hour < current_hour:
            requests.get('https://api.telegram.org/bot383163486:AAF5llYAvHZqCkdF4H6FQegwhJQCbUFfjic/sendMessage?chat_id=385220023&text=Ok')
            hour = current_hour


if __name__=='__main__':
    main()
