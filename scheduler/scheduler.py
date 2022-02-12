from apscheduler.schedulers.background import BackgroundScheduler
from scheduler.tasks.task_catch_data import CatchDataFromReceivedData


def start():
    scheduler = BackgroundScheduler(timezone='Brazil/East')
    catch_data = CatchDataFromReceivedData()
    scheduler.add_job(catch_data.get_data, "interval", seconds=20, id="task_001", replace_existing=True)
    scheduler.start()
