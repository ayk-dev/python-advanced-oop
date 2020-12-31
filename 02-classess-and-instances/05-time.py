class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        hh = str(self.hours)
        mm = str(self.minutes)
        ss = str(self.seconds)
        return f"{hh.zfill(2)}:{mm.zfill(2)}:{ss.zfill(2)}"

    def next_second(self):
        self.seconds = (self.seconds + 1) % 60
        self.minutes = (self.minutes + int(self.seconds == 0)) % 60
        self.hours = (self.hours + int(self.minutes == 0 and self.seconds == 0)) % 24
        return self.get_time()


# time = Time(9, 30, 59)
# print(time.next_second())
# time = Time(10, 59, 59)
# print(time.next_second())
time = Time(24, 59, 59)
print(time.get_time())
print(time.next_second())
print(time.next_second())
print(time.next_second())
print(time.next_second())
print(time.next_second())
print(time.next_second())



