import random
from abc import ABC, abstractmethod


class ChristmasTree:
    def __init__(self, tree_id):
        self.tree_id = tree_id
        self.state = f"This is a christmas tree {self.tree_id}. I am decorated with: "

    def __str__(self):
        return self.state


class TreeDecorator(ABC):
    @abstractmethod
    def __init__(self, tree: ChristmasTree):
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass


class ChristmasStar(TreeDecorator):
    def __init__(self, tree: ChristmasTree):
        if isinstance(tree, ChristmasTree):
            self.tree = tree
        else:
            raise TypeError(
                "Only not decorated ChristmasTree can be decorated with ChristmasStar. Perhaps you have already decorated it?"
            )

    def __str__(self) -> str:
        self.tree.state = f"{self.tree.state} Christmas Star"
        return self.tree.state


class Garland(TreeDecorator):
    def __init__(self, tree: ChristmasTree):
        if isinstance(tree, ChristmasTree):
            self.tree = tree
        else:
            raise TypeError(
                "Only not decorated ChristmasTree can be decorated with Garland. Perhaps you have already decorated it?"
            )

    def __str__(self) -> str:
        self.tree.state = f"{self.tree.state} Garland"
        return self.tree.state


class Lights(TreeDecorator):
    def __init__(self, tree: ChristmasTree):
        if isinstance(tree, ChristmasTree):
            self.tree = tree
        else:
            raise TypeError(
                "Only not decorated ChristmasTree can be decorated with Lights. Perhaps you have already decorated it?"
            )

    def __str__(self) -> str:
        self.tree.state = f"{self.tree.state} Lights"
        return self.tree.state


if __name__ == "__main__":
    star_tree = ChristmasStar(ChristmasTree(random.randint(1, 1000)))
    garland_tree = Garland(ChristmasTree(random.randint(1, 1000)))
    lights_tree = Lights(ChristmasTree(random.randint(1, 1000)))
    print(star_tree, garland_tree, lights_tree, sep="\n")
