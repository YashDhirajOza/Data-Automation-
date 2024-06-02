import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from datetime import datetime
from io import StringIO
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class DataAnalyzerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Data Analyzer")
        self.root.configure(bg="black")

        style = ttk.Style()
        style.theme_use("default")
        style.configure("TFrame", background="black")
        style.configure("TLabel", background="black", foreground="white")
        style.configure("TButton", background="gray", foreground="white")
        style.configure("TCombobox", fieldbackground="black", background="gray", foreground="white")

        self.frame = ttk.Frame(self.root, padding="10")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.load_button = ttk.Button(self.frame, text="Load CSV", command=self.load_csv)
        self.load_button.grid(row=0, column=0, padx=5, pady=5)

        self.plot_button = ttk.Button(self.frame, text="Plot", command=self.open_plot_window)
        self.plot_button.grid(row=1, column=0, padx=5, pady=5)

        self.save_button = ttk.Button(self.frame, text="Save Report", command=self.save_report)
        self.save_button.grid(row=0, column=1, padx=5, pady=5)

        self.text = tk.Text(self.frame, wrap=tk.WORD, width=100, height=30, bg="black", fg="white", insertbackground="white")
        self.text.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        self.scrollbar = ttk.Scrollbar(self.frame, orient=tk.VERTICAL, command=self.text.yview)
        self.scrollbar.grid(row=1, column=2, sticky=(tk.N, tk.S))
        self.text['yscrollcommand'] = self.scrollbar.set

        self.data = None
        self.report = ""

    def load_csv(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            try:
                self.data = pd.read_csv(file_path)
                self.generate_report()
                self.display_report()
            except ValueError as e:
                messagebox.showerror("Error", f"Failed to load file: ValueError\n{e}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load file\n{e}")

    def generate_report(self):
        if self.data is None:
            return

        report_lines = []

        report_lines.append("Data Analysis Report")
        report_lines.append(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report_lines.append("=" * 80)

        # Basic Information
        buffer = StringIO()
        self.data.info(buf=buffer)
        report_lines.append("Basic Information")
        report_lines.append(buffer.getvalue())
        report_lines.append("=" * 80)

        # First 5 Rows
        report_lines.append("First 5 Rows of the Dataset")
        report_lines.append(self.data.head().to_string())
        report_lines.append("=" * 80)

        # Statistics Summary
        report_lines.append("Basic Statistics Summary")
        report_lines.append(self.data.describe(include='all').to_string())
        report_lines.append("=" * 80)

        # Mean Values
        report_lines.append("Mean of Numerical Columns")
        report_lines.append(self.data.mean(numeric_only=True).to_string())
        report_lines.append("=" * 80)

        # Median Values
        report_lines.append("Median of Numerical Columns")
        report_lines.append(self.data.median(numeric_only=True).to_string())
        report_lines.append("=" * 80)

        # Standard Deviation
        report_lines.append("Standard Deviation of Numerical Columns")
        report_lines.append(self.data.std(numeric_only=True).to_string())
        report_lines.append("=" * 80)

        # Missing Values
        report_lines.append("Count of Missing Values in Each Column")
        report_lines.append(self.data.isnull().sum().to_string())
        report_lines.append("=" * 80)

        # Correlation Matrix
        report_lines.append("Correlation Matrix")
        report_lines.append(self.data.corr().to_string())
        report_lines.append("=" * 80)

        self.report = "\n".join(report_lines)

    def display_report(self):
        self.text.delete("1.0", tk.END)
        self.text.insert(tk.END, self.report)

    def save_report(self):
        if not self.report:
            messagebox.showwarning("Warning", "No report to save. Please load a CSV file first.")
            return

        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_path:
            try:
                with open(file_path, "w") as file:
                    file.write(self.report)
                messagebox.showinfo("Success", f"Report saved successfully to {file_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save report\n{e}")

    def open_plot_window(self):
        if self.data is None:
            messagebox.showwarning("Warning", "Please load a CSV file first.")
            return
        
        plot_window = tk.Toplevel(self.root)
        plot_window.title("Plot Data")
        plot_window.configure(bg="black")

        ttk.Label(plot_window, text="Select Column for X-axis:").grid(row=0, column=0, padx=5, pady=5)
        x_column = ttk.Combobox(plot_window, values=self.data.columns.tolist())
        x_column.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(plot_window, text="Select Column for Y-axis:").grid(row=1, column=0, padx=5, pady=5)
        y_column = ttk.Combobox(plot_window, values=self.data.columns.tolist())
        y_column.grid(row=1, column=1, padx=5, pady=5)

        def plot_histogram():
            col = x_column.get()
            if col:
                fig, ax = plt.subplots()
                self.data[col].hist(ax=ax)
                ax.set_title(f'Histogram of {col}')
                ax.set_xlabel(col)
                ax.set_ylabel('Frequency')
                self.display_plot(fig, plot_window)

        def plot_regression():
            x_col = x_column.get()
            y_col = y_column.get()
            if x_col and y_col:
                fig, ax = plt.subplots()
                self.data.plot(kind='scatter', x=x_col, y=y_col, ax=ax)
                ax.set_title(f'Regression Plot of {y_col} vs {x_col}')
                self.display_plot(fig, plot_window)

        ttk.Button(plot_window, text="Plot Histogram", command=plot_histogram).grid(row=2, column=0, padx=5, pady=5)
        ttk.Button(plot_window, text="Plot Regression", command=plot_regression).grid(row=2, column=1, padx=5, pady=5)

    def display_plot(self, fig, window):
        canvas = FigureCanvasTkAgg(fig, master=window)
        canvas.draw()
        canvas.get_tk_widget().grid(row=3, column=0, columnspan=2, padx=5, pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = DataAnalyzerApp(root)
    root.mainloop()
