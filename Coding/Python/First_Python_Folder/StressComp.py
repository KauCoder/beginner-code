# ====================================================
#   Intel i9 MacBook Pro CPU Maximum Stress Test    
# ====================================================

import multiprocessing
import time
import math

def stress_intel_core(core_id):
    """Frees the full pipeline of an Intel core using heavy trigonometry math."""
    x = 0.0001
    while True:
        try:
            # Trig functions like sin/cos pressure the floating-point unit (FPU) heavily
            x = math.sin(x) + math.cos(x)
            if x > 1000.0:
                x = 0.0001
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    print("started")
    
    # This will detect 16 logical cores on your Intel i9
    cpu_cores = multiprocessing.cpu_count()
    processes = []
    
    # Launch a process for every single virtual thread
    for i in range(cpu_cores):
        p = multiprocessing.Process(target=stress_intel_core, args=(i,))
        p.start()
        processes.append(p)
        
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping Intel test...")
        for p in processes:
            p.terminate()
            p.join()