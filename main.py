"""
See https://core.telegram.org/bots/api#getupdates
"""
import os
import time
import requests

telegram_token = os.getenv('TELEGRAM_TOKEN')
api_url = f"https://api.telegram.org/bot{telegram_token}/"


def run_bot():
    offset = 0

    while True:
        response = requests.get(f"{api_url}getUpdates?offset={offset}")
        if response.status_code == 200:
            content = response.json()
            updates = content['result']
            process_updates(updates)

            if updates:
                offset = updates[-1]['update_id'] + 1  # Mark update as processed
        else:
            print(f"Failed to get updates {response.text}")

        time.sleep(2)


def process_updates(updates):
    for update in updates:
        chat = update['message']['chat']
        username = chat['username']
        requests.post(f"{api_url}sendMessage", json={"chat_id": chat["id"], "text": f"Welcome, {username}"})
        print(username)


if __name__ == '__main__':
    run_bot()
