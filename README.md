# Animated video MCP Server


## Overview

This is an MCP (Model Context Protocol) server that executes Manim animation code and returns the generated video. It allows users to send Manim scripts and receive the rendered animation.

## Features

- Executes Manim Python scripts.
- Saves animation output in a visible media folder.
- Allows users to clean up temporary files after execution.
- Portable and configurable via environment variables.

## Installation

### Prerequisites

Ensure you have the following installed:

- Python 3.8+
- Manim (Community Version)
- MCP

### Install Manim

```sh
pip install manim
```

### Install MCP

```sh
pip install mcp
```

### Clone the Repository

```sh
git clone https://github.com/Gorav22/Animated_video.git
cd Animated_video
```

## Integration with Claude

To integrate the Manim MCP server with Claude, add the following to your `claude_desktop_config.json` file:

```json
{
  "mcpServers": {
     "animation-server": {
      "command": "/absolute/path/to/python",
      "args": [
        "/absolute/path/to/manim-mcp-server/src/manim_server.py"
      ],
      "env": {
        "MANIM_EXECUTABLE": "/Path/to/manim/Scripts/manim.exe"
      }
    }
  }
}
```

For cursor, Go to Cursor Settings then MCP then click new a mcp server add this script in mcp.json
```json
{
  "mcpServers": {
     "animation-server": {
      "command": "/absolute/path/to/python",
      "args": [
        "/absolute/path/to/manim-mcp-server/src/manim_server.py"
      ],
      "env": {
        "MANIM_EXECUTABLE": "/Path/to/manim/Scripts/manim.exe"
      }
    }
  }
}
```

### Finding Your Python Path

To find your Python executable path, use the following command:

#### Windows (PowerShell):
```sh
(Get-Command python).Source
```

#### Windows (Command Prompt/Terminal):
```sh
where python
```

#### Linux/macOS (Terminal):
```sh
which python
```

This ensures that Claude can communicate with the Manim MCP server to generate animations dynamically.

## Contributing

1. Fork the repository.
2. Create a new branch:
   ```sh
   git checkout -b add-feature
   ```
3. Make changes and commit:
   ```sh
   git commit -m "Added a new feature"
   ```
4. Push to your fork:
   ```sh
   git push origin add-feature
   ```
5. Open a pull request.

## License

This MCP server is licensed under the MIT License. This means you are free to use, modify, and distribute the software, subject to the terms and conditions of the MIT License. For more details, please see the LICENSE file in the project repository.

## Author

Created by **[Gorav22](https://github.com/Gorav22)**. Contributions welcome! 🚀

