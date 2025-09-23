import numpy as np
import plotly.graph_objects as go


class GraphPlotter:
    def __init__(self):
        self.allowed_vars = {
            'cos': np.cos, 'sin': np.sin, 'tan': np.tan,
            'pi': np.pi, 'sqrt': np.sqrt,
            'log': np.log, 'ln': np.log,
            'exp': np.exp,
            'abs': np.abs,
        }
        self.define_helper_functions()

    def define_helper_functions(self):

        def cot(x) :
            return 1/np.tan(x)
        def sec(x):
            return 1 / np.cos(x)
        def cosec(x):
            return 1 / np.sin(x)

        self.allowed_vars['cot'] = cot
        self.allowed_vars['sec'] = sec
        self.allowed_vars['cosec'] = cosec

    def plot_surface(self, x_eq, y_eq, z_eq, u_range, v_range):

        try:
            u = np.linspace(u_range[0], u_range[1], 100)
            v = np.linspace(v_range[0], v_range[1], 100)
            U, V = np.meshgrid(u, v)

            local_vars = {**self.allowed_vars, 'u': U, 'v': V}

            # Safely evaluate user's equations
            X = eval(x_eq, {"__builtins__": None}, local_vars)
            Y = eval(y_eq, {"__builtins__": None}, local_vars)
            Z = eval(z_eq, {"__builtins__": None}, local_vars)

            # Create the Plotly figure
            fig = go.Figure(data=[go.Surface(z=Z, x=X, y=Y, colorscale='viridis')])
            return fig, True

        except Exception as e:
            return str(e), False