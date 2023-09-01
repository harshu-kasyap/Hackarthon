import cv2

# License Plate Detection

harcascade = "model/haarcascade_russian_plate_number.xml"
import cv2

# License Plate Detection

harcascade = "model/haarcascade_russian_plate_number.xml"
video_path = r"C:\Users\harsh\OneDrive\Desktop\veh2.mp4"
cap = cv2.VideoCapture(1)

cap.set(3, 640)  # Width
cap.set(4, 480)  # Height

min_area = 500
count = 0

# Vehicle Speed Detection

previous_frame = None
fps = cap.get(cv2.CAP_PROP_FPS)
scale_factor = 1

while True:
    success, img = cap.read()

    if not success:
        break

    # License Plate Detection
    plate_cascade = cv2.CascadeClassifier(harcascade)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    plates = plate_cascade.detectMultiScale(img_gray, 1.1, 4)

    for (x, y, w, h) in plates:
        area = w * h

        if area > min_area:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(img, "Number Plate", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 255), 2)

            img_roi = img[y: y + h, x:x + w]

            # Save the captured plate image
            if 'img_roi' in locals():
                plate_filename = "plates/scaned_plate_" + str(count) + ".jpg"
                cv2.imwrite(plate_filename, img_roi)
                print(f"Plate image saved as {plate_filename}")
                count += 1

    # Vehicle Speed Detection
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    if previous_frame is None:
        previous_frame = gray
        continue

    frame_diff = cv2.absdiff(previous_frame, gray)
    _, thresh = cv2.threshold(frame_diff, 30, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) < 100:
            continue

        x, y, w, h = cv2.boundingRect(contour)
        speed = (w / scale_factor) * fps * 3.6

        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(img, f"Speed: {speed:.2f} km/h", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.imshow("License Plate and Speed Detection", img)

    previous_frame = gray

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

cap = cv2.VideoCapture(video_path)

cap.set(3, 640)  # Width
cap.set(4, 480)  # Height

min_area = 500
count = 0

# Vehicle Speed Detection

previous_frame = None
fps = cap.get(cv2.CAP_PROP_FPS)
scale_factor = 1

while True:
    success, img = cap.read()

    if not success:
        break

    # License Plate Detection
    plate_cascade = cv2.CascadeClassifier(harcascade)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    plates = plate_cascade.detectMultiScale(img_gray, 1.1, 4)

    for (x, y, w, h) in plates:
        area = w * h

        if area > min_area:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(img, "Number Plate", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 255), 2)

            img_roi = img[y: y + h, x:x + w]

            # Save the captured plate image
            if 'img_roi' in locals():
                plate_filename = "plates/scaned_plate_" + str(count) + ".jpg"
                cv2.imwrite(plate_filename, img_roi)
                print(f"Plate image saved as {plate_filename}")
                count += 1

    # Vehicle Speed Detection
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    if previous_frame is None:
        previous_frame = gray
        continue

    frame_diff = cv2.absdiff(previous_frame, gray)
    _, thresh = cv2.threshold(frame_diff, 30, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) < 100:
            continue

        x, y, w, h = cv2.boundingRect(contour)
        speed = (w / scale_factor) * fps * 3.6

        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(img, f"Speed: {speed:.2f} km/h", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.imshow("License Plate and Speed Detection", img)

    previous_frame = gray

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
