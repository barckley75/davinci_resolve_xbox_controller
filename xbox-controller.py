import pygame
import time
import subprocess
from threading import Thread

class XboxController:
    def __init__(self):
        pygame.init()
        pygame.joystick.init()
        
        self.deadzone = 0.2
        self.running = True
        self.last_keystroke_time = 0
        self.keystroke_delay = 0.2
        self.current_direction = None
        
        self.setup_controller()

    def setup_controller(self):
        if pygame.joystick.get_count() == 0:
            print("No controllers found!")
            return False
            
        self.controller = pygame.joystick.Joystick(0)
        self.controller.init()
        print(f"Connected to: {self.controller.get_name()}")
        return True

    def send_keystroke(self, key):
        """Send keystroke using AppleScript"""
        cmd = f'''osascript -e 'tell application "System Events" to key code {key}' '''
        subprocess.run(cmd, shell=True)

    def send_keystroke_with_modifier(self, key, modifier):
        """Send keystroke with modifier using AppleScript"""
        cmd = f'''osascript -e 'tell application "System Events" to keystroke "{key}" using {modifier} down' '''
        subprocess.run(cmd, shell=True)

    def handle_button_event(self, event):
        if event.type == pygame.JOYBUTTONDOWN:
            button = event.button
            
            # Map buttons to macOS key codes
            if button == 0:    # A Button - Space
                self.send_keystroke(49)
            elif button == 1:  # B Button - Shift+Delete
                cmd = '''osascript -e 'tell application "System Events" to key code 51 using {shift down}' '''
                subprocess.run(cmd, shell=True)
            elif button == 2:  # X Button - Command+Z
                self.send_keystroke_with_modifier("z", "command")
            elif button == 3:  # Y Button - Y
                self.send_keystroke(16)
            elif button == 7:  # Right Shoulder - Shift+Delete
                cmd = '''osascript -e 'tell application "System Events" to key code 51 using {shift down}' '''
                subprocess.run(cmd, shell=True)
            elif button == 9:  # Left Trigger - I
                self.send_keystroke(34)
            elif button == 10: # Right Trigger - O
                self.send_keystroke(31)
            elif button == 11: # Left Menu - Up Arrow
                self.send_keystroke(126)
            elif button == 12: # Right Menu - Down Arrow
                self.send_keystroke(125)
            elif button == 13: # D-pad Left - [
                self.send_keystroke(33)
            elif button == 14: # D-pad Right - ]
                self.send_keystroke(30)

    def handle_axis_event(self, event):
        current_time = time.time()
        value = event.value
            
        # Apply deadzone
        if abs(value) < self.deadzone:
            if event.axis in [0, 2, 3]:
                self.current_direction = None
            return
        
        if current_time - self.last_keystroke_time >= self.keystroke_delay:
            if event.axis == 0:  # Left stick horizontal - J/L
                if value > 0:
                    new_direction = 'right'
                    keystroke = 37  # L key
                else:
                    new_direction = 'left'
                    keystroke = 38  # J key
                    
                if new_direction != self.current_direction:
                    self.send_keystroke(keystroke)
                    self.last_keystroke_time = current_time
                    self.current_direction = new_direction
                    
            elif event.axis == 2:  # Right stick horizontal - Left/Right Arrow
                if value > 0:
                    self.send_keystroke(124)  # Right Arrow
                else:
                    self.send_keystroke(123)  # Left Arrow
                self.last_keystroke_time = current_time
                    
            elif event.axis == 3:  # Right stick vertical - K/Y
                if value > 0:
                    new_direction = 'down'
                    keystroke = 40  # K key
                else:
                    new_direction = 'up'
                    keystroke = 40  # K key
                    
                if new_direction != self.current_direction:
                    self.send_keystroke(keystroke)
                    self.last_keystroke_time = current_time
                    self.current_direction = new_direction

    def main_loop(self):
        if not hasattr(self, 'controller'):
            print("No controller connected!")
            return
            
        print("Controller active! Press Ctrl+C to stop.")
        
        try:
            while self.running:
                for event in pygame.event.get():
                    if event.type == pygame.JOYAXISMOTION:
                        self.handle_axis_event(event)
                    elif event.type in [pygame.JOYBUTTONDOWN, pygame.JOYBUTTONUP]:
                        self.handle_button_event(event)
                time.sleep(0.01)
                
        except KeyboardInterrupt:
            print("\nStopping controller input...")
            
        finally:
            self.running = False
            pygame.quit()

if __name__ == "__main__":
    controller = XboxController()
    controller.main_loop()