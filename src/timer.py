import pygame
import datetime

# model
class Timer:
    def __init__(self, seconds):
        self.start_time = datetime.datetime.now()
        self.seconds = seconds

    def time_remaining(self):
        time_since_start = datetime.datetime.now() - self.start_time
        time_remaining_sec = self.seconds - time_since_start.total_seconds()
        return time_remaining_sec
