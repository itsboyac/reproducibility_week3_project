from typing import List

class DataProcessor:
    def __init__(self, data:List[float]):
        self.data = data

    def mean(self) ->float:
        if not self.data:
            return ValueError("Data list is empty")
        return sum(self.data) / len(self.data) 
    
    def variance(self) -> float:
        m = self.mean()
        return sum((x - m)**2 for x in self.data) / len(self.data)
    

if __name__ == "__main__":
    p = DataProcessor([1.0, 2.0, 3.0])
    print(p.mean())
    
