def MinimumSeats(seats,students):
    return sum(abs(seat-student) for seat,student in zip(sorted(seats),sorted(students)))

print(MinimumSeats([10,5,3], [7,6,4]))