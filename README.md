# Data Analyzer

Data Analyzer is a Tkinter-based desktop application designed for analyzing CSV files. It allows users to load CSV files, generate detailed reports, and visualize data through histograms and regression plots. The application features a dark theme for better readability and a modern look.

## Features

- Load CSV files and display basic information about the dataset.
- Generate a detailed report including:
  - Basic information about the dataset.
  - The first 5 rows of the dataset.
  - Basic statistics summary.
  - Mean, median, and standard deviation of numerical columns.
  - Count of missing values in each column.
  - Correlation matrix.
- Save the generated report as a text file.
- Visualize data with histograms and regression plots.
- Dark theme for all application windows.

## Requirements

- Python 3.x
- pandas
- tkinter
- matplotlib

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/data-analyzer.git
    cd data-analyzer
    ```

2. Install the required packages:
    ```sh
    pip install pandas matplotlib
    ```

## Usage

1. Run the application:
    ```sh
    python data_analyzer.py
    ```

2. Use the GUI to:
   - **Load CSV**: Load a CSV file for analysis.
   - **Plot**: Open the plot window to generate histograms or regression plots.
   - **Save Report**: Save the generated report as a text file.

### Plotting Data

In the plot window:
- Select the column for the X-axis.
- Select the column for the Y-axis (only for regression plots).
- Choose to plot a histogram or a regression plot.

## Code Overview

### `DataAnalyzerApp` Class

- `__init__(self, root)`: Initializes the main application window and configures the dark theme.
- `load_csv(self)`: Loads a CSV file and generates a report.
- `generate_report(self)`: Generates a detailed report of the loaded dataset.
- `display_report(self)`: Displays the generated report in the text widget.
- `save_report(self)`: Saves the generated report to a text file.
- `open_plot_window(self)`: Opens a new window for plotting data.
- `plot_histogram(self)`: Plots a histogram of the selected column.
- `plot_regression(self)`: Plots a regression plot of the selected columns.
- `display_plot(self, fig, window)`: Displays the plot in the plot window.

### Main Application

- The main application is initialized and run within the `if __name__ == "__main__":` block.

## Screenshots

_Add screenshots of the application here if available._

## Contributing

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Make your changes and commit them: `git commit -m 'Add feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
