import git

def track_changes(directory):
  """
  Tracks the changes to the code in the specified directory using git.

  Args:
    directory: The directory to track changes for.
  """

  # Initialize a git repository in the directory.
  git.init(directory)

  # Add all of the files in the directory to the git repository.
  git.add(directory)

  # Commit the changes to the git repository.
  git.commit("Initial commit")

  # Start tracking changes to the files in the directory.
  git.watch(directory)

def main():
  # Track changes to the code in the current directory.
  track_changes(".")

if __name__ == "__main__":
  main()
