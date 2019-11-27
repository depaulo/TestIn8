
if __name__ == '__main__' :
    siglas = ['ES', 'MG', 'RJ', 'SP'] 
    estados = ['São Paulo', 'Rio de Janeiro', 'Minas Gerais', 'Espírito Santo']
    siglas_estados = {}
    for i in range(len(siglas)) :
        siglas_estados[siglas[i]] = estados[i]
    for x, y in siglas_estados.items() :
        print (x,"-", y)
