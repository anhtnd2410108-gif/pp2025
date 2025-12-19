import subprocess
import shlex
import sys


def run_command(command):
    try:
        process = subprocess.Popen(
            command,
            shell=True,
            stdin=sys.stdin,
            stdout=sys.stdout,
            stderr=sys.stderr
        )
        process.communicate()
    except Exception as e:
        print("Error:", e)


def shell():
    while True:
        try:
            cmd = input("pysh> ")
            if not cmd.strip():
                continue

            if cmd in ("exit", "quit"):
                break

            run_command(cmd)

        except KeyboardInterrupt:
            print()
        except EOFError:
            break


if __name__ == "__main__":
    shell()
