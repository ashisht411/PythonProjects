import argparse

def count_lines(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            print(f"Line count: {len(lines)}")
    except FileNotFoundError:
        print(f"File not found: {filename}")
    except PermissionError:
        print(f"Permission denied: {filename}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def main():
    parser = argparse.ArgumentParser(description="Counts lines in a file")
    parser.add_argument("filename", help="Path to the file")
    args = parser.parse_args()

    count_lines(args.filename)

if __name__ == "__main__":
    main()
