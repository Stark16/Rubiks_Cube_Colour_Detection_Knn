# Rubiks_Cube_Colour_Detection_Knn
This is the part of Rubik's cube solving project, where Computer vision is used to detect the colours of cube pixels

File Structure:
  1. Dataset contains the Image Dataset and the dataset file created from it.
  2. Papers: List of research papers that inspired or helped implimenting certain parts of the project
  
  3. Image_dataset: This file takes the live camera feed and marks ROI on the feed, then it saves the cropped images of the ROIs in the respective folder
     The user needs to solve 1 face of the cube so that all the 9 faces facing the camera are of same colour, which can be saved to it's respctive folder
     also, it is suggested to save multiple sets of images of each colour in varying light condition, to later help generelize the model.
  
  4. Dataset_creation: This script reads all the trained images from their respective folders and extracts Hue and saturation peaks from each image's 
     Hue and saturation histograms and saved them on a text file.
     
  5. Colour_detection: This script detects colour in reatime of the pixels inside the ROI
     It captures and crops the ROI. It then extracts the features, and passes it to Knn to recognise the colours
     
  6. Knn: Takes input as an array of Hue and saturation features from Colour_detection, performs K-Nearest-Neighbour and returns a string of detected colours.
