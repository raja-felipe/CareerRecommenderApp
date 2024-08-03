#  would store in db


TagDict : dict[int : str] = dict()

def newTag(tagID : int, tagName : str):
    if tagName not in TagDict.values():
        TagDict.update({ tagID : tagName })

def removeTag(tagID : int):
    if tagID in TagDict.keys():
        TagDict.pop(tagID)

def getTagName(tagID : int) -> str:
    if tagID in TagDict.keys():
        return TagDict[tagID]
