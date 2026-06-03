class Solution:
    def earliestFinishTime(self, landStartTime, landDuration,
                           waterStartTime, waterDuration):
        min_land_finish = float('inf')
        for i in range(len(landStartTime)):
            min_land_finish = min(
                min_land_finish,
                landStartTime[i] + landDuration[i]
            )
        ans = float('inf')
        for j in range(len(waterStartTime)):
            ans = min(
                ans,
                max(min_land_finish, waterStartTime[j])
                + waterDuration[j]
            )
        min_water_finish = float('inf')
        for j in range(len(waterStartTime)):
            min_water_finish = min(
                min_water_finish,
                waterStartTime[j] + waterDuration[j]
            )
        for i in range(len(landStartTime)):
            ans = min(
                ans,
                max(min_water_finish, landStartTime[i])
                + landDuration[i]
            )
        return ans