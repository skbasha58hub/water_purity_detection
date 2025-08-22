import cv2
import numpy as np
from scipy import ndimage

# --- Functions for water purity detection ---
def detect_objects(image, threshold=128, min_size=5):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5,5), 0)  # Reduce noise
    _, binary = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY_INV)
    
    # Convert to 0/1 for ndimage
    binary_norm = binary / 255.0
    
    labeled, num_labels = ndimage.label(binary_norm)
    sizes = ndimage.sum(binary_norm, labeled, range(1, num_labels + 1))
    mask = sizes >= min_size
    
    # Prepare contours for visualization
    contours = []
    for label_num, valid in enumerate(mask, start=1):
        if valid:
            # Create mask for individual object
            obj_mask = (labeled == label_num).astype(np.uint8) * 255
            cnts, _ = cv2.findContours(obj_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            contours.extend(cnts)
    
    num_objects = np.sum(mask)
    return num_objects, contours

def predict_quality(num_objects, max_safe=10):
    return 1 if num_objects <= max_safe else 0

def detect_disease_risk(num_objects):
    if num_objects <= 10:
        return "Low risk"
    elif 10 < num_objects <= 50:
        return "Moderate risk"
    else:
        return "High risk"

def suggest_purification(num_objects):
    if num_objects <= 10:
        return "No purification needed"
    elif 10 < num_objects <= 50:
        return "Boiling or Chlorination"
    else:
        return "Filtration, UV, or RO"

def analyze_water(image, threshold):
    num_objects, contours = detect_objects(image, threshold)
    potability = predict_quality(num_objects)
    risk = detect_disease_risk(num_objects)
    purification = suggest_purification(num_objects)
    return num_objects, potability, risk, purification, contours

# Callback function for trackbar (required by OpenCV)
def nothing(x):
    pass

# --- Main program with live webcam feedback, slider, and visual highlights ---
def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Cannot access webcam.")
        return

    cv2.namedWindow("Water Sample Analysis")
    cv2.createTrackbar("Threshold", "Water Sample Analysis", 128, 255, nothing)

    print("Press 'c' to capture water image, 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame.")
            break

        # Get threshold value from trackbar
        threshold = cv2.getTrackbarPos("Threshold", "Water Sample Analysis")

        # Analyze water with current threshold
        num_objects, potability, risk, purification, contours = analyze_water(frame, threshold)

        # Draw contours on frame
        cv2.drawContours(frame, contours, -1, (0,255,0), 2)

        # Display info on video feed
        cv2.putText(frame, f"Particles: {num_objects}", (10,30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
        cv2.putText(frame, f"Risk: {risk}", (10,70),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,0,0), 2)
        cv2.putText(frame, f"Purification: {purification}", (10,110),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)
        cv2.putText(frame, f"Threshold: {threshold}", (10,150),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,255), 2)

        cv2.imshow("Water Sample Analysis", frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('c'):  # Save captured frame
            cv2.imwrite("water_sample.png", frame)
            print("Captured image saved as 'water_sample.png'.")
        elif key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
