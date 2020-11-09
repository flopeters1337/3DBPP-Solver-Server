
from abc import ABC, abstractmethod
from py3dbp import Bin, Item, Packer


class AbstractSolver(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def solve(self, bins, items):
        return None


class DummySolver(AbstractSolver):
    def __init__(self):
        pass    # TODO

    def solve(self, bins, items):
        pass    # TODO


class SimpleSolver(AbstractSolver):
    def __init__(self):
        super().__init__()
        self.packer = Packer()

    @staticmethod
    def convert_rotation(rotation_type):
        rotation = (0, 0, 0)

        if rotation_type == 1:
            rotation = (90, 0, 0)
        elif rotation_type == 2:
            rotation = (0, 90, 0)
        elif rotation_type == 3:
            rotation = (0, 90, 90)
        elif rotation_type == 4:
            rotation = (0, 0, 90)
        elif rotation_type == 5:
            rotation = (90, 0, 90)

        return rotation

    def solve(self, bins, items):
        for bin in bins:
            self.packer.add_bin(Bin(bin.name, bin.width, bin.height, bin.depth, bin.max_weight))

        for item in items:
            self.packer.add_item(Item(item.name, item.width, item.height, item.depth, item.weight))

        self.packer.pack(distribute_items=True)

        return self.parse_solution()

    def parse_solution(self):
        solution = {}

        bins = []
        for bin in self.packer.bins:
            items = []
            for item in bin.items:
                rotation_coords = self.convert_rotation(item.rotation_type)
                items.append(
                    {
                        "name": item.name,
                        "width": item.width,
                        "height": item.height,
                        "depth": item.depth,
                        "x": item.position[2],  # Because Z and X axes swapped for Unity
                        "y": item.position[1],
                        "z": item.position[0],
                        "rotation_x": rotation_coords[0],
                        "rotation_y": rotation_coords[1],
                        "rotation_z": rotation_coords[2]
                    }
                )

            bins.append({"name": bin.name, "items": items})

        solution['bins'] = bins

        return solution


class GenericBin:
    def __init__(self, name, width, height, depth, max_weight):
        self.name = name
        self.width = width
        self.height = height
        self.depth = depth
        self.max_weight = max_weight


class GenericItem:
    def __init__(self, name, width, height, depth, weight):
        self.name = name
        self.width = width
        self.height = height
        self.depth = depth
        self.weight = weight
