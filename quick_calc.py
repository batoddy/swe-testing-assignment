import tkinter as tk
from tkinter import ttk, messagebox


class Calculator:
    crr_value = 0

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b


class CalculatorGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator (Tkinter)")
        self.resizable(False, False)

        self.calc = Calculator()

        # --- UI variables ---
        self.var_a = tk.StringVar()
        self.var_b = tk.StringVar()
        self.var_result = tk.StringVar(value="Result: -")

        # Apply dark mode styling (ONLY addition requested)
        self._apply_dark_mode()

        self._build_ui()

    def _apply_dark_mode(self):
        # --- Dark palette ---
        self.bg = "#121212"
        self.fg = "#EAEAEA"
        self.entry_bg = "#1E1E1E"
        self.entry_fg = "#FFFFFF"
        self.btn_bg = "#2A2A2A"
        self.btn_fg = "#FFFFFF"
        self.border = "#3A3A3A"
        self.active_bg = "#3B3B3B"

        # Set root background
        self.configure(bg=self.bg)

        # ttk style overrides
        style = ttk.Style(self)

        # Pick a theme that is easy to override
        # 'clam' works well across platforms
        try:
            style.theme_use("clam")
        except tk.TclError:
            pass

        # Base styles
        style.configure(".", background=self.bg, foreground=self.fg)

        style.configure("TFrame", background=self.bg)

        style.configure("TLabel", background=self.bg, foreground=self.fg)

        style.configure(
            "TButton",
            background=self.btn_bg,
            foreground=self.btn_fg,
            bordercolor=self.border,
            focusthickness=2,
            focuscolor=self.border,
            padding=6,
        )
        style.map(
            "TButton",
            background=[("active", self.active_bg), ("pressed", self.active_bg)],
            foreground=[("disabled", "#888888")],
        )

        style.configure(
            "TEntry",
            fieldbackground=self.entry_bg,
            background=self.entry_bg,
            foreground=self.entry_fg,
            bordercolor=self.border,
            insertcolor=self.entry_fg,
        )

        # Make messageboxes less jarring by setting a darker window background (best-effort)
        # Note: Native messageboxes may ignore these settings on some OS.
        self.option_add("*Dialog*background", self.bg)
        self.option_add("*Dialog*foreground", self.fg)
        self.option_add("*Dialog*selectBackground", self.active_bg)
        self.option_add("*Dialog*selectForeground", self.fg)

    def _build_ui(self):
        # Main container frame
        main = ttk.Frame(self, padding=14)
        main.grid(row=0, column=0, sticky="nsew")

        # Input fields
        ttk.Label(main, text="A:").grid(
            row=0, column=0, sticky="w", padx=(0, 6), pady=(0, 8)
        )
        a_entry = ttk.Entry(main, textvariable=self.var_a, width=18)
        a_entry.grid(row=0, column=1, sticky="ew", pady=(0, 8))

        ttk.Label(main, text="B:").grid(
            row=1, column=0, sticky="w", padx=(0, 6), pady=(0, 12)
        )
        b_entry = ttk.Entry(main, textvariable=self.var_b, width=18)
        b_entry.grid(row=1, column=1, sticky="ew", pady=(0, 12))

        # Operation buttons
        btns = ttk.Frame(main)
        btns.grid(row=2, column=0, columnspan=2, sticky="ew")

        ttk.Button(btns, text="+", width=6, command=lambda: self._compute("add")).grid(
            row=0, column=0, padx=4, pady=4
        )
        ttk.Button(btns, text="-", width=6, command=lambda: self._compute("sub")).grid(
            row=0, column=1, padx=4, pady=4
        )
        ttk.Button(btns, text="×", width=6, command=lambda: self._compute("mul")).grid(
            row=0, column=2, padx=4, pady=4
        )
        ttk.Button(btns, text="÷", width=6, command=lambda: self._compute("div")).grid(
            row=0, column=3, padx=4, pady=4
        )

        # Clear button
        ttk.Button(main, text="Clear", command=self._clear).grid(
            row=3, column=0, columnspan=2, sticky="ew", pady=(10, 0)
        )

        # Result label
        res = ttk.Label(
            main, textvariable=self.var_result, font=("Segoe UI", 12, "bold")
        )
        res.grid(row=4, column=0, columnspan=2, sticky="w", pady=(12, 0))

        # Bind Enter key to perform an operation (default: addition)
        a_entry.bind("<Return>", lambda e: self._compute("add"))
        b_entry.bind("<Return>", lambda e: self._compute("add"))

        # Set initial focus
        a_entry.focus()

    def _parse_inputs(self):
        # Read and validate inputs
        a_text = self.var_a.get().strip()
        b_text = self.var_b.get().strip()

        if not a_text or not b_text:
            raise ValueError("Please enter values for A and B.")

        try:
            a = float(a_text)
            b = float(b_text)
        except ValueError:
            raise ValueError("A and B must be numeric. (e.g., 12, 3.5)")

        return a, b

    def _compute(self, op):
        try:
            a, b = self._parse_inputs()

            # Dispatch operation
            if op == "add":
                out = self.calc.add(a, b)
                sym = "+"
            elif op == "sub":
                out = self.calc.subtract(a, b)
                sym = "-"
            elif op == "mul":
                out = self.calc.multiply(a, b)
                sym = "×"
            elif op == "div":
                out = self.calc.divide(a, b)
                sym = "÷"
            else:
                raise ValueError("Unknown operation")

            # Display formatted result
            self.var_result.set(f"Result: {a:g} {sym} {b:g} = {out:g}")

        except Exception as ex:
            messagebox.showerror("Error", str(ex))

    def _clear(self):
        # Reset input fields and result text
        self.var_a.set("")
        self.var_b.set("")
        self.var_result.set("Result: -")


if __name__ == "__main__":
    app = CalculatorGUI()
    app.mainloop()
