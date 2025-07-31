import marimo

__generated_with = "0.13.8"
app = marimo.App(width="medium")

with app.setup:
    # Initialization code that runs before all other cells
    import marimo as mo
    from core import _defaults

    _defaults.FILEURL = _defaults.get_url()

    _defaults.set_plotly_template()


@app.cell
def _():
    _defaults.set_sidebar()
    return


@app.cell
def _():
    mo.md(
        r"""
    # Minimum Power Required: simplified jet aircraft

    $$
    \begin{aligned}
        \min_{C_L, \delta_T} 
        & \quad P = DV = \frac{1}{2}\rho V^2S(C_{D_0}+KC_L^2)V \\
        \text{subject to} 
        & \quad c_1^\mathrm{eq} = L-W = \frac{1}{2}\rho V^2 S C_L - W = 0 \\
        & \quad c_2^\mathrm{eq} = T-D = \delta_T T_a(V,h) - \frac{1}{2} \rho V^2 S (C_{D_0}+K C_L^2) =0 \\
        \text{for } 
        & \quad C_L \in [0, C_{L_\mathrm{max}}] \\
        & \quad \delta_T \in [0, 1] \\
        \text{with } 
        & \quad T_a(V,h) = \frac{P_a(h)}{V} = \frac{P_{a0}\sigma^\beta}{V} \\
    \end{aligned}
    $$
    """
    )
    return


@app.cell
def _():
    mo.md(
        r"""
    ## KKT formulation
    To be reconducted in the standard KKT analysis format, the objective function is expressed in terms of the controls by direct elimination of $c_1^\mathrm{eq}$. The velocity $V$ can be expressed as: 

    $$
    V = \sqrt{\frac{2}{\rho}\frac{W}{S}\frac{1}{C_L}}
    $$

    Moreover, in previous analyses we found $\delta_T=C_L=0$ does not correspond to a sensible solution, thus we can write:

    $$
    0\lt \delta_T \le 1 \quad \land \quad  0\lt C_L\le C_{L_{\mathrm{max}}}
    $$

    Notice the open interval in the lower bounds.
    """
    )
    return


@app.cell
def _():
    mo.md(
        r"""
    The KKT formulation can now be written: 

    $$
    \begin{aligned}
        \min_{C_L, \delta_T} 
        & \quad P = DV = W \left(\frac{C_{D_0} +K C_L^2}{C_L}\right)\sqrt{\frac{2}{\rho}\frac{W}{S}\frac{1}{C_L}}=\sqrt{\frac{2W^3}{\rho S}}\left(\frac{C_{D_0}+K C_L^2}{C_L^{3/2}}\right) = \sqrt{\frac{2W^3}{\rho S}}\left(C_{D_0} C_L^{-3/2}+K C_L^{1/2}\right)\\
        \text{subject to} 
        & \quad g_1 = T - W\, \frac{1}{E}  =\frac{\delta_T P_{a0}\sigma^\beta}{V} - W\frac{C_{D_0} + K C_L^2}{C_L} = 0 \quad \Rightarrow \quad \delta_T P_{a0}\sigma^\beta - \sqrt{\frac{2W^{3}}{\rho S}} \left(C_{D_0} C_L^{-3/2}+K C_L^{1/2}\right) = 0\\
        & \quad h_1 = C_L - C_{L_\mathrm{max}} \le 0 \\
        & \quad h_2 = \delta_T - 1 \le 0 \\
    \end{aligned}
    $$
    """
    )
    return


@app.cell
def _():
    mo.md(
        r"""
    ### Lagrangian function and KKT conditions

    The Lagrangian function combines the objective function with eqaulity constraints using Lagrange multipliers ($\lambda_i$) and inequality constraints using KKT multipliers ($\mu_j$).

    $$
    \begin{aligned}
    \mathcal{L}(C_L, \delta_T, \lambda_1, \mu_1, \mu_2) = & P + \lambda_1 \left[T - D\right]+ \mu_1 (C_L - C_{L_\mathrm{max}}) +\mu_2 (\delta_T - 1)\\ 
    =&\quad \sqrt{\frac{2W^3}{\rho S}}\left(C_{D_0} C_L^{-3/2}+K C_L^{1/2}\right)(1 - \lambda_1) +\\
    & + \lambda_1 \delta_T P_{a0}\sigma^\beta \\
    & + \mu_1 (C_L - C_{L_\mathrm{max}}) + \\
    & + \mu_2 (\delta_T - 1) +\\
    \end{aligned}
    $$
    """
    )
    return


@app.cell
def _():
    mo.md(
        r"""
    A necessary condition for an optimal solution of the optimization problem $(C_L^*, \delta_T^*)$ to exist, the multipliers $\lambda_1, \mu_1, \mu_2$ have to meet the following conditions:

    **A. Stationarity ($\nabla L = 0$):** the gradient of the Lagrangian with respect to each decision variable must be zero

    1. $\displaystyle \frac{\partial \mathcal{L}}{\partial C_L} = \sqrt{\frac{2W^3}{\rho S}}\left(-\frac{3}{2}C_{D_0}C_L^{-5/2} + \frac{1}{2} K C_L^{-1/2}\right)(1-\lambda_1) + \mu_1= 0$

    2.  $\displaystyle \frac{\partial \mathcal{L}}{\partial \delta_T} = \lambda_1 P_{a0}\sigma^\beta+ \mu_2= 0$
    """
    )
    return


@app.cell
def _():
    mo.md(
        r"""
    **B. Primal feasibility: constraints are satisfied**

    3.  $\displaystyle \delta_T P_{a0}\sigma^\beta - \sqrt{\frac{2W^{3}}{\rho S}} \left(C_{D_0} C_L^{-3/2}+K C_L^{1/2}\right) = 0$
    4.  $C_L - C_{L_\mathrm{max}} \le 0$
    5.  $\delta_T - 1 \le 0$
    """
    )
    return


@app.cell
def _():
    mo.md(
        r"""
    **C. Dual feasibility: KKT multipliers for inequalities must be non-negative**

    6.  $\mu_1, \mu_2 \ge 0$
    """
    )
    return


@app.cell
def _():
    mo.md(
        r"""
    **D. Complementary slackness ($\mu_j h_j = 0$)**: inactive inequality constraint have null multipliers, as they do not contribute to the objective function. Active inequality constraints have positive multipliers, as they make the objective function worse.

    7.  $\mu_1 (C_L - C_{L_\mathrm{max}}) = 0$
    8. $\mu_3 (\delta_T - 1) = 0$
    """
    )
    return


@app.cell
def _():
    mo.md(
        r"""
    ## KKT analysis

    We can now proceed to systematically examine the conditions where various inequality constraints are active 
    or inactive.

    ### _Interior solutions_ 

    In this case: $C_L \lt C_{L_{\mathrm{max}}}$, $\delta_T \lt 1$, $\mu_1=\mu_2= 0$

    from stationarity condition (2): $\lambda_1 = 0$

    from stationarity condition (1): 

    $$
    -\frac{3}{2}C_{D_0} C_L^{-5/2}+\frac{1}{2}KC_L^{-1/2}= 0 \quad \Rightarrow \quad KC_L^2 = 3C_{D_0} \quad \Rightarrow \quad C_L^* = \sqrt{\frac{3C_{D_0}}{K}} = \sqrt{3}C_{L_E} = C_{L_P}
    $$
    """
    )
    return


@app.cell
def _():
    mo.md(
        r"""
    Before finding the corresponding $\delta_T$ value find the velocity associated with $C_{L_P}$:

    $$
    V_P = \sqrt{\frac{2W}{\rho S}}\sqrt{\frac{K}{3C_{D_0}}}
    $$


    The optimum $\delta_T$ value is obtained from primal feasibility constraint (3), using the velocity for minimum power we find:

    $$
    \delta_T^* = \frac{W}{E_P}\frac{V_P}{P_{a0}\sigma^\beta}
    $$

    Where: $\displaystyle E_{\mathrm{P}} = \frac{\sqrt{3}}{2}E_{\mathrm{max}}$

    This is valid for:  

    $$
    \delta_T^*\lt 1 \Leftrightarrow \frac{W^{3/2}}{\sigma^{\beta+1/2}} \lt \sqrt{\frac{1}{2}\rho_0SC_L^*} \; P_{a0} \,E_P = \sqrt{\frac{3}{2}\rho_0 \frac{C_{D_0}}{K}} \; P_{a0} \,E_P
    $$
    """
    )
    return


@app.cell
def _():
    mo.md(
        r"""
    Finally, the optimum for the interior of the domain is thus:

    $$
    \boxed{C_L^* = \sqrt{\frac{3C_{D_0}}{K}} = \sqrt{3}C_{L_E}} \quad \land \quad \boxed{\delta_T^* = \frac{W}{E_P}\frac{V_P}{P_{a0}\sigma^\beta}} \qquad \mathrm{with} \quad V_P = \sqrt{\frac{2W}{\rho S}\frac{K}{3C_{D_0}}} \qquad \mathrm{for} \quad \frac{W^{3/2}}{\sigma^{\beta+1/2}} \lt \sqrt{\frac{3}{2}\rho_0 \frac{C_{D_0}}{K}} \; P_{a0} \,E_P
    $$
    """
    )
    return


@app.cell
def _():
    mo.md(
        r"""
    ### _Lift limited solutions (stall)_

    In this case: $C_L = C_{L_{\mathrm{max}}}$, $\delta_T \lt 1$, $\mu_1 \gt 0$, $\mu_2= 0$

    from stationarity condition (2): $\lambda_1 = 0$

    from stationarity condition (1):

    $$
    \mu_1 = -\sqrt{\frac{2W^3}{\rho S}}\left(-\frac{3}{2}C_{D_0}C_{L_{\mathrm{max}}}^{-5/2} + \frac{1}{2} K C_{L_{\mathrm{max}}}^{-1/2}\right) \gt 0
    $$

    $$
    \Rightarrow -3C_{D_0}C_{L_{\mathrm{max}}}^{-5/2} + K C_{L_{\mathrm{max}}}^{-1/2} \lt 0 \quad  \Rightarrow \quad C_{L_{\mathrm{max}}} \lt \sqrt{\frac{3C_{D_0}}{K}} = \sqrt{3}C_{L_E} = C_{L_P}
    $$
    """
    )
    return


@app.cell
def _():
    mo.md(
        r"""
    We can give a meaning to this result. If we design an aircraft such that it stalls before reaching $C_{L_P}$ then we obtain minimum power required at stall. 

    - [ ] plot graph showing this
    """
    )
    return


@app.cell
def _():
    mo.md(
        r"""
    We can now calculate the optimal $\delta_T^*$. As before, define the velocity at which the aircraft is flying for a cleaner solution. Note that $C_L = C_{L_{\mathrm{max}}}$ thus the aircraft is flying at stall speed $V_S$: 

    $$
    V_S= \sqrt{\frac{2W}{\rho S C_{L_{\mathrm{max}}}}}
    $$

    The correrponding $\delta_T^*$, found from the primal feasibility constraint (3): 

    $$
    \delta_T^* = \frac{W}{E_S}\frac{V_S}{P_{a0}\sigma^\beta}
    $$

    This is valid for: 

    $$
    \delta_T^*\lt 1 \Leftrightarrow \frac{W^{3/2}}{\sigma^{\beta+1/2}} \lt  \; P_{a0} \,E_S\sqrt{\frac{1}{2}\rho_0SC_{L_{\mathrm{max}}}}
    $$

    """
    )
    return


@app.cell
def _():
    mo.md(
        r"""
    Finally, the optimum for the lift-limited case is:

    $$
    \boxed{C_L^* = C_{L_{\mathrm{max}}}} \quad \land \quad \boxed{\delta_T^* = \frac{W}{E_S}\frac{V_S}{P_{a0}\sigma^\beta}} \qquad \mathrm{with} \quad V_S= \sqrt{\frac{2W}{\rho S C_{L_{\mathrm{max}}}}} \qquad \mathrm{for} \quad \frac{W^{3/2}}{\sigma^{\beta+1/2}} \lt  \; P_{a0} \,E_S\sqrt{\frac{1}{2}\rho_0SC_{L_{\mathrm{max}}}}
    $$
    """
    )
    return


@app.cell
def _():
    mo.md(
        r"""
    ### _Thrust limited solutions (stall)_

    In this case: $C_L \lt C_{L_{\mathrm{max}}}$, $\delta_T = 1$, $\mu_1 = 0$, $\mu_2 \gt 0$

    from stationarity condition (2): $\displaystyle \lambda_1 = -\frac{\mu_2}{P_{a0}\sigma^\beta} \quad \Rightarrow \quad \lambda_1 \lt 0$

    Thus, from stationarity condition (1): 

    $$
    \sqrt{\frac{2W^3}{\rho S}}\left(-\frac{3}{2}C_{D_0}C_L^{-5/2} + \frac{1}{2} K C_L^{-1/2}\right)(1-\lambda_1) = 0 \quad \Rightarrow \quad 1-\lambda_1 \gt 0
    $$

    $$
    \Rightarrow -3C_{D_0}C_L^{-5/2} + KC_L^{1/2} = 0
    $$


    $$
    C_L^* = \sqrt{\frac{3C_{D_0}}{K}} = \sqrt{3}C_{L_E} = C_{L_P}
    $$
    """
    )
    return


@app.cell
def _():
    mo.md(
        r"""
    The condition for which this is true is found using the primal feasibility constraint (3). 

    $$
    \frac{W^{3/2}}{\sigma^{\beta+1/2}} = \sqrt{\frac{3}{2}\rho_0 \frac{C_{D_0}}{K}} \; P_{a0} \,E_P
    $$

    This can be compared with what we found in the interior of the domain, showing the thrust limited case represents the limit case of the interior optima.
    """
    )
    return


@app.cell
def _():
    mo.md(
        r"""
    Finally, the optimum for the thrust-limited case is:

    $$
    \boxed{C_L^* = C_{L_P}} \quad \land \quad \boxed{\delta_T^* = 1} \qquad  \mathrm{for} \quad \frac{W^{3/2}}{\sigma^{\beta+1/2}} = \sqrt{\frac{3}{2}\rho_0 \frac{C_{D_0}}{K}} \; P_{a0} \,E_P
    $$
    """
    )
    return


@app.cell
def _():
    mo.md(
        r"""
    ### _Lift- and thrust- limited optimum_

    In this case: $C_L = C_{L_{\mathrm{max}}}$, $\delta_T = 1$, $\mu_1 \gt 0$, $\mu_2 \gt 0$

    from stationarity condition (2): $\displaystyle \lambda_1 = -\frac{\mu_2}{P_{a0}\sigma^\beta} \quad \Rightarrow \quad \lambda_1 \lt 0$

    Thus, from stationarity condition (1), since $1-\lambda_1 \gt 0$: 

    $$
    \mu_1 = -\sqrt{\frac{2W^3}{\rho S}}\left(-\frac{3}{2}C_{D_0}C_{L_{\mathrm{max}}}^{-5/2} + \frac{1}{2} K C_{L_{\mathrm{max}}}^{-1/2}\right)(1-\lambda_1)\gt 0
    $$

    $$
    \Rightarrow -3C_{D_0}C_{L_{\mathrm{max}}}^{-5/2} + KC_{L_{\mathrm{max}}}^{1/2} \lt 0
    $$


    $$
    \Rightarrow C_{L_{\mathrm{max}}} \lt \sqrt{\frac{3C_{D_0}}{K}} = \sqrt{3}C_{L_E} = C_{L_P}
    $$
    """
    )
    return


@app.cell
def _():
    mo.md(
        r"""
    The condition for which this is true is found using the primal feasibility constraint (3). 

    $$
    \frac{W^{3/2}}{\sigma^{\beta+1/2}} = P_{a0}E_S \sqrt{\frac{1}{2}\rho_0SC_{L_{\mathrm{max}}}}
    $$
    """
    )
    return


@app.cell
def _():
    mo.md(
        r"""
    This is only possible if: 

    $$
    C_{L_{\mathrm{max}}} \lt \sqrt{\frac{3C_{D_0}}{K}}
    $$

    as otherwise it's impossible to minimise power at stall and maximum thrust as the aircraft will reach the unconstrained minium before stalling. 
    """
    )
    return


@app.cell
def _():
    mo.md(
        r"""
    Finally, the optimum for the thrust-limited case is:

    $$
    \boxed{C_L^* = C_{L_\mathrm{max}}} \quad \land \quad \boxed{\delta_T^* = 1} \qquad  \mathrm{for} \quad \frac{W^{3/2}}{\sigma^{\beta+1/2}} = P_{a0}E_S \sqrt{\frac{1}{2}\rho_0SC_{L_{\mathrm{max}}}}
    $$
    """
    )
    return


if __name__ == "__main__":
    app.run()
