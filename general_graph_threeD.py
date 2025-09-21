import streamlit as st
import numpy as np
import plotly.graph_objects as go
import plotly.io as pio

# Set the Plotly renderer for Streamlit to ensure smooth interaction
pio.renderers.default = "browser"


def plot_dynamic_3d_graph(x_eq, y_eq, z_eq, u_range, v_range):
    """Generates and displays an a
    interactive 3D plot from user-defined equations."""

    try:
        # Define the parameter space based on user constraints
        u = np.linspace(u_range[0], u_range[1], 100)
        v = np.linspace(v_range[0], v_range[1], 100)
        U, V = np.meshgrid(u, v)

        # Define helper functions for the new mathematical operations
        def cot(x):
            return 1 / np.tan(x)

        def sec(x):
            return 1 / np.cos(x)

        def cosec(x):
            return 1 / np.sin(x)

        def log(x):
            return np.log(x)

        def ln(x):
            return np.log(x)

        def exp(x):
            return np.exp(x)

        def power(x, y):
            return np.power(x, y)

        # Create a safe environment for evaluating user-entered expressions
        # This maps simple function names to their NumPy equivalents
        allowed_vars = {
            'u': U, 'v': V,
            'cos': np.cos, 'sin': np.sin, 'tan': np.tan,
            'pi': np.pi, 'sqrt': np.sqrt,
            'cot': cot, 'sec': sec, 'cosec': cosec,
            'log': log, 'ln': ln, 'exp': exp,
            'power': power,
        }

        # Evaluate the user's equations
        X = eval(x_eq, {"__builtins__": None}, allowed_vars)
        Y = eval(y_eq, {"__builtins__": None}, allowed_vars)
        Z = eval(z_eq, {"__builtins__": None}, allowed_vars)

        # Create the interactive Plotly 3D surface plot
        fig = go.Figure(data=[go.Surface(z=Z, x=X, y=Y, colorscale='viridis')])

        # Update the layout for better aesthetics and interaction
        fig.update_layout(
            title='Interactive 3D Parametric Grapher',
            autosize=True,
            scene=dict(
                xaxis_title='X-axis',
                yaxis_title='Y-axis',
                zaxis_title='Z-axis',
            )
        )

        # Display the plot in the Streamlit app
        st.plotly_chart(fig, use_container_width=True)

    except Exception as e:
        # Display a user-friendly error message if the evaluation fails
        st.error(f"Error plotting the graph: {e}")
        st.info("Please check your equation syntax. Use `u` and `v` as variables.")


# --- Streamlit User Interface ---
st.title("Dynamic 3D Parametric Grapher 🚀")

st.markdown("""
Enter your 3D parametric equations below. The graph will update in real time.
You can use functions like `cos`, `sin`, `pi`, `sqrt`, `log`, `ln`, `cot`, `sec`, `cosec`, `exp`, and `power`.
""")

col1, col2 = st.columns(2)

with col1:
    x_eq = st.text_input("X Equation", value="-(4 - 2 * cos(u)) * cos(v) + 6 * (sin(u) + 1) * cos(u)")
    y_eq = st.text_input("Y Equation", value="16 * sin(u)")
    z_eq = st.text_input("Z Equation", value="(4 - 2 * cos(u)) * sin(v)")

with col2:
    st.markdown("### Constraints")
    u_min, u_max = st.slider("u range", min_value=0.0, max_value=2 * np.pi, value=(0.0, 2 * np.pi))
    v_min, v_max = st.slider("v range", min_value=0.0, max_value=2 * np.pi, value=(0.0, 2 * np.pi))

# Call the plotting function with user input
plot_dynamic_3d_graph(x_eq, y_eq, z_eq, (u_min, u_max), (v_min, v_max))