class Solution:
    def numberOfBoomerangs(self, points: list[list[int]]) -> int:
        ans = 0
        for x1, y1 in points:
            dist_map = Counter((x1 - x2) ** 2 + (y1 - y2) ** 2 for x2, y2 in points)
            ans += sum((count * (count - 1) for count in dist_map.values()))
        return ans