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
                l = 0
                r = len(self.hashmap[key]) - 1
                while l <= r:
                    curr = (l + r)//2
                    if self.hashmap[key][curr][1] <= timestamp:
                        res = self.hashmap[key][curr][0]
                        l = curr + 1
                    else:
                        r = curr - 1
                        
                return res
                

        
