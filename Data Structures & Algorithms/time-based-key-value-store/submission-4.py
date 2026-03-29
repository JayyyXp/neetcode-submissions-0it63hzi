class TimeMap:

    def __init__(self):
        # key -> {timestamp -> value}
        self.valueDict = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.valueDict:
            self.valueDict[key][timestamp] = value 
        else:
            self.valueDict[key] = {timestamp: value}

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.valueDict:
            return ""
        
        delta = -1
        value = ""
        for ts, val in self.valueDict[key].items():
            # Only consider timestamps less than or equal to the requested timestamp
            if ts <= timestamp and ts > delta:
                delta = ts
                value = val
        
        return value
        

