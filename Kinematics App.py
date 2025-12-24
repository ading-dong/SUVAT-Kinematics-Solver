import streamlit as st
import math

# Page configuration
st.set_page_config(
    page_title="SUVAT Solver | Engineering Mechanics",
    page_icon="🚀",
    layout="centered"
)

# App title and description
st.title("🚀 SUVAT Equations Solver")
st.markdown("**Engineering Mechanics - Constant Acceleration Kinematics**")
st.markdown("*Solve problems involving displacement (s), initial velocity (u), final velocity (v), acceleration (a), and time (t)*")
st.markdown("---")

# Sidebar with instructions
with st.sidebar:
    st.header("📋 How to Use")
    st.markdown("""
    1. **Select 3 known variables**
    2. **Enter their values**
    3. **Leave unknown variables empty**
    4. Click **Solve Problem**
    
    *The app will calculate the 2 unknown variables.*
    """)
    
    st.markdown("---")
    st.header("📚 SUVAT Variables")
    st.latex(r'''
    \begin{align*}
    s &= \text{displacement (m)} \\
    u &= \text{initial velocity (m/s)} \\
    v &= \text{final velocity (m/s)} \\
    a &= \text{acceleration (m/s}^2\text{)} \\
    t &= \text{time (s)}
    \end{align*}
    ''')
    
    st.markdown("---")
    st.header("🧪 Example: Find v")
    st.markdown("**Given:** u = 0, a = 2, t = 5")
    st.markdown("**Find:** v = u + at = 0 + 2×5 = **10 m/s**")

# Main content area
st.header("🔢 Enter Known Values")

# Create two columns for better layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("Variable 1")
    s = st.number_input("Displacement, s (m)", 
                       value=None, 
                       placeholder="Enter or leave empty",
                       key="s_input")
    
    st.subheader("Variable 2")
    u = st.number_input("Initial Velocity, u (m/s)", 
                       value=None, 
                       placeholder="Enter or leave empty",
                       key="u_input")

with col2:
    st.subheader("Variable 3")
    v = st.number_input("Final Velocity, v (m/s)", 
                       value=None, 
                       placeholder="Enter or leave empty",
                       key="v_input")
    
    st.subheader("Variable 4")
    a = st.number_input("Acceleration, a (m/s²)", 
                       value=None, 
                       placeholder="Enter or leave empty",
                       key="a_input")

# Time input below columns
st.subheader("Variable 5")
t = st.number_input("Time, t (s)", 
                   value=None, 
                   placeholder="Enter or leave empty",
                   key="t_input")

# Convert None to actual None values
s_val = s if s is not None else None
u_val = u if u is not None else None
v_val = v if v is not None else None
a_val = a if a is not None else None
t_val = t if t is not None else None

# Solve button
st.markdown("---")
solve_button = st.button("🚀 Solve SUVAT Problem", type="primary", use_container_width=True)

if solve_button:
    # Count how many variables are provided
    provided_vars = [var for var in [s_val, u_val, v_val, a_val, t_val] if var is not None]
    
    if len(provided_vars) != 3:
        st.error(f"❌ Please enter exactly 3 known variables. You entered {len(provided_vars)}.")
        if len(provided_vars) < 3:
            st.info("💡 You need 3 knowns to solve for 2 unknowns.")
    else:
        st.success("✅ Solving...")
        
        # Display given values
        st.subheader("📋 Given Values:")
        given_text = ""
        if s_val is not None: given_text += f"s = {s_val} m, "
        if u_val is not None: given_text += f"u = {u_val} m/s, "
        if v_val is not None: given_text += f"v = {v_val} m/s, "
        if a_val is not None: given_text += f"a = {a_val} m/s², "
        if t_val is not None: given_text += f"t = {t_val} s, "
        st.write(given_text[:-2])  # Remove last comma and space
        
        # Initialize results
        results = []
        equations_used = []
        calculations = []
        
        try:
            # ====================================================
            # FIXED LOGIC: Checks for ALL possible combinations
            # ====================================================
            
            # CASE 1: If u, a, t are known → find v FIRST (your issue!)
            if u_val is not None and a_val is not None and t_val is not None:
                # Priority 1: Find v if it's unknown
                if v_val is None:
                    v_calc = u_val + a_val * t_val
                    results.append(("v", v_calc, "m/s"))
                    equations_used.append(r"v = u + at")
                    calculations.append(f"v = u + at = {u_val} + ({a_val})×({t_val}) = {v_calc:.3f} m/s")
                
                # Priority 2: Find s if it's unknown
                if s_val is None:
                    s_calc = u_val * t_val + 0.5 * a_val * t_val**2
                    results.append(("s", s_calc, "m"))
                    equations_used.append(r"s = ut + \frac{1}{2}at^2")
                    calculations.append(f"s = ut + ½at² = ({u_val})×({t_val}) + ½×({a_val})×({t_val})² = {s_calc:.3f} m")
            
            # CASE 2: If u, v, t are known
            elif u_val is not None and v_val is not None and t_val is not None:
                if a_val is None:
                    a_calc = (v_val - u_val) / t_val
                    results.append(("a", a_calc, "m/s²"))
                    equations_used.append(r"a = \frac{v - u}{t}")
                    calculations.append(f"a = (v - u)/t = ({v_val} - {u_val})/{t_val} = {a_calc:.3f} m/s²")
                if s_val is None:
                    s_calc = 0.5 * (u_val + v_val) * t_val
                    results.append(("s", s_calc, "m"))
                    equations_used.append(r"s = \frac{u + v}{2}t")
                    calculations.append(f"s = ½(u + v)t = ½({u_val} + {v_val})×{t_val} = {s_calc:.3f} m")
            
            # CASE 3: If u, v, a are known
            elif u_val is not None and v_val is not None and a_val is not None:
                if t_val is None:
                    t_calc = (v_val - u_val) / a_val
                    results.append(("t", t_calc, "s"))
                    equations_used.append(r"t = \frac{v - u}{a}")
                    calculations.append(f"t = (v - u)/a = ({v_val} - {u_val})/{a_val} = {t_calc:.3f} s")
                if s_val is None:
                    s_calc = (v_val**2 - u_val**2) / (2 * a_val)
                    results.append(("s", s_calc, "m"))
                    equations_used.append(r"v^2 = u^2 + 2as")
                    calculations.append(f"s = (v² - u²)/(2a) = ({v_val}² - {u_val}²)/(2×{a_val}) = {s_calc:.3f} m")
            
            # CASE 4: If s, u, t are known
            elif s_val is not None and u_val is not None and t_val is not None:
                if a_val is None:
                    a_calc = 2 * (s_val - u_val * t_val) / t_val**2
                    results.append(("a", a_calc, "m/s²"))
                    equations_used.append(r"s = ut + \frac{1}{2}at^2")
                    calculations.append(f"a = 2(s - ut)/t² = 2({s_val} - {u_val}×{t_val})/{t_val}² = {a_calc:.3f} m/s²")
                if v_val is None:
                    # Can use v = u + at with the a we just calculated
                    v_calc = u_val + a_calc * t_val
                    results.append(("v", v_calc, "m/s"))
                    equations_used.append(r"v = u + at")
                    calculations.append(f"v = u + at = {u_val} + ({a_calc:.3f})×({t_val}) = {v_calc:.3f} m/s")
            
            # CASE 5: If s, v, t are known
            elif s_val is not None and v_val is not None and t_val is not None:
                if u_val is None:
                    u_calc = (2 * s_val / t_val) - v_val
                    results.append(("u", u_calc, "m/s"))
                    equations_used.append(r"s = \frac{u + v}{2}t")
                    calculations.append(f"u = 2s/t - v = 2({s_val})/{t_val} - {v_val} = {u_calc:.3f} m/s")
                if a_val is None:
                    a_calc = 2 * (s_val - v_val * t_val) / t_val**2
                    results.append(("a", a_calc, "m/s²"))
                    equations_used.append(r"s = vt - \frac{1}{2}at^2")
                    calculations.append(f"a = 2(s - vt)/t² = 2({s_val} - {v_val}×{t_val})/{t_val}² = {a_calc:.3f} m/s²")
            
            # CASE 6: If s, u, a are known
            elif s_val is not None and u_val is not None and a_val is not None:
                if v_val is None:
                    v_calc = math.sqrt(u_val**2 + 2 * a_val * s_val)
                    results.append(("v", v_calc, "m/s"))
                    equations_used.append(r"v^2 = u^2 + 2as")
                    calculations.append(f"v = √(u² + 2as) = √({u_val}² + 2×{a_val}×{s_val}) = {v_calc:.3f} m/s")
                if t_val is None:
                    # Use v from above to find t
                    if v_val is None:
                        v_calc = math.sqrt(u_val**2 + 2 * a_val * s_val)
                    t_calc = (v_calc - u_val) / a_val
                    results.append(("t", t_calc, "s"))
                    equations_used.append(r"v = u + at")
                    calculations.append(f"t = (v - u)/a = ({v_calc:.3f} - {u_val})/{a_val} = {t_calc:.3f} s")
            
            # CASE 7: If s, v, a are known
            elif s_val is not None and v_val is not None and a_val is not None:
                if u_val is None:
                    u_calc = math.sqrt(v_val**2 - 2 * a_val * s_val)
                    results.append(("u", u_calc, "m/s"))
                    equations_used.append(r"v^2 = u^2 + 2as")
                    calculations.append(f"u = √(v² - 2as) = √({v_val}² - 2×{a_val}×{s_val}) = {u_calc:.3f} m/s")
                if t_val is None:
                    # Use u from above to find t
                    if u_val is None:
                        u_calc = math.sqrt(v_val**2 - 2 * a_val * s_val)
                    t_calc = (v_val - u_calc) / a_val
                    results.append(("t", t_calc, "s"))
                    equations_used.append(r"v = u + at")
                    calculations.append(f"t = (v - u)/a = ({v_val} - {u_calc:.3f})/{a_val} = {t_calc:.3f} s")
            
            # CASE 8: If u, a, s are known (already covered in CASE 6)
            # CASE 9: If v, a, t are known
            elif v_val is not None and a_val is not None and t_val is not None:
                if u_val is None:
                    u_calc = v_val - a_val * t_val
                    results.append(("u", u_calc, "m/s"))
                    equations_used.append(r"v = u + at")
                    calculations.append(f"u = v - at = {v_val} - ({a_val})×({t_val}) = {u_calc:.3f} m/s")
                if s_val is None:
                    s_calc = v_val * t_val - 0.5 * a_val * t_val**2
                    results.append(("s", s_calc, "m"))
                    equations_used.append(r"s = vt - \frac{1}{2}at^2")
                    calculations.append(f"s = vt - ½at² = ({v_val})×({t_val}) - ½×({a_val})×({t_val})² = {s_calc:.3f} m")
            
            # CASE 10: If s, a, t are known
            elif s_val is not None and a_val is not None and t_val is not None:
                if u_val is None:
                    u_calc = (s_val - 0.5 * a_val * t_val**2) / t_val
                    results.append(("u", u_calc, "m/s"))
                    equations_used.append(r"s = ut + \frac{1}{2}at^2")
                    calculations.append(f"u = (s - ½at²)/t = ({s_val} - ½×{a_val}×{t_val}²)/{t_val} = {u_calc:.3f} m/s")
                if v_val is None:
                    v_calc = u_calc + a_val * t_val if 'u_calc' in locals() else (s_val + 0.5 * a_val * t_val**2) / t_val
                    results.append(("v", v_calc, "m/s"))
                    equations_used.append(r"v = u + at")
                    calculations.append(f"v = u + at = {u_calc:.3f} + ({a_val})×({t_val}) = {v_calc:.3f} m/s")
            
            # Display results
            if results:
                st.subheader("🎯 Solutions Found:")
                for i, (var_name, var_value, unit) in enumerate(results):
                    st.metric(label=f"{var_name.upper()} ({var_name})", 
                             value=f"{var_value:.3f}", 
                             delta=unit)
                
                st.subheader("📝 Calculation Steps:")
                for i, calc in enumerate(calculations):
                    st.write(f"{i+1}. {calc}")
                
                st.subheader("📐 Equations Used:")
                for i, eq in enumerate(equations_used):
                    st.latex(eq)
                
                # Reset button
                if st.button("🔄 Solve Another Problem", key="reset_button"):
                    st.rerun()
            else:
                st.warning("⚠️ Could not solve with this combination of variables. Try a different set.")
                
        except ZeroDivisionError:
            st.error("Division by zero! Check your inputs (time or acceleration cannot be zero).")
        except ValueError as e:
            st.error(f"Math error: {e}. Check if values lead to impossible calculations (like square root of negative number).")
        except Exception as e:
            st.error(f"Unexpected error: {e}")

# Footer
st.markdown("---")
st.caption("**Engineering Mechanics Project** | Chemical Engineering | Constant Acceleration Kinematics")
st.caption("Built with Streamlit & Python | SUVAT Equations Solver")