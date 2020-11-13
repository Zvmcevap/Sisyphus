class Task:
    def __init__(self, user_id, task_name, task_colour, task_image):
        self.task_id = 0
        self.user_id = user_id
        self.task_name = task_name
        self.task_colour = task_colour
        self.task_image = task_image
        self.onesies_todo = []
        self.onesies_complete = []
        self.finite = True
        self.task_completion = False

    def onesie_finished(self, onesie):
        self.onesies_complete.append(onesie)
        self.onesies_todo.remove(onesie)
        if self.finite and len(self.onesies_todo) == 0:
            self.task_completion = True


class Onesie:
    def __init__(self, task_id, start, finish):
        self.onesie_id = 0
        self.task_id = task_id
        self.start = start
        self.finish = finish
        self.onesie_complete = False
