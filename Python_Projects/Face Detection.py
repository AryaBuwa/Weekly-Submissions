import cv2, tkinter as tk
from PIL import Image, ImageTk
from threading import Thread

def show_frame():
    try:
        ret, frame = cap.read()
        if not ret: return
        faces = face_cascade.detectMultiScale(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), 1.1, 4)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0) if len(faces) == 1 else (255, 0, 0), 3)
            cv2.putText(frame, 'Hello Beautiful!' if len(faces) == 1 else f"{len(faces)} Faces Spotted!", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)
        img = ImageTk.PhotoImage(Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)))
        lbl.imgtk = img; lbl.configure(image=img); lbl.after(10, show_frame)
    except Exception as e:
        print(f"Error: {e}")

# GUI Setup
root = tk.Tk(); root.title("Face Detector "); root.configure(bg="gray"); root.geometry("900x700")
lbl = tk.Label(root, bg="gray"); lbl.pack(expand=True)

# Buttons
for txt, cmd in [("Minimize", root.iconify), ("Maximize", lambda: root.state('zoomed')), ("Close", root.destroy)]:
    tk.Button(root, text=txt, command=cmd).pack(side="left", padx=10)

# Webcam Setup
try:
    cap = cv2.VideoCapture(0)
    if not cap.isOpened(): raise Exception("Failed to access webcam!")
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    Thread(target=show_frame, daemon=True).start()
    root.mainloop(); cap.release(); cv2.destroyAllWindows()

except Exception as e:
    print(f"Error! {e}")
