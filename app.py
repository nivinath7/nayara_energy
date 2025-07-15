import streamlit as st
from openai import OpenAI
new_key = "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"
client = OpenAI(api_key=new_key)
from datetime import datetime
import base64

# --- App Config ---
st.set_page_config(
    page_title="KPMG IT Contract Analyzer", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- OpenAI Key ---

# --- Custom CSS ---
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #00338D 0%, #0047AB 100%);
        padding: 2rem 1rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        color: white;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0, 51, 141, 0.3);
    }
    
    .kpmg-logo {
        font-size: 3rem;
        font-weight: bold;
        letter-spacing: 8px;
        margin-bottom: 1rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .subtitle {
        font-size: 1.5rem;
        margin-bottom: 0.5rem;
        opacity: 0.9;
    }
    
    .tagline {
        font-size: 1.1rem;
        opacity: 0.8;
        font-style: italic;
    }
    
    .feature-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 1.5rem;
        margin: 2rem 0;
    }
    
    .feature-card {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        border: 1px solid #e0e0e0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.15);
    }
    
    .feature-icon {
        font-size: 2.5rem;
        margin-bottom: 1rem;
        display: block;
    }
    
    .feature-title {
        font-size: 1.2rem;
        font-weight: bold;
        color: #00338D;
        margin-bottom: 0.5rem;
    }
    
    .upload-section {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        padding: 2rem;
        border-radius: 15px;
        border: 2px dashed #00338D;
        margin: 2rem 0;
        text-align: center;
    }
    
    .upload-icon {
        font-size: 4rem;
        color: #00338D;
        margin-bottom: 1rem;
    }
    
    .analyze-button {
        background: linear-gradient(135deg, #00338D 0%, #0047AB 100%);
        color: white;
        padding: 1rem 2rem;
        border: none;
        border-radius: 8px;
        font-size: 1.1rem;
        font-weight: bold;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0, 51, 141, 0.3);
    }
    
    .analyze-button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0, 51, 141, 0.4);
    }
    
    .result-card {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        border-left: 4px solid #00338D;
        margin: 1rem 0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    
    .contract-title {
        color: #00338D;
        font-size: 1.3rem;
        font-weight: bold;
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .status-badge {
        display: inline-block;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-size: 0.9rem;
        font-weight: bold;
        margin: 0.2rem;
    }
    
    .present {
        background: #d4edda;
        color: #155724;
    }
    
    .missing {
        background: #f8d7da;
        color: #721c24;
    }
    
    .stats-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 1rem;
        margin: 2rem 0;
    }
    
    .stat-box {
        background: linear-gradient(135deg, #00338D 0%, #0047AB 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 12px;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0, 51, 141, 0.3);
    }
    
    .stat-number {
        font-size: 2.5rem;
        font-weight: bold;
        display: block;
    }
    
    .stat-label {
        font-size: 0.9rem;
        opacity: 0.9;
    }
    
    .footer {
        margin-top: 3rem;
        padding: 2rem;
        background: #f8f9fa;
        border-radius: 15px;
        text-align: center;
        color: #666;
    }
</style>
""", unsafe_allow_html=True)

# --- Header ---
st.markdown("""
<div class="main-header">
    <div class="kpmg-logo">KPMG</div>
    <div class="subtitle">IT Contract Analyzer</div>
    <div class="tagline">Intelligent Contract Analysis & Risk Assessment</div>
</div>
""", unsafe_allow_html=True)

# --- Features Section ---
st.markdown("## 🎯 **Key Features**")

feature_html = """
<div class="feature-grid">
    <div class="feature-card">
        <span class="feature-icon">⚖️</span>
        <div class="feature-title">SLA Compliance</div>
        <p>Automatically detects Service Level Agreement clauses and compliance requirements</p>
    </div>
    <div class="feature-card">
        <span class="feature-icon">🛡️</span>
        <div class="feature-title">Risk Assessment</div>
        <p>Identifies penalty clauses and potential financial risks in contracts</p>
    </div>
    <div class="feature-card">
        <span class="feature-icon">🔐</span>
        <div class="feature-title">Security Analysis</div>
        <p>Scans for data security provisions and compliance requirements</p>
    </div>
    <div class="feature-card">
        <span class="feature-icon">📋</span>
        <div class="feature-title">Termination Review</div>
        <p>Analyzes termination conditions and exit clauses</p>
    </div>
</div>
"""

st.markdown(feature_html, unsafe_allow_html=True)

# --- LLM Selection Section ---
st.markdown("## 🤖 **Select AI Model**")

llm_selection_html = """
<div style="background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%); padding: 1.5rem; border-radius: 15px; margin: 1rem 0;">
    <h4 style="color: #00338D; margin-bottom: 1rem;">Choose Your AI Analysis Engine</h4>
    <p style="color: #666; margin-bottom: 1rem;">Select the AI model that best fits your analysis needs</p>
</div>
"""

st.markdown(llm_selection_html, unsafe_allow_html=True)

# LLM Options
llm_options = {
    "gpt-4o": {
        "name": "GPT-4 Omni",
        "description": "Most advanced model with superior reasoning and analysis capabilities",
        "icon": "🧠",
        "performance": "Excellent",
        "speed": "Fast"
    },
    "gpt-4-turbo": {
        "name": "GPT-4 Turbo",
        "description": "High-performance model optimized for complex legal document analysis",
        "icon": "⚡",
        "performance": "Excellent",
        "speed": "Very Fast"
    },
    "gpt-4": {
        "name": "GPT-4",
        "description": "Reliable and consistent model for professional contract review",
        "icon": "🎯",
        "performance": "Very Good",
        "speed": "Moderate"
    },
    "gpt-3.5-turbo": {
        "name": "GPT-3.5 Turbo",
        "description": "Fast and efficient model for standard contract analysis",
        "icon": "🚀",
        "performance": "Good",
        "speed": "Very Fast"
    }
}

# Create columns for LLM selection
col1, col2 = st.columns([2, 1])

with col1:
    selected_llm = st.selectbox(
        "Select AI Model",
        options=list(llm_options.keys()),
        format_func=lambda x: f"{llm_options[x]['icon']} {llm_options[x]['name']}",
        index=0,
        help="Choose the AI model for contract analysis"
    )

with col2:
    # Display model info
    model_info = llm_options[selected_llm]
    st.markdown(f"""
    <div style="background: white; padding: 1rem; border-radius: 10px; border: 1px solid #e0e0e0; margin-top: 1.5rem;">
        <h5 style="color: #00338D; margin-bottom: 0.5rem;">{model_info['icon']} {model_info['name']}</h5>
        <p style="font-size: 0.9rem; color: #666; margin-bottom: 0.5rem;">{model_info['description']}</p>
        <div style="display: flex; gap: 1rem; font-size: 0.8rem;">
            <span><strong>Performance:</strong> {model_info['performance']}</span>
            <span><strong>Speed:</strong> {model_info['speed']}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- Upload Section ---
st.markdown("## 📂 **Upload Contracts**")

upload_html = """
<div class="upload-section">
    <div class="upload-icon">📁</div>
    <h3>Upload Multiple Contract Files</h3>
    <p>Select all your .txt contract files at once for batch analysis</p>
</div>
"""

st.markdown(upload_html, unsafe_allow_html=True)

uploaded_files = st.file_uploader(
    "Choose contract files", 
    type="txt", 
    accept_multiple_files=True,
    help="Select multiple .txt files containing your IT contracts"
)

# --- Analysis Section ---
if uploaded_files:
    st.markdown(f"## 📊 **Ready to Analyze {len(uploaded_files)} Contract(s)**")

    # Stats before analysis
    stats_html = f"""
    <div class="stats-container">
        <div class="stat-box">
            <span class="stat-number">{len(uploaded_files)}</span>
            <span class="stat-label">Contracts Uploaded</span>
        </div>
        <div class="stat-box">
            <span class="stat-number">4</span>
            <span class="stat-label">Key Clauses Checked</span>
        </div>
        <div class="stat-box">
            <span class="stat-number">{llm_options[selected_llm]['icon']}</span>
            <span class="stat-label">{llm_options[selected_llm]['name']}</span>
        </div>
    </div>
    """
    st.markdown(stats_html, unsafe_allow_html=True)

# --- Prompt Templates ---
system_prompt = (
    "You are a senior legal contract reviewer at KPMG. Your job is to analyze IT contracts and determine whether these critical clauses are present or missing:\n"
    "- SLA (Service Level Agreement)\n"
    "- Penalties\n"
    "- Data Security\n"
    "- Termination Conditions\n\n"
    "Respond in a clear, professional format. For each clause, indicate if it's Present or Missing, and provide a brief explanation.\n"
    "Use this format:\n"
    "✅ **Present**: SLA - Clear performance metrics defined\n"
    "❌ **Missing**: Penalties - No penalty clauses found\n"
    "✅ **Present**: Data Security - Comprehensive security requirements\n"
    "❌ **Missing**: Termination - Exit conditions not specified"
)

user_prompt_template = """
Contract Name: {filename}
Contract Text:
\"\"\"
{contract_text}
\"\"\"

Please analyze this contract and provide a detailed assessment of the four key clauses.
"""

# --- Analysis Trigger ---
if uploaded_files and st.button("🔍 **Start Analysis**", use_container_width=True):
    with st.spinner(f"🤖 {llm_options[selected_llm]['name']} is analyzing your contracts..."):
        st.success(f"✨ **Analysis Started** - Processing {len(uploaded_files)} contract(s) with {llm_options[selected_llm]['name']}")

        results = []
        progress_bar = st.progress(0)

        for idx, uploaded_file in enumerate(uploaded_files):
            try:
                filename = uploaded_file.name
                contract_text = uploaded_file.read().decode("utf-8").strip()

                user_prompt = user_prompt_template.format(
                    filename=filename, 
                    contract_text=contract_text
                )

                response = client.chat.completions.create(model=selected_llm,  # Use the selected LLM model
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.2)

                reply = response.choices[0].message.content.strip()
                results.append((filename, reply))

                progress_bar.progress((idx + 1) / len(uploaded_files))

            except Exception as e:
                st.error(f"❌ **Error processing {uploaded_file.name}**: {str(e)}")

        # Display Results
        st.markdown(f"## 📋 **Analysis Results** (Powered by {llm_options[selected_llm]['name']})")

        for filename, analysis in results:
            result_html = f"""
            <div class="result-card">
                <div class="contract-title">
                    📄 {filename}
                    <span style="background: linear-gradient(135deg, #00338D 0%, #0047AB 100%); color: white; padding: 0.2rem 0.5rem; border-radius: 12px; font-size: 0.8rem; margin-left: auto;">
                        {llm_options[selected_llm]['icon']} {llm_options[selected_llm]['name']}
                    </span>
                </div>
                <div style="line-height: 1.6;">
                    {analysis.replace('✅', '<span style="color: #28a745; font-weight: bold;">✅</span>').replace('❌', '<span style="color: #dc3545; font-weight: bold;">❌</span>')}
                </div>
            </div>
            """
            st.markdown(result_html, unsafe_allow_html=True)

        # Summary
        st.markdown("## 📈 **Analysis Complete**")
        st.balloons()

        summary_html = f"""
        <div class="stats-container">
            <div class="stat-box">
                <span class="stat-number">{len(results)}</span>
                <span class="stat-label">Contracts Analyzed</span>
            </div>
            <div class="stat-box">
                <span class="stat-number">{llm_options[selected_llm]['icon']}</span>
                <span class="stat-label">{llm_options[selected_llm]['name']}</span>
            </div>
            <div class="stat-box">
                <span class="stat-number">{datetime.now().strftime('%H:%M')}</span>
                <span class="stat-label">Completed At</span>
            </div>
        </div>
        """
        st.markdown(summary_html, unsafe_allow_html=True)

# --- Instructions ---
if not uploaded_files:
    st.markdown("## 📝 **How to Use**")

    instructions = """
    1. **Upload**: Select multiple .txt contract files using the file uploader above
    2. **Analyze**: Click the 'Start Analysis' button to begin AI-powered contract review
    3. **Review**: Get detailed insights on SLA, Penalties, Data Security, and Termination clauses
    4. **Export**: Use the results to make informed decisions about your contracts
    """

    st.markdown(instructions)

# --- Footer ---
footer_html = f"""
<div class="footer">
    <p><strong>KPMG IT Contract Analyzer</strong> | Powered by Advanced AI</p>
    <p>© 2025 KPMG. Generated on {datetime.now().strftime('%B %d, %Y at %I:%M %p')}</p>
    <p><em>This tool provides AI-assisted contract analysis. Always consult with legal professionals for final decisions.</em></p>
</div>
"""

st.markdown(footer_html, unsafe_allow_html=True)
