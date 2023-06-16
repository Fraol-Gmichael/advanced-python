from datetime import timedelta, date

class ContainerDateRangeIterable:
    """I am implementing container iterable no need to implement __next__ method since __iter__ method is generatpr function."""
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self._present_date = start_date

    def __iter__(self):
        current_date = self.start_date
        print("Iter is called")

        while current_date < self.end_date:
            yield current_date
            current_date += timedelta(days=1)

if __name__ == '__main__':
    dates = ContainerDateRangeIterable(date(2023, 5, 1), date(2023, 5, 6))
    for d in dates:
        print(d)
    
