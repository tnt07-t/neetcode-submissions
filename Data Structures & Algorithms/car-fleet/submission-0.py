class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        def TimeToTarget(target, position, speed):
            return (target-position)/speed

        cars = sorted(zip(position,speed), key = lambda x: x[0], reverse = True)
        fleets = 0
        currTime = 0

        for pos,speed in cars:
            time = TimeToTarget(target, pos,speed)
            if time > currTime:
                fleets += 1

            currTime = max(currTime,time)
        return fleets
            
            

        