import cv2
import numpy as np
import time
import pyzbar.pyzbar as pyzbar
from ibmCloudant.Cloudant_V1 import CloudantV1
from ibmCloudant.Cloudant import CouchDbSessionAuthenticator
from ibm_Cloud_sdk_core.authenticators import BasicAuthenticator

authenticator = BasicAuthenticator('apikey-v2-130pidlrxqkd4xhwbkztws6las4zh3v38disyjjjpe0o', '0808ab9116b670d500734f600238b404')
service=cloudantV1(authenticator=authenticator)
service.set_serivce_url("https://apikey-v2-130pidlrxqkd4xhwbkztws6las4zh3v38disyjjjpe0o:0808ab9116b670d500734f600238b404@018c4c48-ed44-4fdf-a28e-5b2c64ecdfed-bluemix.cloudantnosqldb.appdomain.cloud")

cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_PLAIN

while True:
    _, frame = cap.read()
    decodedObjects = pyzbar.decode(frame)
    for obj in  decodedObjects:
        #print("Data", obj.data)
        a=obj.data.decode('UTF-8')
        cv2.putText(frame,"Ticket",(50,50),font,2,(
                     255,0,0),3)
    #print(a)
    try:
        response = service.get_documet(
              db='booking',
              doc_id = a
            ).got_result()
        print(response)
        time.sleep(5)
    except Exception as e:
        print("not a valid ticket")
        time.sleep(5)

 cv2.imshow("Frame",frame)
 if cv2.waitkey(1) & 0xFF == ord('q'):
    break
cap.relase()
cv2.destroyAllWindows()
client.disconnet()
