# DIRECT-STEM climate workshop
Materials for the DIRECT-STEM climate workshop at UCI

## Description and goals
The goal of this workshop is to introduce students to the use of the Python programming language for data analysis, using data related to climate change in the Arctic as a testbed/case-study to illustrate various concepts. The Arctic is warming twice as fast as the rest of the globe and its future is uncertain. Participants will form teams to address scientific questions of interest using python to process and visualize global climate model data. For the first half-day the instructors will walk through an example analysis, simultaneously covering the technical aspects and the scientific background. The python toolkit will include numpy, pandas, matplotlib, and jupyter notebooks. Most of the workshop time will be devoted to performing data analysis and visualization, with the support of the instructors. The workshop will end with each team presenting their findings.

## About this repository

With the exception of the climate data, all materials for teaching are contained in this repository. Climate data is not included because it is very large. Following the instructions below to download and run the notebooks. All of the materials are viewable online, without downloading.

+ `README.md`: overview, setup instructions, link to data.
+ `Questions.md`: resouces, themes, scientific questions of interest, information about data.
+ `Schedule.md`: daily schedule for the workshop.
+ `Teams.md` : defines teams.
+ `data`: mostly empty directory structure to place downloaded data. Directory structure matches Google Drive.
+ `notebooks`: the instructional Jupyter notebooks and supporting python code.

## Instructions

1.  If you haven't do so already, download and **install the [Anaconda Scientific Python Distribution version 2.7](https://www.continuum.io/downloads)**.  If it offers to make itself your default Python distribution, allow it. In Windows, you will be asked to i) select a location to install anaconda (pick wherever you want); ii) to add Anaconda to the system PATH (check the box); iii) whether you want to register Anaconda as the system Python (check the box).
2. Whether you've just installed Anaconda, or you have done so previously, you should now **update Anaconda** to the latest version of the distribution.  It changes a lot so do this today even if you did recently.
 1. Open a terminal or command prompt or an 'Anaconda prompt' (In Windows you can find the latter in the start menu programs).
 2. Type ```conda update conda``` and press enter or return.  Confirm that you'd like it to make any changes that it offers.
 3. Type ```conda update anaconda``` and press enter or return.  Confirm that you'd like it to make any changes that it offers.
 4. Type ```conda install -c anaconda netcdf4=1.2.4``` and press enter or return. Confirm that you'd like it to make any changes that it offers.
 5.	Type ```conda install -c anaconda basemap``` and press enter or return. Confirm that you'd like it to make any changes that it offers.
 6.	Type ```conda install -c anaconda seaborn``` and press enter or return. Confirm that you'd like it to make any changes that it offers.

3. **Download the code repository**.  
 1. [Download](https://github.com/strongh/DIRECT-STEM-climate-workshop/archive/master.zip) to download a zip file containing this entire repository.
 2. Unzip that file into a directory you know how to find; you'll need it several times throughout the day.
4. **Start a Jupyter notebook server**.
 1. Open a terminal/command prompt/Anaconda prompt and navigate to the directory where you saved the code repository; open the 'notebooks' directory.
 2. Once insdie the notebooks directory, type ```jupyter notebook``` to open Jupyter with access to those pre-saved notebooks from the code repository.
 2. Open "Test Notebook.ipynb" within Jupyter. 
 3. Click "Cell" at the top of the opened notebook, followed by "Run All" and ensure that 1) there are no errors and that 2) the output from the first cell is the same as that in the second.  If it doesn't match, raise your hand.
 4. If everything looks good, close the browser tab containing the test notebook but keep open the tab listing all the other notebooks.

## Data

The data are available on Google Drive, using this link:

[https://drive.google.com/open?id=0B2OMTC2qNBRtXzlTa1FBdnpJZ2s](https://drive.google.com/open?id=0B2OMTC2qNBRtXzlTa1FBdnpJZ2s)
