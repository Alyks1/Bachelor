import csv
import os
import shutil
import collections


class Dataset:
    labelList = []
    path = "rawData/onlyCoins/"

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
                # trust = row[2]
                # src = row[3] maybe needed in the future
                # Use below 2 lines to regression model
                # label = self.normalizeLabel(int(label))
                # self.createData(id, index, label)
                self.createCategories(label, id)

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

    def createData(self, id, index, label):
        # use trust here
        imagePath = self.path + id + ".jpg"
        shutil.copyfile(
            imagePath,
            "data/" + str(index) + "_" + str(label) + ".jpg",
        )
        self.labelList.append(label)
