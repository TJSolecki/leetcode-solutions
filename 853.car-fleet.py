class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        stack = []
        cars = zip(position, speed)
        cars = sorted(cars, key=lambda car: car[0], reverse=True)
        for car in cars:
            arival_time = (target - car[0]) / car[1]
            if not stack or stack[-1] < arival_time:
                stack.append(arival_time)

        return len(stack)
