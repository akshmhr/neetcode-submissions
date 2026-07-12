
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        cars = []

        for i in range(len(position)):
            time = (target - position[i]) / speed[i]
            cars.append([position[i], time])

        cars.sort(key=lambda car: car[0], reverse=True)

    

        count = 0
        prevTime = 0

        for car in cars:
            if car[1] > prevTime:
                count+=1
                prevTime = car[1]


        return count