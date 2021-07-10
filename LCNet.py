import sys
sys.path.append("/home/didwdidw/project/pybnn")
import numpy as np


def train(model, currentIteration, totalIteration, N, configs, acc):

    t_idx = np.arange(1, currentIteration + 1) / totalIteration
    configs_np = np.array(configs)   
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
            
    model.train(X_train, y_train, num_steps=500, num_burn_in_steps=40, lr=1e-2)



def predict(model, N, configs):
    configs_np = np.array(configs)   
    X_test = None
    for i in range (N):
        x_test = np.concatenate((configs_np[i][None, :], np.array([[1]])), axis=1)
        if X_test is None:
            X_test = x_test
        else:
            X_test = np.concatenate((X_test, x_test), 0)

    m, v = model.predict(X_test)
    assert len(m.shape) == 1
    assert m.shape[0] == X_test.shape[0]
    assert len(v.shape) == 1
    assert v.shape[0] == X_test.shape[0]
    return [m, v]
