# -*- coding: utf-8 -*-

import numpy as np
import copy


class tournament(object):

    @property
    def tournament_size(self):
        return self._tournament_size

    @property
    def offspring(self):
        return self._offspring

    @property
    def parent(self):
        return self._parent

    @property
    def CI(self):
        return self._CI

    def __init__(self, tsize=10):
        # CI is assigned according to paper
        self._CI = [(4, 10), (80, 100), (57, 73), (70, 94), (92, 112), (93, 112),
             (91, 113), (91, 113), (84, 104), (64, 82), (45, 58), (38, 52), (23, 33),
             (14, 24), (15, 25), (6, 14), (6, 14)]
        self._tournament_size = tsize

    def selection(self, input_pop):
        self._offspring = np.zeros(input_pop.size, int)
        self._parent = copy.deepcopy(input_pop)
        for i in range(self._parent.size):
            np.random.shuffle(self._parent)
            self._offspring[i] = np.amax(self._parent[0:self._tournament_size])
        return self._offspring
