emaillar = ['panda@gmail.com', 'panda1@gmail.com', 'panda2gmail.com']

# Har bir emailni for sikli bilan tekshirish
for email in emaillar:
    if "@" not in email:
        print(f"Notogri email: {email}")


parollar = ['password123', 'Qwerty!', 'admin', 'StrongPass1!']
for parol in parollar:
    if len(parol) <8:
        print(f"'{parol}' -> Juda qisqa")
    elif not (any(char.isdigit() for char in parol) or any(not char.isalmun() for char in parol)):
        print(f"'{parol}' -> kuchsiz parol")
    else:
        print(f"'{parol}' -> kuchli parol")