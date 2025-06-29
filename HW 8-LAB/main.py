def collect_names():
    names = []
    while True:
        name = input("შეიყვანე სახელი (ან 'stop' გასაჩერებლად): ").strip()
        if name.lower() == "stop":
            break
        names.append(name)
    return names

result = collect_names()
print("შენ მიერ შეყვანილი სახელებია:", result)
