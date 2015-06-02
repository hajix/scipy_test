# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt


class utils(object):

    # initial generation
    @property
    def g1pop(self):
        return self._g1pop

    @property
    def g1dist(self):
        return self._g1dist

    @property
    def g2pop(self):
        return self._g2pop

    @property
    def g2dist(self):
        return self._g2dist

    def __init__(self):
        self.g1()

    def g1(self):
        # make fitness distribution
        # s(1) = 590
        init_pop = np.ones(1000, int)
        # s(2) = 200
        tmp = np.array([200])
        tmp.fill(2)
        init_pop[590:790] = tmp
        # s(3) = 42
        tmp = np.array([42])
        tmp.fill(3)
        init_pop[790:832] = tmp
        # s(4) = 36
        tmp = np.array([36])
        tmp.fill(4)
        init_pop[832:868] = tmp
        # s(5) = 30
        tmp = np.array([30])
        tmp.fill(5)
        init_pop[868:898] = tmp
        # s(6) = 22
        tmp = np.array([22])
        tmp.fill(6)
        init_pop[898:920] = tmp
        # s(7) 20
        tmp = np.array([20])
        tmp.fill(7)
        init_pop[920:940] = tmp
        # s(8) = 18
        tmp = np.array([18])
        tmp.fill(8)
        init_pop[940:958] = tmp
        # s(9) = 15
        tmp = np.array([15])
        tmp.fill(9)
        init_pop[958:973] = tmp
        # s(10) = 11
        tmp = np.array([11])
        tmp.fill(10)
        init_pop[973:984] = tmp
        # s(11) = 6
        tmp = np.array([6])
        tmp.fill(11)
        init_pop[984:990] = tmp
        # s(12) = 4
        tmp = np.array([4])
        tmp.fill(12)
        init_pop[990:994] = tmp
        # s(13) = 2
        tmp = np.array([2])
        tmp.fill(13)
        init_pop[994:996] = tmp
        # s(14) = 1
        tmp = np.array([1])
        tmp.fill(14)
        init_pop[996:997] = tmp
        # s(15) = 1
        tmp = np.array([1])
        tmp.fill(15)
        init_pop[997:998] = tmp
        # s(16) = 1
        tmp = np.array([1])
        tmp.fill(16)
        init_pop[998:999] = tmp
        # s(17) = 1
        tmp = np.array([1])
        tmp.fill(17)
        init_pop[999:1000] = tmp
        self._g1pop = init_pop
        return init_pop

    def ditribution(self):
        self._g1dist = np.bincount(self._g1pop)[1:18]
        self._g2dist = np.bincount(self._g2pop)[1:18]
        print((self._g1dist))
        print((self._g2dist))

    def plotter(self, fig_name=0, confidance_interval=None):
        self._g2pop.sort()
        self.ditribution()
        x = np.linspace(1, 17, 17)

        # cumulative
        #plt.figure(1)
        #plt.title('cumulative fitness distribution')
        #plt.plot(x, np.cumsum(self._g1dist), 'b', x, np.cumsum(self._g2dist), 'r')
        #plt.legend(['befor selection', 'after selection'], loc=4)
        #plt.grid()

        # distriution
        plt.figure(str(fig_name))
        plt.title('fitness distribution')
        plt.plot(x, self._g2dist, 'r')
        #plt.plot(x, self._g1dist, 'b')
        # draw CI if exist
        if (confidance_interval is not None):
            for i in range(len(confidance_interval)):
                plt.plot(np.array([i + 1, i + 1], int), np.array([confidance_interval[i][0], confidance_interval[i][1]], int),
                     c='b', linewidth=3, solid_capstyle='round')
                plt.legend(['after selection', 'CI'], loc=1)
        else:
            plt.legend(['after selection'], loc=1)
        plt.grid()
        plt.show()
