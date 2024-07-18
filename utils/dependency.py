import subprocess
import sys

def check_dependency(dependency):
    try:
        subprocess.check_output(["pip3", "show", dependency])
        print(f"{dependency} is already installed.")
        return True
    except subprocess.CalledProcessError:
        print(f"{dependency} is not installed.")
        return False

def install_dependency(dependency):
    try:
        subprocess.check_output(["pip3", "install", dependency])
        print(f"{dependency} has been installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error installing {dependency}: {e}")

def main():
    dependencies = ["pyqt5"]
    for dependency in dependencies:
        if not check_dependency(dependency):
            install_dependency(dependency)

if __name__ == "__main__":
    main()