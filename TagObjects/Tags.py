class Tag:
    Name : str = str
    TagID : int = int
    def __init__(self, name : str, id : int) -> None:
        
        self.Name = name
        self.TagID = id
        pass
    
    def getName(self) -> str:
        return self.Name
    
    def getID(self) -> int:
        return self.TagID
    