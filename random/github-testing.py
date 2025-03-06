import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from github import Github

# Replace with your GitHub access token
github_token = 

# Initialize the GitHub API client
g = Github(github_token)

# Specify the organization or user
organization_name = 'Planning-Inspectorate'

# Create the main window
root = tk.Tk()
root.title("GitHub Compliance Checker")

# Create a treeview widget to display the results in a table
tree = ttk.Treeview(root, columns=("Repository", "Branch Protection", "CODEOWNERS File Found", "Overall Compliance"))
tree.heading("#1", text="Repository")
tree.heading("#2", text="Branch Protection")
tree.heading("#3", text="CODEOWNERS File Found")
tree.heading("#4", text="Overall Compliance")
tree.pack()

# Function to perform the compliance checks
def perform_compliance_checks():
    # Clear the treeview widget
    for item in tree.get_children():
        tree.delete(item)

    # Get the organization or user
    org_or_user = g.get_organization(organization_name)

    # Loop through repositories in the organization or user
    for repo in org_or_user.get_repos():
        row = [repo.name]

        # Check if CODEOWNERS file exists
        try:
            codeowners_file = repo.get_contents('CODEOWNERS')
            row.append("True")
        except Exception as e:
            row.append("False")

        # Check if branch protection is enabled for the default branch
        default_branch = repo.default_branch
        branch = repo.get_branch(default_branch)
        if branch.protected:
            row.append("True")
        else:
            row.append("False")

        # Calculate Overall Compliance
        overall_compliance = "False" if "False" in row[1:2] else "True"
        row.append(overall_compliance)

        # Insert the row into the treeview
        tree.insert("", "end", values=row)

# Create a button to run the compliance checks
check_button = tk.Button(root, text="Run Compliance Checks", command=perform_compliance_checks)
check_button.pack()

# Run the Tkinter main loop
root.mainloop()
