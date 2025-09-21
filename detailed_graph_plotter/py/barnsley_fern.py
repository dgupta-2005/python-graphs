import streamlit as st
import random
import plotly.io as pio
import plotly.graph_objects as go

pio.renderers.default = "browser"
def barnsley_fern_3d(num_points):
    """
    Generates the points for a 3D Barnsley Fern fractal.
    """
    x, y, z = 0.0, 0.0, 0.0
    points = []

    for _ in range(num_points):
        r = random.random()

        if r < 0.01:
            x_new = 0.5 * x
            y_new = 0.5 * y
            z_new = 0.5 * z
        elif r < 0.86:
            x_new = 0.85 * x
            y_new = 0.85 * y + 0.1
            z_new = 0.85 * z
        elif r < 0.93:
            x_new = 0.5 * x + 0.15
            y_new = 0.5 * y + 0.1
            z_new = 0.5 * z
        else:
            x_new = 0.5 * x
            y_new = 0.5 * y + 0.1
            z_new = 0.5 * z + 0.1

        x, y, z = x_new, y_new, z_new
        points.append((x, y, z))

    return points


# --- Streamlit Application ---
st.title("Interactive 3D Barnsley Fern 🌿")
st.markdown("Generates a 3D fractal with interactive controls.")

# Add a slider to control the number of points
num_points = st.slider("Number of Points", min_value=1000, max_value=500000, value=100000, step=1000)

# Generate points when the button is clicked
if st.button("Generate Fern"):
    # Generate the fractal points
    fern_points = barnsley_fern_3d(num_points)

    # Extract coordinates for plotting
    x_coords = [p[0] for p in fern_points]
    y_coords = [p[1] for p in fern_points]
    z_coords = [p[2] for p in fern_points]

    # Create a Plotly 3D scatter plot
    fig = go.Figure(data=[go.Scatter3d(
        x=x_coords,
        y=y_coords,
        z=z_coords,
        mode='markers',
        marker=dict(
            size=1,
            color='green',
            opacity=0.8
        )
    )])

    # Add titles and a clean layout
    fig.update_layout(
        title='3D Barnsley Fern',
        scene=dict(
            xaxis_title='X-axis',
            yaxis_title='Y-axis',
            zaxis_title='Z-axis',
        )
    )

    # Display the plot
    st.plotly_chart(fig, use_container_width=True)