import subprocess
import sys


def setup():
    process = subprocess.Popen("""/sbin/ip route|awk '/default/{print$3}'""", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    if err.decode('ascii').strip() != "":
        sys.exit(err)
    host = out.decode('ascii').strip()
    create_env_file(host)

    install_docker_compose()
    subprocess.run(to_args("rm ~/.docker/config.json"))
    subprocess.run(to_args("docker-compose up"))


def create_env_file(host: str):
    line = "HOST = " + host
    with open(".env", 'w+') as f:
        f.write(line)
    print(".env created with " + line)


def install_docker_compose():
    process = subprocess.Popen(to_args("docker-compose --version"), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    if "docker-compose" in out.decode('ascii') and "version" in out.decode('ascii'):
        return
    subprocess.run(to_args("""curl -L "https://github.com/docker/compose/releases/download/1.28.3/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose"""))
    subprocess.run(to_args("chmod +x /usr/local/bin/docker-compose"))


def to_args(command: str):
    return command.split(" ")


if __name__ == "__main__":
    setup()