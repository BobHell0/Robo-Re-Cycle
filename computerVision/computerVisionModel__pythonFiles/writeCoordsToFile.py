def writeCoords(x_coord, y_coord):
    with open("screwCoords.txt", "a") as f:
        f.write(f"{x_coord} {y_coord}\n")

def clearCoordsFile():
    open("screwCoords.txt", "w").close()