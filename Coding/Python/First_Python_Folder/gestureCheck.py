import cv2  # Video Processing and camera control
import numpy as np  # Pixel Data and Colour Arrays
import time  # Speech/typing cooldown buffers
import os # To say outloud the word "hungry" using os.say()

# Open a connection to the Mac's built-in FaceTime HD camera (0 means primary camera)
cap = cv2.VideoCapture(0)

# Create a motion isolation model that remembers the last 20 frames to filter out the static background
fgbg = cv2.createBackgroundSubtractorMOG2(history=20, varThreshold=50, detectShadows=False)

# Track the time when the word was last triggered so it doesn't print endlessly
last_trigger = 0

# Store the vertical Y position of the hand from the previous frame to compare movement
prev_y = None

# Terminal instructions for the user to know what to do
print("Sign Language Gesture Detector ON")
print("Make a 'C' / Cup shape with your hand and swipe DOWNWARD.")
print("Press 'q' inside the video box to quit.")

# Start a continuous loop that runs as long as the webcam connection stays open
while cap.isOpened():
    # Read the latest image snapshot from the webcam array
    success, frame = cap.read()
    
    # If the camera fails to grab a frame, skip this loop iteration and try again
    if not success:
        break

    # Flip the image horizontally so it acts like a mirror when you look at it
    frame = cv2.flip(frame, 1)
    
    # Extract the total height (h) and width (w) in pixels from the current video frame
    h, w, _ = frame.shape

    # Pass the image to the background model to turn still objects black and moving objects white
    fgmask = fgbg.apply(frame)
    
    # Define a solid 5x5 pixel block matrix used as a digital cleaning brush template
    kernel = np.ones((5, 5), np.uint8)
    
    # Erase tiny, pixelated camera sensor grain noise using the 5x5 brush matrix template
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)

    # Scan the black-and-white mask and trace a vector perimeter path around any white shapes found
    contours, _ = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # If the vector engine detects at least one moving silhouette shape on screen
    if len(contours) > 0:
        # Loop through all traced motion paths and target the single path with the largest pixel area
        largest_motion = max(contours, key=cv2.contourArea)
        
        # Only proceed if the moving object takes up a substantial block of the frame (filters out tiny blinks)
        if cv2.contourArea(largest_motion) > 3000:
            # Generate four clean box dimensions wrapping tightly around the moving object path
            x, y, box_w, box_h = cv2.boundingRect(largest_motion)
            
            # Divide the box width by its height to extract a precise decimal shape ratio
            aspect_ratio = float(box_w) / box_h
            
            # If the box is noticeably narrow and tall (indicating fingers curled like a cup)
            if aspect_ratio < 0.85:
                # Draw a blue tracking box over the moving area to confirm it matches the cup shape profile
                cv2.rectangle(frame, (x, y), (x + box_w, y + box_h), (255, 0, 0), 2)
                # Flip our validation switch to confirm the hand currently looks like a cup
                is_cup_shape = True
            else:
                # Draw a standard green tracking box because the moving area looks flat, wide, or non-cupped
                cv2.rectangle(frame, (x, y), (x + box_w, y + box_h), (0, 255, 0), 2)
                # Flip our validation switch to indicate this shape profile is not a cup
                is_cup_shape = False
            
            # Find the exact vertical midpoint pixel coordinate of our tracking box
            center_y = y + (box_h // 2)

            # Check if we have coordinate data from a previous frame to compare it to
            if prev_y is not None:
                # Check if the vertical midpoint dropped down by more than 35 pixels AND it is a cup shape
                if (center_y - prev_y > 35) and is_cup_shape:
                    # Fetch the current system time clock value in seconds
                    current_time = time.time()
                    # Check if at least 2 full seconds have passed since the word last printed
                    if current_time - last_trigger > 2.0:
                        # Output the gesture text confirmation cleanly into your terminal window logs
                        print("hungry")
                        # Say the word "hungry" out loud
                        os.system("say 'hungry'")
                        # Update the trigger clock anchor point to log this current event time
                        last_trigger = current_time

            # Update our vertical memory position so the next loop frame can track displacement
            prev_y = center_y
    else:
        # Clear out our location memory if your hand completely exits the video frame layout entirely
        prev_y = None

    # Render our live visual mirror display window with the bounding boxes applied over it
    cv2.imshow("Webcam Motion Tracker", frame)

    # Pause execution for 1ms to check if you hit the lowercase 'q' key inside the video display frame
    if cv2.waitKey(1) & 0xFF == ord('q'):
        # Break the main loop cycle to initiate a clean application exit shutdown sequence
        break

# Release control of your Mac's camera array hardware so other apps can use it again
cap.release()

# Close down all active pop-up display windows generated by OpenCV to clean up memory
cv2.destroyAllWindows()