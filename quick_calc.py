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

        # Theme state
        self.is_dark = tk.BooleanVar(value=True)

        # Build UI first (so toggle exists), then apply theme
        self._build_ui()
        self._apply_theme()

    def _build_ui(self):
        # Main container frame
        self.main = ttk.Frame(self, padding=14)
        self.main.grid(row=0, column=0, sticky="nsew")

        # Top bar (title + toggle)
        top = ttk.Frame(self.main)
        top.grid(row=0, column=0, columnspan=2, sticky="ew", pady=(0, 10))
        top.columnconfigure(0, weight=1)

        ttk.Label(top, text="Calculator", font=("Segoe UI", 12, "bold")).grid(
            row=0, column=0, sticky="w"
        )

        # Theme toggle (Checkbutton)
        self.toggle_btn = ttk.Checkbutton(
            top, text="Dark mode", variable=self.is_dark, command=self._apply_theme
        )
        self.toggle_btn.grid(row=0, column=1, sticky="e")

        # Input fields
        ttk.Label(self.main, text="A:").grid(
            row=1, column=0, sticky="w", padx=(0, 6), pady=(0, 8)
        )
        self.a_entry = ttk.Entry(self.main, textvariable=self.var_a, width=18)
        self.a_entry.grid(row=1, column=1, sticky="ew", pady=(0, 8))

        ttk.Label(self.main, text="B:").grid(
            row=2, column=0, sticky="w", padx=(0, 6), pady=(0, 12)
        )
        self.b_entry = ttk.Entry(self.main, textvariable=self.var_b, width=18)
        self.b_entry.grid(row=2, column=1, sticky="ew", pady=(0, 12))

        # Operation buttons
        btns = ttk.Frame(self.main)
        btns.grid(row=3, column=0, columnspan=2, sticky="ew")

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
        ttk.Button(self.main, text="Clear", command=self._clear).grid(
            row=4, column=0, columnspan=2, sticky="ew", pady=(10, 0)
        )

        # Result label
        ttk.Label(
            self.main, textvariable=self.var_result, font=("Segoe UI", 12, "bold")
        ).grid(row=5, column=0, columnspan=2, sticky="w", pady=(12, 0))

        # Bind Enter key to perform an operation (default: addition)
        self.a_entry.bind("<Return>", lambda e: self._compute("add"))
        self.b_entry.bind("<Return>", lambda e: self._compute("add"))

        # Set initial focus
        self.a_entry.focus()

    def _apply_theme(self):
        """
        Apply light/dark theme by overriding ttk styles.
        Note: ttk uses native rendering on some platforms; 'clam' is easier to style consistently.
        """
        style = ttk.Style(self)

        try:
            style.theme_use("clam")
        except tk.TclError:
            pass

        if self.is_dark.get():
            # --- Dark palette ---
            bg = "#121212"
            fg = "#EAEAEA"
            entry_bg = "#1E1E1E"
            entry_fg = "#FFFFFF"
            btn_bg = "#2A2A2A"
            btn_fg = "#FFFFFF"
            border = "#3A3A3A"
            active_bg = "#3B3B3B"
            self.toggle_btn.configure(text="Dark mode")
        else:
            # --- Light palette ---
            bg = "#F2F2F2"
            fg = "#111111"
            entry_bg = "#FFFFFF"
            entry_fg = "#111111"
            btn_bg = "#E6E6E6"
            btn_fg = "#111111"
            border = "#BDBDBD"
            active_bg = "#D6D6D6"
            self.toggle_btn.configure(text="Light mode")

        # Root background (covers non-ttk regions)
        self.configure(bg=bg)

        # Base styles
        style.configure(".", background=bg, foreground=fg)

        style.configure("TFrame", background=bg)
        style.configure("TLabel", background=bg, foreground=fg)

        style.configure(
            "TButton",
            background=btn_bg,
            foreground=btn_fg,
            bordercolor=border,
            focusthickness=2,
            focuscolor=border,
            padding=6,
        )
        style.map(
            "TButton",
            background=[("active", active_bg), ("pressed", active_bg)],
            foreground=[("disabled", "#888888")],
        )

        style.configure(
            "TEntry",
            fieldbackground=entry_bg,
            background=entry_bg,
            foreground=entry_fg,
            bordercolor=border,
            insertcolor=entry_fg,
        )

        style.configure("TCheckbutton", background=bg, foreground=fg)
        style.map(
            "TCheckbutton", background=[("active", bg)], foreground=[("active", fg)]
        )

        # Best-effort: make dialogs less jarring (native messageboxes may ignore this)
        self.option_add("*Dialog*background", bg)
        self.option_add("*Dialog*foreground", fg)
        self.option_add("*Dialog*selectBackground", active_bg)
        self.option_add("*Dialog*selectForeground", fg)

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
