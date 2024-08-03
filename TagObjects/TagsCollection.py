import TagDict


class TagCollection:
    TagCollection : dict[int : float] = dict()

    def __init__(self) -> None:
        for ID in TagDict.TagDict.keys():
            self.TagCollection.update({ ID : float(0)})

        pass

    def updateTagScore(self, tagID : int, tagScore : float):
        if tagID in self.TagCollection.keys():
            self.TagCollection[tagID] = tagScore

        pass
    

    pass