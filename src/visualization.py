"""
src.visualization
-----------------
Utils and settings for plots.
"""

############################################################
# Imports
############################################################

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.ticker import PercentFormatter
from typing import Literal


############################################################
# Color Definitions
############################################################

# Core colors
blue = "#002147"
dark_blue = "#00152E"
light_blue = "#6CACE4"

gold = "#C7A252"
light_gold = "#E6D3A3"

green = "#5DA685"
dark_green = "#3F7D6C"
light_green = "#A8D5BA"

red = "#C4473A"
coral = "#E06A5F"

gray = "#6F6F6F"
light_gray = "#D9D9D9"

white = "#FFFFFF"


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Primary palette (balanced, publication-safe)
palette = [
    blue,
    green,
    gold,
    light_blue,
    coral,
    gray,
]

# Muted palette (good for papers)
muted = [
    dark_blue,
    dark_green,
    light_gold,
    light_blue,
    coral,
    light_gray,
]

# Vibrant palette (presentations)
vibrant = [
    blue,
    light_blue,
    green,
    gold,
    red,
    coral,
]

# Monochrome blue palette
blues = [
    dark_blue,
    blue,
    light_blue,
    light_gray,
]


############################################################
# Custom colormaps
############################################################

class cmap:
    """Container of custom colormaps."""

    blue_cmap = mcolors.LinearSegmentedColormap.from_list(
        "blue_scale",
        [white, light_blue, blue]
    )

    green_cmap = mcolors.LinearSegmentedColormap.from_list(
        "green_scale",
        [white, light_green, green]
    )

    coral_cmap = mcolors.LinearSegmentedColormap.from_list(
        "coral_scale",
        [white, coral]
    )

    heat_cmap = mcolors.LinearSegmentedColormap.from_list(
        "heat",
        [light_blue, white, coral, red]
    )

    diverging_cmap = mcolors.LinearSegmentedColormap.from_list(
        "diverging",
        [coral, white, blue]
    )

    categorical_cmap = mcolors.ListedColormap(palette)



############################################################
# Applied Global Settings
############################################################

plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['CMU Sans Serif'],
    'axes.titleweight': 'bold',
    'axes.prop_cycle': plt.cycler(color=palette),
})


############################################################
# Plotting
############################################################

def percent_axis(which: Literal['x', 'y']):
    """Formats an axis to have ticks in percent.

    Assumes values in [0,1].

    Parameters:
    -----------
    which : Literal['x', 'y']
        Which axis to format.
    """
    if which.lower() == 'x':
        plt.gca().xaxis.set_major_formatter(PercentFormatter(1))
    elif which.lower() == 'y':
        plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
