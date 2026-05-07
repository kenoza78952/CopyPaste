import os
import sys

def setup_output_directory(directory="output"):
    if not os.path.exists(directory):
        os.makedirs(directory)
    return directory

def collect_code_from_directory(root_dir, extensions):
    collected_files = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            ext = os.path.splitext(filename)[1].lower()
            if ext in extensions:
                full_path = os.path.join(dirpath, filename)
                try:
                    with open(full_path, "r", encoding="utf-8") as f:
                        content = f.read()
                    collected_files.append((full_path, content))
                except Exception as e:
                    print(f"Error reading file {full_path}: {e}")
    return collected_files

def save_collected_code(collected_files, output_path):
    with open(output_path, "w", encoding="utf-8") as out_file:
        for file_path, content in collected_files:
            out_file.write(f"\n=== File: {file_path} ===\n")
            out_file.write(content)
            out_file.write("\n" + "=" * 80 + "\n")
    print(f"Collected code saved to: {output_path}")

def main():
    default_extensions = [
        ".py", ".js", ".css", ".html", ".htm", ".json", ".xml", ".java",
        ".c", ".cpp", ".cs", ".php", ".rb", ".sh", ".go", ".ts", ".sql",
        ".pl", ".swift", ".kt", ".r", ".m", ".vb", ".scala", ".lua",
        ".dart", ".hs", ".erl", ".ex", ".exs", ".clj", ".coffee"
    ]
    
    base_dir = None
    extensions = []
    
    if len(sys.argv) == 1:
        base_dir = os.getcwd()
        extensions = default_extensions
    else:
        if os.path.isdir(sys.argv[1]):
            base_dir = sys.argv[1]
            if len(sys.argv) > 2:
                extensions = sys.argv[2:]
            else:
                extensions = default_extensions
        else:
            base_dir = os.getcwd()
            extensions = sys.argv[1:]
    
    normalized_exts = []
    for ext in extensions:
        if not ext.startswith('.'):
            ext = '.' + ext
        normalized_exts.append(ext.lower())
    
    print(f"Collecting code from base directory: {base_dir}")
    print(f"Looking for files with extensions: {', '.join(normalized_exts)}")
    
    collected_files = collect_code_from_directory(base_dir, normalized_exts)
    print(f"Found {len(collected_files)} file(s) matching the criteria.")
    
    output_dir = setup_output_directory("output")
    base_name = os.path.basename(os.path.normpath(base_dir))
    output_filename = f"{base_name}_fulldata.txt"
    output_path = os.path.join(output_dir, output_filename)
    
    save_collected_code(collected_files, output_path)

if __name__ == "__main__":
    main()
