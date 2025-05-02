import marimo

__generated_with = "0.13.3"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import _defaults as defs

    defs.set_plotly_template()
    mo.sidebar(
        defs.sidebar,
        width="300px",
        # footer=mo.md(""),
    )
    return defs, mo


@app.cell
def _(mo):
    mo.md("""# Nomenclature""")
    return


@app.cell
def _(mo):
    mo.md(r"""## List of symbols""")
    return


@app.cell
def _(mo):
    mo.md(r"""## List of acronyms""")
    return


@app.cell
def _(defs, mo):
    nav_foot = mo.nav_menu(
        {
            f"{defs._fileurl}Scope.py": f"{mo.icon('lucide:arrow-big-left')} Scope",
            f"{defs._fileurl}Atmosphere.py": f"Atmosphere {mo.icon('lucide:arrow-big-right')}",
        }
    ).center()
    nav_foot
    return


if __name__ == "__main__":
    app.run()
