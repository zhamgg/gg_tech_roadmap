import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# Set page configuration
st.set_page_config(
    page_title="Status Assessment Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Add custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        color: #E45F9D;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.8rem;
        font-weight: 600;
        color: #8DD3C7;
        margin-top: 1rem;
        margin-bottom: 0.5rem;
    }
    .card {
        border-radius: 5px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        background-color: #1E1E1E;
        color: #FFFFFF;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
    }
    .metric-card {
        text-align: center;
        padding: 1rem;
        border-radius: 5px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
        color: white;
    }
    .metric-value {
        font-size: 2.2rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    .metric-label {
        font-size: 1rem;
        color: rgba(255, 255, 255, 0.8);
    }
    .status-on-track {
        color: #8DD3C7;
        font-weight: 600;
    }
    .status-at-risk {
        color: #FFBB78;
        font-weight: 600;
    }
    .status-escalation {
        color: #E45F9D;
        font-weight: 600;
    }
    .highlight {
        background-color: rgba(141, 211, 199, 0.2);
        padding: 0.5rem;
        border-radius: 3px;
        font-weight: 500;
    }
    /* Custom Great Gray branding */
    h1, h2, h3 {
        color: #E45F9D !important;
    }
    h4, h5, h6 {
        color: #8DD3C7 !important;
    }
    .stRadio > div {
        background-color: #1E1E1E;
        border-radius: 5px;
        padding: 10px;
    }
    /* Custom styling for tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: #1E1E1E;
        border-radius: 4px 4px 0 0;
        color: white;
        padding: 10px 16px;
    }
    .stTabs [aria-selected="true"] {
        background-color: #8DD3C7;
        color: #1E1E1E;
    }
    /* Override Streamlit's default background */
    .stApp {
        background-color: #121212;
    }
    /* Make text white by default for better contrast on dark background */
    .stMarkdown, p, li {
        color: white;
    }
    /* Customize sidebar */
    [data-testid="stSidebar"] {
        background-color: #1E1E1E;
    }
    /* Add Great Gray logo at the top of sidebar */
    .sidebar-logo {
        display: flex;
        justify-content: center;
        margin-bottom: 20px;
    }
    .sidebar-logo img {
        max-width: 80%;
    }
</style>

<div class="sidebar-logo">
    <img src="https://raw.githubusercontent.com/yourusername/gg_tech_roadmap/main/assets/gg_logo.png" alt="Great Gray Trust Company Logo">
</div>
""", unsafe_allow_html=True)


# Sidebar navigation
st.sidebar.markdown("# Navigation")
page = st.sidebar.radio(
    "Select a Page",
    ["Executive Dashboard", "Project Status", "Analytics Hub", "AI/ML Roadmap", "Strategic Recommendations"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### Dashboard Info")
st.sidebar.info("""
This dashboard provides an overview of Great Gray's Analytics Hub project.
Data as of March 7, 2025.
""")

# Dummy data for the dashboard
project_status_data = {
    "Overall Project": "ON TRACK",
    "Timeline": "ON TRACK",
    "Budget": "ON TRACK",
    "Deliverables and Scope": "ON TRACK"
}

phase_completion = {
    "Phase 1 - AUA Reporting": 100,
    "Phase 2 - Ownership/Omnibus & Invoice Reporting": 75,
    "Enhanced Data Quality Checks": 40,
    "State Street SFTP Cutover": 100,
    "Phase 3 Planning": 20
}

challenges = [
    "Data Quality Issues: Persistent problems with custodian data (Northern Trust, State Street) requiring manual intervention",
    "Limited Adoption: Business users aren't fully utilizing the Analytics Hub capabilities",
    "Lack of Data Governance: No formal structure or policy exists to manage data assets",
    "Technical Approach: Focus on manual fixes rather than automated solutions for data quality",
    "Organization Structure: No dedicated analytics team with clear ownership and accountability"
]

achievements = [
    "Phase 1 Completed: Automated executive reporting (Daily AUA/AUM, Monthly Portfolio, Quarterly KPI)",
    "Phase 2 In Progress: Ownership/Omnibus reporting and Invoice reporting functionality delivered",
    "Technical Foundation: Established data warehouse, data marts, and visualization capabilities",
    "Efficiency Gains: Reduced manual effort in report generation across daily, monthly, and quarterly reporting"
]

ai_ml_roadmap_phases = {
    "Phase 1: Intelligent Data Ingestion (Q2-Q3 2025)": [
        "ML-Powered File Ingestion Service",
        "Adaptive Data Pipeline Framework",
        "RPAG ML-Powered Ingestion POC",
        "Team Onboarding & Infrastructure Setup"
    ],
    "Phase 2: Proactive Data Quality Management (Q3-Q4 2025)": [
        "ML-Based Data Quality Monitoring",
        "Intelligent Data Reconciliation",
        "Data Quality Baseline",
        "Predictive DQ Monitoring"
    ],
    "Phase 3: Advanced Analytics & Data as a Service (Q1-Q2 2026)": [
        "AI-Powered Analytics Engine",
        "Data as a Service (DaaS) Platform",
        "Security and Access Controls",
        "Self-service Data Access Portal"
    ]
}

strategic_recommendations = {
    "Immediate Actions (Next 30 Days)": [
        "Establish Data Governance Framework",
        "Address Technical Priorities",
        "Enhance Business Adoption"
    ],
    "Medium-Term Initiatives (60-90 Days)": [
        "AI/ML-Powered Data Quality",
        "RPAG Data Integration Acceleration",
        "Team Structure & Capabilities"
    ],
    "Strategic Roadmap (6-12 Months)": [
        "Recordkeeper Initiative & Data as a Service",
        "Alteryx Migration & Process Transformation",
        "Master Data Management & Intelligence",
        "Advanced Analytics Platform"
    ]
}

team_allocation = {
    "Data Engineers": 2,
    "Data Scientists": 2,
    "Project Managers": 1
}

investment_data = {
    "Phase 1": 500000,
    "Phase 2 (Estimated)": 600000,
    "Phase 3 (Projected)": 750000
}

risk_data = [
    {"Risk": "Data quality issues more severe than anticipated", "Impact": "High", "Likelihood": "Medium"},
    {"Risk": "Custodian resistance to new data standards", "Impact": "Medium", "Likelihood": "High"},
    {"Risk": "Difficulty hiring specialized ML talent", "Impact": "High", "Likelihood": "Medium"},
    {"Risk": "Model performance degradation over time", "Impact": "Medium", "Likelihood": "Medium"},
    {"Risk": "Integration challenges with existing systems", "Impact": "Medium", "Likelihood": "Medium"},
    {"Risk": "Scope creep during implementation", "Impact": "Medium", "Likelihood": "High"}
]

success_metrics = {
    "Phase 1": [
        "Reduction in manual processing time: 70% for RPAG file processing",
        "File processing accuracy: 95% correct schema identification",
        "Processing time: 80% reduction in end-to-end processing time",
        "Team productivity: 5x increase in files processed per analyst"
    ],
    "Phase 2": [
        "Data quality issues detected: 90% before impacting downstream systems",
        "False positive rate: <5% for anomaly detection",
        "Reconciliation accuracy: 95% automated reconciliation across sources",
        "Time to resolution: 60% reduction in time to resolve data quality issues"
    ],
    "Phase 3": [
        "Insight generation: 50+ automated insights per month",
        "API utilization: Adoption by 3+ internal systems in first quarter",
        "Model performance: 10% quarterly improvement",
        "User satisfaction: 85% satisfaction rating from business users"
    ]
}

# Create functions for each page
def executive_dashboard():
    # Header
    st.markdown("<div class='main-header'>Great Gray Analytics Hub</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-header'>Executive Dashboard</div>", unsafe_allow_html=True)
    st.markdown("Last updated: March 7, 2025")
    
    # Key metrics at the top - with 3 centered tiles
    empty_left, col1, col2, col3, empty_right = st.columns([1, 2, 2, 2, 1])
    
    with col1:
        st.markdown("""
        <div class='metric-card' style='background-color: #F0FDF4;'>
            <div class='metric-value'>33</div>
            <div class='metric-label'>Automated Reports</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='metric-card' style='background-color: #FEF3C7;'>
            <div class='metric-value'>75%</div>
            <div class='metric-label'>Phase 2 Completion</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class='metric-card' style='background-color: #DBEAFE;'>
            <div class='metric-value'>2025 Q3</div>
            <div class='metric-label'>AI/ML Launch Target</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Phase Completion section
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<div class='sub-header'>Phase Completion</div>", unsafe_allow_html=True)
    
    # Create a horizontal bar chart
    fig = go.Figure()
    
    for phase, completion in phase_completion.items():
        fig.add_trace(go.Bar(
            y=[phase],
            x=[completion],
            orientation='h',
            marker=dict(
                color=px.colors.sequential.Blues[int(completion/20)],
                line=dict(color='rgb(8,48,107)', width=1)
            ),
            text=[f"{completion}%"],
            textposition='auto',
            name=phase
        ))
    
    fig.update_layout(
        height=300,
        margin=dict(l=0, r=0, t=10, b=0),
        xaxis=dict(
            title='Completion Percentage',
            range=[0, 100]
        ),
        yaxis=dict(
            title=None,
            autorange="reversed"
        )
    )
    
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Key Achievements section
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<div class='sub-header'>Key Achievements</div>", unsafe_allow_html=True)
    
    for achievement in achievements:
        st.markdown(f"- {achievement}")
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Critical challenges
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<div class='sub-header'>Critical Challenges</div>", unsafe_allow_html=True)
    
    for challenge in challenges:
        st.markdown(f"- {challenge}")
    
    st.markdown("</div>", unsafe_allow_html=True)
    
   
def project_status_page():
    st.markdown("<div class='main-header'>Project Status</div>", unsafe_allow_html=True)
    st.markdown("Last updated: March 7, 2025")
    
    # Project status overview
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<div class='sub-header'>Status Overview</div>", unsafe_allow_html=True)
    
  
    # Recent activities
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<div class='sub-header'>Recent Activities</div>", unsafe_allow_html=True)
    
    activities = [
        {
            "date": "February 27, 2025",
            "activity": "State Street SFTP cutover completed Tuesdayday, March 4."
        },
        {
            "date": "February 27, 2025",
            "activity": "Enhanced Data Quality checks scheduled to be released Friday, March 14."
        },
        {
            "date": "February 27, 2025",
            "activity": "Ownership: 22/26 fixes will be deployed upon completion of the March 3 release."
        },
        {
            "date": "February 27, 2025",
            "activity": "Omnibus: 2/4 fixes will be deployed upon completion of the March 3 release. Including a high-priority fix for version handling."
        },
        {
            "date": "February 13, 2025",
            "activity": "Continued generation and distribution of the automated daily reports to Power BI Pro users."
        },
        {
            "date": "February 6, 2025",
            "activity": "Phase 2 - Ownership/Omnibus & Invoice Reporting: continued supporting GG team with ongoing validation, data exploration, & consumption efforts."
        }
    ]
    
    for activity in activities:
        st.markdown(f"""
        <div style='display: flex; margin-bottom: 15px;'>
            <div style='min-width: 150px; font-weight: 500;'>{activity['date']}</div>
            <div>{activity['activity']}</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Plan for next week
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<div class='sub-header'>Planned Activities</div>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Phase 1 – AUA Reporting")
        st.markdown("- Deploy the cutover to State Street SFTP")
        st.markdown("- Begin ingestion and development work for Enhanced Data Quality Checks")
        
        st.markdown("#### Phase 2 - Ownership/Omnibus & Invoice Reporting")
        st.markdown("- Develop and finalize additional enhancement requests")
        st.markdown("- Include high priority updates for Tax IDs, value precision, and new account file contents joined to account balances")
    
    with col2:
        st.markdown("#### Production Enablement")
        st.markdown("- Continue supporting enablement for Power BI and Databricks for Ownership, Omnibus, & Invoice Reporting")
        
        st.markdown("#### Other Updates")
        st.markdown("- Require signed SOW for current phase of work")
        st.markdown("- Focus on making AUA fully usable with enhanced DQ checks and SSB SFTP files")
        st.markdown("- Continue enablement and Office Hours")
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Risks and issues
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<div class='sub-header'>Risks & Issues</div>", unsafe_allow_html=True)
    
    risk_df = pd.DataFrame(risk_data)
    
    # Create a risk matrix
    fig = go.Figure()
    
    # Define impact and likelihood mappings
    impact_map = {"Low": 1, "Medium": 2, "High": 3}
    likelihood_map = {"Low": 1, "Medium": 2, "High": 3}
    
    # Add a heatmap for the background
    fig.add_trace(go.Heatmap(
        z=[[1, 2, 3], [2, 4, 6], [3, 6, 9]],
        x=["Low", "Medium", "High"],
        y=["Low", "Medium", "High"],
        colorscale=[
            [0, 'rgb(220, 250, 220)'],
            [3/9, 'rgb(255, 255, 200)'],
            [6/9, 'rgb(255, 200, 200)'],
            [1, 'rgb(250, 150, 150)']
        ],
        showscale=False
    ))
    
    # Add scatter plot for the risks
    for i, risk in risk_df.iterrows():
        fig.add_trace(go.Scatter(
            x=[risk["Likelihood"]],
            y=[risk["Impact"]],
            mode='markers+text',
            marker=dict(
                size=20,
                color='rgba(50, 50, 200, 0.7)'
            ),
            text=[i+1],
            textposition="middle center",
            textfont=dict(color='white'),
            name=risk["Risk"]
        ))
    
    fig.update_layout(
        height=400,
        margin=dict(l=0, r=0, t=20, b=0),
        xaxis=dict(
            title='Likelihood',
            tickvals=["Low", "Medium", "High"]
        ),
        yaxis=dict(
            title='Impact',
            tickvals=["Low", "Medium", "High"]
        )
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Risk table
    for i, risk in risk_df.iterrows():
        impact_class = "status-on-track" if risk["Impact"] == "Low" else "status-at-risk" if risk["Impact"] == "Medium" else "status-escalation"
        likelihood_class = "status-on-track" if risk["Likelihood"] == "Low" else "status-at-risk" if risk["Likelihood"] == "Medium" else "status-escalation"
        
        st.markdown(f"""
        <div style='display: flex; margin-bottom: 15px;'>
            <div style='min-width: 30px; font-weight: 600;'>{i+1}.</div>
            <div style='flex-grow: 1;'>{risk['Risk']}</div>
            <div style='min-width: 100px;' class='{impact_class}'>Impact: {risk['Impact']}</div>
            <div style='min-width: 150px;' class='{likelihood_class}'>Likelihood: {risk['Likelihood']}</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

def analytics_hub():
    st.markdown("<div class='main-header'>Analytics Hub</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-header'>Overview & Capabilities</div>", unsafe_allow_html=True)
    
    # About the Analytics Hub
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### About the Analytics Hub")
    st.markdown("""
    The Analytics Hub is a modern, indefinitely scalable analytics platform for business-critical reporting needs. It establishes a 'certified' data asset that serves as the single source of truth for organization-wide analytics and consumption.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Key Benefits")
        st.markdown("""
        - **Reduced Time-to-Insight**: Key reports are delivered daily across all desired time horizons (daily, monthly, and quarterly)
        - **Single Source of Truth**: Key operational and financial data is consolidated and centralized
        - **Automation**: Eliminated and/or greatly reduced manual data acquisition, processing, reformatting, and report builds
        - **Foundation for Future Growth**: Highly-scalable and flexible modern data platform
        """)
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Capabilities and reports
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### Capabilities Delivered")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Automated Executive Reporting")
        st.markdown("- **Daily**: AUA/AUM Metrics (10 reports)")
        st.markdown("- **Monthly**: Portfolio Metrics (12 reports)")
        st.markdown("- **Quarterly**: KPI Reporting (11 reports)")
    
    with col2:
        st.markdown("#### Business Enablement")
        st.markdown("- 'Self-Service' data analysis and access")
        st.markdown("- SSO implementation for accessing Analytics Hub data assets")
        st.markdown("- Training in Databricks and Power BI / SQL")
        st.markdown("- Office Hours for questions and support")
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Technical architecture
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### Technical Architecture")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Data Sources")
        st.markdown("- Northern Trust - transactional data (balances)")
        st.markdown("- State Street - transactional data (balances)")
        st.markdown("- FactSet – operational system")
        st.markdown("- Boarding Pass – onboarding application")
        
        st.markdown("#### Data Processing")
        st.markdown("- Databricks")
    
    with col2:
        st.markdown("#### Data Marts")
        st.markdown("**Medallion Data Store (Delta Tables)**")
        st.markdown("- **Bronze**: Raw, unprocessed data")
        st.markdown("- **Silver**: Cleansed, de-duplicated and transformed data")
        st.markdown("- **Gold**: Curated, aggregated and enriched data")
        
        st.markdown("**Data Warehouse (MSSQL Server)**")
        st.markdown("- Dimensional Data for Reporting")
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Report examples with tabs
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### Report Examples")
    
    report_tabs = st.tabs(["Daily AUA Reports", "Monthly MOR Reports", "Quarterly QOR Reports"])
    
    with report_tabs[0]:
        st.image("https://via.placeholder.com/800x400?text=Daily+AUA+Reports+Visualization", use_container_width=True)
        st.markdown("""
        These key operational reports are automatically sent out daily to users from Power BI. Benefits compared to existing reports:
        - Interactive, allowing users to select any day to see history
        - Automated generation eliminates manual effort
        - Consistent formatting and calculations
        """)
    
    with report_tabs[1]:
        st.image("https://via.placeholder.com/800x400?text=Monthly+MOR+Reports+Visualization", use_container_width=True)
        st.markdown("""
        Monthly Operating Review ("MOR") reports show trends and further analysis at a higher level. Improvements:
        - Interactive and available on demand in Power BI
        - Previously static and manually prepared monthly
        - Includes drill-down capabilities for detailed analysis
        """)
    
    with report_tabs[2]:
        st.image("https://via.placeholder.com/800x400?text=Quarterly+QOR+Reports+Visualization", use_container_width=True)
        st.markdown("""
        Quarterly Operating Review ("QOR") reports show trends and further analysis at a higher level. Improvements:
        - Interactive and available on demand in Power BI
        - Previously static and manually prepared quarterly
        - Comprehensive KPIs with historical trend analysis
        """)
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Current challenges
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### Current Challenges")
    
    for challenge in challenges:
        st.markdown(f"- {challenge}")
    
    st.markdown("</div>", unsafe_allow_html=True)


def ai_ml_roadmap():
    st.markdown("<div class='main-header'>AI/ML Technical Roadmap</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-header'>Q2 2025 - Q2 2026</div>", unsafe_allow_html=True)
    
    # Executive summary
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### Executive Summary")
    st.markdown("""
    This technical roadmap outlines a structured approach to implementing AI/ML capabilities at Great Gray, with a strong focus on addressing immediate data quality and processing challenges while building toward a scalable Data as a Service (DaaS) foundation. The plan leverages the existing Analytics Hub infrastructure while introducing new AI/ML components to enhance automation, improve data quality, and enable advanced analytics.
    """)
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Strategic objectives
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### Strategic Objectives")
    
    objectives = [
        "**Reduce Manual Effort**: Automate repetitive data processing tasks to free up operational resources",
        "**Improve Data Quality**: Implement proactive monitoring and correction of data issues",
        "**Enable New Insights**: Develop AI-powered analytics capabilities",
        "**Enable Scalability**: Build systems that can handle growing data volumes and complexity",
        "**Foundation for DaaS**: Establish the infrastructure and processes to offer Data as a Service"
    ]
    
    for objective in objectives:
        st.markdown(f"- {objective}")
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Timeline with phases
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### Implementation Timeline")
    
    # Create a timeline visualization
    timeline_data = [
        {"Phase": "Phase 1: Intelligent Data Ingestion", "Start": "2025-04-01", "End": "2025-09-30", "Color": "#3b82f6"},
        {"Phase": "Phase 2: Proactive Data Quality", "Start": "2025-07-01", "End": "2025-12-31", "Color": "#10b981"},
        {"Phase": "Phase 3: Advanced Analytics & DaaS", "Start": "2026-01-01", "End": "2026-06-30", "Color": "#6366f1"}
    ]
    
    fig = go.Figure()
    
    current_date = datetime.now().strftime('%Y-%m-%d')
    
    for item in timeline_data:
        fig.add_trace(go.Bar(
            name=item["Phase"],
            y=[item["Phase"]],
            x=[(datetime.strptime(item["End"], '%Y-%m-%d') - datetime.strptime(item["Start"], '%Y-%m-%d')).days],
            orientation='h',
            marker=dict(color=item["Color"]),
            base=[(datetime.strptime(item["Start"], '%Y-%m-%d') - datetime.strptime("2025-04-01", '%Y-%m-%d')).days],
            hovertemplate=f"{item['Phase']}<br>Start: {item['Start']}<br>End: {item['End']}<extra></extra>"
        ))
    
    # Add a line for current date
    fig.add_vline(x=(datetime.strptime("2025-03-07", '%Y-%m-%d') - datetime.strptime("2025-04-01", '%Y-%m-%d')).days, 
                  line_dash="dash", line_color="red", annotation_text="Current Date: March 7, 2025")
    
    fig.update_layout(
        height=200,
        barmode='overlay',
        xaxis=dict(
            title="Days from April 1, 2025",
            tickvals=[0, 91, 183, 274, 365, 456],
            ticktext=["Apr 2025", "Jul 2025", "Oct 2025", "Jan 2026", "Apr 2026", "Jul 2026"]
        ),
        yaxis=dict(
            title=None
        ),
        margin=dict(l=0, r=0, t=10, b=0),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.3,
            xanchor="center",
            x=0.5
        )
    )
    
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Phases breakdown
    phases_tabs = st.tabs(["Phase 1", "Phase 2", "Phase 3"])
    
    with phases_tabs[0]:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("### Phase 1: Intelligent Data Ingestion (Q2-Q3 2025)")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### Core Components")
            st.markdown("1. **ML-Powered File Ingestion Service**")
            st.markdown("   - Classification models for categorizing files")
            st.markdown("   - Feature extraction for schema detection")
            st.markdown("   - Transformer-based models for column mapping")
            st.markdown("   - Anomaly detection for data validation")
            
            st.markdown("2. **Adaptive Data Pipeline Framework**")
            st.markdown("   - Pipeline template library")
            st.markdown("   - Self-optimizing transformation rules")
            st.markdown("   - Feedback loop for continuous improvement")
        
        with col2:
            st.markdown("#### Key Milestones")
            st.markdown("**Q2 2025 (Months 1-3)**")
            st.markdown("- RPAG ML-Powered Ingestion POC")
            st.markdown("- Team Onboarding & Infrastructure Setup")
            
            st.markdown("**Q3 2025 (Months 4-6)**")
            st.markdown("- Expand ML Ingestion to All File Types")
            st.markdown("- Adaptive Pipeline Framework")
            
            st.markdown("#### Key Deliverables")
            st.markdown("- Working POC for RPAG file types")
            st.markdown("- ML development infrastructure")
            st.markdown("- Full production implementation")
            st.markdown("- Documentation and knowledge transfer")
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    with phases_tabs[1]:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("### Phase 2: Proactive Data Quality Management (Q3-Q4 2025)")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### Core Components")
            st.markdown("1. **ML-Based Data Quality Monitoring**")
            st.markdown("   - Statistical profiling for data sources")
            st.markdown("   - Anomaly detection algorithms")
            st.markdown("   - Time-series forecasting for trend analysis")
            st.markdown("   - Classification models for issue categorization")
            
            st.markdown("2. **Intelligent Data Reconciliation**")
            st.markdown("   - Entity resolution models")
            st.markdown("   - Semantic matching algorithms")
            st.markdown("   - Confidence scoring and decision rules")
            st.markdown("   - Human-in-the-loop feedback mechanisms")
        
        with col2:
            st.markdown("#### Key Milestones")
            st.markdown("**Q3 2025 (Months 6-7)**")
            st.markdown("- Data Quality Baseline")
            
            st.markdown("**Q4 2025 (Months 8-10)**")
            st.markdown("- Predictive DQ Monitoring")
            st.markdown("- Intelligent Reconciliation")
            
            st.markdown("#### Key Deliverables")
            st.markdown("- End-to-end data quality monitoring system")
            st.markdown("- Predictive alerts for potential data issues")
            st.markdown("- Automated reconciliation for multi-source data")
            st.markdown("- Comprehensive data quality reporting")
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    with phases_tabs[2]:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("### Phase 3: Advanced Analytics & Data as a Service (Q1-Q2 2026)")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### Core Components")
            st.markdown("1. **AI-Powered Analytics Engine**")
            st.markdown("   - Pattern recognition for trend identification")
            st.markdown("   - Causal inference models")
            st.markdown("   - Natural language generation for insights")
            st.markdown("   - Recommendation systems for action items")
            
            st.markdown("2. **Data as a Service (DaaS) Platform**")
            st.markdown("   - API gateway with ML-based access control")
            st.markdown("   - Data virtualization layer")
            st.markdown("   - Real-time feature store")
            st.markdown("   - ML model registry and deployment platform")
        
        with col2:
            st.markdown("#### Key Milestones")
            st.markdown("**Q1 2026 (Months 11-13)**")
            st.markdown("- AI-Powered Analytics")
            st.markdown("- DaaS Framework")
            
            st.markdown("**Q2 2026 (Months 14-16)**")
            st.markdown("- DaaS Platform")
            
            st.markdown("#### Key Deliverables")
            st.markdown("- AI-powered analytics capabilities in Power BI")
            st.markdown("- Complete DaaS platform for internal/external use")
            st.markdown("- Documentation and training materials")
            st.markdown("- Governance framework for ongoing operations")
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Technology stack
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### Technology Stack")
    
    tech_tabs = st.tabs(["Core ML Components", "Integration Components", "Team Structure"])
    
    with tech_tabs[0]:
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### Data Processing & Feature Engineering")
            st.markdown("- PySpark (Databricks)")
            st.markdown("- Feature Store: Feast or Databricks Feature Store")
            st.markdown("- Data validation: Great Expectations")
            
            st.markdown("#### Model Development")
            st.markdown("- Frameworks: Scikit-learn, TensorFlow, PyTorch")
            st.markdown("- AI: Claude suite, Cursor and Phi 4 (Azure)")
            st.markdown("- NLP: Hugging Face Transformers, spaCy")
            st.markdown("- Time-series: Prophet, statsmodels")
            st.markdown("- AutoML: Databricks AutoML")
        
        with col2:
            st.markdown("#### MLOps")
            st.markdown("- Experiment tracking: MLflow")
            st.markdown("- Model registry: MLflow Model Registry")
            st.markdown("- Deployment: Docker containers, Kubernetes")
            st.markdown("- Monitoring: Prometheus, Grafana")
            
            st.markdown("#### Data Quality")
            st.markdown("- Profiling: Databricks Data Profiler")
            st.markdown("- Monitoring: Custom ML models + Great Expectations")
            st.markdown("- Alerting: Integration with existing monitoring tools")
    
    with tech_tabs[1]:
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### Data Ingestion")
            st.markdown("- Apache Airflow for orchestration")
            st.markdown("- Custom ML-powered ingestion service")
            st.markdown("- SFTP/API connectors for data sources")
        
        with col2:
            st.markdown("#### Data Storage")
            st.markdown("- Delta Lake (existing)")
            st.markdown("- Real-time feature store")
            st.markdown("- Model artifact storage")
            
            st.markdown("#### API & Services")
            st.markdown("- FastAPI for service endpoints")
            st.markdown("- API Gateway for access control")
            st.markdown("- Authentication & authorization services")
    
    with tech_tabs[2]:
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### Core Team (Immediate Hiring)")
            st.markdown("**Data Engineers (2)**")
            st.markdown("- Databricks/Spark expertise")
            st.markdown("- Data pipeline development")
            st.markdown("- Integration experience")
            
            st.markdown("**Data Scientists (2)**")
            st.markdown("- ML model development")
            st.markdown("- Feature engineering")
            st.markdown("- Model evaluation and validation")
        
        with col2:
            st.markdown("**Project Manager (1)**")
            st.markdown("- Agile project management")
            st.markdown("- ML/data science project experience")
            st.markdown("- Stakeholder management")
            
            st.markdown("#### Extended Team (Future Consideration)")
            st.markdown("- MLOps Engineer")
            st.markdown("- Data Governance Specialist")
            st.markdown("- AI Product Manager")
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Success metrics
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### Success Metrics")
    
    metrics_tabs = st.tabs(["Phase 1 Metrics", "Phase 2 Metrics", "Phase 3 Metrics"])
    
    with metrics_tabs[0]:
        for metric in success_metrics["Phase 1"]:
            st.markdown(f"- {metric}")
    
    with metrics_tabs[1]:
        for metric in success_metrics["Phase 2"]:
            st.markdown(f"- {metric}")
    
    with metrics_tabs[2]:
        for metric in success_metrics["Phase 3"]:
            st.markdown(f"- {metric}")
    
    st.markdown("</div>", unsafe_allow_html=True)

def strategic_recommendations():
    st.markdown("<div class='main-header'>Strategic Recommendations</div>", unsafe_allow_html=True)
    st.markdown("As of March 7, 2025")
    
    # Summary of assessment
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### Executive Summary")
    st.markdown("""
    After a thorough assessment of the Analytics Hub initiative with Inspire11, significant progress has been made through Phase 1 (AUA Reporting) and Phase 2 (Ownership/Omnibus & Invoice Reporting), but substantial challenges remain with data quality, business adoption, and lack of formalized data governance that are impeding the ability to scale.
    
    The Analytics Hub has delivered automation of key reports and established a foundation for data centralization, but the path forward requires:
    1. Technical Improvements: Implementing more sophisticated tools to address persistent data quality issues
    2. Organizational Changes: Establishing formal data governance and increasing business adoption
    3. Strategic Roadmap: Refining the approach to Phase 3 initiatives to deliver higher business value
    """)
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Recommendations by timeframe
    rec_tabs = st.tabs(["Immediate Actions (30 Days)", "Medium-Term (60-90 Days)", "Strategic Roadmap (6-12 Months)"])
    
    with rec_tabs[0]:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("### Immediate Actions (Next 30 Days)")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 1. Establish Data Governance Framework")
            st.markdown("- Define data ownership, quality standards, and stewardship roles")
            st.markdown("- Create data quality SLAs for internal and external data sources")
            st.markdown("- Implement data quality monitoring dashboards")
            
            st.markdown("#### 2. Address Technical Priorities")
            st.markdown("- Complete State Street SFTP cutover (pending 1 bug, should be completed EOW)")
            st.markdown("- Implement enhanced data quality checks")
            st.markdown("- Develop automated data quality monitoring and alerting")
        
        with col2:
            st.markdown("#### 3. Enhance Business Adoption")
            st.markdown("- Conduct targeted training sessions for business users")
            st.markdown("- Create user-friendly documentation and guides")
            st.markdown("- Establish regular touch points to gather feedback")
            
            st.markdown("#### Expected Outcomes")
            st.markdown("- Improved data quality and reduced manual intervention")
            st.markdown("- Greater business engagement with Analytics Hub")
            st.markdown("- Clear ownership and accountability for data assets")
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    with rec_tabs[1]:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("### Medium-Term Initiatives (60-90 Days)")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 1. AI/ML-Powered Data Quality")
            st.markdown("- Implement AI solution to automatically detect and remediate data quality issues from custodians")
            st.markdown("- Deploy ML models for data validation, anomaly detection, and auto-correction")
            st.markdown("- Create intelligent data quality monitoring dashboard with predictive capabilities")
            
            st.markdown("#### 2. RPAG Data Integration Acceleration")
            st.markdown("- Develop ML-powered solution to manage the 400+ files with different formats from RPAG")
            st.markdown("- Implement intelligent schema detection and mapping for variable data formats")
            st.markdown("- Automate reconciliation and validation processes")
        
        with col2:
            st.markdown("#### 3. Team Structure & Capabilities")
            st.markdown("- Strategically onboard new headcount:")
            st.markdown("  - 2 Data Engineers focused on pipeline optimization and automation")
            st.markdown("  - 2 Data Scientists dedicated to ML/AI solutions")
            st.markdown("  - 1 Project Manager to drive adoption and governance")
            
            st.markdown("#### Expected Outcomes")
            st.markdown("- 70% reduction in manual processing for data quality issues")
            st.markdown("- Streamlined RPAG data integration")
            st.markdown("- Dedicated team with clear responsibilities")
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    with rec_tabs[2]:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("### Strategic Roadmap (6-12 Months)")
        
        st.markdown("A strategic pivot toward AI/ML-powered solutions is recommended to address the most critical challenges:")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 1. Recordkeeper Initiative & Data as a Service")
            st.markdown("- Implement AI-powered data integration platform")
            st.markdown("- Develop intelligent APIs for data as a service capabilities")
            st.markdown("- Create ML models to standardize data across platforms")
            
            st.markdown("#### 2. Alteryx Migration & Process Transformation")
            st.markdown("- Leverage AI to accelerate migration of reports")
            st.markdown("- Implement intelligent workflow automation")
            st.markdown("- Create self-service analytics with AI assistants")
        
        with col2:
            st.markdown("#### 3. Master Data Management & Intelligence")
            st.markdown("- Build AI-powered MDM solution for funds and plans")
            st.markdown("- Replace FactSet with in-house solution (potential $250k/year savings)")
            st.markdown("- Implement automated data lineage and impact analysis")
            
            st.markdown("#### 4. Advanced Analytics Platform")
            st.markdown("- Develop AI models for profitability and performance prediction")
            st.markdown("- Implement intelligent anomaly detection")
            st.markdown("- Create predictive analytics for business growth")
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Resource allocation
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### Resource Allocation")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("#### Data Engineers (2)")
        st.markdown("- **Engineer 1**: AI/ML-powered data quality automation and RPAG integration")
        st.markdown("- **Engineer 2**: Recordkeeper Initiative architecture and Data as a Service implementation")
    
    with col2:
        st.markdown("#### Data Scientists (2)")
        st.markdown("- **Scientist 1**: ML models for data ingestion, classification, and anomaly detection")
        st.markdown("- **Scientist 2**: AI for predictive analytics and intelligent data processing applications")
    
    with col3:
        st.markdown("#### Project Manager")
        st.markdown("- Coordinate Enterprise Data Governance implementation")
        st.markdown("- Drive user adoption through targeted enablement programs")
        st.markdown("- Manage Alteryx migration and process transformation initiatives")
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Key benefits
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### Expected Benefits")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Operational Benefits")
        st.markdown("- 70% reduction in manual data processing")
        st.markdown("- 90% automation of data quality validation")
        st.markdown("- 60% faster time to insight for business users")
        st.markdown("- $250k potential annual savings from FactSet replacement")
    
    with col2:
        st.markdown("#### Strategic Benefits")
        st.markdown("- Data-driven decision making across the organization")
        st.markdown("- Scalable platform for future acquisitions and growth")
        st.markdown("- Improved data quality and confidence in reporting")
        st.markdown("- Enhanced ability to identify business opportunities")
    
    st.markdown("</div>", unsafe_allow_html=True)


# Run the selected page
st.write(f"Current page selected: {page}")  # Debug line

if page == "Executive Dashboard":
    #st.write("Loading Executive Dashboard...")  # Debug line
    executive_dashboard()
elif page == "Project Status":
    #st.write("Loading Project Status...")  # Debug line
    project_status_page()
elif page == "Analytics Hub":
    #st.write("Loading Analytics Hub...")  # Debug line
    analytics_hub()
elif page == "AI/ML Roadmap":
    #st.write("Loading AI/ML Roadmap...")  # Debug line
    ai_ml_roadmap()
elif page == "Strategic Recommendations":
    #st.write("Loading Strategic Recommendations...")  # Debug line
    strategic_recommendations()
