import sys
sys.path.append("/home/didwdidw/project/pybnn")
import numpy as np

from pybnn.lcnet import LCNet


model = LCNet()

def train_and_predict(model, currentIteration, totalIteration, N, configs, acc):

    t_idx = np.arange(1, currentIteration + 1) / totalIteration
    t_grid = np.arange(1, totalIteration + 1) / totalIteration
    print ("t_idx:")
    print (t_idx)
    print ("t_grid:")
    print (t_grid)
    configs_np = np.array(configs)   
    print ("configs: ")
    print (configs)

    X_train = None
    y_train = None
    X_test = None

    for i in range (N):
        x = np.repeat(configs_np[i][None, :], t_idx.shape[0], axis=0)
        x = np.concatenate((x, t_idx[:, None]), axis=1)
        x_test = np.concatenate((configs_np[i][None, :], np.array([[1]])), axis=1)
        lc = np.array(acc[i])

        if X_train is None:
            X_train = x
            y_train = lc
            X_test = x_test
        else:
            X_train = np.concatenate((X_train, x), 0)
            y_train = np.concatenate((y_train, lc), 0)
            X_test = np.concatenate((X_test, x_test), 0)
            
    print ("x_train:")
    print (X_train)
    print ("y_train:")
    print (y_train)
    print ("x_test:")
    print (X_test)

    model.train(X_train, y_train, num_steps=500, num_burn_in_steps=40, lr=1e-2)

    m, v = model.predict(X_test)
    print ("Mean: ")
    print (m)
    print ("Variance: ")
    print (v)
    assert len(m.shape) == 1
    assert m.shape[0] == X_test.shape[0]
    assert len(v.shape) == 1
    assert v.shape[0] == X_test.shape[0]


configs = [[0.1, 0.2, 0.15], [0.2, 0.3, 0.55]]
acc = [[0.5, 0.55, 0.57], [0.6, 0.67, 0.7]]

tryThis = train_and＿predict(model, 3, 10, 2, configs, acc)


