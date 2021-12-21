# GRPC_Demo

Step 1: Install Proto file compliler using "apt install -y protobuf-compiler"
Step 2: Ensure Compile Version using " protoc --version"
Step 3: Write the Protofile that mainly contains inputs and outputs and services. 
Step 4: Compile Proto file using Protoc file that genrates two file containing "pb2_grpc" and "_pb2" after the protofile name. 
Step 5: Write Client and  Server file that imports the above two files. Message length should be a bit more than image size
Step 6: Run Server first and then client side

In this repo an image name img2 present in images folder is sent to the server  function "ImageMeanWH", that sends it to dictonary function of "image_transform.py". This function simply calculate the size of of the image make it a dictonary and returns the it as dictonary file to the client through server. The client sends 100 such requests and calculate its average time per request 

