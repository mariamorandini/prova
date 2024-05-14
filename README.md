# World Energy Consumption


The reference dataset is [World Energy Dataset](https://github.com/owid/energy-data)
In these directories is organized the submission of the work wich involves some analysis and the aggregation of them in an interactive [website](https://mariamorandini.github.io/world-energy-consumption-/). 

Specifically:
- [**data**](./data): contains all the data coming from the resource above, and the processed files aggregated over nations. In [map files](.data/ne_10m_admin_0_countries) are stored .shp files needed for the plots of the world maps. Lastly in [backround map](./data/MAP.png) is available the .png file containing the background wallpaper used for the final [website](https://mariamorandini.github.io/world-energy-consumption-/). 

- [**src_**](./src_): contains different .py files used in the cleaning steps of the dataset. They have all indicated their functions within, but we give here a brief outline: 
    - [*insert iso code*](./src_/consumptions_dataset.py): inserts ISO codes corresponding to each country, to ease the plots on the world map;
    - [*renaming countries*](./src_/renaming_countries.py): renames some countries to avoid disambiguations with the plots; 
    - [*consumption dataset*](./src_/consumptions_dataset.py), [*consumption per capita*](./src_/consumptions_per_capita.py) and [*create world*](./src_/create_world_df.py) perform some filtering and agggregations of the dataset needed in the analyses. 

- [**analyses**](./analyses): contains different jupyter notebooks to be run separately, to obtain the different  interactive .HTML files then aggregated in the final output. 

The outputs are not stored in any folder, to ease the conflicts with the reproducibility of the website. The [index](./index.html) file stores the code to create the final website, according to the format defined in [format](./styles2.css). 

# -------------------
## Reproducibility: 

To reproduce the outputs is then suggested to: 
- *Option 1 - Observing The result from Local Machine*:  Run the HTML file [final output](./outputs/index.html), on the local machine. 
- *Option 2 - Reproducing the Result*: 
    - Run the [Analyses Scripts](./analyses) to generate the single outputs;
    - Run the Run the HTML file [final output](./outputs/index.html), on the local machine. 
- *Option 1 - Observing The result directly*:  The results can also be directly inspected at the following [link](https://mariamorandini.github.io/world-energy-consumption-/).
