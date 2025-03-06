import subprocess

# Specify the filename containing the list of branches
branches_file = "../branches.txt"

# Check if the branches file exists
def delete_branches():
    try:
        with open(branches_file, 'r') as f:
            branches = f.readlines()
    except FileNotFoundError:
        print(f"Error: Branches file '{branches_file}' not found.")
        exit(1)

    # Iterate over each branch and delete it
    for branch in branches:
        branch = branch.strip()
        # Skip if it's the current branch
        if not branch.startswith('*'):
            print(f"Deleting branch: {branch}")
            subprocess.run(['git', 'branch', '-d', branch], check=True)

def main():
    delete_branches()

if __name__ == "__main__":
    main()
