Theme
======
"The possible futures of Artic sea ice"

Background
=======
+ IPCC AR5 WG1 CH4 - [The Cryosphere](http://www.ipcc.ch/pdf/assessment-report/ar5/wg1/WG1AR5_Chapter04_FINAL.pdf)
+ Francis, J. A., and S. J. Vavrus, 2012: Evidence linking Arctic amplification to extreme
weather in mid-latitudes. Geophysical Research Letters, doi:10.1029/2012GL051000, URL http://doi.wiley.com/10.1029/2012GL051000.
+ Overland, J., J. A. Francis, R. Hall, E. Hanna, S.-J. Kim, and T. Vihma (2015), The Melting Arctic and Midlatitude Weather Patterns: Are They Connected?*, Journal of Climate, doi:10.1175/JCLI-D-14-00822.1, URL http://journals.ametsoc.org/doi/abs/10.1175/JCLI-D-14-00822.1
+ Screen, J. A., and I. Simmonds, 2010: The central role of diminishing sea ice in recent Arctic
temperature amplication. Nature, doi:10.1038/nature09051, URL
http://dx.doi.org/10.1038/nature09051.
+ Stroeve, J. C., M. C. Serreze, M. M. Holland, J. E. Kay, J. Malanik, and A. P. Barrett,
2011: The Arctics rapidly shrinking sea ice cover: a research synthesis. Climatic Change, doi:10.1007/s10584-011-0101-1, URL http://link.springer.com/10.1007/s10584-011-0101-1.
+ Wang, M., and J. E. Overland (2012), A sea ice free summer Arctic within 30 years: An update from CMIP5 models, Geophysical Research Letters, doi:10.1029/2012GL052868, URL http://onlinelibrary.wiley.com/doi/10.1029/2012GL052868/abstract.

Frequently Asked Questions on Arctic Sea Ice
=======
+ http://nsidc.org/arcticseaicenews/faq/
+ [What's causing Arctic amplification?](https://www.skepticalscience.com/Melting-ice-isnt-warming-Arctic.htm)
+ [Arctic Amplification Positive Feedback Loop](http://www.grida.no/graphicslib/detail/climate-feedbacks-the-connectivity-of-the-positive-icesnow-albedo-feedback-terrestrial-snow-and-vegetation-feedbacks-and-the-negative-cloudradiat_5eb0)

Current Arctic Sea Ice Graphs
=======
+ https://ads.nipr.ac.jp/vishop/#/extent
+ https://sites.google.com/site/arcticseaicegraphs/

Broad Questions
=======
+ when will the first Arctic-sea-ice-free summer be?
      + compare across possible scenarios
+ which areas are most sensitive/robust to climate changes?
      + compare across possible scenarios
+ which climate scenarios are most alarming?
      + are there "clusters" of scenarios which result in "similar" retreat of Arctic sea ice?
+ examine a component of the [Arctic amplification](https://en.wikipedia.org/wiki/Polar_amplification) feedback system.
+ what is/are the relationships between Arctic sea ice and snow cover/cloud cover/SST
+ what is the relationship between Artic sea ice and salinity?
+ how will the regional Arctic climate change compared to global climate?
      + compare across possible scenarios

Example question (for use during lecture component):
+ Under varying scenarios, which physical variables (sea ice extent, snow cover, water vapor, etc) are most closely related to warming (TAS?).
   
CMIP5 Data
=======
+ Standard Output - [Table of Variables](http://cmip-pcmdi.llnl.gov/cmip5/docs/standard_output.pdf) 
+ CMIP5 Data Portal - [Earth System Federation Grid](https://pcmdi.llnl.gov/projects/esgf-llnl/) --> Create an account!
+ Model : CCSM4 (http://www.cesm.ucar.edu/models/ccsm4.0/)
+ Ensembles : #1-5
      + This will allow analysis of interannual variability and addressing model noise
+ RCP Scenarios : 2.6 | 4.5 | 8.5 [[Vuuren et al., 2011]](http://link.springer.com/article/10.1007/s10584-011-0148-z%20/fulltext.html)
+ Time : MONTHLY{ Historical (1850 - 2005), Future (RCP, 2006 - 2100)}

Datasets
=======
+ [CMIP5 Portal](https://pcmdi.llnl.gov/search/cmip5/) -- Focus on Arctic Circle (*on GoogleDrive)
      + Select --> CMIP5, CCSM4, historical, RCP2.6/RCP4.5/RCP8.5, mon (monthly)
      + *TAS (near-surface air temperature, K)
      + *PR (kg m-2 s-1)
      + *SIC (sea ice concentration, %)
      + *SIT (sea ice thickness, m)
      + *TOS (sea surface temperature,)
      + snd (snow depth on sea ice, m)
      + snomelt (snow melt rate, kg m-2 s-1)
      + snowToIce (snow-ice formation rate, kg m-2 s-1)
      + tsice (surface temperature of sea ice, K)
      + *psl (sea level pressure, Pa)
      + *areacella (area of atmospheric grid cell) 
      + *areacello (area of oceanic grid cell)
      + *sftlf (land cover mask)
      + *sftof (ocean cover mask)
+ This is a significant amount of data (50GB+). I think it may be beneficial for us to have some data sets already available for common fields (TAS/PR/SIC/areacella/areacello/sftlf/sftof), but have the rest as options for the participants to download for whatever project they are interested in. Setting up an account on the site is usually easy and may even be beneficial. We can include steps on how to navigate the site and understand the modeling terminology (should not take long).
