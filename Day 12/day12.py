from dataclasses import dataclass

from tqdm import tqdm

dict_regions = {}


@dataclass
class Region:
    indexes: list[list[int]]
    area: int = 0
    perimeter: int = 0
    sides: int = 0
    fence_price: int = 0
    discounted_fence_price: int = 0

    def __post_init__(self):
        if self.area is None:
            self.area = 0
        if self.perimeter is None:
            self.perimeter = 0
        if self.sides is None:
            self.sides = 0
        if self.fence_price is None:
            self.fence_price = 0
        if self.discounted_fence_price is None:
            self.discounted_fence_price = 0

    def get_indexes(self):
        return self.indexes

    def add_index(self, i, j):
        self.indexes.append([i, j])

    def add_new_region(self, list_indexes):
        for index in list_indexes:
            if index not in self.indexes:
                self.indexes.append([index[0], index[1]])

    def calculate_area(self):
        self.area = len(self.indexes)

    def get_fence_price(self):
        return self.fence_price

    def get_discounted_fence_price(self):
        return self.discounted_fence_price

    def calculate_perimeter(self):
        perimeter = 4 * self.area
        for i in range(len(self.indexes)):
            pos = self.indexes[i]
            adjacent_cells = getAdjacent(pos[0], pos[1], self.indexes)
            perimeter = perimeter - adjacent_cells
        self.perimeter = perimeter

    def calculate_sides(self):
        corners = 0
        for index in self.indexes:
            x = index[0]
            y = index[1]
            # Outer corners
            if [x - 1, y] not in self.indexes and [x, y - 1] not in self.indexes:
                corners += 1
            if [x + 1, y] not in self.indexes and [x, y - 1] not in self.indexes:
                corners += 1
            if [x - 1, y] not in self.indexes and [x, y + 1] not in self.indexes:
                corners += 1
            if [x + 1, y] not in self.indexes and [x, y + 1] not in self.indexes:
                corners += 1
            # Inner corners
            if [x - 1, y] in self.indexes and [x, y - 1] in self.indexes and [x - 1,
                                                                              y - 1] not in self.indexes:
                corners += 1
            if [x + 1, y] in self.indexes and [x, y - 1] in self.indexes and [x + 1,
                                                                              y - 1] not in self.indexes:
                corners += 1
            if [x - 1, y] in self.indexes and [x, y + 1] in self.indexes and [x - 1,
                                                                              y + 1] not in self.indexes:
                corners += 1
            if [x + 1, y] in self.indexes and [x, y + 1] in self.indexes and [x + 1,
                                                                              y + 1] not in self.indexes:
                corners += 1
        self.sides = corners
        self.discounted_fence_price = self.area * self.sides

    def checkDown(self, index):
        if isValidPosition(index[0] + 1, index[1]) and [index[0] + 1, index[1]] in self.indexes:
            return True
        return False

    def checkUp(self, index):
        if isValidPosition(index[0] - 1, index[1]) and [index[0] - 1, index[1]] in self.indexes:
            return True
        return False

    def checkLeft(self, index):
        if isValidPosition(index[0], index[1] - 1) and [index[0], index[1] - 1] in self.indexes:
            return True
        return False

    def checkRight(self, index):
        if isValidPosition(index[0], index[1] + 1) and [index[0], index[1] + 1] in self.indexes:
            return True
        return False

    def update(self):
        self.calculate_area()
        self.calculate_perimeter()
        self.calculate_fence_price()
        self.calculate_sides()

    def calculate_fence_price(self):
        self.fence_price = self.area * self.perimeter

    def calculate_fence_price_discounted(self):
        pass


def main():
    with open("input.txt", "r") as file:
        matrix = file.readlines()

    matrix = [line.replace("\n", "") for line in matrix]
    len_matrix = len(matrix)
    len_line = len(matrix[0])

    for i in range(len_matrix):
        for j in range(len_line):
            plant = matrix[i][j]
            if dict_regions.get(plant) is None:
                dict_regions[plant] = [Region(indexes=[[i, j]])]

            else:
                list_of_regions = dict_regions.get(plant)
                found_adjacent = False
                for region in list_of_regions:
                    indexes_region = region.get_indexes()
                    if getAdjacent(i, j, indexes_region):
                        region.add_index(i, j)
                        found_adjacent = True
                if not found_adjacent:
                    list_of_regions.append(Region(indexes=[[i, j]]))

    # dict_copy_regions = dict(dict_regions)
    for key, list_regions in tqdm(dict_regions.items()):
        optimizing_regions = True
        value_iteration_changed = True

        delete_index = False
        while not delete_index and optimizing_regions:
            if len(list_regions) == 1:
                break
            delete_index = False
            index_to_delete = 0
            for i in range(len(list_regions)):
                for j in range(len(list_regions)):
                    if i != j:
                        indexes_region1 = list_regions[i].get_indexes()
                        indexes_region2 = list_regions[j].get_indexes()
                        if not delete_index and (any_index_is_adjacent(indexes_region1,
                                                                       indexes_region2)):
                            list_regions[i].add_new_region(indexes_region2)
                            delete_index = True
                            index_to_delete = j
            if delete_index:
                del list_regions[index_to_delete]
                delete_index = False
            else:
                optimizing_regions = False

    total_fence_price = 0
    total_discounted_fence_price = 0
    for key, value in dict_regions.items():
        for region in value:
            region.update()
            total_fence_price = total_fence_price + region.get_fence_price()
            total_discounted_fence_price = total_discounted_fence_price + region.get_discounted_fence_price()

    print("PART 1")
    print(f"The total fence price is {total_fence_price}")
    print("PART 2")
    print(f"The total discounted fence price is {total_discounted_fence_price}")
    # print(dict_regions)


def any_index_is_adjacent(list_indexes_1, list_indexes_2):
    for index in list_indexes_1:
        count_adjacent = getAdjacent(index[0], index[1], list_indexes_2)
        if count_adjacent > 0:
            return True

    return False


def any_index_is_same(list_indexes_1, list_indexes_2):
    for index in list_indexes_1:
        if index in list_indexes_2:
            return True
    return False


def isValidPosition(i, j):
    if i < 0 or j < 0:
        return 0
    return 1


def getAdjacent(i, j, region):
    adj = 0
    # Check all the possible adjacent positions
    if isValidPosition(i - 1, j):
        if [i - 1, j] in region:
            adj += 1
    if isValidPosition(i + 1, j):
        if [i + 1, j] in region:
            adj += 1
    if isValidPosition(i, j - 1):
        if [i, j - 1] in region:
            adj += 1
    if isValidPosition(i, j + 1):
        if [i, j + 1] in region:
            adj += 1
    return adj


if __name__ == "__main__":
    main()
