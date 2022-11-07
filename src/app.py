from scheduler import Scheduler
import main

scheduler = Scheduler()
scheduler.add_task(main.fetch_and_retweet)

