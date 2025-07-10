# Contributing to Command Prompt 3D ASCII Renderer

Thank you for your interest in contributing! This project focuses specifically on creating amazing 3D graphics experiences within the Windows Command Prompt environment.

## 🎯 Project Focus

This project is specifically designed for **Windows Command Prompt (CMD.EXE)**:
- Optimized for `msvcrt` keyboard handling
- Uses ANSI escape sequences for flicker-free rendering
- Designed for monospace fonts and character-based graphics
- Emphasizes performance within command prompt constraints

## 🚀 Getting Started

### Prerequisites
- Python 3.7 or higher
- Windows OS with Command Prompt
- Git
- Text editor or IDE

### Development Setup
1. Fork the repository on GitHub
2. Clone your fork locally:
   ```cmd
   git clone https://github.com/yourusername/command-prompt-3d-renderer.git
   cd command-prompt-3d-renderer
   ```
3. Run the setup check:
   ```cmd
   python setup.py
   ```
4. Test the renderer in Command Prompt:
   ```cmd
   python cmdASCIIRenderer.py
   ```

## 🎯 How to Contribute

### Reporting Bugs
- Use the GitHub issue tracker
- Include your operating system and Python version
- Provide steps to reproduce the bug
- Include any error messages

### Suggesting Features
- Open an issue with the "enhancement" label
- Describe the feature and its benefits
- Provide examples if possible

### Code Contributions

#### Code Style
- Follow PEP 8 Python style guidelines
- Use meaningful variable and function names
- Add docstrings to classes and functions
- Keep functions focused and small

#### Making Changes
1. Create a new branch for your feature:
   ```bash
   git checkout -b feature/your-feature-name
   ```
2. Make your changes
3. Test thoroughly on your platform
4. Commit with clear messages:
   ```bash
   git commit -m "Add feature: description of what you added"
   ```
5. Push to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```
6. Create a Pull Request

## 🎨 Feature Ideas

Here are some ideas for contributions:

### Command Prompt Specific
- Add Windows-specific optimizations
- Improve ANSI escape sequence handling  
- Create better monospace font detection
- Add command prompt theme compatibility

### Medium
- Add color support with Windows console colors
- Implement different 3D shapes optimized for text display
- Add wireframe/solid ASCII rendering toggle
- Create batch file automation tools

### Advanced
- Implement face culling for better performance
- Add lighting simulation
- Create texture mapping with ASCII patterns
- Build a scene editor

## 🧪 Testing

### Manual Testing
- Test primarily in Windows Command Prompt (CMD.EXE)
- Try different command prompt window sizes
- Test with different monospace fonts
- Verify keyboard responsiveness with `msvcrt`
- Test ANSI escape sequence compatibility

### Code Quality
- Ensure no syntax errors
- Check for proper error handling
- Verify cross-platform compatibility
- Test edge cases (very small/large movements)

## 📝 Documentation

When contributing:
- Update README.md if adding new features
- Add inline comments for complex code
- Update this CONTRIBUTING.md if changing development process
- Include examples in docstrings

## ⚡ Performance Guidelines

- Keep frame rate at 60 FPS or higher
- Minimize memory allocations in render loop
- Use efficient algorithms for 3D math
- Profile code for bottlenecks

## 🐛 Debugging Tips

### Common Issues
- **Flickering**: Usually caused by screen clearing methods
- **Input lag**: Check input thread timing
- **Projection errors**: Verify 3D math calculations
- **Platform issues**: Test cross-platform keyboard handling

### Debugging Tools
- Use Python debugger (pdb) for step-through debugging
- Add temporary print statements for values
- Test with simplified scenes
- Use profiling tools for performance analysis

## 📚 Resources

### 3D Graphics
- [3D Computer Graphics](https://en.wikipedia.org/wiki/3D_computer_graphics)
- [Perspective Projection](https://en.wikipedia.org/wiki/3D_projection#Perspective_projection)
- [Line Drawing Algorithms](https://en.wikipedia.org/wiki/Line_drawing_algorithm)

### Python
- [PEP 8 Style Guide](https://pep8.org/)
- [Python Threading](https://docs.python.org/3/library/threading.html)
- [Python Dataclasses](https://docs.python.org/3/library/dataclasses.html)

## 🏆 Recognition

Contributors will be recognized in:
- README.md acknowledgments section
- GitHub contributors list
- Release notes for significant contributions

## 📞 Questions?

If you have questions about contributing:
- Open a GitHub issue with the "question" label
- Check existing issues and discussions
- Review this document and the README

Thank you for helping make 3D ASCII graphics more awesome! 🎮✨
