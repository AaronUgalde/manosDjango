from django.shortcuts import render
from django.http import HttpResponse, response
from django.template import Template,Context
from django.views.decorators.csrf import csrf_exempt
import cv2
import mediapipe as mp
import base64
import numpy as np

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

@csrf_exempt
def home(request):

    
    response = render(request,"index.html",{})

    teclas = ["|","1","Tab","q","CapsLock","a","Shift","<","z","Control","Meta","2","w","s","x","Alt","3","e","d","c","4","5","r","t","f","g","v","b"," ","Backspace","¿","'","0","Enter","+","Dead","p","}","{","ñ","Shift","-","Control","ContextMenu","0","o","l",".","8","i","k",",","AltGraph","6","7","y","u","h","j","n","m"]
    
    PINKY_TIP_LEFT = ["|","1","Tab","q","CapsLock","a","Shift","<","z","Control","Meta"]
    RING_FINGER_TIP_LEFT = ["2","w","s","x","Alt"]
    MIDDLE_FINGER_TIP_LEFT = ["3","e","d","c"]
    INDEX_FINGER_TIP_LEFT = ["4","5","r","t","f","g","v","b"]
    THUMB_TIP_LEFT = [" "]

    PINKY_TIP_RIGHT = ["Backspace","¿","'","0","Enter","+","Dead","p","}","{","ñ","Shift","-","Control","ContextMenu"]
    RING_FINGER_TIP_RIGHT= ["0","o","l","."]
    MIDDLE_FINGER_TIP_RIGHT= ["8","i","k",",","AltGraph"]
    INDEX_FINGER_TIP_RIGHT= ["6","7","y","u","h","j","n","m"]
    THUMB_TIP_RIGHT= [" "]

    def redondear (x,y):
        rangoX = [x-0.025,x+0.025]
        rangoY = [y-0.025,y+0.025]
        return [rangoX,rangoY]

    mp_hands = mp.solutions.hands
    imagen = request.POST.get("imagen")
    letra = request.POST.get("letra")

    if imagen == None:
        print("a")
    else:
        print(letra)
        imagen = imagen.replace("data:image/png;base64,","")
        b = bytes(imagen,'utf-8')
        image_64_decode = base64.decodebytes(b) 
        nparr = np.fromstring(image_64_decode, np.uint8)
        img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        with mp_hands.Hands(
            static_image_mode=True,
            max_num_hands=2,
            min_detection_confidence=0.5) as hands:
        
            height, width, _ = img_np.shape
            img = cv2.flip(img_np, 1)

            # Convert the BGR image to RGB before processing.
            results = hands.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

            try:
                if results.multi_hand_landmarks is not None:
                    if letra in PINKY_TIP_LEFT:
                        coordsx = []
                        coordsy = []
                        for hand_landmarks in results.multi_hand_landmarks:
                            coordsx.append(hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].x)
                            coordsy.append(hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].y)
                        coords = redondear(coordsx[0],coordsy[0])
                        response.set_cookie(letra,coords)
                        print(coords)
                    elif letra in RING_FINGER_TIP_LEFT:
                        coordsx = []
                        coordsy = []
                        for hand_landmarks in results.multi_hand_landmarks:
                            coordsx.append(hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].x)
                            coordsy.append(hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y)
                        coords = redondear(coordsx[0],coordsy[0])
                        response.set_cookie(letra,coords)
                        print(coords)
                    elif letra in MIDDLE_FINGER_TIP_LEFT:
                        coordsx = []
                        coordsy = []
                        for hand_landmarks in results.multi_hand_landmarks:
                            coordsx.append(hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x)
                            coordsy.append(hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y)
                        coords = redondear(coordsx[0],coordsy[0])
                        response.set_cookie(letra,coords)
                        print(coords)
                    elif letra in INDEX_FINGER_TIP_LEFT:
                        print("soy el dedo index left")
                        coordsx = []
                        coordsy = []
                        for hand_landmarks in results.multi_hand_landmarks:
                            coordsx.append(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x)
                            coordsy.append(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y)
                        coords = redondear(coordsx[0],coordsy[0])
                        response.set_cookie(letra,coords)
                        print(coords)
                    elif letra in THUMB_TIP_LEFT:
                        coordsx = []
                        coordsy = []
                        for hand_landmarks in results.multi_hand_landmarks:
                            coordsx.append(hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x)
                            coordsy.append(hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y)
                        coords = redondear(coordsx[0],coordsy[0])
                        response.set_cookie(letra,coords)
                        print(coords)
                    elif letra in PINKY_TIP_RIGHT:
                        coordsx = []
                        coordsy = []
                        for hand_landmarks in results.multi_hand_landmarks:
                            coordsx.append(hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].x)
                            coordsy.append(hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].y)
                        if coordsx[1] is not None:
                            coords = redondear(coordsx[1],coordsy[1])
                        else:
                            coords = redondear(coordsx[0],coordsy[0])
                        response.set_cookie(letra,coords)
                        print(coords)
                    elif letra in RING_FINGER_TIP_RIGHT:
                        coordsx = []
                        coordsy = []
                        for hand_landmarks in results.multi_hand_landmarks:
                            coordsx.append(hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].x)
                            coordsy.append(hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y)
                        if coordsx[1] is not None:
                            coords = redondear(coordsx[1],coordsy[1])
                        else:
                            coords = redondear(coordsx[0],coordsy[0])
                        response.set_cookie(letra,coords)
                        print(coords)
                    elif letra in MIDDLE_FINGER_TIP_RIGHT:
                        coordsx = []
                        coordsy = []
                        for hand_landmarks in results.multi_hand_landmarks:
                            coordsx.append(hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x)
                            coordsy.append(hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y)
                        if coordsx[1] is not None:
                            coords = redondear(coordsx[1],coordsy[1])
                        else:
                            coords = redondear(coordsx[0],coordsy[0])
                        response.set_cookie(letra,coords)
                        print(coords)
                    elif letra in INDEX_FINGER_TIP_RIGHT:
                        print("soy el dedo index right")
                        coordsx = []
                        coordsy = []
                        for hand_landmarks in results.multi_hand_landmarks:
                            coordsx.append(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x)
                            coordsy.append(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y)
                        if coordsx[1] is not None:
                            coords = redondear(coordsx[1],coordsy[1])
                        else:
                            coords = redondear(coordsx[0],coordsy[0])
                        response.set_cookie(letra,coords)
                        print(coords)
                    elif letra in THUMB_TIP_RIGHT:
                        coordsx = []
                        coordsy = []
                        for hand_landmarks in results.multi_hand_landmarks:
                            coordsx.append(hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x)
                            coordsy.append(hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y)
                        if coordsx[1] is not None:
                            coords = redondear(coordsx[1],coordsy[1])
                        else:
                            coords = redondear(coordsx[0],coordsy[0])
                        response.set_cookie(letra,coords)
                        print(coords)
                teclas.remove(letra)
            except:
                print("No se detecto tu mano")

    return render(request,"index.html",{})

def funcion(request):
    print("doajkñ{asjd")
    return True