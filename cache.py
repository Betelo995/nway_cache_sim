from math import log2, floor
import random

class cache:
    def __init__(self, cache_capacity, cache_assoc, block_size, repl_policy):
        #Escriba aquí el init de la clase
        self.total_access = 0
        self.total_misses = 0
        self.total_reads = 0
        self.total_read_misses = 0
        self.total_writes = 0
        self.total_write_misses = 0

        self.cache_capacity = int(cache_capacity)
        self.cache_assoc = int(cache_assoc)
        self.block_size = int(block_size)
        self.repl_policy = repl_policy
        
        #Variables extra que vamos a necesitar:
        self.byte_offset_size = log2(self.block_size)
        self.num_sets = int((self.cache_capacity * 1024) / (self.block_size * self.cache_assoc))
        self.index_size = int(log2(self.num_sets))
        self.valid_table = [[False for _ in range(self.cache_assoc)] for _ in range(self.num_sets)]
        self.tag_table = [[0 for _ in range(self.cache_assoc)] for _ in range(self.num_sets)]
        self.repl_table = [[0 for _ in range(self.cache_assoc)] for _ in range(self.num_sets)]
    
    def print_info(self):
        print("Parámetros del caché:")
        print("\tCapacidad:\t\t\t"+str(self.cache_capacity)+"kB")
        print("\tAsociatividad:\t\t\t"+str(self.cache_assoc))
        print("\tTamaño de Bloque:\t\t\t"+str(self.block_size)+"B")
        print("\tPolítica de Reemplazo:\t\t\t"+str(self.repl_policy))

    def print_stats(self):
        print("Resultados de la simulación")
        miss_rate = (100.0*self.total_misses) / self.total_access
        miss_rate = "{:.3f}".format(miss_rate)
        read_miss_rate = (100.0*self.total_read_misses) / self.total_reads
        read_miss_rate = "{:.3f}".format(read_miss_rate)
        write_miss_rate = (100.0*self.total_write_misses) / self.total_writes
        write_miss_rate = "{:.3f}".format(write_miss_rate)
        result_str = str(self.total_misses)+","+miss_rate+"%,"+str(self.total_read_misses)+","
        result_str += read_miss_rate+"%,"+str(self.total_write_misses)+","+write_miss_rate+"%"
        print(result_str)

    def access(self, mode, address):
        #Se calculan las variables para buscar en el caché
        index = int(floor(address / (2 ** self.byte_offset_size)) % (2 ** self.index_size))
        tag = int(floor(address / (2 ** (self.byte_offset_size + self.index_size))))
        #Se accede al caché
        cache_index = self.find_in_cache(index, tag)
        #Se suma acceso ya que se ingresa al caché
        self.total_access += 1
        
        #Comportamiento basado en si se encontró el dato en el caché o no se encontró
        if cache_index == False:
            self.upload_to_cache(index, tag)
            self.total_misses += 1
            if mode == "r":
                self.total_read_misses += 1
            else:
                self.total_write_misses += 1
        else:
            if mode == "r":
                self.total_reads += 1
            else:
                self.total_writes += 1

    #Función extra que busca dentro del caché si se encuentra el dato por medio del
    #index y del tag
    def find_in_cache(self, index, tag):
        for i in range(self.cache_assoc):
            if self.valid_table[index][i] and (self.tag_table[index][i] == tag):
                return True
        return False

    #Función que permite cargar a caché cuando no se encuentra el dato
    def upload_to_cache(self, index, tag):
        #Verificamos que haya espacio en el caché
        if False in self.valid_table[index]:
            empty_space = self.valid_table[index].index(False)
            self.valid_table[index][empty_space] = True
            self.tag_table[index][empty_space] = tag
            self.repl_table[index][empty_space] = max(max(self.repl_table[index])+1, 1)
        
        #En caso de que el caché se encuentre lleno:
        else:
            #Si la política es LRU
            if self.repl_policy == "l":
                min_repl = min(self.repl_table[index])
                lru_slot = self.repl_table[index].index(min_repl)
                self.tag_table[index][lru_slot] = tag
                self.repl_table[index][lru_slot] = max(max(self.repl_table[index]) + 1, 1)
            
            #Si la política es random
            elif self.repl_policy == 'r':
                random_slot = random.randint(0, self.cache_assoc - 1)
                self.tag_table[index][random_slot] = tag
                self.repl_table[index][random_slot] = max(max(self.repl_table[index]) + 1, 1)

