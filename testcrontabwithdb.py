import pandas as pd
import pyodbc
import subprocess
import platform
import time

try:
    cnxn=pyodbc.connect("DRIVER={SQL Server};SERVER=192.168.0.41;PORT=1433;DATABASE=DB_WEB;UID=hary;PWD=1234",autocommit=True)
    cursor=cnxn.cursor()
    print("Koneksi Berhasil")
except:
    print("Koneksi Gagal")
    
    
def run_cron():
    df_data_run=pd.read_sql("select id_job, \
    nama_job, \
    directory, \
    next_running \
    from ms_detail_projek_python where next_running<=CURRENT_TIMESTAMP",cnxn)
    print(df_data_run)

    list_colomn_for_run=[str(value) for value in df_data_run['directory']]
    print(list_colomn_for_run)

    if __name__ == "__main__":
        # List of script paths
        script_paths = list_colomn_for_run

        # Run the scripts in the background
        processes = []
        for path in script_paths:
            if platform.system() == "Windows":
                command = ["start", "python", path]
            else:
                command = ["nohup", "python", path, "&"]
            processes.append(subprocess.Popen(command, shell=True))

        # Wait for all processes to finish
        for process in processes:
            process.wait()

        print("All processes have finished")

for a in range(5):
    run_cron()
    time.sleep(25)