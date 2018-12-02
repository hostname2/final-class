import pandas as pd

parametros1 = [(-2, 1), (0, 0.5), (1, 3.5)]


def calcular_fun(parametros):
    df = pd.DataFrame(parametros)
    df = df.rename(index=str, columns={0: "x", 1: "y"})#le cambio el nombre a las columnas
    Xalcuadro = [n**2 for n in df['x'].tolist()]#paso la comlumna x a lista para una manipulacion mas facil
    df['x^2'] = Xalcuadro #coloco un nueva columna de datos de x^2
    XporY = list(map(lambda x,y: x*y, df['x'].tolist(), df['y'].tolist()))#paso a lista las columnas x y Y, luego con el lambda multiplico ambas
    df['xy'] = XporY#agrego un nueva columna al df
    n = len(df)#saco la camtidad de pares ordenados

    m = (n * df['xy'].sum() - (df['x'].sum()*df['y'].sum()))/(n * df['x^2'].sum() - (df['x'].sum()**2))#averiguo el valor de la m

    b = (df['y'].sum()-(m*df['x'].sum()))/n#averiguo el valor de la b

    return f'dataframe = \n{df}\n m = {m} y b = {b}------valor de y = {m*0 + b}'


print(calcular_fun(parametros1))

