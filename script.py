import subprocess

def run_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    return output.decode("utf-8"), error.decode("utf-8")

def run_tests():
    traces = ["400.perlbench-41B","454.calculix-104B", "401.bzip2-226B", 
              "456.hmmer-191B", "403.gcc-16B", "458.sjeng-1088B", 
              "410.bwaves-1963B", "459.GemsFDTD-1169B", "416.gamess-875B", 
              "462.libquantum-1343B", "429.mcf-184B", "464.h264ref-30B", 
              "433.milc-127B", "465.tonto-1769B", "435.gromacs-111B", 
              "470.lbm-1274B", "436.cactusADM-1804B", "471.omnetpp-188B", 
              "437.leslie3d-134B", "473.astar-153B", "444.namd-120B", 
              "481.wrf-1170B", "445.gobmk-17B", "482.sphinx3-1100B", 
              "450.soplex-247B", "483.xalancbmk-127B", "453.povray-887B"]
    
    # Test 1: Altering the size of the cache
    cache_sizes = [8, 16, 32, 64, 128]
    assoc = 8
    block_size = 64
    repl_policy = "l"
    
    print("Running Test 1: Altering the size of the cache")
    test1_results = []
    for size in cache_sizes:
        command = f"python3 cache_sim.py -s {size} -a {assoc} -b {block_size} -r {repl_policy}"
        test_results = []
        for trace in traces:
            full_command = command + f" -t /home/isaacrojas/Documents/Estructuras/Tarea_IV/traces/{trace}.trace.txt.gz"
            output, _ = run_command(full_command)
            test_results.append(f"Cache Size: {size}\n"
                                f"Associativity: {assoc}\n"
                                f"Block Size: {block_size}\n"
                                f"Replacement Policy: {repl_policy}\n"
                                f"Trace: {trace}\n"
                                f"{output}\n")
        test1_results.append("\n".join(test_results))
    
    # Save Test 1 results to file
    save_results(test1_results, "test1_results.txt")
    
    # Test 2: Changing associativity
    cache_capacity = 32
    associativities = [1, 2, 4, 8, 16]
    
    print("Running Test 2: Changing associativity")
    test2_results = []
    for assoc in associativities:
        command = f"python3 cache_sim.py -s {cache_capacity} -a {assoc} -b {block_size} -r {repl_policy}"
        test_results = []
        for trace in traces:
            full_command = command + f" -t /home/isaacrojas/Documents/Estructuras/Tarea_IV/traces/{trace}.trace.txt.gz"
            output, _ = run_command(full_command)
            test_results.append(f"Cache Size: {cache_capacity}\n"
                                f"Associativity: {assoc}\n"
                                f"Block Size: {block_size}\n"
                                f"Replacement Policy: {repl_policy}\n"
                                f"Trace: {trace}\n"
                                f"{output}\n")
        test2_results.append("\n".join(test_results))
    
    # Save Test 2 results to file
    save_results(test2_results, "test2_results.txt")
    
    # Test 3: Changing block size
    block_sizes = [16, 32, 64, 128]
    
    print("Running Test 3: Changing block size")
    test3_results = []
    for block_size in block_sizes:
        command = f"python3 cache_sim.py -s {cache_capacity} -a {assoc} -b {block_size} -r {repl_policy}"
        test_results = []
        for trace in traces:
            full_command = command + f" -t /home/isaacrojas/Documents/Estructuras/Tarea_IV/traces/{trace}.trace.txt.gz"
            output, _ = run_command(full_command)
            test_results.append(f"Cache Size: {cache_capacity}\n"
                                f"Associativity: {assoc}\n"
                                f"Block Size: {block_size}\n"
                                f"Replacement Policy: {repl_policy}\n"
                                f"Trace: {trace}\n"
                                f"{output}\n")
        test3_results.append("\n".join(test_results))
    
    # Save Test 3 results to file
    save_results(test3_results, "test3_results.txt")
    
    # Test 4: Changing replacement policy
    repl_policies = ["l", "r"]
    assoc = 8
    block_size = 64
    print("Running Test 4: Changing replacement policy")
    test4_results = []
    for policy in repl_policies:
        command = f"python3 cache_sim.py -s {cache_capacity} -a {assoc} -b {block_size} -r {policy}"
        test_results = []
        for trace in traces:
            full_command = command + f" -t /home/isaacrojas/Documents/Estructuras/Tarea_IV/traces/{trace}.trace.txt.gz"
            output, _ = run_command(full_command)
            test_results.append(f"Cache Size: {cache_capacity}\n"
                                f"Associativity: {assoc}\n"
                                f"Block Size: {block_size}\n"
                                f"Replacement Policy: {policy}\n"
                                f"Trace: {trace}\n"
                                f"{output}\n")
        test4_results.append("\n".join(test_results))
    
    # Save Test 4 results to file
    save_results(test4_results, "test4_results.txt")

def save_results(results, filename):
    with open(filename, "w") as file:
        file.write("\n\n\n\n".join(results))

if __name__ == "__main__":
    run_tests()
