class TimeMap:

    def __init__(self):
        self.hashmap = {}
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hashmap:
            self.hashmap[key].append((value, timestamp))
        else:
            self.hashmap[key] = []
            self.hashmap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap:
            return ""
        else:
            if timestamp > self.hashmap[key][-1][1]:
                return self.hashmap[key][-1][0]
            else:
                res = ""
                for value, ts in self.hashmap[key]:
                    if ts <= timestamp:
                        res = value
                    else:
                        break
                return res
                

        
