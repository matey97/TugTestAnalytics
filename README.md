# TUG Test Analytics

This repository contains the data and code supporting the experiments for the paper "Instrumented Timed Up and Go (TUG) test
using inertial sensors from consumer wearable devices".

## Repository structure

- [DATA](./DATA): contains RAW accelerometer and gyroscope data collected to train the machine learning model for activity inference.
All the data corresponds to a single person. File naming convention is [type]\_[num]\_[device]\_[timestamp].json, where type takes
the following values:
  - ll: smartwatch on **left** hand, turns to the **left**.
  - lr: smartwatch on **left** hand, turns to the **right**.
  - rl: smartwatch on **right** hand, turns to the **left**.
  - rr: smartwatch on **right** hand, turns to the **right**.
- [FEATURES](./FEATURES): contains the features extracted from the RAW data, used to train the machine learning model.
- [IMAGES](./IMAGES): contains some figures with the results of the experiment.
- [MODEL](./MODEL): constains the trained machine learning model. The following files are included:
  - *labels.txt*: file with the labels (clases) of the trained model.
  - *model_full_norm.h5*: trained Keras model.
  - *model_full_norm.tflite*: TensorFlow Lite model with *labels.txt* embedded (through additional metadata file), ready to use.
- [RESULTS](./RESULTS): includes the results of the experiments. It contains two folders:
  - [INPUT](./RESULTS/INPUT): includes manual and system computed results from the TUG test executions experiments:
    - app-[subject]-results.json: results of TUG executions computed by the smartphone application.
    - man-[subject]-results.json: results of TUG executions manually computed from visual inspection.
  - [OUTPUT](./RESULTS/OUTPUT): files containing results obtained from the processing of the result of the experiments:
    - [error_results.json](./RESULTS/OUTPUT/error_results.json): difference between system and manual computed durations for each TUG test execution.
    - [average_rmse.json](./RESULTS/OUTPUT/average_rmse.json): RMSE of all executions. Uses error_results.json content.
    - [subject_rmse.json](./RESULTS/OUTPUT/subject_rmse.json): RMSE of executions of each subject. Uses error_results.json content.
    - [end_type.json](./RESULTS/OUTPUT/end_type.json): number of TUG executions automatically/manually ended for each subject.
    - [failures_by_subject.json](./RESULTS/OUTPUT/failures_by_subject.json): failed executions for each subject.
- [scripts](./scripts): utility scripts.
- [feature-extraction.ipynb](./feature-extraction.ipynb): Jupyter Notebook containing all the required code to process the RAW data from DATA and obtain the features from FEATURES.
- [model-training.ipynb](./model-training.ipynb): Jupyter Notebook containing all the required code to train a machine learning model using the features in FEATURES and save the resulting model resources in MODEL.
- [results-evaluation.ipynb](./results-evaluation.ipynb): Jupyter Notebook containing all the required code to process and analyze the results of the experiments in RESULTS/INPUT and obtain the results
included in the paper.
- [requirements.txt](./requirements.txt): file with the dependencies and versions used through all the code. To install them:
```
pip install -r requirements.txt
```

## License

All data and code contained in this repository is licensed under MIT License (See [LICENSE](./LICENSE)).