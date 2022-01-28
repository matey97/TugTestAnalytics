# TUG Test Analytics

This repository contains the data and code supporting the experiments for the paper "Instrumented Timed Up and Go (TUG) test
using inertial sensors from consumer wearable devices".

## Repository structure

- DATA: contains RAW accelerometer and gyroscope data collected to train the machine learning model for activity inference.
All the data corresponds to a single person. File naming convention is [type]\_[num]\_[device]\_[timestamp].json, where type takes
the following values:
  - ll: smartwatch on **left** hand, turns to the **left**.
  - lr: smartwatch on **left** hand, turns to the **right**.
  - rl: smartwatch on **right** hand, turns to the **left**.
  - rr: smartwatch on **right** hand, turns to the **right**.
- FEATURES: contains the features extracted from the RAW data, used to train the machine learning model.
- IMAGES: contains some figures with the results of the experiment.
- MODEL: constains the trained machine learning model. The following files are included:
  - *labels.txt*: file with the labels (clases) of the trained model.
  - *model_full_norm.h5*: trained Keras model.
  - *model_full_norm.tflite*: TensorFlow Lite model with *labels.txt* embedded (through additional metadata file), ready to use.
- RESULTS: includes the results of the experiments. It contains two folders:
  - INPUT: includes manual and system computed results from the TUG test executions experiments.
  - OUTPUT: files containing results obtained from the processing of the result of the experiments:
- scripts: utility scripts.
- feature-extraction.ipynb: Jupyter Notebook containing all the required code to process the RAW data from DATA and obtain the features from FEATURES.
- model-training.ipynb: Jupyter Notebook containing all the required code to train a machine learning model using the features in FEATURES and save the resulting model resources in MODEL.
- results-evaluation.ipynb: Jupyter Notebook containing all the required code to process and analyze the results of the experiments in RESULTS/INPUT and obtain the results
included in the paper.
- requirements.txt: file with the dependencies and versions used through all the code. To install them:
```
pip install -r requirements.txt
```

