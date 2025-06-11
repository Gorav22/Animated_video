import subprocess
import tempfile
import os
import shutil
from mcp.server.fastmcp import FastMCP

mcp = FastMCP()

MANIM_EXECUTABLE_PATH = os.getenv("MANIM_EXECUTABLE", "manim")

print(MANIM_EXECUTABLE_PATH)

BASE_DIR = os.path.join(os.path.dirname(__file__), "media")
os.makedirs(BASE_DIR, exist_ok=True)

@mcp.tool()
def manin_executable_code(manim_code: str ) -> str:
    """
        This function take the manim_code and then run it in the file named manim_code.py
        The output will be saved in the media directory and the path to the file will be returned.
    """

    tempDir = os.path.join(BASE_DIR, "temp")
    os.makedirs(tempDir, exist_ok=True)
    file_path = os.path.join(tempDir, "manim_code.py")

    try:
        with open(file_path, "w") as f:
            f.write(manim_code)

        # Run the manim command
        result = subprocess.run(
            [MANIM_EXECUTABLE_PATH, "-p", file_path],
            capture_output=True,
            text=True,
            cwd=tempDir,
        )

        if result.returncode == 0:
            # Find the output file in the media directory
            media_dir = os.path.join(BASE_DIR, "media")
            output_files = os.listdir(media_dir)
            if output_files:
                # Assuming the first file is the one we want
                output_file = os.path.join(media_dir, output_files[0])
                return output_file
            else:
                return "No output files found."
        else:
            return f"Error: {result.stderr}"
    except Exception as e:
        return f"An error occurred: {str(e)}"


@mcp.tool()
def clean_manim_media(directory: str) -> str:
    """
        This function will clean the media directory.
    """
    try:
        if os.path.exists(directory):
            shutil.rmtree(directory)
            return "Media directory cleaned."
        else:
            return "Media directory does not exist."
    except Exception as e:
        return f"An error occurred: {str(e)}"
    
@mcp.prompt()
def manim_prompt(prompt: str) -> str:
    """
        This function will take a prompt and return the manim code.
    """
    main_prompt = f"""
    You are a pro manim developer, where your task is to make sure that the code you generate is correct and it will run without any errors and will be generated according to what the user want. The prompt that he is giving you is: {prompt}.
    You will return the code in a code block with the language manim.
    """
    return main_prompt


if __name__ == "__main__":
    mcp.run(transport="stdio")