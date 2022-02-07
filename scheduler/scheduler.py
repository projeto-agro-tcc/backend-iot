from apscheduler.schedulers.background import BackgroundScheduler
from scheduler.tasks.task_catch_data import CatchDataFromReceivedData


def start():
    scheduler = BackgroundScheduler()
    catch_data = CatchDataFromReceivedData()
    scheduler.add_job(catch_data.get_data, "interval", minutes=1, id="task_001", replace_existing=True)
    scheduler.start()
