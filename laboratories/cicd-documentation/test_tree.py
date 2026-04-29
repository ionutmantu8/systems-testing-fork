
from tree import Tree


def test_find_existing_node():
    tree = Tree()
    tree.add(10)
    tree.add(5)
    tree.add(15)

    node = tree._find(5, tree.root)

    assert node is not None
    assert node.data == 5


def test_find_non_existing_node():
    tree = Tree()
    tree.add(10)
    tree.add(5)
    tree.add(15)

    node = tree._find(99, tree.root)

    assert node is None