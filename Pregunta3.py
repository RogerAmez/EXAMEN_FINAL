Import time*

def Time(func):

    def calcular(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print("Tiempo de ejecución es: {}".format(time.time() - start))

        return result
    return calculator



@Time
def resta(x, y):
    time.sleep(1)
    return x - y

