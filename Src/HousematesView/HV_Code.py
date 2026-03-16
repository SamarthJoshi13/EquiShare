import customtkinter as ctk


class HousematesView(ctk.CTkFrame):
    def __init__(self, parent,app):
        super().__init__(parent)
        self.app=app

        self.grid_columnconfigure(0, weight=1)

        title = ctk.CTkLabel(self, text="Housemates", font=ctk.CTkFont(size=22, weight="bold"))
        title.grid(row=0, column=0, padx=25, pady=(25, 10), sticky="w")

        info = ctk.CTkLabel(self, text="Add and manage housemates (dummy list).", text_color="gray70")
        info.grid(row=1, column=0, padx=25, pady=(0, 15), sticky="w")

        form = ctk.CTkFrame(self)
        form.grid(row=2, column=0, padx=25, pady=10, sticky="ew")
        form.grid_columnconfigure((0, 1, 2), weight=1)

        self.name_entry = ctk.CTkEntry(form, placeholder_text="Name (e.g., Aisha)")
        self.name_entry.grid(row=0, column=0, padx=10, pady=15, sticky="ew")

        self.weight_entry = ctk.CTkEntry(form, placeholder_text="Weighting (optional, e.g., 1.0)")
        self.weight_entry.grid(row=0, column=1, padx=10, pady=15, sticky="ew")

        add_btn = ctk.CTkButton(form, text="Add", command=self._demo_add)
        add_btn.grid(row=0, column=2, padx=10, pady=15, sticky="ew")

        self.list_box = ctk.CTkTextbox(self, height=280)
        self.list_box.grid(row=3, column=0, padx=25, pady=15, sticky="nsew")
        self.list_box.configure(state="disabled")
        
        self.refresh()

    def _demo_add(self):
        name = self.name_entry.get().strip()
        weight_text= self.weight_entry.get().strip()
        if not name:
            return
        try:
            weight=float(weight_text) if weigh_text else 1.0
        except:
            weight=1.0
        self.app.housemates.append({"name":name,"weight":weight,"assigned_poitns":0})
        
        #Clearing the entry box test
        self.name_entry.delete(0,"end")
        self.weight_entry.delete(0,"end")
        
        self.app.refresh_all()
    def refresh(self):
        self.list_box.delete("1.0","end")
        self.list_box.configure(state="normal")
        for i in self.app.housemates:
            self.list_box.insert("end", f"• {i['name']} (weight {i['weight']})\n")