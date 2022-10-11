from heapq import *
from collections import *
class TimeMap:
    '''
    Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.
    Implement the TimeMap class:
    TimeMap() Initializes the object of the data structure.
    void set(String key, String value, int timestamp) Stores the key with the value at the given time timestamp.
    String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".
    void remove() Remove the key-value pair stored at the exact timestamp.

    Example 1:
    Input
    ["TimeMap", "set", "get", "get", "set", "get", "get"]
    [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
    Output
    [null, null, "bar", "bar", null, "bar2", "bar2"]

    Explanation
    TimeMap timeMap = new TimeMap();
    timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
    timeMap.get("foo", 1);         // return "bar"
    timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
    timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
    timeMap.get("foo", 4);         // return "bar2"
    timeMap.get("foo", 5);         // return "bar2"

    Constraints:
    1 <= key.length, value.length <= 100
    key and value consist of lowercase English letters and digits.
    1 <= timestamp <= 107
    All the timestamps timestamp of set are strictly increasing.
    At most 2 * 105 calls will be made to set and get.

    Related Topics:
    Hash Table, String, Binary Search, Design

    Next Challeges:
    Stock Price Fluctuation

    turo
    '''
    #? keywords: time-based, multiple values for the same key,
    #?           get - timestamp_prev <= timestamp, largest timestamp_prev,
    #?           del - at the exact timestamp
    #? approach: dict -> list -> tuple - key -> [(timestamp, value)]
    #?           sorting - heap
    # input ["TimeMap", "set", "get", "get", "set", "get", "get"]
    #       [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
    def __init__(self):
        self.dict = defaultdict(list)
    # min heap tc: logn
    def set(self, key: str, value: str, timestamp: int) -> None:
        heappush(self.dict[key], (-timestamp, value))

    # min heap tc: n tc: n
    def get(self, key: str, timestamp: int) -> str:
        ans = ''
        if key in self.dict:
            cache = []
            while self.dict[key] and -self.dict[key][0][0] > timestamp:
                cache.append(heapq.heappop(self.dict[key]))
            if self.dict[key]:
                ans = self.dict[key][0][1]
            if cache:
                for ele in cache:
                    heapq.heappush(self.dict[key], ele)
        return ans

    # tc: n
    def remove(self, key: str, timestamp: int):
        if key in self.dict:
            for ele in self.dict[key]:
                if ele[0] == -timestamp:
                    self.dict[key].remove(ele)

    def main(self):
        timeMap = TimeMap()
        timeMap.set("foo", "bar21", 21)
        timeMap.set("foo", "bar1", 1)
        timeMap.set("foo", "bar36", 36)
        timeMap.set("foo", "bar12", 12)
        timeMap.set("foo", "bar43", 43)
        timeMap.set("foo", "bar7", 7)
        print(timeMap.dict['foo'])
        print(timeMap.get("foo", 23))
        timeMap.set("foo", "bar2", 4)
        print(timeMap.get("foo", 4))
        print(timeMap.get("foo", 5))

S = TimeMap()
S.main()