"""
## Problem 2
Use flyweight design pattern and classes of your choice to implement the logic in the diagram
below. The tree factory should decide if it needs to create a new tree object or reuse an existing
one, based on the values of the attributes
"""

from ast import For
from dataclasses import dataclass
from typing import Dict


# objects holding the intrinsic states should be immutable
@dataclass(frozen=True)
class TreeType:
    name: str
    color: str
    texture: str

    def __repr__(self):
        return "_".join([self.color, self.texture, self.name])

    def draw(self, canvas, x, y):
        print(f"Drawing {self} with coordinates {x, y} on {canvas}.")


@dataclass
class Tree:
    x: int
    y: int
    tree_type: TreeType

    def draw(self, canvas):
        self.tree_type.draw(canvas, self.x, self.y)


class TreeFactory:
    initial_trees = {}

    def __init__(self, initial_trees: list[Dict]) -> None:
        for state in initial_trees:
            self.initial_trees[self.get_state_key(state)] = TreeType(**state)

    def get_state_key(self, state: Dict) -> str:
        return "_".join(state.values())

    def get_tree_type(self, name, color, texture):
        key = self.get_state_key({"name": name, "color": color, "texture": texture})
        if not self.initial_trees.get(key):
            print("Creating new treetype: ", key)
            self.initial_trees[key] = TreeType(name=name, color=color, texture=texture)
        else:
            print("Using existing treetype: ", key)
        return self.initial_trees[key]


class Forest:
    def __init__(self) -> None:
        self.trees = []

    def plant_tree(self, tree_factory: TreeFactory, x, y, name, color, texture):
        tree_type = tree_factory.get_tree_type(name, color, texture)
        tree = Tree(x, y, tree_type)
        self.trees.append(tree)

    def draw(self, canvas):
        for tree in self.trees:
            tree.draw(canvas)


if __name__ == "__main__":
    canvas = "BigCanvas"
    initial_trees = [
        {"name": "Olive", "color": "Brown", "texture": "Thick"},
        {"name": "Hazel", "color": "Gray", "texture": "Thin"},
    ]
    factory = TreeFactory(initial_trees)
    forest = Forest()
    tree_variants = [
        [1, 1, "Olive", "Brown", "Thick"],
        [1, 2, "Olive", "Brown", "Thin"],
        [3, 5, "Hazel", "Brown", "Thin"],
        [2, 5, "Hazel", "Gray", "Thin"],
        [2, 5, "Hazel", "Gray", "Cracked"],
        [4, 8, "Magnolia", "Pinky", "Thick"],
        [1, 7, "Olive", "Brown", "Thick"],
        [4, 6, "Olive", "Brown", "Thin"],
    ]
    for variant in tree_variants:
        forest.plant_tree(factory, *variant)
    forest.draw(canvas)
