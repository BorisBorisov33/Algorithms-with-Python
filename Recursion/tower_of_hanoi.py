def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        # Base case: Move the top disk from the source peg to the destination peg.
        print(f"Move disk 1 from {source} to {destination}")
        return

    # Move n-1 disks from source to auxiliary peg using destination as the auxiliary peg.
    tower_of_hanoi(n - 1, source, destination, auxiliary)

    # Move the largest disk (disk n) from source to destination peg.
    print(f"Move disk {n} from {source} to {destination}")

    # Move the remaining n-1 disks from auxiliary peg to destination peg using source as the auxiliary peg.
    tower_of_hanoi(n - 1, auxiliary, source, destination)


# Test the function for three disks.
tower_of_hanoi(7, 'A', 'B', 'C')
