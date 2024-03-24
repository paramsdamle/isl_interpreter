![Sign Shakti](./img/sign_shakti_logo.png "Sign Shakti")

A real-time automated interpreter for Indian/Pakistani Sign Language.

Created by Param Damle, Eli Kin, and Flavien Moise for HooHacks 2024.

_Shakti_ means "power" or "ability" in Hindi. With our solution, we hope to bridge gaps between communities regardless of communication style and community of origin, and empower learners of all walks of life to connect with the wider world through technology.

## Usage
Sign Shakti deploys in a React app. Clone this repository, and in the main folder run

`npm start`

Allow webcam usage and you should begin to see live prediction of ISL letters and numbers. For more info on ISL gestures, [click here](https://www.1specialplace.com/2021/02/11/all-about-indian-sign-language/).

## Build it Yourself!

Download the gestures dataset as "pathikreet_dataset". Also download the "frame_images_DB" dataset from YT Faces (11GB, this may take a while). All sources are linked below.

Run the cells in [data_generation.ipynb](data_generation.ipynb) to create sample images with transformation. You can specify the number of total samples (different source images of the sign for letter A, for example) and the number of iterations (for a given sample image, how many different transformed versions will we augment to the dataset?).

To train the model, run [isl_model.ipynb](isl_model.ipynb) and define your training parameters (duration, etc). There are two cells that will generate a command line command you will have to run _outside the Python shell_:

1. The training command
2. The export command. Use this to export the trained model as the [SavedModel format](https://www.tensorflow.org/hub/model_formats#savedmodel) (.pb) and continue to the next step.

You will need to use [this script](https://www.tensorflow.org/js/tutorials/conversion/import_saved_model) to convert the SavedModel type to a JSON for TensorFlow.JS. Once you have the model weights as .JSON, run the app using `npm start` and watch magic happen!


## Sources
This project was heavily inspired by [Nicholas Renotte](https://github.com/nicknochnack)'s series on [building a TensorFlow object detection model](https://www.youtube.com/watch?v=pDXdlXlaCco) and [deploying it on a React webapp](https://www.youtube.com/watch?v=ZTSRZt04JkY).

The datasets used include the [ISL Gesture dataset](https://www.kaggle.com/datasets/pathikreet/indian​) by Kaggle user [Pathikreet Chowdhury](https://www.kaggle.com/pathikreet) and the [YouTube Faces dataset](https://www.cs.tau.ac.il/~wolf/ytfaces) published by [Professor Lior Wolf](https://www.cs.tau.ac.il/~wolf).