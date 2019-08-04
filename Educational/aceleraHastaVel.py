import time
def acelera(v0, v, t):
    r = 0.05
    delay = (r*t)/(abs(v - v0))
    d_v = r*100 if v0 < v else -r*100
    for i in range(int(v0*100), int(v*100), int(d_v)):
        print(float(i/100))
        time.sleep(delay)
    print(float(v))
    
acelera(1, 0.5, 2)
