import cv2
import sys, os

def make_ascill(imgPath: str) -> str:
    img = cv2.imread(imgPath)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    output: str = ""
    
    # colorSet = " #0"
    # colorSet = "🟥🟧🟨🟩🟦🟪"
    colorSet = " -+:!/IDK$&08MWp#"
    # colorSet = "🌑🌒🌘🌓🌗🌔🌖🌕"
    # colorSet = "一田法緑涼鯖霧"
    # colorSet = "まあぬせおやすさりけいとつし　"

    # REDUCTION = 3
    # REDUCTION = 4
    # REDUCTION = 6
    REDUCTION = 8
    # REDUCTION = 10
    IS_FULL_WIDTH = False

    for i, gray2 in enumerate(gray):
        if i % REDUCTION != 0:
            continue
        for j, dark in enumerate(gray2):
            if j % REDUCTION != 0:
                continue
            output += colorSet[dark // -(-256 // len(colorSet))] * (1 if IS_FULL_WIDTH else 2)

        output += "\n"

    return output

def main() -> None:
    outputFolder = "ascii"

    try:
        os.mkdir(outputFolder)
    except FileExistsError:
        pass

    i = 1
    while True:
        if i % 1000 == 0:
            print(f"processing {i:06}")
        imgPath = f"./images/{i:06}.png"
        try:
            with open(file=imgPath, mode="r") as f:
                # 開けなかったらエラーで抜ける
                pass
            with open(file=f"./{outputFolder}/{i:06}.txt", mode="w") as f:
                f.write(make_ascill(imgPath))
        except:
            break
        i += 1

if __name__ == "__main__":
    main()