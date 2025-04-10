🏡 Real Estate Dashboard
========================

Welcome to the **Real Estate Dashboard** project! This Python-based data analysis tool visualizes real estate sales data from 2001 to 2022, sourced from the Real\_Estate\_Sales\_2001-2022\_GL.csv dataset. Using powerful libraries like Pandas, NumPy, Seaborn, and Matplotlib, this project generates insightful charts and a comprehensive dashboard to explore trends, correlations, and distributions in the real estate market.

📋 Overview
-----------

The Real Estate Dashboard processes and visualizes real estate sales data to uncover trends over time, property type distributions, town-wise sales, and more. It performs data cleaning (e.g., outlier removal, missing value handling) and creates eight individual charts plus a unified dashboard for a holistic view of the data.

Key metrics analyzed:

*   Sale Amount (in millions)
    
*   Assessed Value (in millions)
    
*   Sales Ratio
    
*   Property Types and Residential Types
    
*   Town-wise distributions
    

✨ Features
----------

*   **Data Cleaning**: Filters invalid data and removes outliers using Z-scores.
    
*   **Visualizations**:
    
    *   📈 Line Chart: Total Sale Amount over years (2001-2022).
        
    *   📊 Stacked Bar Chart: Residential type distribution by top towns.
        
    *   🌡️ Correlation Heatmap: Relationships between Assessed Value, Sale Amount, and Sales Ratio.
        
    *   📉 Vertical Bar Chart: Total sales by town.
        
    *   ➡️ Horizontal Bar Chart: Average Sales Ratio by town.
        
    *   🥧 Pie Chart: Distribution of top 5 property types.
        
    *   📊📈 Combo Chart: Yearly Assessed Value vs. Sale Amount.
        
    *   🔢 Count Plot: Property count by town.
        
    *   🖼️ Complete Dashboard: All charts combined in a single view.
        
*   **Custom Styling**: Dark background with vibrant colors using Seaborn’s "husl" palette and Matplotlib’s customization.
    
*   **Output**: Saves all charts as high-quality PNGs in an images/ folder.
    

🚀 Installation
---------------

Follow these steps to set up and run the project on your local machine:

1.  **Clone the Repository**: ```bash git clone https://github.com/mansityagi01/Real_Estate_Dashboard_Python.gitcd real-estate-dashboard```
    
2.  **Install Dependencies**:Ensure you have Python 3.x installed. Then, install the required libraries:bashCollapseWrapCopypip install numpy pandas seaborn matplotlib scipy
    
3.  **Download the Dataset**:
    
    *   Obtain the Real\_Estate\_Sales\_2001-2022\_GL.csv file (e.g., from a public data source or your own dataset).
        
    *   Place it in the project root directory.
        
4.  **Run the Script**: ```bash python real\_estate\_dashboard.py```
    

🛠️ Usage
---------

1.  **Prepare the Data**: Ensure the Real\_Estate\_Sales\_2001-2022\_GL.csv file is in the root directory.
    
2.  **Execute the Script**: Run the Python script to:
    
    *   Load and clean the data.
        
    *   Generate individual charts and save them in the images/ folder.
        
    *   Create a complete dashboard (complete\_dashboard.png).
        
3.  **View Results**: Open the images/ folder to explore the visualizations.
    

Example output files:

*   line\_chart.png
    
*   stacked\_bar\_chart.png
    
*   heatmap.png
    
*   vertical\_bar\_chart.png
    
*   horizontal\_bar\_chart.png
    
*   pie\_chart.png
    
*   combo\_chart.png
    
*   count\_plot.png
    
*   complete\_dashboard.png
    

📚 Dependencies
---------------

*   **Python 3.x**
    
*   **NumPy**: For numerical operations.
    
*   **Pandas**: For data manipulation and analysis.
    
*   **Seaborn**: For statistical data visualization.
    
*   **Matplotlib**: For creating static, animated, and interactive visualizations.
    
*   **SciPy**: For Z-score outlier detection.
    

Install all dependencies with:

```bash
pip install -r requirements.txt
```

(You can create a requirements.txt file with the following content:)

```bash
numpy
pandas
seaborn
matplotlib
scipy
```

🔍 Data Source
--------------

The dataset Real\_Estate\_Sales\_2001-2022\_GL.csv contains real estate sales data from 2001 to 2022. Key columns include:

*   List Year
    
*   Town
    
*   Sale Amount
    
*   Assessed Value
    
*   Sales Ratio
    
*   Property Type
    
*   Residential Type
    

Ensure your CSV file matches this structure for the script to work correctly.

🎨 Customization
----------------

*   **Styling**: Modify plt.style.use('dark\_background') or sns.set\_palette("husl") to change the visual theme.
    
*   **Chart Sizes**: Adjust figsize=(12, 8) in each plot for different dimensions.
    
*   **Outlier Threshold**: Change z\_scores < 3 to adjust outlier sensitivity.
    

📜 License
----------

This project is licensed under the MIT License. See the file for details.

🙌 Contributing
---------------

Contributions are welcome! To contribute:

1.  Fork the repository.
    
2.  Create a new branch (git checkout -b feature-branch).
    
3.  Make your changes and commit (git commit -m "Add feature").
    
4.  Push to the branch (git push origin feature-branch).
    
5.  Open a Pull Request.
    

📧 Contact
----------

For questions or suggestions, feel free to reach out:

*   **Email**: [mail me here](mailto:mansityagi472@gmail.com)
    
*   **GitHub**: [click here](https://github.com/mansityagi01)
    

Happy analyzing! 🏠📊
