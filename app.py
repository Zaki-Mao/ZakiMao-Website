import streamlit as st

# 1. 页面基础配置
st.set_page_config(
    page_title="Zaki Mao | Portfolio",
    page_icon="⚫",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. 自定义 CSS (核心部分：复刻 Grain Archive 的视觉风格)
st.markdown("""
<style>
    /* 全局设置：深色背景，无衬线字体 */
    .stApp {
        background-color: #0e0e0e;
        color: #ffffff;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
    
    /* 隐藏 Streamlit 默认的 Header 和 Footer */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* 顶部导航栏样式 */
    .nav-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 20px 0;
        border-bottom: 1px solid #333;
        margin-bottom: 40px;
    }
    .logo {
        font-size: 24px;
        font-weight: bold;
        border: 2px solid white;
        border-radius: 50%;
        width: 40px;
        height: 40px;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .nav-links {
        display: flex;
        gap: 15px;
    }
    .nav-pill {
        padding: 8px 20px;
        border-radius: 50px;
        text-decoration: none;
        color: black !important;
        font-weight: bold;
        font-size: 14px;
        transition: transform 0.2s;
    }
    .nav-pill:hover { transform: scale(1.05); }
    
    /* 颜色类 */
    .bg-orange { background-color: #ff6b00; }
    .bg-green { background-color: #2bd464; }
    .bg-blue { background-color: #8faaff; }

    /* Hero 大标题样式 */
    .hero-title {
        font-size: clamp(60px, 10vw, 150px); /* 响应式字体 */
        font-weight: 900;
        line-height: 0.85;
        letter-spacing: -2px;
        margin-bottom: 30px;
        text-transform: uppercase;
    }

    /* 项目卡片样式 (Grid) */
    .project-card {
        position: relative;
        margin-bottom: 20px;
        cursor: pointer;
        transition: opacity 0.3s;
    }
    .project-card:hover { opacity: 0.9; }
    .project-img {
        width: 100%;
        height: 400px;
        object-fit: cover;
        border-radius: 4px; /* 轻微圆角 */
        filter: grayscale(20%); /* 稍微降低饱和度以符合风格 */
    }
    .project-overlay {
        position: absolute;
        bottom: 0;
        left: 0;
        width: 100%;
        padding: 15px;
        background: linear-gradient(to top, rgba(0,0,0,0.8), transparent);
        color: white;
    }
    .project-title {
        font-size: 18px;
        font-weight: bold;
        margin: 0;
    }
    .project-meta {
        font-size: 12px;
        opacity: 0.8;
        margin-top: 5px;
    }

    /* 列表区域样式 (Cinema Selects 风格) */
    .list-header {
        font-size: 60px;
        font-weight: 800;
        letter-spacing: -2px;
        margin-top: 80px;
        margin-bottom: 40px;
        line-height: 0.9;
    }
    .list-row {
        display: flex;
        border-top: 1px solid #333;
        padding: 20px 0;
        align-items: center;
        transition: background 0.3s;
    }
    .list-row:hover { background-color: #1a1a1a; }
    .col-1 { width: 30%; font-weight: bold; font-size: 18px; }
    .col-2 { width: 15%; color: #888; }
    .col-3 { width: 55%; text-align: right; }
    a.row-link { color: white; text-decoration: none; display: block; width: 100%; }

    /* Footer */
    .footer-section {
        margin-top: 100px;
        padding: 60px 0;
        border-top: 1px solid #333;
        text-align: center;
    }
    
    /* 按钮基础样式覆盖 */
    div.stButton > button {
        width: 100%;
        border-radius: 0;
        background-color: transparent;
        border: 1px solid #333;
        color: white;
        padding: 20px;
    }
</style>
""", unsafe_allow_html=True)

# 3. 顶部导航栏 (HTML注入)
st.markdown("""
    <div class="nav-container">
        <div class="logo">ZM</div>
        <div class="nav-links">
            <a href="#" class="nav-pill bg-orange">Home</a>
            <a href="#projects" class="nav-pill bg-green">Projects</a>
            <a href="#about" class="nav-pill bg-blue">About</a>
        </div>
    </div>
""", unsafe_allow_html=True)

# 4. Hero 区域 (大标题)
st.markdown('<div class="hero-title">Zaki<br>Mao.</div>', unsafe_allow_html=True)
st.markdown("Independent developer & visual designer based in the cloud.")

st.markdown("---")

# 5. 项目展示区域 (Grid System)
st.markdown('<div id="projects"></div>', unsafe_allow_html=True) # 锚点

# 定义你的项目数据
projects = [
    {
        "name": "FotoZaki",
        "category": "Photography / Visuals",
        "year": "2024",
        "img": "https://images.unsplash.com/photo-1542038784424-48ed38935839?q=80&w=1000&auto=format&fit=crop",
        "link": "https://fotozaki.com" # 假设链接
    },
    {
        "name": "BeHolmes",
        "category": "Data Analysis / Detective",
        "year": "2025",
        "img": "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?q=80&w=1000&auto=format&fit=crop",
        "link": "https://beholmes.com" # 假设链接
    },
    {
        "name": "Grain Archive",
        "category": "Design System",
        "year": "2023",
        "img": "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?q=80&w=1000&auto=format&fit=crop",
        "link": "#"
    },
    {
        "name": "System Zero",
        "category": "Infrastructure",
        "year": "2024",
        "img": "https://images.unsplash.com/photo-1518770660439-4636190af475?q=80&w=1000&auto=format&fit=crop",
        "link": "#"
    }
]

# 创建 2列布局
col1, col2 = st.columns(2)

# 渲染项目卡片函数
def render_project_card(project):
    # 使用 HTML 创建可点击的卡片效果
    card_html = f"""
    <a href="{project['link']}" target="_blank" style="text-decoration:none;">
        <div class="project-card">
            <img src="{project['img']}" class="project-img">
            <div class="project-overlay">
                <p class="project-title">{project['name']}</p>
                <div style="display:flex; justify-content:space-between; margin-top:5px;">
                    <span class="project-meta">{project['category']}</span>
                    <span class="project-meta">{project['year']}</span>
                </div>
            </div>
        </div>
    </a>
    """
    st.markdown(card_html, unsafe_allow_html=True)

# 分配卡片到左右两列
with col1:
    render_project_card(projects[0]) # FotoZaki
    render_project_card(projects[2])

with col2:
    render_project_card(projects[1]) # BeHolmes
    render_project_card(projects[3])

# 6. 列表/详细信息区域 (复刻 Figma 中的 "Cinema Selects")
st.markdown('<div class="list-header" id="about">Selected<br>Works</div>', unsafe_allow_html=True)

# 定义列表数据
works = [
    {"title": "Interactive Python Dashboards", "year": "2024", "desc": "Streamlit & Data Viz"},
    {"title": "Neural Network Art", "year": "2023", "desc": "Generative AI"},
    {"title": "Minimalist Web Design", "year": "2025", "desc": "UI/UX Research"},
    {"title": "Open Source Contributions", "year": "2022", "desc": "GitHub Maintainer"},
]

# 渲染列表
for work in works:
    st.markdown(f"""
    <div class="list-row">
        <div class="col-1">{work['title']}</div>
        <div class="col-2">{work['year']}</div>
        <div class="col-3">{work['desc']} ↗</div>
    </div>
    """, unsafe_allow_html=True)

# 7. 底部 Footer
st.markdown("""
    <div class="footer-section">
        <h1 style="font-size: 80px; margin:0; line-height:1;">ZAKIMAO</h1>
        <p style="color:#666; margin-top:20px;">© 2026 Zaki Mao. All rights reserved.</p>
        <div style="margin-top:30px;">
            <a href="#" style="color:white; margin:0 10px;">Email</a>
            <a href="#" style="color:white; margin:0 10px;">GitHub</a>
            <a href="#" style="color:white; margin:0 10px;">Twitter</a>
        </div>
    </div>
""", unsafe_allow_html=True)
