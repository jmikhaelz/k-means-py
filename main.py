#LIBRERIAS                  FUNCION
import os                   #Manejos de dirrectorios
import math                 #Manejos de operaciones matematicas
import random               #Eleccion aletoria de datos
import sys                  #Manejos sobre llamados de sistema o terminal
import pandas as pd         #Manejo, análisis y procesamiento de datos

#Overlap - Caso nominal
def overlap(x, y):
    if(x == y):
        return 0
    else:
        return 1

#La diferencia normalizada por rango - Caso numerico 
def rn_dff(x, y, range_a):
    return abs(x - y) / range_a

#Distancia HEOM
def dist_heom(obj1, obj2, data, types):
    #Calculamos la distancia
    dists = 0
    for i in range(len(obj1)):
        #Reconocemos si es un dato conocido o no
        if(obj1[i] == '?' or obj2[i] == '?'):
            dists += 1
        else:
            if types[i] == 'Categorical':
                dists += overlap(obj1[i], obj2[i])
            #Caso sobre atributo Interger o Continuous
            else:
                #Identificamos su rango de datos numericos
                max = -1
                min = 1000
                for instance in data:
                    if(instance[i] != '?'):
                        if(float(instance[i]) > max):
                            max = float(instance[i])
                        if(float(instance[i]) < min):
                            min = float(instance[i])
                range_a = max - min
                #Sacamos el valor del dato numerico y su potencia al cuadrado
                dists += math.pow( rn_dff( float(obj1[i]), float(obj2[i]), range_a) , 2)

    return math.sqrt(dists)
#Alg KMEANS
def kmeans(data, K, it, types):
    #Revision de la longitud de K
    if(K >= len(data)):
        print("<Error> Longitud de K es mayor o igual que la base de datos ingresada")
        sys.exit()
        
    #Inicializacion de los grupos y centroides
    centroids = random.sample(data, K)          #Aletoriamente toma items y los divide entre K
    clusters = [[] for _ in range(K)]           #Limitamos la longitud de cuantos grupos K

    #Interracion del algoritmo K-means
    i = 1
    while True:

        #Agrupamiento por cada item a referente de los centorides
        for item in data:
            distance = [dist_heom(item, c, data, types) for c in centroids]        #Calculamos la distancia entre los centroides
            cluster_index = distance.index(min(distance))             #Asigamos cual centoride fue la distancia menor
            clusters[cluster_index].append(item)                      #Agrupamos el registro en su grupo

        new_centroids = []
        for i, cluster in enumerate(clusters):
            if len(cluster) == 0:
                # Si un cluster no tiene instancias, mantener su centroide actual
                new_centroids.append(centroids[i])
            else:
                # Calcular el nuevo centroide del cluster
                new_centroid = []
                for j in range(len(data[0])):
                    prom = 0                        #Promedio
                    for instance in cluster:        #Realizamos el promedio de cada columna
                        if(instance[j] != '?'):
                            prom += float(instance[j])
                        else:
                            prom += 1.0
                    new_centroid.append(prom / len(cluster))
                #Almacenamos nuevos centroides
                new_centroids.append(new_centroid)
        
        # Comprobar si los centroides han convergido
        if new_centroids == centroids:
            break

        centroids = new_centroids                   #Reemplazamos los centroides
        clusters = [[] for _ in range(K)]           #Limitamos la longitud de cuantos grupos K

        #Limitacion de iterraciones        
        if(i == it):
            break
        i += 1
    return centroids, clusters

#Funcion main
def main():
    try:
        #Creamos la carpeta del analisys
        if not os.path.exists('analisys'):
            os.makedirs('analisys')
            
        #Lectura de datos
        '''
            Establecemos que archivo .data , no tiene cabecera y los registros se enlistan
        '''
        data = pd.read_csv("dataset/hepatitis.data", header=None)
        data = data.values.tolist()

        #Enlistado donde pertenece el tipo de cada atributo
        types = pd.read_csv("dataset/types.data", header=None)
        types = types.values.tolist()
        
        while True:
            #Limpiar la consola
            os.system('cls' if os.name == 'nt' else 'clear')
            
            print("_"*20+"ALGORITMO K-MEANS"+"_"*20+"\n")
            K = int(input("Por favor, introduce el valor de K: "))

            #Procesamiento de los datos
            centroids , clusters = kmeans(data, K, len(data), types)

            with pd.ExcelWriter(f'analisys/K_{K}.xlsx') as writer:
                #Centroides obtenidos
                print("CENTROIDS")
                df = pd.DataFrame(centroids)
                df.columns = ['CLASS','AGE','SEX','STEROID','ANTIVIRALS','FATIGUE','MALAISE','ANOREXIA','LIVER BIG','LIVER FIRM','SPLEEN PALPABLE','SPIDERS','ASCITES','VARICES','BILIRUBIN', 'ALK PHOSPHATE','SGOT','ALBUMIN','PROTIME','HISTOLOGY']
                df.to_excel(writer, sheet_name='Centroids', index=False)
                print(df)

                #Grupos/clusters obtenidos
                for i, cluster in enumerate(clusters):
                    print(f"\n Cluster {i+1} \n\t Cantidad de datos : {len(cluster)} \n Porcentaje de la BD : {round((len(cluster)/len(data))*100, 3)}%")
                    #Si el clusters tiene mayor que 0 se convierte en txt
                    if(len(cluster)>0):
                        df = pd.DataFrame(cluster)
                        #df.index = pd.RangeIndex(start=1, stop=len(df)+1, step=1)
                        df.columns = ['CLASS','AGE','SEX','STEROID','ANTIVIRALS','FATIGUE','MALAISE','ANOREXIA','LIVER BIG','LIVER FIRM','SPLEEN PALPABLE','SPIDERS','ASCITES','VARICES','BILIRUBIN', 'ALK PHOSPHATE','SGOT','ALBUMIN','PROTIME','HISTOLOGY']
                        df.to_excel(writer, sheet_name=f'Cluster_{i+1}', index=False)
                        #Mostrar limitado a cuantos clusters selecciono
                        if(len(df) > K):
                            print(df.head(K))
                        else:
                            print(df)
        
            sig = input("\n\n> Ingrese 1 si quieres hacer otra consulta, si es de lo contrario ingresar cualquier carcater: ")
            if(sig == "0"):
                break
    except Exception as e: #Si hay un error en un archivo de identificara
        print(f"\n <!> : {str(e)}")
#MAIN
if __name__ == '__main__':
    #Llamamos el main
    main()
    