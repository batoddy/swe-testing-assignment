import pytest
import tkinter as tk
from tkinter import messagebox

from quick_calc import (
    CalculatorGUI,
)  # GUI + Calculator together :contentReference[oaicite:1]{index=1}


@pytest.fixture
def app(monkeypatch):
    # Prevent popup windows during tests
    monkeypatch.setattr(messagebox, "showerror", lambda *args, **kwargs: None)

    gui = CalculatorGUI()
    gui.withdraw()  # Hide the window (headless-ish)

    yield gui

    gui.destroy()


def _set_entry(entry: tk.Entry, text: str):
    entry.delete(0, tk.END)
    entry.insert(0, text)


def _click_button_by_text(root: tk.Tk, text: str):
    # Find a ttk.Button by its visible text and invoke it
    stack = list(root.winfo_children())
    while stack:
        w = stack.pop()
        stack.extend(w.winfo_children())
        try:
            if w.winfo_class() == "TButton" and w.cget("text") == text:
                w.invoke()
                return
        except Exception:
            pass
    raise AssertionError(f"Button '{text}' not found")


def test_add_flow_updates_result(app):
    # Simulate: enter 5 and 3, press '+', check result shows 8
    _set_entry(app.a_entry, "5")
    _set_entry(app.b_entry, "3")

    _click_button_by_text(app, "+")
    app.update_idletasks()

    assert app.var_result.get().endswith("= 8")


def test_clear_resets_after_calculation(app):
    # Do a calculation first
    _set_entry(app.a_entry, "9")
    _set_entry(app.b_entry, "4")
    _click_button_by_text(app, "-")
    app.update_idletasks()

    # Press clear and verify reset
    _click_button_by_text(app, "Clear")
    app.update_idletasks()

    assert app.var_a.get() == ""
    assert app.var_b.get() == ""
    assert app.var_result.get() == "Result: -"
