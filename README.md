#  Numerical Methods for Mathematical Physics: Boundary Value Problems

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-orange.svg)
![NumPy](https://img.shields.io/badge/NumPy-Math-lightblue.svg)

##  Project Overview
This repository contains my coursework project on **"Numerical Methods for Mathematical Physics"**, completed at Samara National Research University. The project focuses on solving a boundary value problem that models the diffusion of a substance in a porous tube with absorption using the **finite difference method (explicit scheme)**.

##  Physical Problem Statement
The problem models a tube of length $l$ filled with a porous, absorbing material (porosity coefficient $c$, absorption coefficient $D$, diffusion coefficient $a$). One end of the tube is closed, and the other is immersed in a solution with a time-varying concentration $\gamma(t)$.

The diffusion process is described by the following partial differential equation (PDE):
$$c \frac{\partial u}{\partial t} = a \frac{\partial^2 u}{\partial x^2} - D u, \quad 0 \le x \le l, \quad 0 < t \le T$$

**Initial Condition:**
$$u(x, 0) = 0, \quad 0 \le x \le l$$

**Boundary Conditions:**
$$\frac{\partial u}{\partial x} \bigg|_{x=l} = 0, \quad 0 \le t \le T$$
$$u(0, t) = \gamma(t), \quad 0 < t \le T$$

Where $\gamma(t) = \sin^2\left(\frac{2\pi t}{T}\right)$.

##  Numerical Solution: Explicit Difference Scheme
To approximate the continuous PDE, we discretize the domain using a uniform grid with spatial step $h_x$ and time step $h_t$. The continuous derivatives are replaced by finite differences.

The resulting **modified explicit difference scheme** is:
$$c \frac{u_i^{k+1} - u_i^k}{h_t} = a \frac{u_{i+1}^k - 2u_i^k + u_{i-1}^k}{h_x^2} - D u_i^k$$

Rearranging to solve for the next time step $u_i^{k+1}$:
$$u_i^{k+1} = u_i^k + \frac{h_t}{c} \left( a \frac{u_{i+1}^k - 2u_i^k + u_{i-1}^k}{h_x^2} - D u_i^k \right)$$

### Theoretical Analysis
* **Approximation:** The scheme approximates the original problem with an error of order $\mathcal{O}(h_t + h_x^2)$.
* **Stability:** The explicit scheme is conditionally stable. Theoretical analysis proves stability under the Courant-Friedrichs-Lewy (CFL) condition: $\gamma \le \frac{1 - \delta}{2}$, where $\gamma = \frac{a h_t}{h_x^2}$ and $\delta = D h_t$.

##  Implementation
The algorithm is implemented in **Python** using `numpy` for efficient array operations and `matplotlib` for generating comparative plots. 

The program calculates both:
1.  **Numerical Solution:** Using the explicit scheme outlined above.
2.  **Analytical Solution:** Computed using Fourier series expansion for rigorous validation.

`<!-- <div align="center"><img width="600" src="[link_to_image](https://github.com/user-attachments/assets/0ee74c35-c542-45a7-9f59-7044432daa6d)" /></div> -->`


##  Results and Visualization

The numerical experiments confirmed the theoretical findings. 
1. **Convergence:** As the grid is refined (decreasing $h_x$ and $h_t$), the numerical solution converges visually and quantitatively to the analytical Fourier series solution.
2. **Stability:** Running the simulation with grid parameters violating the stability condition explicitly demonstrates unbounded numerical oscillations (instability).

*(Note: You can replace these placeholders with the actual generated plots from your Python script)*

**Concentration vs. Time $u(t)$ at fixed $x=4$**
`<!-- <div align="center"><img width="800" alt="u(t) plot" src="link_to_plot_1" /></div> -->`

**Concentration vs. Coordinate $u(x)$ at fixed $t=115$**
`<!-- <div align="center"><img width="800" alt="u(x) plot" src="link_to_plot_2" /></div> -->`
