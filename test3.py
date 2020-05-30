    def heightChecker(self, heights: List[int]) -> int:
        c = 0
        while(1):
            tmp = None
            for i in range(0, len(heights)):
                if heights[i] != min(heights[i:]) and (tmp is None or a[i] < a[tmp]):
                    tmp = i
            if tmp is None:
                return c
            else:
                a.append(a.pop(tmp))
                c += 1