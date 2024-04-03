class Clock:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def tick(self):
        if self.hours == 23 and self.minutes == 59 and self.seconds == 59:
            self.hours = 0
            self.minutes = 0
            self.seconds = 0
        elif self.minutes == 59 and self.seconds == 59:
            self.hours += 1
            self.minutes = 0
            self.seconds = 0
        elif self.seconds == 59:
            self.minutes += 1
            self.seconds = 0
        else:
            self.seconds += 1

    def set(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes
        self.seconds = 0

    def __str__(self):
        return f"{str(self.hours).zfill(2)}:{str(self.minutes).zfill(2)}:{str(self.seconds).zfill(2)}"


if __name__ == "__main__":
    watch = Clock()
    for i in range(360000):
        print(watch)
        watch.tick()
        if i == 10000:
            break
