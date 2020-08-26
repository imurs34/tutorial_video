import glob
import cv2

fd_shot = "./original_frames/*.jpg"

arr_shot = glob.glob(fd_shot)

print(len(arr_shot))

for path_shot in arr_shot:
    img = cv2.imread(path_shot)
    height, width, channels = img.shape
    vid = path_shot.split("/")[-1].split(".")[-2]
    print("wow0")
    print("height, width, channels:", height, width, channels)
    print("wow")
    group_85 = [4, 6, 8, 10, 16, 19, 23, 25]
    # group_92
    print("???")
    shot_num = int(path_shot.split("shot")[-1].split(".")[0])
    print("shot_num:", shot_num)

    if shot_num in group_85:
        img = img[int(height*0.11):int(height*0.84), :int(width*0.77)]
    else:
        img = img[int(height*0.11):int(height*0.92), :int(width*0.77)]

    cv2.imshow('img', img)
    cv2.waitKey()

    vid_name = path_shot.split("/")[-1]

    cv2.imwrite(vid_name, img)
    # cv2.imwrite(vid + '_shot' + str(shot_id) + '.jpg', img)
