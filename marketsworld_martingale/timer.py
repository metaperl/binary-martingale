import time

class Timer(object):

    def __init__(self, hours):
        if hours:
            self.seconds_to_run = hours * 60 * 60
        else:
            self.seconds_to_run = False

        self.start_time = time.time()

    def elapsed_time(self):
        return time.time() - self.start_time

    def time_over(self):
        if self.seconds_to_run:
            return self.elapsed_time() > self.seconds_to_run
        else:
            return False

    def status(self):
        if self.seconds_to_run:
            return "Executed for {0} of {1} seconds".format(round(self.elapsed_time()), self.seconds_to_run)
        else:
            return "No time constraints"
