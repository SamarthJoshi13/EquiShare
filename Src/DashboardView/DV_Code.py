import customtkinter as ctk
class DashboardView(ctk.CTkFrame):
    def __init__(self, parent,app):
        super().__init__(parent)
        self.app=app
        self.grid_columnconfigure(0, weight=1)

        title = ctk.CTkLabel(self, text="Dashboard", font=ctk.CTkFont(size=22, weight="bold"))
        title.grid(row=0, column=0, padx=25, pady=(25, 10), sticky="w")

        info = ctk.CTkLabel(
            self,
            text="Quick overview of tasks and workload.",
            text_color="gray70",
        )
        info.grid(row=1, column=0, padx=25, pady=(0, 20), sticky="w")
        
        # Simple "cards"
        cards = ctk.CTkFrame(self)
        cards.grid(row=2, column=0, padx=25, pady=10, sticky="ew")
        cards.grid_columnconfigure((0, 1, 2), weight=1)
        
        #Connecting live number of tasks thats not completed------
        due=0
        for i in self.app.tasks:
            if i["completed"]==False:
                due=due+1
        self._card(cards, 0, "Tasks due today",due)
        self._card(cards, 1, "Overdue tasks", "1")
        self._card(cards, 2, "Completed this week", "6")
        #-------
        #Negins Code Changes

        # Workload preview
        box = ctk.CTkFrame(self)
        box.grid(row=3, column=0, padx=25, pady=20, sticky="nsew")
        box.grid_columnconfigure(0, weight=1)

        header = ctk.CTkLabel(box, text="Workload balance (preview)", font=ctk.CTkFont(size=16, weight="bold"))
        header.grid(row=0, column=0, padx=20, pady=(15, 10), sticky="w")
        
        #----New for loop to connect to the live data
        l=len(self.app.housemates)
        cl=0
        for i in self.app.housemates:
            row=ctk.CTkFrame(box)
            row.grid(row=cl,column=0,padx=20, pady=6, sticky="ew")
            row.grid_columnconfigure(0, weight=1)
            
            ctk.CTkLabel(row, text=i["name"]).grid(row=0, column=0, padx=10, pady=8, sticky="w")
            ctk.CTkLabel(row, text=i["assigned_points"], text_color="gray70").grid(row=0, column=1, padx=10, pady=8, sticky="e")
            cl=cl+1
        #=------
    
    def _card(self, parent, col, label, value):
        card = ctk.CTkFrame(parent)
        card.grid(row=0, column=col, padx=10, pady=10, sticky="ew")
        card.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(card, text=label, text_color="gray70").grid(row=0, column=0, padx=15, pady=(12, 2), sticky="w")
        ctk.CTkLabel(card, text=value, font=ctk.CTkFont(size=22, weight="bold")).grid(row=1, column=0, padx=15, pady=(0, 12), sticky="w")
