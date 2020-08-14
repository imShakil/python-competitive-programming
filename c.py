# Segment Tree: is a range queries algorithm.
# we can find maximum/minimum sum/value in a given range


class SegmentTree:
    tree = []
    size = int(0)

    def __init__(self, array=None):
        self.array = array
        self.size = len(self.array)
        self.tree = [0] * (self.size * 3 + 1)  # need 3x space of array size

    def query(self, lower_index, higher_index, start, end, segment):
        if start <= lower_index and end >= higher_index:
            return self.tree[segment]
        elif start > higher_index or end < lower_index:
            return 0
        else:
            mid = (lower_index + higher_index) // 2
            return max(
                self.query(lower_index, mid, start, end, segment * 2),
                self.query(mid + 1, higher_index, start, end, segment * 2 + 1),
            )

    def build(self, lower_index, higher_index, segment):
        if lower_index == higher_index:
            self.tree[segment] = ord(self.array[lower_index]) - ord('0')
            return self.tree[segment]
        mid = (lower_index + higher_index) // 2
        self.tree[segment] = max(self.build(lower_index, mid, segment * 2), self.build(mid + 1, higher_index, segment * 2 + 1))
        return self.tree[segment]


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        line = str(input())
        seg_tree = SegmentTree(line)
        seg_tree.build(0, len(line)-1, 1)
        print(seg_tree.tree)
