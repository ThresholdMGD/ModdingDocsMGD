#!/usr/bin/env python3

import os
import sys
import subprocess
import platform
from pathlib import Path

def print_banner():
    print("=" * 50)
    print("MGD Documentation Universal Build Script")
    print("=" * 50)
    print()

def print_step(step, total, message):
    print(f"[{step}/{total}] {message}")

def print_success(message):
    print(f"✓ {message}")

def print_error(message):
    print(f"⚠ ERROR: {message}", file=sys.stderr)

def print_warning(message):
    print(f"⚠ WARNING: {message}")

def check_python_version():
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 6):
        print_error(f"Python 3.6+ required, found {version.major}.{version.minor}")
        return False
    
    print_success(f"Python {version.major}.{version.minor}.{version.micro} found")
    return True

def check_directory():
    if not Path("mkdocs.yml").exists():
        print_error("mkdocs.yml not found")
        print("Please run this script from the mkDocsMGD root directory")
        return False
    
    if not Path("docs").exists():
        print_error("docs directory not found")
        return False
        
    print_success("Directory structure OK")
    return True

def ensure_pip():
    try:
        import pip
        print_success("pip is available")
        return True
    except ImportError:
        print_warning("pip not found, attempting to install with ensurepip...")
        try:
            import ensurepip
            ensurepip.bootstrap()
            print_success("pip installed via ensurepip")
            return True
        except Exception as e:
            print_error(f"Failed to install pip: {e}")
            print("Try installing pip manually: python -m ensurepip or via your OS package manager.")
            return False

def check_dependencies():
    print_step(2, 4, "Checking dependencies...")
    if not ensure_pip():
        return False
    
    required = [
        "mkdocs",
        "mkdocs-material",
        "mkdocs-macros-plugin",
        "mkdocs-redirects",
        "neoteroi-mkdocs",
        "pyyaml"
    ]
    
    missing = []
    
    for pkg in required:
        try:
            __import__(pkg.replace('-', '_'))
        except ImportError:
            missing.append(pkg)
    
    if missing:
        print_success(f"Installing missing dependencies from requirements.txt...")
        requirements_path = Path("requirements.txt")
        if not requirements_path.exists():
            print_error("requirements.txt not found. Please create it with the required packages.")
            return False
        try:
            subprocess.check_call([
                sys.executable, "-m", "pip", "install", "-r", str(requirements_path)
            ])
            print_success("Dependencies installed from requirements.txt")
        except Exception as e:
            print_error(f"Failed to install dependencies: {e}")
            return False
    else:
        print_success("Dependencies OK")
    
    return True

def generate_navigation():
    if not Path("generate_nav.py").exists():
        print_error("generate_nav.py not found")
        return False
    
    try:
        result = subprocess.run([
            sys.executable, "generate_nav.py"
        ], check=True, capture_output=True, text=True)
        
        # Print the output from generate_nav.py
        print(result.stdout)
        
        print_success("Navigation tree generated")
        return True
        
    except subprocess.CalledProcessError as e:
        print_error("Failed to generate navigation")
        print(f"Error: {e.stderr}")
        return False

def build_documentation():
    try:
        # Run mkdocs using the venv Python
        result = subprocess.run([
            sys.executable, "-m", "mkdocs", "build"
        ], check=True, capture_output=True, text=True)
        print_success("Documentation built successfully")
        return True
    except subprocess.CalledProcessError as e:
        print_error("Failed to build documentation")
        print(f"Error: {e.stderr}")
        return False
    except FileNotFoundError:
        print_error("mkdocs module not found in venv")
        print("Please ensure mkdocs-material is properly installed in mkenv")
        return False

def open_documentation():
    if not Path("site/index.html").exists():
        print_warning("Built site not found")
        return
    
    try:
        response = input("Open documentation in browser? (y/N): ").strip().lower()
        if response in ['y', 'yes']:
            site_path = Path("site/index.html").absolute()
            
            if platform.system() == "Windows":
                os.startfile(site_path)
            elif platform.system() == "Darwin":  # macOS
                subprocess.run(["open", str(site_path)])
            else:  # Linux and others
                subprocess.run(["xdg-open", str(site_path)])
                
            print_success("Opened documentation in browser")
    except KeyboardInterrupt:
        print("\nSkipping browser open")
    except Exception as e:
        print_warning(f"Could not open browser: {e}")

def main():
    print_banner()
    
    # Step 1: Check Python version
    print_step(1, 4, "Checking Python installation...")
    if not check_python_version():
        return 1
    
    # Check directory structure
    if not check_directory():
        return 1
    
    print()
    
    # Step 2: Check dependencies
    print_step(2, 4, "Checking dependencies...")
    if not check_dependencies():
        return 1
    
    print()
    
    # Step 3: Generate navigation
    print_step(3, 4, "Generating navigation tree...")
    if not generate_navigation():
        return 1
    
    print()
    
    # Step 4: Build documentation
    print_step(4, 4, "Building documentation...")
    if not build_documentation():
        return 1
    
    print()
    print_success("Build complete")
    print()
    print("Documentation built successfully in 'site' directory")
    print()
    print("Commands:")
    print("  To serve locally:    mkdocs serve")
    print("  To clean build:      mkdocs build --clean")
    print("  To serve on network: mkdocs serve --dev-addr=0.0.0.0:8000")
    print()
    
    # Optional: open in browser
    open_documentation()
    
    return 0

if __name__ == "__main__":
    try:
        exit_code = main()
        sys.exit(exit_code)
    except KeyboardInterrupt:
        print("\n\nBuild interrupted by user")
        sys.exit(1)
    except Exception as e:
        print_error(f"Unexpected error: {e}")
        sys.exit(1)