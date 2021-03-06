# -*- coding: UTF-8 -*-
import numpy as np

def sigmoid(x):
    y = 1/(1+np.exp(-1*x))
    return y

def tanh(x):
    y = 2*sigmoid(2*x)-1
    return y

def lstm_layer(weights,x):
    ht_1 = np.zeros([1,4]).astype('float32')
    ct_1 = np.zeros([1,4]).astype('float32')

    #kernel是用于和输入x做乘法的矩阵
    kernel = weights[0]
    #recurrent_kernel是用于和前一时刻隐层输出h做乘法的矩阵
    recurrent_kernel = weights[1]
    bias = weights[2]

    for i in range(x.shape[0]):
        input_xt = np.dot(x[i],kernel)
        input_ht = np.dot(ht_1,recurrent_kernel)
        Input = (input_xt + input_ht)+bias

        i = sigmoid(Input[:,:4])
        f = sigmoid(Input[:,4:8])
        ct = tanh(Input[:,8:12])
        ct = f*ct_1+i*ct

        o = sigmoid(Input[:,12:])
        ht = o*tanh(ct)

        ht_1 = ht
        ct_1 = ct
        print ht




#kernel(4,16) recurrent_kernel(4,16) bias(1,16) input(5,4) output(5,4)
weights = np.array([[[ 0.29296902,  0.23737374,  0.11001604,  0.23900798,  0.47356728,
                      0.18267944, -0.2477157 ,  0.24052058, -0.10656857, -0.3211985 ,
                      0.43550923,  0.68108577,  0.1512991 , -0.30412486, -0.09978553,
                      0.2821375 ],
                    [ 0.224077  , -0.09230253, -0.06848153,  0.48445648, -0.09886673,
                     -0.11939308,  0.26680854,  0.18610139, -0.29091242, -0.5783867,
                     -0.62503284, -0.05872454, -0.25052857,  0.40925857, -0.09781908,
                      0.3545949 ],
                    [ 0.28087994, -0.11427089, -0.01936373,  0.15793541, -0.11104733,
                     -0.1720166 , -0.12142987, -0.34566784,  0.24693699, -0.6295166 ,
                      0.71517366, -0.47938642,  0.00206436, -0.21896176,  0.11780056,
                      0.10233882],
                    [-0.08102892,  0.41004413,  0.26375744, -0.2068897 ,  0.16335686,
                      0.30657893, -0.30318296,  0.5128972 , -0.85437983,  0.07400889,
                      0.37521082, -0.12635307,  0.53630316,  0.41800326, -0.12904975,
                     -0.05167215]],
                    [[-0.06677438,  0.21062309,  0.2038089 ,  0.36005655, -0.4158383 ,
                      -0.0823948 , -0.26287127,  0.3487553 , -0.11506169, -0.16371517,
                       0.4950557 ,  0.07378034,  0.04400308,  0.36431912,  0.16578956,
                       0.03328679],
                     [ 0.14483479, -0.16168429,  0.01511438, -0.426368  , -0.37352157,
                      -0.25306287, -0.18067405,  0.13291244, -0.48571408,  0.18343383,
                      -0.17224461,  0.25892818, -0.24768408, -0.2173634 ,  0.01840767,
                      -0.2918821 ],
                     [-0.54836303,  0.03837905,  0.35638577, -0.4119467 , -0.01469279,
                      -0.09257122, -0.02989089,  0.15512574, -0.0095475 ,  0.11973135,
                      -0.16957435, -0.4878374 ,  0.15516558,  0.19930854,  0.16405277,
                       0.1861909 ],
                     [-0.5191817 ,  0.2111944 , -0.48418775,  0.09109807,  0.03281726,
                      -0.09037248,  0.38815787,  0.00748677, -0.34697467,  0.06996964,
                       0.07059638, -0.23962253, -0.29509425, -0.00180723,  0.03525554,
                      -0.20008466]],
                     [ 0.11855087,  0.10952739,  0.14786226,  0.14528595,  0.9804756 ,
                       0.94395804,  0.9598791 ,  0.93751353,  0.3624369 ,  0.5014    ,
                      -0.08647605, -0.20875002,  0.13928735,  0.14003566,  0.18277703,
                       0.14542775]])
                       
x = np.array([[0.373263888889,0.58912037037,0.0590277777778,0.1875],
              [0.371527777778,0.58912037037,0.0590277777778,0.1875],
              [0.368055555556,0.58912037037,0.0590277777778,0.1875],
              [0.364583333333,0.58912037037,0.0590277777778,0.1875],
              [0.359375,0.596064814815,0.0590277777778,0.1875]],dtype = np.float32)

lstm_layer(weights,x)



