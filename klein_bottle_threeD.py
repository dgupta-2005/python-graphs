import streamlit as st
import numpy as np
import plotly.graph_objects as go
import plotly.io as pio

# Set the Plotly renderer for Streamlit
pio.renderers.default = "browser"

st.title("Dynamic 3D Parametric Grapher 🚀")

st.markdown("""
Enter your 3D parametric equations below. Use `u` and `v` as variables.
You can use standard math functions like `cos`, `sin`, `pi`, `sqrt`, etc.
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

try:
    u = np.linspace(u_min, u_max, 100)
    v = np.linspace(v_min, v_max, 100)
    U, V = np.meshgrid(u, v)

    # Defining a dictionary of allowed functions and variables for safe evaluation
    allowed_vars = {
        'u': U, 'v': V,
        'cos': np.cos, 'sin': np.sin, 'tan': np.tan,
        'pi': np.pi, 'sqrt': np.sqrt, 'exp': np.exp,
        'log': np.log, 'abs': np.abs
    }

    # Evaluating the user's input with the allowed functions
    X = eval(x_eq, {"__builtins__": None}, allowed_vars)
    Y = eval(y_eq, {"__builtins__": None}, allowed_vars)
    Z = eval(z_eq, {"__builtins__": None}, allowed_vars)

    # Create the Plotly figure
    fig = go.Figure(data=[go.Surface(z=Z, x=X, y=Y, colorscale='Viridis')])

    # Update the layout for a clean, interactive view
    fig.update_layout(
        title='Interactive Parametric 3D Plot',
        autosize=True,
        scene=dict(
            xaxis_title='X-axis',
            yaxis_title='Y-axis',
            zaxis_title='Z-axis',
        )
    )

    # Displaying the plot
    st.plotly_chart(fig, use_container_width=True)

except Exception as e:
    st.error(f"Error plotting the graph: {e}")
    st.info("Please check your equation syntax.")