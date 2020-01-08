# Pymaceuticals

Click ![here](https://maivey.github.io/matplotlib-challenge/) to go to the deployed website.

In this study, 250 mice were treated through a variety of drug regimes over the course of 45 days. Their physiological responses were then monitored over the course of that time. The objective is to analyze the data to show how four treatments (Capomulin, Infubinol, Ketapril, and Placebo) compare.

## Setup
### Prerequisites
This script requires imports of the following:
```code
%matplotlib inline
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import warnings
```

### Hide warning messages and Import files

Hide warning messages in notebook:
```code
warnings.filterwarnings('ignore')
```

Import Mouse and Drug Data and store in DataFrame
```code
mouse_drug_data_to_load = "data/mouse_drug_data.csv"
mouse_df = pd.read_csv(mouse_drug_data_to_load)
```

Import Clinical Trial Data and store in DataFrame
```code
clinical_trial_data_to_load = "data/clinicaltrial_data.csv"
drug_df = pd.read_csv(clinical_trial_data_to_load)
```


This script is for the following scenario: While your data companions rushed off to jobs in finance and government, you remained adamant that science was the way for you. Staying true to your mission, you've since joined Pymaceuticals Inc., a burgeoning pharmaceutical company based out of San Diego, CA. Pymaceuticals specializes in drug-based, anti-cancer pharmaceuticals. In their most recent efforts, they've since begun screening for potential treatments to squamous cell carcinoma (SCC), a commonly occurring form of skin cancer.

This sctipt analyses the data to show how four treatments (Capomulin, Infubinol, Ketapril, and Placebo) compare.

To do this, the script does the following:

- Creates a scatter plot that shows how the tumor volume changes over time for each treatment.

- Creates a scatter plot that shows how the number of metastatic (cancer spreading) sites changes over time for each treatment.

- Creates a scatter plot that shows the number of mice still alive through the course of treatment (Survival Rate)

- Creates a bar graph that compares the total % tumor volume change for each drug across the full 45 days.

- Includes 3 observations about the results of the study-- using the visualizations  generated from the study data as the basis for the observations.
