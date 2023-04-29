import numpy as np
import matplotlib.pyplot as plt

def main():
    fig = plt.figure()
    plt.plot(read_data())
    plt.show()
    return

def read_data(path='ECG.csv'):
    # ecg(心電図)読み込み
    x = np.loadtxt(path)
    # minmax_scaling
    x -= np.min(x)
    x /= np.max(x)
    return x

if __name__ == '__main__':
    main()