class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight

class BaseRobot:
    def __init__(self, name: str, weight: int, coords: tuple(int, int)) -> None:
        self.name = name
        self.weight = weight
        self.coords = coords

    def move (self) -> None:
        if self.coords = go_forward:
            coords.y += 1
        elif self.coords = go_back:
            coords.y -= 1
        elif self.coords = go_right:
            coords.x += 1
        elif self.coords = go_left:
            coords.x -= 1
        else:
            print("Wrong instruction")
    def get_info(self) -> str:
        return f"Robot: {name}, Weight: {weight}"

class FlyingRobot(BaseRobot):
    def __init__(self, name: str, weight: int, coords: tuple(int, int, int)) -> None:
        super().__init__(name, weight, coords)
        self.coords = [0,0,0]

    def move(self) -> None:
        if self.coords = go_up:
            coords.z += 1
        elif self.coords = go_down:
            coords.z -= 1

