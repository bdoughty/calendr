from datetime import datetime

from calendr.Event import Event


class Calendar:
    def __init__(self):
        self.events_list = []

    def get_events_within_range(self, start, end):
        return [event for event in self.events_list if event.start < end and event.end > start]

    def add_event(self, name, start, end):
        self.events_list.append(Event(name, start, end))

    @staticmethod
    def parse_string_to_datetime(str):
        year, month, day = map(int, str.split())
        return datetime(year, month, day)


if __name__ == "__main__":
    c = Calendar()
    c.add_event("ween", c.parse_string_to_datetime("2017 12 31"), c.parse_string_to_datetime("2018 12 31"))
    print(c.events_list)
