import os
import subprocess

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

def parse_makefile(filename):
    """Parse the Makefile to extract source files."""
    src_files = []
    with open(filename, 'r') as f:
        for line in f:
            if line.startswith('SRC'):
                src_files.extend(line.strip().split('=')[1].split())
    return src_files

def compile_project(source_files, compiler, options):
    """Compile the project using the given compiler and options."""
    compile_command = [compiler] + options + source_files
    subprocess.run(compile_command, check=True)

def main():
    # Detect the operating system
    os_name = detect_os()
    print("Detected OS:", os_name)

    # Choose compiler based on OS
    if os_name == 'posix':  # Unix-like systems
        compiler = 'g++'
    elif os_name == 'nt':   # Windows
        compiler = 'g++'  # Adjust if using a different compiler on Windows
    else:
        print("Unsupported operating system")
        return

    # Check for the presence of the compiler
    if not check_compiler(compiler):
        print("Compiler not found:", compiler)
        return

    # Parse the Makefile to extract source files
    makefile = 'Makefile'
    if not os.path.exists(makefile):
        print(f"{makefile} not found")
        return

    source_files = parse_makefile(makefile)

    # Compile the project
    try:
        compile_project(source_files, compiler, ['-std=c++11', '-o', 'output'])
        print("Project compiled successfully.")
    except subprocess.CalledProcessError as e:
        print("Compilation failed:", e)

if __name__ == "__main__":
    main()
