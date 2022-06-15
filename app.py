from celery import Celery
import time

celery = Celery(
    __name__,
    broker='redis://127.0.0.1:6379/0',
    backend='redis://127.0.0.1:6379/0',
)

@celery.task
def someHeavyFunction(a, b):
    print("**********************")
    print("Calculation initiated")
    summation = a + b
    time.sleep(5)
    print(f"{a}+{b} = {summation}")
    print("**********************")
    return summation
