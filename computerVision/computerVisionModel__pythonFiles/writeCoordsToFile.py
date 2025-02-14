def writeCoords(x_coord, y_coord):
    with open("screwCoords.txt", "a") as f:
        f.write(f"{x_coord} {y_coord}\n")

def clearCoordsFile():
    open("screwCoords.txt", "w").close()

if __name__ == "__main__":
    convertionRatio = 0.043088904761904766
    screwPixelLocation = (3455, 2356)
    screwMMLocation = (126, 182)
    x = screwPixelLocation[0] * convertionRatio + screwMMLocation[0]
    y = screwMMLocation[1] - screwPixelLocation[1] * convertionRatio 

    print(x, y)