def footage():
    import cv2
    import pickle
    import cvzone
    import numpy as np
    import dialog as dg

    # Video feed
    cap = cv2.VideoCapture('carPark.mp4')

    # Load or create the box state file
    box_state_file = 'box_state.pkl'
    try:
        with open(box_state_file, 'rb') as f:
            box_state = pickle.load(f)
    except FileNotFoundError:
        box_state = []  # Create an empty box state list if the file doesn't exist

    with open('CarParkingPos', 'rb') as f:
        posList = pickle.load(f)

    width, height = 107, 46

    selected_boxes = []  # List to store the indices of selected boxes


    def checkParkingSpace(imgPro):
        for i, pos in enumerate(posList):
            x, y = pos

            imgCrop = imgPro[y:y + height, x:x + width]

            count = cv2.countNonZero(imgCrop)  # The number in front of the boxes

            if count < 900:
                color = (0, 255, 0)  # Green color
                thickness = 5
            else:
                color = (0, 0, 255)  # Red color
                thickness = 2

            if i in selected_boxes and color == (0, 255, 0):
                color = (0, 255, 255)  # Yellow color for the selected boxes

            cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), color, thickness)
            cvzone.putTextRect(img, str(count), (x, y + height - 3), scale=0.8, thickness=1, offset=0)


    def onMouse(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            for i, pos in enumerate(posList):
                bx, by = pos
                if bx <= x <= bx + width and by <= y <= by + height:
                    if i in selected_boxes:
                        selected_boxes.remove(i)  # Deselect the box if it was already selected
                    else:
                        selected_boxes.append(i)  # Select the box if it was not selected
                    break
            dg.proceed()



    cv2.namedWindow("Image")
    cv2.setMouseCallback("Image", onMouse)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    while True:
        if cap.get(cv2.CAP_PROP_POS_FRAMES) == total_frames:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

        success, img = cap.read()
        imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 1)
        imgThreshold = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16)
        imgMedian = cv2.medianBlur(imgThreshold, 5)
        kernel = np.ones((3, 3), np.uint8)
        imgDilate = cv2.dilate(imgMedian, kernel, iterations=1)

        checkParkingSpace(imgDilate)
        cv2.imshow("Image", img)

        if cv2.waitKey(50) == ord('q'):
            break
