import numpy as np
import matplotlib.pyplot as plt
import pdb
import sys

import open3d as o3d

import os
import time


from parablade.common.config import ReadUserInput
from parablade.blade_3D import Blade3D
from parablade.blade_plot import BladePlot
from parablade.blade_output import BladeOutput

input_config = ReadUserInput('3D.cfg')

t = time.time()
blade_object = Blade3D(input_config)
blade_object.make_blade()
print('The blade geometry was generated in %(my_time).5f seconds\n' % {'my_time': time.time() - t})

# --------------------------------------------------------------------------------------------#
# Write the output files
# --------------------------------------------------------------------------------------------#
blade_output_object = BladeOutput(blade_object)
blade_output_object.print_blade_coordinates()
blade_output_object.print_hub_coordinates()
blade_output_object.print_shroud_coordinates()
if input_config['OPERATION_TYPE'] == "SENSITIVITY":
    blade_output_object.print_sensitivity()

# --------------------------------------------------------------------------------------------#
# Write Mesh files
# --------------------------------------------------------------------------------------------#

# blade_output_object.write_mesh_file()

# blade_output_object.make_stl()


plot_blade_object = BladePlot(blade_object)
plot_blade_object.PLOT_FORMAT = 'MATPLOTLIB'
plot_blade_object.make_plots()