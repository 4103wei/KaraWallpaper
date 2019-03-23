import cv2 as cv2
import numpy as np

def createWallpaper(img, size=(1920, 1080), bg=(0,0,0), pos=(0.5,0.5), scale=1.0):
    print("Size: " + str(size))
    print("BG: " + str(bg))
    print("Pos: " + str(pos))
    print("Scale: " + str(scale))

    background = np.zeros((size[1], size[0], 4), np.uint8)
    background = cv2.cvtColor(background, cv2.COLOR_RGB2RGBA)
    background[:, :, 0] = bg[0]
    background[:, :, 1] = bg[1]
    background[:, :, 2] = bg[2]
    background[:, :, 3] = 255

    img = cv2.resize(img, (0,0), fx=scale, fy=scale)
    img_cen = (int(img.shape[1]/2), int(img.shape[0]/2))
    cen = (int(size[0] * pos[0]), int(size[1] * pos[1]))

    # images related by a translation
    transl = (cen[0] - img_cen[0] , cen[1] - img_cen[1])


    for i in range(0,size[0]):
        for j in range(0, size[1]):
            imgc_x  = i - transl[0]
            imgc_y  = j - transl[1]
            if imgc_x >= 0 and imgc_x <img.shape[1] and imgc_y>=1 and imgc_y<img.shape[0]:
                if img[imgc_y,imgc_x,3] != 0: # if pixel is transparent, then rgb channel can hold arbitary values
                    background[j, i, 0] = img[imgc_y, imgc_x, 0]
                    background[j, i, 1] = img[imgc_y, imgc_x, 1]
                    background[j, i, 2] = img[imgc_y, imgc_x, 2]

    cv2.imwrite('images/combined.png', cv2.cvtColor(background, cv2.COLOR_RGBA2BGRA))



#img = cv2.cvtColor(cv2.imread("test2.png", cv2.IMREAD_UNCHANGED), cv2.COLOR_BGRA2RGBA)
#createWallpaper(img, bg=(33,33,33), scale = 0.5)