import subprocess
import time
import os
def runScripts():
    for file in os.listdir("."):
        if file.endswith("test.py"):
            start = time.time()
            th = subprocess.check_output(["python "+file+" > "+ file+".txt"],shell=True)#(["python", os.path.join(".", file)],stdout=subprocess.PIPE,shell=True)
            #print(th)
            print("It took", time.time() - start, "to run", file)


if __name__ == "__main__":

        runScripts()

