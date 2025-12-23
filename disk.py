def fcfs(requests, head):
    total = 0
    current = head

    for r in requests:
        total += abs(current - r)
        current = r

    print("FCFS Total Head Movement =", total)

requests = [82, 170, 43, 140, 24, 16, 190]
head = 50
disk_size = 200

fcfs(requests, head)

def scan(requests, head, disk_size):
    left = [r for r in requests if r < head]
    right = [r for r in requests if r >= head]

    left.sort(reverse=True)
    right.sort()

    total = 0
    current = head

    # Move right first
    for r in right:
        total += abs(current - r)
        current = r

    # Go to end of disk
    total += abs(current - (disk_size - 1))
    current = disk_size - 1

    # Move left
    for r in left:
        total += abs(current - r)
        current = r

    print("SCAN Total Head Movement =", total)



def cscan(requests, head, disk_size):
    left = [r for r in requests if r < head]
    right = [r for r in requests if r >= head]

    left.sort()
    right.sort()

    total = 0
    current = head

    # Move right first
    for r in right:
        total += abs(current - r)
        current = r

    # Jump from end → start (no cost)
    total += abs(current - (disk_size - 1))
    current = 0

    # Move from start again
    for r in left:
        total += abs(current - r)
        current = r

    print("CSCAN Total Head Movement =", total)



def look(requests, head):
    left = [r for r in requests if r < head]
    right = [r for r in requests if r >= head]

    left.sort(reverse=True)
    right.sort()

    total = 0
    current = head

    # Move right only until last right request
    for r in right:
        total += abs(current - r)
        current = r

    # Then move left until last left request
    for r in left:
        total += abs(current - r)
        current = r

    print("LOOK Total Head Movement =", total)
