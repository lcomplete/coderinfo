#coding=utf-8

from capture.dbhelper import get_db
from capture.site_capture import SiteCapture
from datetime import datetime
import traceback
from apscheduler.scheduler import Scheduler

def init_scheduler():
    scheduler=Scheduler()
    scheduler.start()
    scheduler.add_interval_job(capture_job, minutes=1)

def capture_job():
    with get_db() as db:
        site_configs= db.query('''select id,site_url,article_limit,capture_class,site_name from capture_site
                where isenabled=1 and isdeleted=0 and
                now()>date_add(capture_date,interval interval_minute minute)''')

    for config in site_configs:
        try:
            capture = SiteCapture(config)
            capture.crawl()
        except :
            print traceback.print_exc()
            with get_db() as db:
                db.execute('update capture_site set failed_date= %s where id= %s',datetime.now(),config.id)
        finally:
            with get_db() as db:
                db.execute('update capture_site set capture_date= %s where id= %s',datetime.now(),config.id)


if __name__=='__main__':
    init_scheduler()
