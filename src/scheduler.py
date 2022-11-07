from apscheduler.schedulers.background import BackgroundScheduler
# from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime, timedelta


class Scheduler:
    def __init__(self) -> None:
        self._scheduler = BackgroundScheduler(timezone="Europe/Stockholm")
        self._scheduler.start()

    def add_task(self, function) -> None:
        self._scheduler.add_job(function, next_run_time=datetime.now()+timedelta(minutes=1))
