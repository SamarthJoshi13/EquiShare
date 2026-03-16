import customtkinter as ctk
from datetime import datetime


class TasksView(ctk.CTkFrame):
    def __init__(self, parent,app):
        super().__init__(parent)
        self.app=app

        self.grid_columnconfigure(0, weight=1)

        title = ctk.CTkLabel(self, text="Tasks", font=ctk.CTkFont(size=22, weight="bold"))
        title.grid(row=0, column=0, padx=25, pady=(25, 10), sticky="w")

        info = ctk.CTkLabel(
            self,
            text="Create tasks and (later) auto-assign fairly. This is a UI placeholder.",
            text_color="gray70",
        )
        info.grid(row=1, column=0, padx=25, pady=(0, 15), sticky="w")

        form = ctk.CTkFrame(self)
        form.grid(row=2, column=0, padx=25, pady=10, sticky="ew")
        form.grid_columnconfigure((0, 1, 4), weight=1)

        self.task_entry = ctk.CTkEntry(form, placeholder_text="Task name (e.g., Take bins out)")
        self.task_entry.grid(row=0, column=0, padx=10, pady=15, sticky="ew")

        self.points_entry = ctk.CTkEntry(form, placeholder_text="Effort points (e.g., 2)")
        self.points_entry.grid(row=0, column=1, padx=10, pady=15, sticky="ew")

        add_btn = ctk.CTkButton(form, text="Add", command=self._demo_add)
        add_btn.grid(row=0, column=2, padx=10, pady=15, sticky="ew")

        actions = ctk.CTkFrame(self)
        actions.grid(row=3, column=0, padx=25, pady=(5, 10), sticky="ew")
        actions.grid_columnconfigure((0, 1), weight=1)

        ctk.CTkButton(actions, text="Auto-assign",command=self.auto_assign).grid(
            row=0, column=0, padx=10, pady=12, sticky="ew"
        )
        ctk.CTkButton(actions, text="Mark complete",command=self.mark_complete).grid(
            row=0, column=1, padx=10, pady=12, sticky="ew"
        )

        self.list_box = ctk.CTkTextbox(self,height=280)
        self.list_box.grid(row=4, column=0, padx=25, pady=15, sticky="nsew")
        self.list_box.configure(state="disabled")
        #--------Changes to the new layout are being made here:
        self.Name_of_completor=ctk.CTkEntry(form,placeholder_text="Name of completor")
        self.Name_of_completor.grid(row=1, column=0, padx=10,sticky="ew")
        
        self.task_Number=ctk.CTkEntry(form,placeholder_text="Completed Task Number")
        self.task_Number.grid(row=1, column=1, padx=10, pady=15,sticky="ew")
        
        
        
        #-----
        self.refresh()

    def _demo_add(self):
        tasks=self.task_entry.get().strip()
        points_text=self.points_entry.get().strip()
        if not tasks:
            return
        try:
            points = int(points_text) if points_text else 1
        except ValueError:
            points = 1
        self.app.tasks.append({"name":tasks,"points":points,"assigned_to": None, "completed": False})
        self.task_entry.delete(0, "end")
        self.points_entry.delete(0, "end")
        
        self.app.refresh_all()
        self.refresh()
        
    def auto_assign(self):
        if not self.app.housemates:
            return
        workload = {h["name"]: 0 for h in self.app.housemates}
        for t in self.app.tasks:
            if t["completed"]:
                continue
            if t["assigned_to"] is not None:
                workload[t["assigned_to"]] += int(t["points"])
        for t in self.app.tasks:
            if t["completed"]:
                continue
            if t["assigned_to"] is not None:
                continue
            chosen_name = min(workload, key=workload.get)
            t["assigned_to"] = chosen_name
            workload[chosen_name] += int(t["points"])
        self.app.refresh_all()
    def mark_complete(self):
        Name_of_completor=self.Name_of_completor.get().strip()
        task_Number=self.task_Number.get().strip()
        if Name_of_completor!="" and task_Number!="":
            for h in self.app.housemates:
                if h["name"].lower()==Name_of_completor.lower():
                        if h["name"]==self.app.tasks[int(task_Number)-1]["assigned_to"]:
                            self.app.tasks[int(task_Number)-1]["completed"]=True
                            self.Name_of_completor.delete(0,"end")
                            self.task_Number.delete(0,"end")
                            self.app.refresh_all()
        
    def refresh(self):
        self.list_box.configure(state="normal")
        self.list_box.delete("1.0", "end")
        for idx, t in enumerate(self.app.tasks, start=1):
            status = "✅" if t["completed"] else "⏳"
            who = t["assigned_to"] if t["assigned_to"] else "unassigned"
            self.list_box.insert("end",f"{idx}. {status} {t['name']} ({t['points']} pts) – {who}\n")
        self.list_box.configure(state="disabled")