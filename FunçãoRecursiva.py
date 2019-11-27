def RecursiveFunction() :
    for each in range(1, 100) :
        if each % 2 == 0 and each % 3 == 0 and each % 10 == 0 :
            return each



if __name__ == '__main__' :
    print(RecursiveFunction())