import numpy as np
from scipy.integrate import solve_ivp
from bokeh.plotting import figure, show
from bokeh.io import output_file

def reaction_rates(t, y, k):
    rate_A = -k * y[0]**1.25 * y[1]**0.59
    rate_B = -k * y[0]**1.25 * y[1]**0.59
    return [rate_A, rate_B]

# Parametreleri tanımlayın
A0 = 1.0  # mol/L
B0 = 2.0  # mol/L
k = 0.5  # L^(0.66)/(mol^(0.66)*s)
t_span = (0, 10)
initial_conditions = [A0, B0]

# ODE çözümünü elde etmek için solve_ivp fonksiyonunu kullanın
sol = solve_ivp(reaction_rates, t_span, initial_conditions, args=(k,), dense_output=True)

# Zaman aralığını ve çözümü oluşturun
t_values = np.linspace(t_span[0], t_span[1], 500)
y_values = sol.sol(t_values)

# Grafiği oluşturun
output_file("mixed_order_reaction.html")
p = figure(title="1.25 & 0.59 Order Reaction", x_axis_label="Time (s)", y_axis_label="Concentration (mol/L)")
p.line(t_values, y_values[0], line_width=2, legend_label="[A]", color="blue")
p.line(t_values, y_values[1], line_width=2, legend_label="[B]", color="red")
p.legend.location = "top_right"

# Grafiği gösterin
show(p)