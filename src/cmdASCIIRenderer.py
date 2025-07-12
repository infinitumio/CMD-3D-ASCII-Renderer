"""
3D ASCII Cube Renderer for Windows Command Prompt
================================================

A real-time 3D wireframe cube renderer built specifically for Windows Command Prompt.
Demonstrates 3D graphics using pure ASCII characters and Python standard library.

Features:
- Real-time 3D rendering at 60 FPS in CMD.EXE
- WASD movement with Q/E rotation controls
- Anti-flicker ANSI escape sequence optimization
- Windows msvcrt keyboard handling for responsiveness
- Pure ASCII wireframe graphics with depth perception

License: MIT
Platform: Windows Command Prompt (CMD.EXE)
"""

import math
import os
import sys
import time
import threading
from dataclasses import dataclass
from typing import List, Tuple

try:
    import msvcrt
except ImportError:
    import termios
    import tty
    import select

@dataclass
class Vector3:
    x: float
    y: float
    z: float
    
    def __add__(self, other):
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other):
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __mul__(self, scalar):
        return Vector3(self.x * scalar, self.y * scalar, self.z * scalar)

class SimpleRenderer:
    def __init__(self, width=80, height=24):
        self.width = width
        self.height = height
        self.buffer = [[' ' for _ in range(width)] for _ in range(height)]
        
    def clear(self):
        for y in range(self.height):
            for x in range(self.width):
                self.buffer[y][x] = ' '
    
    def draw_pixel(self, x: int, y: int, char: str):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.buffer[y][x] = char
    
    def draw_simple_cube(self, camera_pos: Vector3, camera_yaw: float, cube_rotation: float = 0.0):
        """Draw a full 3D cube using basic projection with rotation"""
        cube_center = Vector3(0, 1, 0)
        size = 2.0
        half_size = size / 2
        
        # All 8 vertices of the cube
        vertices = [
            Vector3(-half_size, -half_size, -half_size),  # 0: front-bottom-left
            Vector3(half_size, -half_size, -half_size),   # 1: front-bottom-right
            Vector3(half_size, half_size, -half_size),    # 2: front-top-right
            Vector3(-half_size, half_size, -half_size),   # 3: front-top-left
            Vector3(-half_size, -half_size, half_size),   # 4: back-bottom-left
            Vector3(half_size, -half_size, half_size),    # 5: back-bottom-right
            Vector3(half_size, half_size, half_size),     # 6: back-top-right
            Vector3(-half_size, half_size, half_size),    # 7: back-top-left
        ]
        
        # Apply cube rotation first
        cos_cube = math.cos(cube_rotation)
        sin_cube = math.sin(cube_rotation)
        
        rotated_vertices = []
        for vertex in vertices:
            # Rotate around Y-axis
            rotated_x = vertex.x * cos_cube - vertex.z * sin_cube
            rotated_z = vertex.x * sin_cube + vertex.z * cos_cube
            rotated_vertices.append(Vector3(rotated_x, vertex.y, rotated_z))
        
        # Project vertices with camera rotation
        projected = []
        for vertex in rotated_vertices:
            world_pos = vertex + cube_center
            relative = world_pos - camera_pos
            
            # Apply camera rotation (yaw only for simplicity)
            cos_yaw = math.cos(-camera_yaw)
            sin_yaw = math.sin(-camera_yaw)
            rotated_x = relative.x * cos_yaw - relative.z * sin_yaw
            rotated_z = relative.x * sin_yaw + relative.z * cos_yaw
            
            # Simple projection
            if rotated_z > 0.1:  # In front of camera
                scale = 20.0 / rotated_z
                screen_x = int(rotated_x * scale + self.width / 2)
                screen_y = int(-relative.y * scale + self.height / 2)
                projected.append((screen_x, screen_y))
            else:
                projected.append(None)
        
        # Define all edges of the cube with different characters
        edges = [
            # Front face
            (0, 1, '#'), (1, 2, '#'), (2, 3, '#'), (3, 0, '#'),
            # Back face
            (4, 5, '#'), (5, 6, '#'), (6, 7, '#'), (7, 4, '#'),
            # Connecting edges
            (0, 4, '*'), (1, 5, '*'), (2, 6, '*'), (3, 7, '*'),
        ]
        
        # Draw edges
        for start, end, char in edges:
            if projected[start] and projected[end]:
                self.draw_line(projected[start], projected[end], char)
    
    def draw_line(self, p1, p2, char):
        """Simple line drawing"""
        x1, y1 = p1
        x2, y2 = p2
        
        # Simple line algorithm
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        sx = 1 if x1 < x2 else -1
        sy = 1 if y1 < y2 else -1
        err = dx - dy
        
        x, y = x1, y1
        while True:
            self.draw_pixel(x, y, char)
            if x == x2 and y == y2:
                break
            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x += sx
            if e2 < dx:
                err += dx
                y += sy
    
    def draw_simple_floor(self, camera_pos: Vector3, camera_yaw: float):
        """Draw a simple floor with camera rotation"""
        # Draw a grid floor
        for i in range(-10, 11, 4):
            # Lines parallel to X-axis
            start = Vector3(-10, 0, i) - camera_pos
            end = Vector3(10, 0, i) - camera_pos
            
            # Apply camera rotation
            cos_yaw = math.cos(-camera_yaw)
            sin_yaw = math.sin(-camera_yaw)
            
            start_x = start.x * cos_yaw - start.z * sin_yaw
            start_z = start.x * sin_yaw + start.z * cos_yaw
            end_x = end.x * cos_yaw - end.z * sin_yaw
            end_z = end.x * sin_yaw + end.z * cos_yaw
            
            if start_z > 0.1 and end_z > 0.1:
                scale_start = 20.0 / start_z
                scale_end = 20.0 / end_z
                
                x1 = int(start_x * scale_start + self.width / 2)
                y1 = int(-start.y * scale_start + self.height / 2)
                x2 = int(end_x * scale_end + self.width / 2)
                y2 = int(-end.y * scale_end + self.height / 2)
                
                self.draw_line((x1, y1), (x2, y2), '|')
            
            # Lines parallel to Z-axis
            start = Vector3(i, 0, -10) - camera_pos
            end = Vector3(i, 0, 10) - camera_pos
            
            start_x = start.x * cos_yaw - start.z * sin_yaw
            start_z = start.x * sin_yaw + start.z * cos_yaw
            end_x = end.x * cos_yaw - end.z * sin_yaw
            end_z = end.x * sin_yaw + end.z * cos_yaw
            
            if start_z > 0.1 and end_z > 0.1:
                scale_start = 20.0 / start_z
                scale_end = 20.0 / end_z
                
                x1 = int(start_x * scale_start + self.width / 2)
                y1 = int(-start.y * scale_start + self.height / 2)
                x2 = int(end_x * scale_end + self.width / 2)
                y2 = int(-end.y * scale_end + self.height / 2)
                
                self.draw_line((x1, y1), (x2, y2), '|')
    
    def render(self):
        # Move cursor to top-left and hide cursor
        print('\033[H\033[?25l', end='')
        for row in self.buffer:
            print(''.join(row))
        # Show cursor again
        print('\033[?25h', end='', flush=True)

class DebugGame:
    def __init__(self):
        self.renderer = SimpleRenderer()
        self.camera_pos = Vector3(0, 3, -8)
        self.camera_yaw = 0.0  # Rotation around Y-axis
        self.cube_rotation = 0.0  # Cube's own rotation
        self.running = True
        self.keys_pressed = set()
        self.animation_paused = False
        
    def input_thread(self):
        while self.running:
            if os.name == 'nt':
                if msvcrt.kbhit():
                    key = msvcrt.getch().decode('utf-8').lower()
                    if key == 'x' or key == '\x1b':
                        self.running = False
                    elif key == 'p':
                        # Toggle pause/play animation
                        self.animation_paused = not self.animation_paused
                    elif key == 'w':
                        # Move backward (inverted)
                        self.camera_pos.x -= math.sin(self.camera_yaw) * 0.5
                        self.camera_pos.z += math.cos(self.camera_yaw) * 0.5
                    elif key == 's':
                        # Move forward (inverted)
                        self.camera_pos.x += math.sin(self.camera_yaw) * 0.5
                        self.camera_pos.z -= math.cos(self.camera_yaw) * 0.5
                    elif key == 'a':
                        # Strafe left
                        self.camera_pos.x -= math.cos(self.camera_yaw) * 0.5
                        self.camera_pos.z -= math.sin(self.camera_yaw) * 0.5
                    elif key == 'd':
                        # Strafe right
                        self.camera_pos.x += math.cos(self.camera_yaw) * 0.5
                        self.camera_pos.z += math.sin(self.camera_yaw) * 0.5
                    elif key == 'q':
                        # Turn left (7.5 degrees)
                        self.camera_yaw -= math.pi / 24
                    elif key == 'e':
                        # Turn right (7.5 degrees)
                        self.camera_yaw += math.pi / 24
                    elif key == ' ':
                        self.camera_pos.y += 0.5
                    elif key == 'c':
                        self.camera_pos.y -= 0.5
            time.sleep(0.01)
    
    def run(self):
        # Show ASCII art banner
        print()
        print("  ██████╗███╗   ███╗██████╗      ██████╗ ██████╗ ")
        print(" ██╔════╝████╗ ████║██╔══██╗     ╚════██╗██╔══██╗")
        print(" ██║     ██╔████╔██║██║  ██║█████╗ ███╔═╝██║  ██║")
        print(" ██║     ██║╚██╔╝██║██║  ██║╚════╝ ╚══██╗██║  ██║")
        print(" ╚██████╗██║ ╚═╝ ██║██████╔╝     ██████╔╝██████╔╝")
        print("  ╚═════╝╚═╝     ╚═╝╚═════╝      ╚═════╝ ╚═════╝ ")
        print()
        print("        Command Prompt 3D ASCII Renderer")
        print("          Real-time 3D graphics in CMD!")
        print()
        print("Controls: WASD=Move, QE=Turn, Space/C=Up/Down, X=Exit")
        print("Starting...")
        time.sleep(3)
        
        # Clear screen once at start and set up terminal
        os.system('cls' if os.name == 'nt' else 'clear')
        print('\033[?25l', end='')  # Hide cursor
        
        input_thread = threading.Thread(target=self.input_thread, daemon=True)
        input_thread.start()
        
        try:
            while self.running:
                self.renderer.clear()
                
                # Draw simple floor
                self.renderer.draw_simple_floor(self.camera_pos, self.camera_yaw)
                
                # Draw 3D cube
                self.renderer.draw_simple_cube(self.camera_pos, self.camera_yaw)
                
                # Add debug info
                info = f"Pos: ({self.camera_pos.x:.1f}, {self.camera_pos.y:.1f}, {self.camera_pos.z:.1f}) Yaw: {math.degrees(self.camera_yaw):.0f}°"
                for i, char in enumerate(info):
                    if i < self.renderer.width:
                        self.renderer.buffer[0][i] = char
                
                # Add controls info
                controls = "WASD=Move, QE=Turn, Space/C=Up/Down, X=Exit"
                for i, char in enumerate(controls):
                    if i < self.renderer.width:
                        self.renderer.buffer[1][i] = char
                
                self.renderer.render()
                time.sleep(1/60)  # 60 FPS
        finally:
            print('\033[?25h', end='')  # Show cursor again
        
        print("Game ended!")

if __name__ == "__main__":
    try:
        game = DebugGame()
        game.run()
    except KeyboardInterrupt:
        print("\nGame interrupted.")
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
