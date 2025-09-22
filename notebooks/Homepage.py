import marimo

__generated_with = "0.15.2"
app = marimo.App(width="medium")


@app.cell
def _():
    # Initialization code that runs before all other cells
    import marimo as mo

    # Import dependencies
    from core import _defaults

    # Set local/online filepath
    _defaults.FILEURL = _defaults.get_url()

    # Plotly dark mode template
    _defaults.set_plotly_template()

    # Data directory
    data_dir = str(mo.notebook_location() / "public" / "AircraftDB_Standard.csv")
    return (mo,)


@app.cell
def _():
    # Set navbar on the right
    _defaults.set_sidebar()
    return


@app.cell
def _(mo):
    mo.md("# FPAO-CC \n").center()
    return


@app.cell
def _(mo):
    mo.md(
        """## Flight Performance Analysis and Optimization: from Calculus to Computers"""
    ).center()
    return


if __name__ == "__main__":
    app.run()
