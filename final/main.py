"""Small CLI task tracker. Baseline snapshot; intentionally not hardened."""
tasks = []

def add_task(name):
    tasks.append(name)
    return True

def delete_task(number):
    tasks.pop(number - 1)
    return True

def list_tasks():
    return list(tasks)

def main():
    while True:
        print("\n1 Add  2 List  3 Delete  4 Exit")
        choice = input("Choose: ")
        if choice == "1":
            add_task(input("Task: "))
        elif choice == "2":
            print(list_tasks())
        elif choice == "3":
            delete_task(int(input("Number: ")))
        elif choice == "4":
            break

if __name__ == "__main__":
    main()
