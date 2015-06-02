# -*- coding: utf-8 -*-

import utils
import tournament

# get instances
my_utils = utils.utils()
my_selection = tournament.tournament(10)

# do selection and plot results
for i in range(5):
    my_utils._g2pop = my_selection.selection(my_utils._g1pop)
    my_utils.plotter(i, my_selection._CI)
