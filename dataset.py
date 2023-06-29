import csv
import os
import shutil
import collections
from PIL import Image


class Dataset:
    labelList = []
    path = "rawData/BasicImages/"

    def __init__(self):
        self.setupDataset()

    def setupDataset(self):
        with open(self.path + "_datasetInfo.csv") as csvfile:
            reader = csv.reader(csvfile, delimiter=",")
            # for row, get image
            # Rename image to indexnr.jpg
            # get label and save as lists
            index = 0
            for row in reader:
                index += 1
                id = row[0]
                label = row[1]
                trust = row[2]
                # src = row[3] maybe needed in the future
                # Use below 2 lines to regression model
                # label = self.normalizeLabel(int(label))
                index = self.createData(id, index, int(label), trust)
                # self.createCategories(label, id)

    def getLabelList(self):
        print(self.labelList)
        print(len(self.labelList))
        return self.labelList

    def normalizeLabel(self, label):
        return round(int(label) / 100)

    def createCategories(self, label, id):
        rootDir = "data/"
        normalizedLabel = str(self.normalizeLabel(label))
        imagePath = self.path + id + ".jpg"
        path = rootDir + "/" + normalizedLabel
        if not os.path.exists(path):
            os.makedirs(path)
        shutil.copyfile(imagePath, path + "/" + id + ".jpg")

    def createData(self, id, index, label, trust):
        # use trust here
        imagePath = self.path + id + ".jpg"
        # Copy image Trust amount of times, to keep seperate names, increase index and return
        # for i in range(int(2)):
        img = Image.open(imagePath)
        img.transpose(Image.FLIP_LEFT_RIGHT).save(
            "data/" + str(index) + "_" + str(label) + ".jpg"
        )
        self.labelList.append(label)
        index += 1
        shutil.copyfile(
            imagePath,
            "data/" + str(index) + "_" + str(label) + ".jpg",
        )
        self.labelList.append(label)
        index += 1

        # Index increases by one even if the loop is returned. This means a number is skipped, so -1
        index -= 1
        return index
