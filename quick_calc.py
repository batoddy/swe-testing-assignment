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

        # --- UI değişkenleri ---
        self.var_a = tk.StringVar()
        self.var_b = tk.StringVar()
        self.var_result = tk.StringVar(value="Sonuç: -")

        self._build_ui()

    def _build_ui(self):
        main = ttk.Frame(self, padding=14)
        main.grid(row=0, column=0, sticky="nsew")

        # Girişler
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

        # Butonlar
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

        ttk.Button(main, text="Temizle", command=self._clear).grid(
            row=3, column=0, columnspan=2, sticky="ew", pady=(10, 0)
        )

        # Sonuç
        res = ttk.Label(
            main, textvariable=self.var_result, font=("Segoe UI", 12, "bold")
        )
        res.grid(row=4, column=0, columnspan=2, sticky="w", pady=(12, 0))

        # Kullanışlı: enter basınca hesapla (örnek: toplama)
        a_entry.bind("<Return>", lambda e: self._compute("add"))
        b_entry.bind("<Return>", lambda e: self._compute("add"))

        a_entry.focus()

    def _parse_inputs(self):
        a_text = self.var_a.get().strip()
        b_text = self.var_b.get().strip()

        if not a_text or not b_text:
            raise ValueError("Lütfen A ve B için değer gir.")

        try:
            a = float(a_text)
            b = float(b_text)
        except ValueError:
            raise ValueError("A ve B sayısal olmalı. (Örn: 12, 3.5)")

        return a, b

    def _compute(self, op):
        try:
            a, b = self._parse_inputs()

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
                raise ValueError("Bilinmeyen işlem")

            # Sonucu biraz düzgün gösterelim
            self.var_result.set(f"Sonuç: {a:g} {sym} {b:g} = {out:g}")

        except Exception as ex:
            messagebox.showerror("Hata", str(ex))

    def _clear(self):
        self.var_a.set("")
        self.var_b.set("")
        self.var_result.set("Sonuç: -")


if __name__ == "__main__":
    app = CalculatorGUI()
    app.mainloop()
