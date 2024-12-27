# Xbox Controller to macOS Keyboard Mapper

This Python script allows you to use an Xbox controller as a keyboard input device on macOS. It maps controller buttons and joystick movements to specific keyboard keys and shortcuts, enabling alternative input methods for various applications.

## Features

- Maps Xbox controller buttons to keyboard keys and shortcuts
- Supports analog stick input with customizable deadzone
- Handles modifier keys (Command, Shift) for complex keyboard combinations
- Provides smooth joystick-to-key mapping with anti-repeat protection
- Real-time input processing with minimal latency

## Prerequisites

- Python 3.x
- macOS
- Xbox controller (compatible with pygame)
- Required Python packages:
  ```
  pygame
  ```

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/xbox-controller-mapper.git
   cd xbox-controller-mapper
   ```

2. Install required packages:
   ```bash
   pip install pygame
   ```

## Usage

1. Connect your Xbox controller to your Mac via USB or Bluetooth
2. Run the script:
   ```bash
   python xbox-controller.py
   ```
3. Press Ctrl+C to stop the script

## Button Mappings

| Controller Input | Keyboard Output |
|-----------------|-----------------|
| A Button        | Space           |
| B Button        | Shift + Delete  |
| X Button        | Command + Z     |
| Y Button        | Y              |
| Right Shoulder  | Shift + Delete  |
| Left Trigger    | I              |
| Right Trigger   | O              |
| Left Menu       | Up Arrow       |
| Right Menu      | Down Arrow     |
| D-pad Left      | [              |
| D-pad Right     | ]              |

### Analog Stick Mappings

#### Left Stick
- Left: J key
- Right: L key

#### Right Stick
- Left/Right: Arrow keys
- Up/Down: K key

## Configuration

You can modify the following parameters in the script:

- `deadzone` (default: 0.2): Minimum analog stick movement required for input
- `keystroke_delay` (default: 0.2): Minimum time between repeated keystrokes

## Technical Details

- Uses pygame for controller input detection
- Implements AppleScript for system-level keyboard event simulation
- Includes deadzone protection for analog inputs
- Features thread-safe event handling

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Thanks to the pygame community for the excellent gamepad support
- Inspired by various keyboard mapping tools for macOS

## Troubleshooting

### Common Issues

1. "No controllers found!"
   - Ensure your controller is properly connected
   - Try reconnecting the controller
   - Verify the controller is recognized in macOS System Settings

2. Unresponsive inputs
   - Check the controller battery level
   - Verify the deadzone settings
   - Ensure no other applications are capturing controller input

### Getting Help

If you encounter any issues:
1. Check the existing issues on GitHub
2. Provide detailed information about your setup when reporting new issues
3. Include any relevant error messages or unexpected behavior
