from fabric.api import run
from fabric.tasks import execute


def do_something():
    run("echo $RANDOM")

if __name__ == "__main__":
    execute(do_something, hosts=["username@host"])