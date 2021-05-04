import string

def print_rangoli(size):
    characters = string.ascii_lowercase
    lst = []
    width  = 4 * size -3
    i=0
    while i<n:
        s = '-'.join(characters[i:size])
        lst.append((s[::-1] + s[1:]).center(width,'-'))
        i=i+1
    print('\n'.join(lst[:0:-1] + lst))

n = int(input("Enter number to print Rangoli:"))
print_rangoli(n)


#   SAMPLE PATTERN
# Enter number to print Rangoli:8
# --------------h--------------
# ------------h-g-h------------
# ----------h-g-f-g-h----------
# --------h-g-f-e-f-g-h--------
# ------h-g-f-e-d-e-f-g-h------
# ----h-g-f-e-d-c-d-e-f-g-h----
# --h-g-f-e-d-c-b-c-d-e-f-g-h--
# h-g-f-e-d-c-b-a-b-c-d-e-f-g-h
# --h-g-f-e-d-c-b-c-d-e-f-g-h--
# ----h-g-f-e-d-c-d-e-f-g-h----
# ------h-g-f-e-d-e-f-g-h------
# --------h-g-f-e-f-g-h--------
# ----------h-g-f-g-h----------
# ------------h-g-h------------
# --------------h--------------