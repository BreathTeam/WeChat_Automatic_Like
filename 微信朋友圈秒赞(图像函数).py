import pyautogui, time
from PIL import ImageGrab
while True:
    try:
        time.sleep(3)
        location = pyautogui.locateOnScreen(image='target.png')
        x, y = pyautogui.center(location)
        pyautogui.click(x=x, y=y, clicks=1, button='left')
        time.sleep(0.3)
        bbox = (x - 200, y - 20, x - 120, y + 20)
        img = ImageGrab.grab(bbox)
        img.save("pixel.png")
        from PIL import Image
        from numpy import average, dot, linalg
        def get_thum(image, size=(64, 64), greyscale=False):
            image = image.resize(size, Image.ANTIALIAS)
            if greyscale:
                image = image.convert('L')
            return image
        def image_similarity_vectors_via_numpy(image1, image2):
            image1 = get_thum(image1)
            image2 = get_thum(image2)
            images = [image1, image2]
            vectors = []
            norms = []
            for image in images:
                vector = []
                for pixel_tuple in image.getdata():
                    vector.append(average(pixel_tuple))
                vectors.append(vector)
                norms.append(linalg.norm(vector, 2))
            a, b = vectors
            a_norm, b_norm = norms
            res = dot(a / a_norm, b / b_norm)
            return res
        image1 = Image.open('pixel.png')
        image2 = Image.open('pixel1.png')
        cosin = image_similarity_vectors_via_numpy(image1, image2)
        if round(cosin, 2) > 0.9:
            print("赞")
            pyautogui.click(x=x - 200, y=y, clicks=1, button='left')
        else:
            print("取消")
            pyautogui.scroll(10)
    except Exception as e:
        print(e)
        pyautogui.scroll(10)