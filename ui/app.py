import customtkinter as ctk


class StudentManagementApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Student Management System")
        self.geometry("1200x750")
        self.minsize(1000, 650)

        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.sidebar_color = "#172B4D"
        self.background_color = "#F5F7FB"
        self.primary_color = "#2563EB"

        self.create_sidebar()

        self.content_frame = ctk.CTkFrame(
            self, corner_radius=0, fg_color=self.background_color
        )

        self.content_frame.grid(row=0, column=1, sticky="nsew")

        self.show_dashboard()

    def create_sidebar(self):

        self.sidebar = ctk.CTkFrame(
            self, width=230, corner_radius=0, fg_color=self.sidebar_color
        )
        self.sidebar.grid(row=0, column=0, sticky="nsew")

        self.sidebar.grid_propagate(False)

        ctk.CTkLabel(
            self.sidebar,
            text="Student Manager",
            font=("Arial", 22, "bold"),
            text_color="white",
        ).pack(pady=(35, 40))

        buttons = [
            ("Dashboard", self.show_dashboard),
            ("All Students", self.show_students),
            ("Add Student", self.show_add_student),
        ]

        for title, command in buttons:
            ctk.CTkButton(
                self.sidebar,
                text=title,
                command=command,
                height=45,
                corner_radius=8,
                fg_color="transparent",
                hover_color="#29466F",
                anchor="w",
            ).pack(fill="x", padx=18, pady=6)

        # Footer - loop ke bahar
        ctk.CTkLabel(
            self.sidebar,
            text="Student Management v1.0",
            text_color="#B8C7DC",
            font=("Arial", 11),
        ).pack(side="bottom", pady=20)

    def clear_content(self):

        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def show_dashboard(self):

        self.clear_content()
        ctk.CTkLabel(
            self.content_frame,
            text="Dashboard",
            font=("Arial", 30, "bold"),
            text_color="#172B4D",
        ).pack(anchor="w", padx=35, pady=(35, 10))

        ctk.CTkLabel(
            self.content_frame,
            text="Welcome to your Student Management System",
            font=("Arial", 14),
            text_color="#64748B",
        ).pack(anchor="w", padx=35)

        stats_frame = ctk.CTkFrame(self.content_frame, fg_color="transparent")
        stats_frame.pack(fill="x", padx=35, pady=(10, 0))

        stats = [
            ("Total Students", "—", "#2563EB"),
            ("Passed Students", "—", "#16A34A"),
            ("Failed Students", "—", "#DC2626"),
            ("Average Marks", "—", "#D97706"),
        ]
        for index, (title, value, color) in enumerate(stats):
            stats_frame.grid_columnconfigure(index, weight=1)

            card = ctk.CTkFrame(
                stats_frame, fg_color="white", corner_radius=12, height=130
            )
            card.grid(row=0, column=index, padx=8, sticky="nsew")
            card.grid_propagate(False)

            ctk.CTkLabel(
                card,
                text=title,
                font=("Arial", 14),
                text_color="#64748B",
            ).pack(anchor="w", padx=18, pady=(20, 8))

            ctk.CTkLabel(
                card,
                text=value,
                font=("Arial", 28, "bold"),
                text_color=color,
            ).pack(anchor="w", padx=18)
        # Student performance section
        performance_frame = ctk.CTkFrame(
            self.content_frame, fg_color="white", corner_radius=12, height=200
        )

        performance_frame.pack(
            fill="x",
            padx=35,
            pady=25,
        )
        performance_frame.pack_propagate(False)
        ctk.CTkLabel(
            performance_frame,
            text="Student Performance",
            font=("Arial", 20, "bold"),
            text_color="#172B4D",
        ).pack(anchor="w", padx=20, pady=20)

        ctk.CTkLabel(
            performance_frame,
            text="Grade distributed overview.",
            font=("Arial", 14),
            text_color="#64748B",
        ).pack(anchor="w", padx=20, pady=(0, 15))

        grade_data = [
            {"grade": "A", "count": 18, "percentage": 90, "color": "#16A34A"},
            {"grade": "B", "count": 14, "percentage": 70, "color": "#2563EB"},
            {"grade": "C", "count": 10, "percentage": 50, "color": "#D97706"},
            {"grade": "D", "count": 6, "percentage": 30, "color": "#EA580C"},
            {"grade": "Fail", "count": 3, "percentage": 15, "color": "#DC2626"},
        ]

        chart_area = ctk.CTkFrame(
            performance_frame,
            fg_color="transparent",
        )
        chart_area.pack(fill="both", expand=True, padx=25, pady=(0, 15))

        for index, item in enumerate(grade_data):
            chart_area.grid_columnconfigure(index, weight=1)

            column = ctk.CTkFrame(chart_area, fg_color="transparent")

            column.grid(row=0, column=index, sticky="nsew", padx=12)

            ctk.CTkLabel(
                column,
                text=str(item["count"]),
                font=("Arial", 14, "bold"),
                text_color="#172B4D",
            ).pack(pady=(0, 6))

            bar_track = ctk.CTkFrame(
                column, fg_color="#E8EEF7", corner_radius=6, height=120, width=45
            )
            bar_track.pack()
            bar_track.pack_propagate(False)

            bar_height = int(120 * item["percentage"] / 100)

            bar = ctk.CTkFrame(
                bar_track, fg_color=item["color"], corner_radius=6, height=bar_height
            )
            bar.pack(side="bottom", fill="x")
            ctk.CTkLabel(
                column,
                text=item["grade"],
                font=("Arial", 14, "bold"),
                text_color="#64748B",
            ).pack(pady=(8, 0))

            quick_actions_frame = ctk.CTkFrame(
                self.content_frame, fg_color="white", corner_radius=12, height=180
            )

            quick_actions_frame.pack(fill="x", padx=35, pady=(0, 25))
            quick_actions_frame.pack_propagate(False)

            ctk.CTkLabel(
                quick_actions_frame,
                text="Quick Action",
                font=("Arial", 14, "bold"),
                text_color="#172B4D",
            ).pack(anchor="w", padx=20, pady=(18, 12))

            action_container = ctk.CTkFrame(quick_actions_frame, fg_color="transparent")
            action_container.pack(fill="x", padx=20)

            ctk.CTkButton(
                action_container,
                text="+ Add New Student",
                height=42,
                corner_radius=8,
                fg_color="#2563EB",
                hover="#1D4ED8",
                command=self.show_add_student,
            ).pack(side="left", padx=(0, 12))

            ctk.CTkButton(
                action_container,
                text="View All Students",
                height=42,
                corner_radius=8,
                fg_color="#16A34A",
                hover_color="#15803D",
                command=self.show_students,
            ).pack(side="left")

    def show_students(self):

        self.clear_content()

        ctk.CTkLabel(
            self.content_frame, text="All Students", font=("Arial", 30, "bold")
        ).pack(anchor="w", padx=35, pady=(35, 10))

        ctk.CTkLabel(
            self.content_frame,
            text="All Student Records below",
            font=("Arial", 14),
            text_color="#64748B",
        ).pack(anchor="w", padx=35)

    def show_add_student(self):

        self.clear_content()

        ctk.CTkLabel(
            self.content_frame, text="Add New Student", font=("Arial", 30, "bold")
        ).pack(anchor="w", padx=35, pady=35)
