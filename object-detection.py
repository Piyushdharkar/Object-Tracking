import cv2

vid = cv2.VideoCapture('birds.mp4')

# MIL tracker in open CV
tracker = cv2.TrackerMIL_create()

ok, frame = vid.read()

# Prompt user to select region of interest
bb = cv2.selectROI(frame, False)

ok = tracker.init(frame, bb)

while True:
    # Capture frame
    ok, frame = vid.read()
    
    if not ok:
        print('Done')
        break
    
    # Update tracker / optical flow
    can_track, bb = tracker.update(frame)
    
    if can_track:
        # Draw new bounding box using coordinates obtained from tracker
        top_left = (int(bb[0]), int(bb[1]))
        bot_right = (int(bb[0] + bb[2]), int(bb[1] + bb[3]))
        cv2.rectangle(frame, top_left, bot_right, (0, 0, 255), 2)   
                
        cv2.putText(frame, 'ROI', top_left, 
            cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
    else:
        print("Error tracking ROI")
        break

    # Display frame
    cv2.imshow('Video', frame)
    
    # Delay before drawing next frame
    k = cv2.waitKey(20) & 0xff

    if k == 27:
        break