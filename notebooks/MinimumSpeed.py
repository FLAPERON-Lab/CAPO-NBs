import marimo

__generated_with = "0.13.15"
app = marimo.App(width="medium")

with app.setup:
    # Initialization code that runs before all other cells
    import marimo as mo
    import _defaults

    _defaults.set_plotly_template()


@app.cell
def _():
    _defaults.set_sidebar()
    return


@app.cell
def _():
    mo.md(r"""# Minimum airspeed""")
    return


@app.cell
def _():
    mo.md(r"""## Unconstrained optimization problem""")
    return


@app.cell
def _():
    mo.callout(
        mo.md(
            r"""
        Find the minimum airspeed by changing the lift coefficient and throttle within certain limits:

    $$
    \begin{aligned}
        \min_{C_L, \delta_T} 
        & \quad V \\
        % \text{subject to} 
        % & \quad \bm{c}_\mathrm{eq}(\bm{x},\bm{u}; \bm{p}) = 0 \\
        % & \quad \bm{c_\mathrm{ineq}}(\bm{x},\bm{u}; \bm{p}) \le 0 \\
        \text{for } 
        & \quad C_L \in [0, C_{L_\mathrm{max}}] \\
        & \quad \delta_T \in [0, 1]
    \end{aligned}
    $$
        """
        )
    ).center().style({"text-align": "center"})
    return


@app.cell
def _():
    mo.md(
        r"""
    This problem is ill posed, and it does not make sense to solve it.

    There is no functional relation between the objective function $V$ and the controls $C_L, \delta_T$.
    In other words, there is no equation that specifies how $V$ is allowed to change with respect to the controls. 

    For example, the minimum airspeed achievable could be 0, if the aircraft is standing still on the runway.
    It could even be negative, if someone is pushing the aircraft back, or there is tailwind.

    A relation must be introduced with constraint equatios, starting from the EoMS.
    These will define the problem properly.
    """
    )
    return


@app.cell
def _():
    mo.md(r"""- [ ] Plot a 2D chart with CL on x axis and dT on y axis, and a 3D chart with also V on Z axis (with nothing plotted on it). There is a selection menu for only one aircraft at a time, which is useless (but that's the point). Two sliders allow to pick a value of Cl and dT. The chart shows only the one point in the domain corresponding to the chosen values.""")
    return


@app.cell
def _():
    mo.md(r"""## Constrained optimization problem""")
    return


@app.cell
def _():
    mo.callout(
        mo.md(r"""
        Find the minimum airspeed that can be maintained in Steady Level Flight by changing the lift coefficient and throttle within certain limits

    $$
    \begin{aligned}
        \min_{C_L, \delta_T} 
        & \quad V \\
        \text{subject to} 
        & \quad c_1^\mathrm{eq} = \frac{1}{2}\rho V^2 S C_L - W = 0 \\
        & \quad c_2^\mathrm{eq} = \delta_T T_a(V,h) - \frac{1}{2} \rho V^2 S (C_{D_0}+K C_L^2) =0 \\
        \text{for } 
        & \quad C_L \in [0, C_{L_\mathrm{max}}] \\
        & \quad \delta_T \in [0, 1]
    \end{aligned}
    $$
        """)
    ).center().style({"text-align": "center"})
    return


@app.cell
def _():
    mo.md(
        r"""
    The introduction of the constraints for vertical ($c_1^\mathrm{eq}$) and horizontal equilibrium ($c_2^\mathrm{eq}$) restricts the scope to only a certain type of optimal speeds we are looking for. 

    The constraint equations introduce a functional dependency between the objective function and the controls.
    We are going to use them to reformulate the problem in order to analyse its properties.

    Before that, we notice that the expression of $c_2^\mathrm{eq}$ depends on the type of powertrain of the aircraft, and therefore we must proceed diffently for each powertrain architecture.
    """
    )
    return


@app.cell
def _():
    mo.accordion(
        {
            "## Simplified Jet Aircraft": mo.vstack(
                [
                    mo.md(r"""

    $T_a(V,h) = T_a(h) = T_{a0}\sigma^\beta$

    ### Direct elimination of $c_1^\mathrm{eq}$

    In this case we express the objective function $V$ and other constraints in terms of the control variables by solving $c_1^\mathrm{eq} = 0$ for $V$.

    $$ c_1^\mathrm{eq} = 0 \quad \Rightarrow \quad V = \sqrt{\frac{2W}{\rho S C_L}} $$

    With this, we are limiting our attention to only the airspeeds that are intrinsically capable to guarantee vertical equilibrium thanks to the lift-generating capabilities of the aircraft.
    In other words, we are looking for the _stall speed_.

    """),
                    mo.callout(
                        mo.md(
                            r"""The stall speed $V_s$ is the minimum airspeed at which an aircraft can sustain its weight in Steady Level Flight """
                        )
                    ).style({"text-align": "center"}),
                    mo.callout(
                        mo.md(
                            r"""Find the minimum speed, among those that intrinsically guarantee vertical equilibrium, which is also able to guarantee horizontal equilibrium, by changing the lift coefficient and throttle within certain limits

    $$
    \begin{aligned}
        \min_{C_L, \delta_T} 
        & \quad V = \sqrt{\frac{2W}{\rho S C_L}} \\
        \text{subject to}
        & \quad c_2^\mathrm{eq} = \frac{\delta_T T_{a0}\sigma^\beta}{W} - \frac{C_{D_0} + K C_L^2}{C_L} =0 \\
        \text{for } 
        & \quad C_L \in [0, C_{L_\mathrm{max}}] \\
        & \quad \delta_T \in [0, 1]
    \end{aligned}
    $$  
    """
                        )
                    ).style({"text-align": "center"}),
                    mo.md(
                        r"""
                        In light of the previous substitution, $V$ has now been eliminated from the expression of the objective and the constraint equations.
                        It is now possible to analyse their behaviour as a function of the control variables only.
                        Also, notice how the constraint now expresses the fact that the thrust-to-weight ratio has to be equal to the inverse of the lift-to-drag ratio.

                        - [ ] Same plots as before, this time showing c2eq as a curve in the domain. The 2D plot becomes a contour plot of V, where the constraint curve is also visible.
                        """
                    ),
                    mo.md(
                        r"""
                        ### Monotonicity analysis

                        $V$ does not depend on $\delta_T$ and is monotonically decreasing with $C_L$. 
                        Therefore, it is mininimum at the maximum allowable value of $C_L$.
                    
                        $$
                        V_s = \sqrt{\frac{2W}{\rho S C_{L_\mathrm{max}}}}
                        $$

                        But this optimum value of $C_L$ has to correspond to a specific value of $\delta_T$ which verifies the constraint $c_2^\mathrm{eq}$ for horizontal equilibrium.
                        In other words, we have to make sure that it is possible to fly at the maximum lift coefficient and, if yes, under which conditions.

                        Combining $c_2^\mathrm{eq}$ and the bounds for $\delta_T$ we obtain the following condition that has to be satisfied for $V_s$ to be valid solution to the constrained optimization problem:

                        $$
                        0 \le \delta_T = \frac{W}{T_{a0}\sigma^\beta} \frac{C_{D_0} + K C^2_{L_\mathrm{max}}}{C_{L_\mathrm{max}}} \le 1
                        $$

                        The first inequality is always satisfied, so it is only relevant to analyse the second one.
                        It can be rearranged to draw conclusions on the basis of flight and aircraft parameters.

                        $$
                        \frac{W}{\sigma^\beta} \le T_{a0} \frac{C_{L_\mathrm{max}}}{C_{D_0}+KC^2_{L_\mathrm{max}}}
                        $$

                        This condition should be interpreted as follows:
                    
                        - if $W/\sigma^\beta$ is below a the threshold value ($<)$ (low weight and/or low altitude), the minimum speed in Steady Level Flight is obtained at $C_L = C_{L_\mathrm{max}}$ and $\delta_T<1$, and is indeed the stall speed $V_s$;
                        - if $W/\sigma^\beta$ is exactly equal to the threshold value ($=$), the minimum speed in Steady Level Flight is obtained at $C_L = C_{L_\mathrm{max}}$ and $\delta_T=1$, and is limited both by lift-generating capabilities and propulsive ones (it is still a stall speed); this condition can be used to calculate the highest altitude at which the minimum speed is still limited by aerodynamics, for a certain weight;
                        - [ ] Plot in the flight envelope
                        - if $W/\sigma^\beta$ is above the threshold value ($>$) (high weight and/or high altitude), the current approach does not allow to find a minimum speed; in other words, the minimum speed is not a stall speed, and we need to look for solutions obtained for $C_L < C_{L_\mathrm{max}}$.
                        """
                    ),
                    mo.md(r"""### Direct elimination of $c_2^\mathrm{eq}$

                        In this case we express the objective function $V$ and other constraints in terms of the control variables by solving $c_2^\mathrm{eq} = 0$ for $V$.

    $$ 
    c_2^\mathrm{eq} = 0 
    \quad \Rightarrow \quad 
    V = \sqrt{ \frac{2 \delta_T T_{a0}\sigma^\beta}{\rho S (C_{D_0}+K C_L^2)} } 
    =   V_s \sqrt{  \frac{\delta_T T_{a0}\sigma^\beta}{W} \frac{C_{L_\mathrm{max}}}{C_{D_0}+K C_L^2}}
    $$

    With this, we are limiting our attention to only the airspeeds that are intrinsically capable to guarantee horizontal equilibrium thanks to the thrust-generating capabilities of the aircraft.
    In other words, we are looking for the _power-limited speed_.
                        """),
                    mo.callout(
                        mo.md(
                            r"""Find the minimum speed, among those that intrinsically guarantee horizontal equilibrium, which is also able to guarantee vertical equilibrium, by changing the lift coefficient and throttle within certain limits.

    $$
    \begin{aligned}
        \min_{C_L, \delta_T} 
        & \quad V = V_s \sqrt{  \frac{\delta_T T_{a0}\sigma^\beta}{W} \frac{C_{L_\mathrm{max}}}{C_{D_0}+K C_L^2}} \\
        \text{subject to}
        & \quad c_1^\mathrm{eq} = \frac{\delta_T T_{a0}\sigma^\beta}{W} - \frac{C_{D_0} + K C_L^2}{C_L} =0 \\
        \text{for } 
        & \quad C_L \in [0, C_{L_\mathrm{max}}] \\
        & \quad \delta_T \in [0, 1]
    \end{aligned}
    $$
    """
                        )
                    ),
                    mo.md(r"""                
                    Even if the constraint is exactly the same as in the previous direct elimination, the expression of the objective function is different, allowing us to make different considerations.

    - [ ] Same plots as before, this time showing c2eq as a curve in the domain. The 2D plot becomes a contour plot of V, where the constraint curve is also visible.

    ### Monotonicity analysis
            
                    The objective function can now be appreciated as a monotonically decreasing function of $C_L$ (leading to similar considerations as before) and a monotically increasing function of $\delta_T$.

                    Its unconstrained minimum should therefore be sought for $\delta_T = 0$, but for this value the constraint would never be verified.
                    The question comes then spontaneous: what is the minimum value of $\delta_T$ that satisfies the constraint? This is an unconstrained optimization sub-problem of a continuous bounded function, that can be easily solved.

    $$
    \begin{aligned}
        \min_{C_L} 
        & \quad \delta_T = \frac{W}{T_{a0}\sigma^\beta} \frac{C_{D_0}+K C_L^2}{C_L} \\
        \text{for } 
        & \quad C_L \in [0, C_{L_\mathrm{max}}]
    \end{aligned}
    $$

    The interior minimum is found by equating the gradient of the objecitive function to zero.
    It can be easily verified that this is indeed a minimum by looking at the convexity of the function.

    $$
    \delta_T^\dag =\frac{W \sqrt{4 K C_{D_0}}}{T_{a0}\sigma^\beta}  = \frac{W}{E_\mathrm{max} T_{a0}\sigma^\beta} 
    \quad \text{obtained for} \quad 
    C_L^\dag = \sqrt{\frac{C_{D_0}}{K}}=C_{L_{|_{E_\mathrm{max}}}}
    $$

    Moreover, $\delta_T$ is undefined for $C_L=0$, and the analysis falls back on the previous one for $C_L=C_{L_\mathrm{max}}$.
    Therefore, the only interesting minimum is the interior one.

    The airspeed obtainable for the minimum _feasible_ value of the throttle is obtained by substituting $\delta_T^\dag$ and $C_L^\dag$ in the expression of the objective function.

    $$
    V^\dag = V_s \sqrt{\frac{C_{L_{\mathrm{max}}}}{C_{L_{|_{E_\mathrm{max}}}}}} \ge V_s
    $$

    This tells us that such airspeed is not a minimum airspeed (apart from the limit case), and minimimizing the throttle is not a convenient strategy to minimimize the airspeed.
    Reducing the throttle makes it necessary to increase the lift coefficient to remain in Steady Level Flight, and this has the effect of overall increasing the airspeed.
    In other words, a change in lift coefficient has a stronger impact on the airspeed than a change in throttle.

    Because $V$ remains monotonically increasing with $\delta_T$ and minimizing the latter has proven to be not a successful strategy, the last analysis remaining to be done is the one for the maximum value of $\delta_T$.

    For $\delta_T=1$, the problem becomes

    $$
    \begin{aligned}
        \min_{C_L} 
        & \quad V = V_s \sqrt{  \frac{T_{a0}\sigma^\beta}{W} \frac{C_{L_\mathrm{max}}}{C_{D_0}+K C_L^2}} \\
        \text{subject to}
        & \quad c_1^\mathrm{eq} = \frac{ T_{a0}\sigma^\beta}{W} - \frac{C_{D_0} + K C_L^2}{C_L} =0 \\
        \text{for } 
        & \quad C_L \in [0, C_{L_\mathrm{max}}] \\
    \end{aligned}
    $$

    The objective function is monotonically decreasing with $C_L$, and the case for $C_L=C_{L_\mathrm{max}}$ has already been analysied.
    The question now is: are there other values of $C_L$ that verify the constraint and minimize airspeed at full throttle?
    Contrarily to the previous case, the constraint is implicit in $C_L$ itself, and therefore it is not possible to rewrite the bounds for $C_L$ as inequality constraints for other parameters.
    Of the two possible values of $C_L$ that verify the constraint, the highest one is obtained using the quadratic formula:

    $$
    0 \le 
    C_L^\dag = \frac{T_{a0}\sigma^\beta}{2KW} \left[1+\sqrt{1-\left(\frac{W}{E_\mathrm{max}T_{a0}\sigma^\beta}\right)^2}\right]
    \le C_{L_\mathrm{max}}
    $$

    It is hard to compare this expression to $C_{L_\mathrm{max}}$ explicitly, so a graphical representation is provided to discuss its feasibility for different aircraft.

    - [ ] Plot $C_L^\dag$ as a function of $W/\sigma^\beta$ for an aircraft of choice

    At the same time, this value of $C_L$ is even just achievable by the aircraft if the following condition is met:

    $$
    1-\left(\frac{W}{E_\mathrm{max}T_{a0}\sigma^\beta}\right)^2 \ge 0 
    \quad \Leftrightarrow \quad
    \frac{W}{\sigma^\beta} \le E_\mathrm{max} T_{a0}
    $$

    meaning that:

    - if $W/\sigma^\beta$ is above the threshold value ($>$) (high weight and/or high altitude), the aircraft is not able to fly at $\delta_T=1$ in Steady Level Flight.

    - if $W/\sigma^\beta$ is exactly equal to the threshold value ($=$), the aircraft is able to fly in Steady Level Flight at $\delta_T=1$, and $C_L=C_L^\dag=C_{L_{|_{E_\mathrm{max}}}}$; the corresponding airspeed is again $V_s\sqrt{C_{L_\mathrm{max}}/C_{L_{|_{E_\mathrm{max}}}}}$, which is the only possible airspeed, and hence also the minimum;

    - if $W/\sigma^\beta$ is below the threshold value ($<)$ (low weight and/or low altitude), the aircraft is able to fly at $\delta_T=1$ and $C_L=C_L^\dag$, but the corresponding airspeed may not be lower than the minimum speed obtained in other cases; its expression is:

    $$
    V^\dag = V_s \sqrt{\frac{2KWC_{L_\mathrm{max}}}{T_{a0}\sigma^\beta \left[1+\sqrt{1-\left(\frac{W}{E_\mathrm{max}T_{a0}\sigma^\beta}\right)^2}\right]}}
    $$

    - [ ] Plot this expression in the flight envelope, together with all the other expressions of speeds obtained before

                    
                    """),
                ]
            ),
            "## Simplified Propeller Aircraft": mo.md("TODO"),
        }
    )
    return


@app.cell
def _():
    _defaults.nav_footer("AerodynamicEfficiency.py", "Aerodynamic Efficiency", "", "")
    return


if __name__ == "__main__":
    app.run()
