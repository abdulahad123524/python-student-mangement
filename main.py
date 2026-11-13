from student import (
    add_student,
    view_students,
    view_student_details,
    delete_student,
)


def show_main_view():
    print("\n====================== End ")


def main():
    while True:
        show_main_view()

        choice = input("select an option ").strip()

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()
        elif choice == "3":
            view_student_details()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Thankyou for using mangement_system")
            break
        else:
            print("Invalid option .please select 1 to 5")


if __name__ == "__main__":
    main()
