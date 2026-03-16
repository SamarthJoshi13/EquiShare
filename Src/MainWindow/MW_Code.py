import customtkinter as ctk
class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()

        ctk.set_appearance_mode("System")  # "Dark" / "Light"
        ctk.set_default_color_theme("blue")

        self.title("HouseTask – Prototype")
        self.geometry("1000x650")
        self.minsize(900, 600)

        # Layout: sidebar (col 0) + content (col 1)
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.sidebar = ctk.CTkFrame(self, width=220, corner_radius=0)
        
        self.sidebar.grid(row=0, column=0, sticky="nsw")
        self.sidebar.grid_rowconfigure(10, weight=1)

        self.content = ctk.CTkFrame(self, corner_radius=0)
        self.content.grid(row=0, column=1, sticky="nsew")
        self.content.grid_rowconfigure(0, weight=1)
        self.content.grid_columnconfigure(0, weight=1)

        self._build_sidebar()

        # Views
        self.views = {
            "Dashboard": DashboardView(self.content,self),
            "Housemates": HousematesView(self.content,self),
            "Tasks": TasksView(self.content,self),
        }

        self.current_view = None
        self.show_view("Dashboard")

    def _build_sidebar(self):
        self.housemates = [
    {"name": "Faris", "weight": 1.0, "assigned_points": 0},
    {"name": "Jack", "weight": 1.0, "assigned_points": 0},
    {"name": "Fatima", "weight": 1.0, "assigned_points": 0},]
        
        self.tasks = [
    {"name": "Take bins out", "points": 2, "assigned_to": None, "completed": False},
    {"name": "Clean kitchen", "points": 3, "assigned_to": None, "completed": False},]
        self.history=[]
        
        
        title = ctk.CTkLabel(
            self.sidebar,
            text="HouseTask",
            font=ctk.CTkFont(size=20, weight="bold"),
        )
        title.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="w")

        subtitle = ctk.CTkLabel(
            self.sidebar,
            text="Roommate chores prototype",
            font=ctk.CTkFont(size=12),
            text_color="gray70",
        )
        subtitle.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="w")

        self.btn_dashboard = ctk.CTkButton(
            self.sidebar, text="Dashboard", command=lambda: self.show_view("Dashboard")
        )
        self.btn_dashboard.grid(row=2, column=0, padx=20, pady=10, sticky="ew")

        self.btn_housemates = ctk.CTkButton(
            self.sidebar, text="Housemates", command=lambda: self.show_view("Housemates")
        )
        self.btn_housemates.grid(row=3, column=0, padx=20, pady=10, sticky="ew")

        self.btn_tasks = ctk.CTkButton(
            self.sidebar, text="Tasks", command=lambda: self.show_view("Tasks")
        )
        self.btn_tasks.grid(row=4, column=0, padx=20, pady=10, sticky="ew")

        footer = ctk.CTkLabel(
            self.sidebar,
            text="v0.1 • UI skeleton",
            font=ctk.CTkFont(size=11),
            text_color="gray70",
        )
        footer.grid(row=11, column=0, padx=20, pady=20, sticky="w")

    def show_view(self, name: str):
        if self.current_view is not None:
            self.current_view.grid_forget()

        view = self.views[name]
        view.grid(row=0, column=0, sticky="nsew")
        self.current_view = view
    def refresh_all(self):
        for v in self.views.values():
            if hasattr(v, "refresh"):
                v.refresh()