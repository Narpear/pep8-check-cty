import subprocess

def check_pep8(filename):
    result = subprocess.run(['pylint', filename], capture_output=True, text=True)
    print(result.stdout)

if __name__ == "__main__":
    import sys
    check_pep8(sys.argv[1])
