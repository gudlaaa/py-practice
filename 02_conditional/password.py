# Problem: Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).

password = 'da'

char = len(password)

if char < 6:
    print('Weak')
elif char <= 6 and char >= 10:
    print('Medium')
else:
    print('Strong')
