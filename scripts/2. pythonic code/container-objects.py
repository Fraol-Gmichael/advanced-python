class Boundaries:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height

    def __contains__(self, coordinate):
        x, y = coordinate
        return (0 <= x < self.width) and (0 <= y < self.height)


class Grid:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        self.limits = Boundaries(width, height)

    def __contains__(self, coordinate) -> bool:
        return coordinate in self.limits


if __name__ == "__main__":
    grid = Grid(100, 100)
    print([1, 3] in grid)
