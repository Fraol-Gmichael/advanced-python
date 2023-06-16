from datetime import date, timedelta


class DateRangeSequence:
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self._range = self._create_range()

    def _create_range(self):
        days = []
        current_day = self.start_date
        while current_day < self.end_date:
            days.append(current_day)
            current_day += timedelta(days=1)

        return days

    def __getitem__(self, key):
        return self._range[key]

    def __len__(self):
        return len(self._range)


dates = DateRangeSequence(date(2023, 5, 1), date(2023, 5, 12))
for d in dates:
    print(d)
