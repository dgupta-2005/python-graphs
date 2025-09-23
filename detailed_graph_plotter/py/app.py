import streamlit as st
import numpy as np
import plotly.io as pio
from parametric_graph_plotter import GraphPlotter
from polar_curve_threeD import PolarPlotter

# Set the Plotly renderer for Streamlit
pio.renderers.default = "browser"


def main():
    """Main function to run the Streamlit application."""
    st.title("Dynamic 3D Grapher 🚀")

    # Radio button to select the plotter type
    plotter_type = st.radio(
        "Select Plotter Type:",
        ("Parametric Surfaces", "3D Polar Curves")
    )
    fig_or_error, is_success = None, False

    if plotter_type == "Parametric Surfaces":
        st.subheader("Parametric Surfaces (x, y, z in terms of u, v)")

        # User input for parametric surfaces
        col1, col2 = st.columns(2)
        with col1:
            x_eq = st.text_input("X Equation", value="-(4 - 2 * cos(u)) * cos(v) + 6 * (sin(u) + 1) * cos(u)")
            y_eq = st.text_input("Y Equation", value="16 * sin(u)")
            z_eq = st.text_input("Z Equation", value="(4 - 2 * cos(u)) * sin(v)")
        with col2:
            st.markdown("### Constraints")
            u_min, u_max = st.slider("u range", min_value=0.0, max_value=2 * np.pi, value=(0.0, 2 * np.pi))
            v_min, v_max = st.slider("v range", min_value=0.0, max_value=2 * np.pi, value=(0.0, 2 * np.pi))

        # Plot the parametric surface
        plotter = GraphPlotter()
        fig_or_error, is_success = plotter.plot_surface(x_eq, y_eq, z_eq, (u_min, u_max), (v_min, v_max))

    elif plotter_type == "3D Polar Curves":
        st.subheader("3D Polar Curves (ρ, θ, φ in terms of u, v)")

        # User input for polar curves
        col1, col2 = st.columns(2)
        with col1:
            rho_eq = st.text_input("ρ (rho) Equation", value="u*v")
            theta_eq = st.text_input("θ (theta) Equation", value="cos(u)")
            phi_eq = st.text_input("φ (phi) Equation", value="sin(v)")
        with col2:
            st.markdown("### Constraints")
            u_min, u_max = st.slider("u range", min_value=0.0, max_value=2 * np.pi, value=(0.0, 2 * np.pi))
            v_min, v_max = st.slider("v range", min_value=0.0, max_value=2* np.pi, value=(0.0, 2 * np.pi))

        # Plot the polar curve
        plotter = PolarPlotter()
        fig_or_error, is_success = plotter.plot_surface(rho_eq, theta_eq, phi_eq, (u_min, u_max), (v_min, v_max))

    # Display the result (common to both plotters)
    if is_success:
        st.plotly_chart(fig_or_error, use_container_width=True)
    else:
        st.error(f"Error plotting the graph: {fig_or_error}")
        st.info("Please check your equation syntax.")


if __name__ == "__main__":
    main()