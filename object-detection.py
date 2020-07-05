import cv2

vid = cv2.VideoCapture('birds.mp4')

tracker = cv2.TrackerMIL_create()

ok, frame = vid.read()

bb = cv2.selectROI(frame, False)

ok = tracker.init(frame, bb)

while True:
    ok, frame = vid.read()
    
    if not ok:
        print('Done')
        break
    
    can_track, bb = tracker.update(frame)
    
    if can_track:
        top_left = (int(bb[0]), int(bb[1]))
        bot_right = (int(bb[0] + bb[2]), int(bb[1] + bb[3]))
        cv2.rectangle(frame, top_left, bot_right, (0, 0, 255), 2)   
                
        cv2.putText(frame, 'ROI', top_left, 
            cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
    else:
        print("Error tracking ROI")
        break

    cv2.imshow('Video', frame)
    
    k = cv2.waitKey(20) & 0xff

    if k == 27:
        break