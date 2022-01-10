import subprocess

def start_server() -> subprocess.Popen:
    args = ["python", "secret_santa\secret_santa\manage.py", "runserver"]
    process = subprocess.Popen(args)
    return process


def terminate_server(process):
    process.terminate()