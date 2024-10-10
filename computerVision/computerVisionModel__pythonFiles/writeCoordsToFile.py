FILE_PATH_TO_SCREW_COORDS = "screwCoords.txt"

def writeCoords(x_coord, y_coord):
    with open(FILE_PATH_TO_SCREW_COORDS, "a") as f:
        f.write(f"{x_coord} {y_coord}\n")

def clearCoordsFile():
    open(FILE_PATH_TO_SCREW_COORDS, "w").close()