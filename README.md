# covid_crowds
<br />
Baseline Yolov2 Model:

To perform inference using the pre-trained coursera yolo model, you must substitute the coursera .ipynb file with "yolo_coursera_modified.ipynb", which allows for performing inference on a test set of multiple images of different sizes, and also substitte in the modified "yolo_utils.py" file into the coursera utils folder.  The COVID test data is in the test_data folder. You must have access to the coursera project in order to do this, I ran into trouble in configuring the .h5 model file outside of that environment. 

<br />
<br />

Yolov3 Model:

Files to assist in performing transfer learning on a pre-trained yolov3 network with the Hollywood image dataset, are located in the data_processing_scripts folder. You can perform the transfer learning with these steps:

1) Download the hollywood head dataset here: https://www.di.ens.fr/willow/research/headdetection/

2) Use the data_processing script "process_data.py" to select a subset of the images and annotations from the dataest to use for training. Currently it is set up to select images ending with "001.jpeg" in order to reduce the number of images by ~ 1,000 times and still select equally from the different films. 

3) Use the "convert_to_csv.py" file to convert the subset of .xml annotations to a .csv file, so that the data is compatible with the next steps.

4) Follow the steps here for setting up environment, downloading the pre-trained yolov3 model weights, configuring the annotations for keras, training on the model with additional data, and performing inference on a test dataset: https://blog.insightdatascience.com/how-to-train-your-own-yolov3-detector-from-scratch-224d10e55de2

Note: these steps do not yet auto-analyze the inference results for precision and recall information, so that analysis must be done manually on the test dataset. 

