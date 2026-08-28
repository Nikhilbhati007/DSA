class Solution(object):
    def maximalRectangle(self, mat):

        def hist_Area(nums):
            n = len(nums)
            st = []
            max_area = 0

            for i in range(n):

                while st and nums[st[-1]] > nums[i]:

                    ele = nums[st[-1]]
                    st.pop()

                    nse = i
                    pse = st[-1] if st else -1

                    max_area = max(
                        max_area,
                        ele * (nse - pse - 1)
                    )

                st.append(i)

            while st:

                nse = n

                ele = nums[st[-1]]
                st.pop()

                pse = st[-1] if st else -1

                max_area = max(
                    max_area,
                    ele * (nse - pse - 1)
                )

            return max_area

        n = len(mat)
        m = len(mat[0])

        heights = [0] * m
        max_area = 0

        for i in range(n):

            for j in range(m):

                if mat[i][j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0

            max_area = max(max_area, hist_Area(heights))

        return max_area