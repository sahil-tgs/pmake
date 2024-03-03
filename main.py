import json
import os
import subprocess

def read_config(filename):
    """Read configuration from file."""
    with open(filename, 'r') as f:
        config = json.load(f)
    return config

def detect_os():
    """Detect the operating system."""
    return os.name

def check_compiler(compiler):
    """Check if the given compiler is available."""
    try:
        subprocess.run([compiler, '--version'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        return True
    except FileNotFoundError:
        return False
    except subprocess.CalledProcessError:
        return False

def compile_project(source_files, compiler, options):
    """Compile the project using the given compiler and options."""
    compile_command = [compiler] + options + source_files
    subprocess.run(compile_command, check=True)

def main():
    # Read configuration
    config = read_config('config.json')  # Path adjusted for config.json in the main directory

    # Extract settings
    cpp_source_files = config.get('cpp_source_files', [])
    compiler = config.get('compiler', 'g++')
    compiler_options = config.get('compiler_options', [])

    # Detect the operating system
    os_name = detect_os()
    print("Detected OS:", os_name)

    # Choose terminal script based on OS
    if os_name == 'posix':  # Unix-like systems
        terminal_script = 'bash'
    elif os_name == 'nt':   # Windows
        terminal_script = 'cmd'
    else:
        print("Unsupported operating system")
        return

    # Check for the presence of the compiler
    if not check_compiler(compiler):
        print("Compiler not found:", compiler)
        return

    # Compile the C++ source files
    try:
        compile_project(cpp_source_files, compiler, compiler_options)
        print("C++ project compiled successfully.")
    except subprocess.CalledProcessError as e:
        print("Compilation failed:", e)

if __name__ == "__main__":
    main()
