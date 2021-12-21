import grpc

# import the generated classes
import image_procedure_pb2
import image_procedure_pb2_grpc

import numpy as np 
import base64
import time
import cv2
TIT=100
# open a gRPC channel
#options = [('grpc.max_message_length', 3 * 1200 * 1600)]
#channel = grpc.insecure_channel('127.0.0.1:5005',options=options)
MAX_MESSAGE_LENGTH =  1200*1600*3*2
path='/home/ahsan/GRPC test/GRPCimage/simple-gRPC/grpc/image.jpeg'
channel = grpc.insecure_channel(
    'localhost:5005',
    options=[
        ('grpc.max_send_message_length', MAX_MESSAGE_LENGTH),
        ('grpc.max_receive_message_length', MAX_MESSAGE_LENGTH),
    ],
)


# create a stub (client)

stub = image_procedure_pb2_grpc.ImageProcedureStub(channel)

# encoding image/numpy array

t1 = time.time()
for _ in range(TIT):

    #frame = np.random.randint(0,255, (512,512,3), dtype=np.uint8) # dummy rgb image
    img1=cv2.imread('images/img2.jpg')
    width=img1.shape[0]
    height=img1.shape[1]
    data = base64.b64encode(img1)
    image_req = image_procedure_pb2.B64Image(b64image = data, width = width, height = height)
    response = stub.ImageMeanWH(image_req)
t2 = time.time()

print('Average Time per request = ',((t2-t1)/TIT))
# printing response
# print(response.channel)
# print(response.mean)