# thank you chatgpt

import os

def generate_directory_list(directory):
    # Get the list of items in the directory, ignoring the ones in the ignore list
    items = [item for item in os.listdir(directory) if item not in ignore_list]
    items.sort()

    # Create an unordered list
    html = '<ul>\n'

    for item in items:
        item_path = os.path.join(directory, item)

        if os.path.isdir(item_path):  # If it's a directory, generate a link to its contents
            html += f'<li><a href="{item}/index.html">{item}</a></li>\n'
            generate_directory_list(item_path)  # Recursively generate the contents of the subdirectory
        else:  # If it's a file, display the file name with a link to the file
            html += f'<li><a href="{item_path}">{item}</a></li>\n'

    html += '</ul>\n'

    # Write the HTML content to a file
    with open(os.path.join(directory, 'index.html'), 'w') as f:
        f.write(html)


def recursively_generate_directory_list(root_directory):
    for root, dirs, files in os.walk(root_directory):
        # Exclude directories or files specified in the ignore list
        dirs[:] = [d for d in dirs if d not in ignore_list]
        files[:] = [f for f in files if f not in ignore_list]

        # Generate the directory list for the current directory
        generate_directory_list(root)


# Set the root directory to the current working directory
root_directory = "."

# List of directories or files to ignore during processing
ignore_list = [".git", "__pycache__", ".ipynb_checkpoints", ".gitignore", "index.html"]

# Generate the directory lists recursively
recursively_generate_directory_list(root_directory)
