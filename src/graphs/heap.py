from __future__ import annotations

from typing import List


class Heap:
    def __init__(self, data: List[float] = []):
        self.heap = ['#']
        for el in data:
            self.add(el)

    def add(self, elem: float):
        self.heap.append(elem)
        i = len(self.heap) - 1  # запоминаем позицию элемента, в начале он последний
        while i > 1 and self.heap[i] > self.heap[i // 2]:  # пока элемент больше чем его родители идем вверх
            self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
            i = i // 2

    def get_max(self) -> float:
        return self.heap[1]

    def pop(self) -> float:
        if len(self.heap) == 2:
            return self.heap.pop()
        res = self.heap[1]
        self.heap[1] = self.heap.pop()
        i = 1
        while 2 * i < len(self.heap):  # выполняем пока у элемента i есть левый потомок
            max_val = self.heap[2 * i]
            max_idx = 2 * i

            if 2 * i + 1 < len(self.heap) and self.heap[2 * i + 1] > max_val:  # проверка что есть правый потомок
                max_val = self.heap[2 * i + 1]
                max_idx = 2 * i + 1

            if max_val <= self.heap[i]:
                return res
            else:
                self.heap[i], self.heap[max_idx] = self.heap[max_idx], self.heap[i]
                i = max_idx
        return res

    def sift_down(self, i: int, size: int):
        """

        :param i: индекс опускаемого элемента
        :param size: кол-во элементов в куче, последний элемент в куче имеет индекс size
        :return:
        """
        while 2 * i < size:
            max_val = self.heap[2 * i]
            max_idx = 2 * i

            if 2 * i + 1 < size and self.heap[2 * i + 1] > max_val:  # проверка что есть правый потомок
                max_val = self.heap[2 * i + 1]
                max_idx = 2 * i + 1

            if max_val <= self.heap[i]:
                return
            else:
                self.heap[i], self.heap[max_idx] = self.heap[max_idx], self.heap[i]
                i = max_idx

    @staticmethod
    def sort(data: List[float]) -> Heap:
        n = len(data)
        h = Heap(data)
        i = len(data) // 2
        while i >= 1:
            h.sift_down(i, n)
            i -= 1
        print(h)
        print(h.str_list())
        while n > 1:
            h.heap[1], h.heap[n] = h.heap[n], h.heap[1]
            n -= 1
            h.sift_down(1, n)
        return h

    def __str__(self) -> str:
        s = ""
        queue = [1]
        while queue[-1] <= len(self.heap):
            for el in queue:
                s += str(self.heap[el]) + ' '
            s += '\n'
            new_queue = []
            for el in queue:
                new_queue.append(el * 2)
                new_queue.append(el * 2 + 1)
            queue = new_queue
        return s

    def str_list(self) -> str:
        return self.heap.__str__()
