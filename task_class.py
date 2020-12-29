import sqlite3
from os import path


class Task():
    def __init__(self, taskname=None, taskdescription=None, bgcolor=None, fontcolor=None, wholeday=None, fromtime=None, fromday=None, totime=None, today=None, repeating=False):
        self.taskid = 0
        self.name = taskname
        self.description = taskdescription
        self.bgcolor = bgcolor
        self.fontcolor = fontcolor

        self.wholeday = wholeday
        self.fromtime = fromtime
        self.fromday = fromday
        self.totime = totime
        self.today = today

        self.repeating = repeating

        self.repeatings_week = []
        self.repeatings_month = []
        self.finished_tasks = []

    def create_task_from_form(self, formdata):
        ROOT = path.dirname(path.realpath(__file__))
        conn = sqlite3.connect(path.join(ROOT, "database.db"))
        conn.row_factory = sqlite3.Row

        print(formdata)
        self.name = formdata["taskname"]
        self.description = formdata["taskdescription"]
        self.bgcolor = formdata["bgcolor"]
        self.fontcolor = formdata["fontcolor"]

        if "wholedaycheck" not in formdata:
            self.fromtime = formdata["fromtime"]
            self.totime = formdata["totime"]
        else:
            self.wholeday = True
            self.fromtime = "00:00"
            self.totime = "00:00"
        self.fromday = formdata["fromdate"]
        self.today = formdata["todate"]

        for key in formdata:
            if formdata[key] == "on" and key != "repeat":
                if key.isdigit():
                    self.repeatings_month.append(key)
                else:
                    self.repeatings_week.append(key)
            if len(self.repeatings_week) != 0 or len(self.repeatings_month) != 0:
                self.repeating = True
