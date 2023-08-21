# Bachelor Thesis

This is the repository associated with my bachelor's thesis titled:

_Unearthing the Past: A Study on Utilizing Web Scraping Techniques to Generate an Artifact Dataset for Accurate Dating using Machine Learning Algorithms_

The paper writes about utilizing a Web Scraper which can be found in [this repository](https://github.com/Alyks1/Capstone)

## Project Structure

This project has two main parts:

I.  The `dataset.py` file is tasked to set up the dataset in a format usable by machine learning algorithms.

II.  The `main.ipynb` file is used to set up the machine learning algorithms themselves. 

## Development

### Installation

1. Clone the repository
   
```$ git clone https://github.com/Alyks1/Bachelor.git  && cd Bachelor```

2. Create a virtual environment to run python in
   
`$ python -m venv /path/to/new/virtual/environment`

3. Install the requirements

`$ pip install -r requirements.txt`

2. Produce a dataset of images from the dataset CSV file of the dataset you wish to use. Images should be named by their ID specified in the CSV. Each image is in the format `ID,Year,Trust,ImageLink`.
   
3. Add the dataset to a folder named `rawData` and make sure the dataset path is correct.

To start the training, it is recommended to start only the sections in the notebook needed for training.

### Quick Start Guide

Note: The dataset must be created independently

1. Set the dataset
2. Start the imports cell in the Python Notebook
3. Start the dataset instantiation cell
4. Start the Dataset Creation cell. Note the difference between "inferred" and "LABELS" for classification and regression respectively.
5. Start the `num_classes` instantiation cell
6. Start "EfficientNetB3 with Sparse Categorical Crossentropy" cell
7. Set the number of Epochs (default is 100) and start the cell
8. Start the `modelEfficientNet.fit()` function cell under the EfficientNet header.
9. Optional: Plot a graph with the results using the corresponding cell.

## Licence

Apache License Version 2.0
