# import numpy as np
# import plotly.graph_objects as go
#
#
# class PolarCurvePlotter:
#     """
#     Handles the evaluation of 3D polar curve equations and the generation
#     of the Plotly 3D scatter plot.
#     """
#
#     def __init__(self):
#         """Initializes the allowed mathematical functions for safe evaluation."""
#         self.allowed_vars = {
#             'cos': np.cos, 'sin': np.sin, 'tan': np.tan,
#             'pi': np.pi, 'sqrt': np.sqrt,
#             'log': np.log, 'ln': np.log, 'exp': np.exp, 'abs': np.abs,
#         }
#         self.define_helper_functions()
#
#     def define_helper_functions(self):
#         """Defines and adds helper functions to the allowed variables."""
#
#         def cot(x):
#             return 1 / np.tan(x)
#
#         def sec(x):
#             return 1 / np.cos(x)
#
#         def cosec(x):
#             return 1 / np.sin(x)
#
#         self.allowed_vars['cot'] = cot
#         self.allowed_vars['sec'] = sec
#         self.allowed_vars['cosec'] = cosec
#         self.allowed_vars['power'] = np.power
#
#     def plot_curve(self, rho_eq, theta_eq, phi_eq, t_range):
#         """
#         Generates the Plotly figure from the given equations and parameters.
#         Returns the figure object and a success status.
#         """
#         try:
#             # Create a range for the single parameter 't'
#             t = np.linspace(t_range[0], t_range[1], 1000)
#
#             # Add t to the allowed variables for evaluation
#             local_vars = {**self.allowed_vars, 't': t}
#
#             # Evaluate user's equations for rho, theta, and phi
#             rho = eval(rho_eq, {"__builtins__": None}, local_vars)
#             theta = eval(theta_eq, {"__builtins__": None}, local_vars)
#             phi = eval(phi_eq, {"__builtins__": None}, local_vars)
#
#             # Convert from spherical to Cartesian coordinates
#             x = rho * np.sin(phi) * np.cos(theta)
#             y = rho * np.sin(phi) * np.sin(theta)
#             z = rho * np.cos(phi)
#
#             # Create the Plotly figure
#             fig = go.Figure(data=[go.Scatter3d(
#                 x=x, y=y, z=z,
#                 mode='lines',
#                 marker=dict(size=2, color=t, colorscale='viridis'),
#                 line=dict(color=t, colorscale='viridis', width=4)
#             )])
#
#             return fig, True
#
#         except Exception as e:
#             return str(e), False
import numpy as np
import plotly.graph_objects as go

class PolarPlotter:
    """
    Handles the evaluation of 3D polar equations and the generation
    of both curves and surfaces.
    """

    def __init__(self):
        """Initializes the allowed mathematical functions for safe evaluation."""
        self.allowed_vars = {
            'cos': np.cos, 'sin': np.sin, 'tan': np.tan,
            'pi': np.pi, 'sqrt': np.sqrt,
            'log': np.log, 'ln': np.log, 'exp': np.exp, 'abs': np.abs,
        }
        self.define_helper_functions()

    def define_helper_functions(self):
        """Defines and adds helper functions to the allowed variables."""

        def cot(x):
            return 1 / np.tan(x)

        def sec(x):
            return 1 / np.cos(x)

        def cosec(x):
            return 1 / np.sin(x)

        self.allowed_vars['cot'] = cot
        self.allowed_vars['sec'] = sec
        self.allowed_vars['cosec'] = cosec
        self.allowed_vars['power'] = np.power

    def plot_surface(self, rho_eq, theta_eq, phi_eq, u_range, v_range):
        """Generates a 3D polar surface."""
        try:
            u = np.linspace(u_range[0], u_range[1], 100)
            v = np.linspace(v_range[0], v_range[1], 100)
            U, V = np.meshgrid(u, v)

            local_vars = {**self.allowed_vars, 'u': U, 'v': V}

            rho = eval(rho_eq, {"__builtins__": None}, local_vars)
            theta = eval(theta_eq, {"__builtins__": None}, local_vars)
            phi = eval(phi_eq, {"__builtins__": None}, local_vars)

            # Convert from spherical to Cartesian coordinates
            x = rho * np.sin(phi) * np.cos(theta)
            y = rho * np.sin(phi) * np.sin(theta)
            z = rho * np.cos(phi)

            fig = go.Figure(data=[go.Surface(x=x, y=y, z=z, colorscale='viridis')])
            return fig, True

        except Exception as e:
            return str(e), False

    def plot_curve(self, rho_eq, theta_eq, phi_eq, t_range):
        """Generates a 3D polar curve."""
        try:
            # A curve uses a single parameter 't'
            t = np.linspace(t_range[0], t_range[1], 1000)
            local_vars = {**self.allowed_vars, 't': t}

            rho = eval(rho_eq, {"__builtins__": None}, local_vars)
            theta = eval(theta_eq, {"__builtins__": None}, local_vars)
            phi = eval(phi_eq, {"__builtins__": None}, local_vars)

            # Convert from spherical to Cartesian coordinates
            x = rho * np.sin(phi) * np.cos(theta)
            y = rho * np.sin(phi) * np.sin(theta)
            z = rho * np.cos(phi)

            # Use a scatter plot with 'lines' mode for the curve
            fig = go.Figure(data=[go.Scatter3d(
                x=x, y=y, z=z,
                mode='lines',
                line=dict(color=t, colorscale='viridis', width=4)
            )])
            return fig, True

        except Exception as e:
            return str(e), False