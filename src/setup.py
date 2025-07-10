#!/usr/bin/env python3
"""
Setup script for Command Prompt 3D ASCII Renderer
Verifies Python version and Windows Command Prompt compatibility
"""

import sys
import platform

def check_python_version():
    """Check if Python version is compatible"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 7):
        print("❌ Error: Python 3.7 or higher is required")
        print(f"Current version: {version.major}.{version.minor}.{version.micro}")
        print("Please upgrade Python and try again.")
        return False
    
    print(f"✅ Python {version.major}.{version.minor}.{version.micro} - Compatible")
    return True

def check_platform():
    """Check platform and Command Prompt compatibility"""
    system = platform.system()
    print(f"🖥️  Platform: {system}")
    
    if system == "Windows":
        try:
            import msvcrt
            print("✅ Windows Command Prompt input (msvcrt) - Available")
            print("🎯 Optimized for Windows CMD.EXE")
        except ImportError:
            print("❌ Windows Command Prompt input (msvcrt) - Not available")
            return False
    else:
        print("⚠️  Warning: This renderer is optimized for Windows Command Prompt")
        print("   Fallback terminal support available but limited")
        try:
            import termios
            import tty
            print("✅ Basic terminal control (termios/tty) - Available")
        except ImportError:
            print("❌ Basic terminal control (termios/tty) - Not available")
            return False
    
    return True

def check_required_modules():
    """Check if all required standard library modules are available"""
    required_modules = [
        'math', 'os', 'sys', 'time', 'threading', 
        'dataclasses', 'typing'
    ]
    
    missing_modules = []
    for module in required_modules:
        try:
            __import__(module)
            print(f"✅ {module} - Available")
        except ImportError:
            print(f"❌ {module} - Missing")
            missing_modules.append(module)
    
    if missing_modules:
        print(f"❌ Missing required modules: {', '.join(missing_modules)}")
        return False
    
    return True

def main():
    """Main setup verification"""
    print("🖥️ Command Prompt 3D ASCII Renderer - Setup Check")
    print("=" * 55)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    print()
    
    # Check platform compatibility
    if not check_platform():
        sys.exit(1)
    
    print()
    
    # Check required modules
    if not check_required_modules():
        sys.exit(1)
    
    print()
    print("🎉 All checks passed! You're ready to run the Command Prompt 3D renderer.")
    print()
    print("To start the Command Prompt 3D ASCII Renderer, run:")
    print("  python cmdASCIIRenderer.py")
    print("  OR")
    print("  start.bat")
    print()
    print("Controls:")
    print("  WASD - Move around")
    print("  QE   - Turn left/right") 
    print("  Space/C - Move up/down")
    print("  X    - Exit")
    print()
    print("Have fun with 3D graphics in Command Prompt! 🖥️🚀")

if __name__ == "__main__":
    main()
