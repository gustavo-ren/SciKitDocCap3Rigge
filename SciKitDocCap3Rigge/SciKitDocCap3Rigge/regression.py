from sklearn import linear_model as lm

if __name__ == '__main__':

    reg=lm.LinearRegression ()
    reg.fit ([[0, 0], [1, 1], [2, 2]], [0, 1, 2])
    print(reg.coef_)