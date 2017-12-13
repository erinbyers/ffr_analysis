"""

"""
# todo use the small rectangles to make the migmin_field rectangles

from polygon_utils import *
import E22


# some of the plots are not numbered the same way always in the result
# files (due to waypoint list errors).

def migmin_rectangles():

    def all_field_big_rectangles():
        # old and still used version
        large_rectangles = divide_rectangle(E22.main_rectangle, 3, 1)
        plots = []
        for r in large_rectangles:
            plots += divide_rectangle(r, 16, 1)
        return plots

    plot_indexes = [0,   1,  4,  5,  8, 11, 13, 15,
                    30, 28, 26, 25, 23, 22, 19, 18,
                    32, 35, 36, 38, 41, 43, 46, 47]
    plots = all_field_big_rectangles()
    plots_used = [plots[i] for i in plot_indexes]
    return {key + 1: x for key, x in enumerate(plots_used)}
# my numbering was 18, 19, 22, 23, 25, 26, 28, 30,


treatment_names = {'N': 'Norite', 'O': 'Olivine', 'L': 'Larvikite',
                   'M': 'Marble', 'D': 'Dolomite', 'C': 'Control'}


# # this is with the columnwise numbering (not back and forth in an S)
# treatments = {i + 1: treatment_names[t]
#               for i, t in enumerate('NOLOMNDCDLNMOCDLOMLCDNCM')}

# this is with the columnwise numbering back and forth in an S.
treatments = {i + 1: treatment_names[t]
              for i, t in enumerate('NOLOMNDCLDCOMNLDOMLCDNCM')}


def data_files_rough_filter(filenames):
    """filenames is a list of filenames.  

    Returns a list of filenames where the files which we are sure do
    not belong to the migmin experiment have been taken away

    """
    return [x for x in filenames if x.find('_Plot_') > -1]


def agropro_rectangles():  # todo move
    keys = [128, 228, 127, 227, 214, 213, 112, 111, 211, 108, 107,
            332, 331, 330, 329, 429, 424, 323, 423, 322, 321, 316,
            315, 415, 305, 401, 528, 628, 527, 627, 522, 622, 521,
                621, 518, 517, 617, 508, 507, 606, 505, 605]
    small = small_rectangles()
    return {key: small[key] for key in keys}

# treatments = {}

# for i,t in enumerate(
#     treatments[i+1] = treatment_names[t]
