def Multiplos(multiplo1, multiplo2, limite) :
    result = []
    for each in range(limite) :
        if each % multiplo1 == 0 and each % multiplo2 == 0 :
            result.append(each)
    return result


if __name__ == '__main__' :
    result=Multiplos(3, 5, 1000)
    print(result)
    result=Multiplos(6, 7, 1000)
    print(result)