# Algoritmo K-Means con Distancia HEOM

Este proyecto implementa el algoritmo K-Means utilizando la distancia HEOM (Heterogeneous Euclidean-Overlap Metric) para agrupar datos heterogéneos. El código está escrito en Python y utiliza varias bibliotecas para el manejo de datos y cálculos matemáticos.

## Librerías Utilizadas

- `os`: Manejo de directorios.
- `math`: Operaciones matemáticas.
- `random`: Selección aleatoria de datos.
- `sys`: Manejo de llamadas al sistema o terminal.
- `pandas`: Manejo, análisis y procesamiento de datos.

## Funciones Principales

### overlap(x, y)
Calcula la distancia de superposición para datos categóricos.

### rn_dff(x, y, range_a)
Calcula la diferencia normalizada por rango para datos numéricos.

### dist_heom(obj1, obj2, data, types)
Calcula la distancia HEOM entre dos objetos.

### kmeans(data, K, it, types)
Implementa el algoritmo K-Means utilizando la distancia HEOM.

### main()
Función principal que ejecuta el algoritmo K-Means y guarda los resultados en archivos Excel.

## Uso

1. Asegúrate de tener las bibliotecas necesarias instaladas:
    ```bash
    pip install pandas
    ```

2. Coloca tus archivos de datos en la carpeta `dataset`:
    - `hepatitis.data`: Datos a agrupar.
    - `types.data`: Tipos de atributos (Categorical, Integer, Continuous).

3. Ejecuta el script:
    ```bash
    python script.py
    ```

4. Introduce el valor de K cuando se te solicite.

5. Los resultados se guardarán en la carpeta `analisys` en archivos Excel.

## Estructura de Archivos

- `script.py`: Contiene el código del algoritmo K-Means.
- `dataset/hepatitis.data`: Datos a agrupar.
- `dataset/types.data`: Tipos de atributos.
- `analisys/`: Carpeta donde se guardan los resultados.

## Notas

- Si el valor de K es mayor o igual que la cantidad de datos, el programa mostrará un error y se detendrá.
- Los centroides y clusters se guardarán en archivos Excel en la carpeta `analisys`.

## Ejemplo de Ejecución

```plaintext
____________________ALGORITMO K-MEANS____________________

Por favor, introduce el valor de K: 3
CENTROIDS
   CLASS  AGE  SEX  STEROID  ANTIVIRALS  ...  ALBUMIN  PROTIME  HISTOLOGY
0      2   30    1        1           2  ...      3.5       80          1
1      1   50    2        2           1  ...      4.0       90          2
2      1   40    1        1           1  ...      3.8       85          1

 Cluster 1 
     Cantidad de datos : 50 
     Porcentaje de la BD : 25.0%