


def hello_world():
    print("Hello world!")


def do_work():
    import sys
    import subprocess
    
    subprocess.run(f"python ./app/workers/load_to_db_worker.py {sys.argv[1]} {sys.argv[2]}", shell=True)


if __name__ == "__main__":
    print("waking up worker!")
    do_work()
    
