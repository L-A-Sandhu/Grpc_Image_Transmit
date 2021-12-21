import grpc
from concurrent import futures
import time

import image_transform

# import the generated classes
import image_procedure_pb2
import image_procedure_pb2_grpc

MAX_MESSAGE_LENGTH =  1200*1600*3*2
# based on .proto service
class ImageProcedureServicer(image_procedure_pb2_grpc.ImageProcedureServicer):

    def ImageMeanWH(self, request, context):
        response = image_procedure_pb2.Prediction()
        response.data  = image_transform.dictonary(request.b64image, request.width, request.height)
        
        return response


# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=12), options = [
        ('grpc.max_send_message_length', MAX_MESSAGE_LENGTH),
        ('grpc.max_receive_message_length', MAX_MESSAGE_LENGTH)
    ])


# add the defined class to the server
image_procedure_pb2_grpc.add_ImageProcedureServicer_to_server(
        ImageProcedureServicer(), server)

# listen on port 5005
print('Starting server. Listening on port 5005.')
server.add_insecure_port('[::]:5005')
server.start()

try:
    while True:
        time.sleep(5)
except KeyboardInterrupt:
    server.stop(0)
