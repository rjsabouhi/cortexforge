
import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.set_page_config(page_title="CortexForge: Symbolic Neuroplasticity Engine", layout="wide")

st.title("CortexForge: Symbolic Neuroplasticity Engine")

st.markdown("""
This tool simulates symbolic neuroplasticity using the Recursive Cognitive Dynamics (RCD) framework.
You can visualize how memory (M), hope (H), and reinforcement (R) evolve in symbolic phase space under different conditions,
such as trauma loops, pharmacological agents, and symbolic interventions.
""")

# Sidebar Controls
st.sidebar.header("Simulation Controls")
timesteps = st.sidebar.slider("Timesteps", 100, 1000, 300, step=50)
alpha = st.sidebar.slider("Memory Rigidity (α)", 0.0, 1.0, 0.4, step=0.05)
beta = st.sidebar.slider("Reinforcement Modulation (β)", 0.0, 1.0, 0.5, step=0.05)
gamma = st.sidebar.slider("Symbolic Coherence (γ)", 0.0, 1.0, 0.6, step=0.05)
shock_intensity = st.sidebar.slider("Trauma Shock Intensity", 0.0, 1.0, 0.3, step=0.05)
drug_effect = st.sidebar.selectbox("Pharmacological Analog", ["None", "SSRI", "Dopamine Agonist", "Aletheamine"])

# Initialize arrays
H = np.zeros(timesteps)
M = np.zeros(timesteps)
R = np.zeros(timesteps)

# Initial conditions
H[0], M[0], R[0] = 0.5, 0.5, 0.5

# Simulate recursive symbolic neurodynamics
for t in range(1, timesteps):
    shock = shock_intensity if t % 50 == 0 else 0
    drug_mod = 0
    if drug_effect == "SSRI":
        drug_mod = 0.1
    elif drug_effect == "Dopamine Agonist":
        drug_mod = 0.15
    elif drug_effect == "Aletheamine":
        drug_mod = 0.25

    M[t] = M[t-1] + alpha * (H[t-1] - M[t-1]) - shock
    R[t] = R[t-1] + beta * (H[t-1] - R[t-1]) + drug_mod
    H[t] = H[t-1] + gamma * (M[t-1] - R[t-1])

# 3D Visualization
fig = go.Figure(data=[go.Scatter3d(
    x=H, y=M, z=R, mode='lines+markers',
    marker=dict(size=4, color=np.linspace(0, 1, timesteps), colorscale='Viridis'),
    line=dict(width=2, color='blue')
)])
fig.update_layout(
    scene=dict(
        xaxis_title='Hope (H)',
        yaxis_title='Memory (M)',
        zaxis_title='Reinforcement (R)'
    ),
    title="Symbolic Phase Trajectory: H-M-R Dynamics"
)
st.plotly_chart(fig, use_container_width=True)

# Variable Summary
st.subheader("Variable End States")
st.write(f"Final Hope (H): {H[-1]:.2f}")
st.write(f"Final Memory (M): {M[-1]:.2f}")
st.write(f"Final Reinforcement (R): {R[-1]:.2f}")
