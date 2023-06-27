
# Simulador de Caché

Este programa tiene como intención simular un caché N-Way asociativo, por medio de una implementación en python. El programa utiliza traces en formato 'r' o 'w' + 'dirección' de forma que al final se desplieguen en consola las siguientes estadísticas:
  - Total Misses	
  - Miss Rate Total	
  - Misses Lectura	
  - Miss Rate Lectura	
  - Misses Escritura	
  - Miss Rate Escritura


## Autor

- [@Betelo995](https://github.com/Betelo995)


## Como correr el programa

El programa principal se encuentra en el archivo de simulación `cache_sim.py`, entonces para poder iniciar la simulación se debe correr el siguiente comando:

### Linux
Dentro de la carpeta donde se encuentran los archivos se ejecuta el siguiente comando en la terminal:
```bash
  python3 cache_sim.py -s {size} -a {assoc} -b {block_size} -r {repl_policy} -t {trace_location}
```
La dirección del trace debe ser completa para que haya una ejecución adecuada, de lo contrario el programa podría no encontrar la dirección del archivo y fallar la ejecución.


## Ejemplo de uso

```bash
python3 cache_sim.py -s 32 -a 16 -b 128 -r l -t /home/isaac/Documents/estructurasII/TareaIV/traces/400.perlbench-41B
```
El output del programa sería el siguiente:
```python
Cache Size: 32
Associativity: 16
Block Size: 128
Replacement Policy: l
Trace: 400.perlbench-41B
Resultados de la simulación
268,0.027%,245,0.028%,23,0.021%

```