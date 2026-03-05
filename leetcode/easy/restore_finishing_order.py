from typing import List

class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        friends = set(friends)

        return [_id for _id in order if _id in friends]