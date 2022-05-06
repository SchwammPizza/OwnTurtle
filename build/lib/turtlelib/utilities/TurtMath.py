import math as m

def atan2(x: int, y: int) -> float: return m.atan2(y, x)*180/m.pi

def tan(degrees: float) -> float: return m.tan(degrees/180*m.pi)

def sin(degrees: float) -> float: return m.sin(degrees/180*m.pi)

def cos(degrees: float) -> float: return m.cos(degrees/180*m.pi)

def sign(number: float) -> int:
    if number != 0: return int(abs(number)/number)
    else: return 0