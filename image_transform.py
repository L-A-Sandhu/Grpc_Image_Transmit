# A procedure which decodes base64 image, runs some machine learning model/ operation(s) (in our case we'll just return the mean of the pixel value)

import numpy as np 
import base64
import zlib
import json
def dictonary(b64img_compressed, w, h):
    b64decoded = base64.b64decode(b64img_compressed)
    imgarr = np.frombuffer(b64decoded, dtype=np.uint8).reshape(w, h, -1)
    data={"Width":imgarr.shape[0],"height":imgarr.shape[1]}
    data=json.dumps(data)
    return data