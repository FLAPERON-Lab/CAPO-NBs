# SPDX-FileCopyrightText: 2026 Carmine Varriale <C.varriale@tudelft.nl>
# SPDX-FileCopyrightText: 2026 Federico Angioni <F.angioni@student.tudelft.nl>
# SPDX-FileCopyrightText: 2026 Maarten van Hoven <M.B.vanHoven@tudelft.nl>
#
# SPDX-License-Identifier: Apache-2.0
import marimo

__generated_with = "0.13.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""# Fundamentals""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    <div class="nav-links">
      <a href="?file=Scope.py">&larr; Scope</a>
      <span></span>
    </div>
    """
    )
    return


if __name__ == "__main__":
    app.run()
