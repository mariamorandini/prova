# World Energy Consumption

CID: 02478494



(**Disclaimer**: Please note that this Markdown file differs from the version available on GitHub due to personal reasons (CID, and Summative Report) and structural modifications necessary for the website's final publication. These changes were made to resolve conflicts with the `src` files and other structural elements. This README file corresponds specifically to the accompanying `.zip` file and describes how to set up and run the project locally. This structure follows typical data science project guidelines and should be considered the definitive version.)

The reference dataset is [World Energy Dataset](https://github.com/owid/energy-data)
In these directories is organized the submission of the work wich involves some analysis and the aggregation of them in an interactive [website](https://mariamorandini.github.io/world-energy-consumption-/). 

Specifically:
- **data**: contains all the data: [raw](./data/raw) coming from the reference above, and [cleaned](./data/derived) the re-organized one, aggregated over countries. In addition in [map files](.data/ne_10m_admin_0_countries) are stored .shp files needed for the plots of the world maps. Lastly in [backround map](./data/MAP.png) is available the .png file containing the background wallpaper used for the final .HMTL dahsboard.

- **src**: contains different .py files used in the cleaning steps of the dataset. They have all indicated their functions within, but we give here a brief outline: 
    - [*insert iso code*](./src/preprocessing/consumptions_dataset.py): inserts ISO codes corresponding to each country, to ease the plots on the world map;
    - [*renaming countries*](./src/preprocessing/renaming_countries.py): renames some countries to avoid disambiguations with the plots; 
    - [*consumption dataset*](./src/preprocessing/consumptions_dataset.py), [*consumption per capita*](./src/preprocessing/consumptions_per_capita.py) and [*create world*](./src/preprocessing/create_world_df.py) perform some filtering and agggregations of the dataset needed in the analyses. 

- **analyses**: contains different jupyter notebooks to be run separately, to obtain the different  interactive .HTML files then aggregated in the final output. 
- **makefile**: contains the .css file defining the format of the final .HTML output. As no other aggregation file was needed, this is the only file contained. 
- **outputs**: stores all the .HTML outputs of [analyses](./analyses) and the [final output](./outputs/index.html) to be run to observe the final output. 
- **reports**: contains the final reflective summary. 

# -------------------
## Reproducibility: 

To reproduce the outputs is then suggested to: 
- *Option 1 - Observing The result from Local Machine*:  Run the HTML file [final output](./outputs/index.html), on the local machine. 
- *Option 2 - Reproducing the Result*: 
    - Run the [Analyses Scripts](./analyses) to generate the single outputs;
    - Run the Run the HTML file [final output](./outputs/index.html), on the local machine. 
- *Option 1 - Observing The result directly*:  The results can also be directly inspected at the following [link](https://mariamorandini.github.io/world-energy-consumption-/).
