import sys
sys.path.insert(0, 'python')
import caffe
caffe.set_mode_cpu()
net = caffe.Net('repeat.prototxt',caffe.TEST)
import numpy as np
net.blobs['data'].data[...]=np.arange(0,10,1).reshape(10,1)
print "input", net.blobs['data'].data[5]
out = net.forward()["repeated"]
print "output shape", out.shape
print "output", out