import math 

def H_xPrism(x,y,z, w, h, M = 1):
    totalMagField = 0
    for sigmaX in [-1, 1]:
        for sigmaY in [-1, 1]:
            for sigmaZ in [-1, 1]:
                x_sigma = x - sigmaX * (w / 2)
                y_sigma = y - sigmaY * (w / 2)
                z_sigma = z - sigmaZ * (h / 2)
                
                R = math.sqrt(x_sigma**2 + y_sigma**2 + z_sigma**2)
                
                sign = sigmaX * sigmaY * sigmaZ

                final = math.log(y_sigma + R) + (x_sigma * (x_sigma + y_sigma + z_sigma + R)) / ((y_sigma + R) * R)

                totalMagField += sign * final
    return totalMagField * -(M / (4*math.pi))

def H_yPrism(x,y,z, w, h, M = 1):
    totalMagField = 0
    for sigmaX in [-1, 1]:
        for sigmaY in [-1, 1]:
            for sigmaZ in [-1, 1]:
                x_sigma = x - sigmaX * (w / 2)
                y_sigma = y - sigmaY * (w / 2)
                z_sigma = z - sigmaZ * (h / 2)
                
                R = math.sqrt(x_sigma**2 + y_sigma**2 + z_sigma**2)
                
                sign = sigmaX * sigmaY * sigmaZ

                final = math.log(x_sigma + R) + (y_sigma * (x_sigma + y_sigma + z_sigma + R)) / ((x_sigma + R) * R)

                totalMagField += sign * final
    return totalMagField * -(M / (4*math.pi))

def H_ZPrism(x,y,z, w, h, M = 1):
    totalMagField = 0
    for sigmaX in [-1, 1]:
        for sigmaY in [-1, 1]:
            for sigmaZ in [-1, 1]:
                x_sigma = x - sigmaX * (w / 2)
                y_sigma = y - sigmaY * (w / 2)
                z_sigma = z - sigmaZ * (h / 2)
                
                R = math.sqrt(x_sigma**2 + y_sigma**2 + z_sigma**2)
                
                sign = sigmaX * sigmaY * sigmaZ

                denom = (x_sigma**2 + z_sigma**2) * (y_sigma**2 + z_sigma**2) * R

                final = math.atan((x_sigma * y_sigma) / (z_sigma * R)) - (((x_sigma * z_sigma**2) * (x_sigma**2 + z_sigma**2)) / (denom)) - (((y_sigma * z_sigma**2) * (y_sigma**2 + z_sigma**2)) / (denom)) + (((x_sigma * y_sigma * z_sigma) * (x_sigma**2 * y_sigma**2 * (2*z_sigma**2)))/(denom))

                totalMagField += sign * final
    return totalMagField * -(M / (4*math.pi))



numbers = [1, 2, 3, 4]

for n in numbers:
    print(n)
