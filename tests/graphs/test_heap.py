from graphs.heap import Heap


def test_heap():
    heap = Heap()
    heap.add(10)
    heap.add(8)
    heap.add(3)
    heap.add(17)
    assert heap.get_max() == 17
    heap.pop()
    assert heap.get_max() == 10
