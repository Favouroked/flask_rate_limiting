from multiprocessing import Queue

from services.message import send_sms

message_queue = Queue()


def start_message_job():
    while True:
        if message_queue.empty():
            continue
        data = message_queue.get()
        send_sms(data)
