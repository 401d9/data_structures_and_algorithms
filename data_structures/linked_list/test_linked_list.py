from .linked_list import LinkedList, Node
import pytest


@pytest.fixture
def empty_list():
    return LinkedList()


@pytest.fixture
def small_list():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    return ll


def test_linked_list_alive():
    assert LinkedList


def test_create_instance_of_list():
    ll = LinkedList()
    assert isinstance(ll, LinkedList)


def test_default_property_length(empty_list):
    assert empty_list._length == 0


def test_insertion_successful(empty_list):
    assert empty_list.head.val is None
    empty_list.insert(25)
    assert empty_list.head.val == 25


def test_length_of_list_increases_on_insertion(empty_list):
    assert len(empty_list) == 0
    empty_list.insert(25)
    assert len(empty_list) == 1

def test_includes_returns_false_if_not.....():
    pass
