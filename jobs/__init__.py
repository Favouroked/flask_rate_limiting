from multiprocessing import Process

from .sms import start_message_job


def terminate_worker(worker):
    try:
        worker.terminate()
        worker.join()
        worker.close()
    except Exception as err:
        print('====> Error occurred terminating process', err)


def init_sms_worker():
    worker = Process(target=start_message_job)
    worker.start()
    return worker

