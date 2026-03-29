class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        if mountainArr.length() < 3:
            return -1
        l, r = 0, mountainArr.length() - 1
        peak,peakVal = 0, 0
        while l < r:
            m = (r + l) // 2

            mValL = mountainArr.get(m-1)
            mVal = mountainArr.get(m)
            mValR = mountainArr.get(m+1)
            if mValL < mVal > mValR:
                peak = m
                peakVal = mVal
                break
            elif mValL < mValR:
                l = m
            else:
                r = m + 1
        print(peak, peakVal)
        print("left")
        l, r = 0, peak
        while l <= r:
            m = (r + l) // 2
            lVal = mountainArr.get(l)
            mVal = mountainArr.get(m)
            rVal = mountainArr.get(r)
            print(lVal,mVal,rVal)
            if mVal == target:
                return m
            elif lVal <= target < mVal:
                r = m-1
            else:
                l = m+1
        print("right")
        l, r = peak+1, mountainArr.length() - 1
        while l <= r:
            m = (r + l) // 2
            lVal = mountainArr.get(l)
            mVal = mountainArr.get(m)
            rVal = mountainArr.get(r)
            print(lVal,mVal,rVal)
            if mVal == target:
                return m
            elif lVal >= target > mVal:
                r = m-1
            else:
                l = m+1
        return -1

        