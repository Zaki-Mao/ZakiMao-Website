import streamlit as st

# 1. 页面配置
st.set_page_config(
    page_title="Zaki Mao | Portfolio",
    page_icon="⚫",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==========================================
# 👇 在这里替换你的图片链接 (留空处)
# ==========================================
# 建议图片比例 4:3 或 16:9，分辨率 1200px 以上效果最佳
IMG_FOTOZAKI = "https://images.unsplash.com/photo-1542038784424-48ed38935839?q=80&w=1200&auto=format&fit=crop"  # 替换为 FotoZaki 封面图
IMG_SPOTMARK = "https://images.unsplash.com/photo-1611162617474-5b21e879e113?q=80&w=1200&auto=format&fit=crop"  # 替换为 SpotMark 界面图
IMG_LOVEMARK = "https://images.unsplash.com/photo-1518531933037-91b2f5f229cc?q=80&w=1200&auto=format&fit=crop"  # 替换为 LoveMark 概念图
IMG_BEHOLMES = "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?q=80&w=1200&auto=format&fit=crop"  # 替换为 BeHolmes 封面图
# ==========================================

# 2. 自定义 CSS (核心视觉升级)
st.markdown("""
<style>
    /* 全局深色模式 */
    .stApp {
        background-color: #050505;
        color: #ffffff;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
    
    /* 隐藏默认元素 */
    #MainMenu, footer, header {visibility: hidden;}

    /* 顶部导航 */
    .nav-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 30px 0;
        border-bottom: 1px solid #222;
        margin-bottom: 60px;
    }
    .logo {
        font-size: 24px;
        font-weight: 800;
        border: 2px solid white;
        border-radius: 50%;
        width: 44px;
        height: 44px;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .nav-pill {
        padding: 8px 24px;
        border-radius: 100px;
        text-decoration: none;
        color: #000 !important;
        font-weight: 700;
        font-size: 14px;
        margin-left: 10px;
        transition: transform 0.2s;
    }
    .nav-pill:hover { transform: scale(1.05); }
    .bg-orange { background-color: #FF5C00; }
    .bg-green { background-color: #00D26A; }
    .bg-blue { background-color: #5C95FF; }

    /* Hero 标题 (横向排版) */
    .hero-title {
        font-size: clamp(60px, 11vw, 180px); /* 响应式超大字 */
        font-weight: 900;
        line-height: 0.9;
        letter-spacing: -0.04em;
        margin-bottom: 10px;
        white-space: nowrap; /* 强制不换行 */
    }
    .hero-subtitle {
        font-size: 20px;
        color: #888;
        max-width: 600px;
        margin-bottom: 80px;
    }

    /* 项目卡片 - 悬浮特效核心代码 */
    .project-card {
        position: relative;
        width: 100%;
        height: 450px; /* 固定高度，确保整齐 */
        overflow: hidden;
        border-radius: 8px;
        margin-bottom: 40px;
        cursor: pointer;
    }
    
    /* 背景图片样式 */
    .project-img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        transition: transform 0.6s cubic-bezier(0.25, 0.46, 0.45, 0.94);
    }
    
    /* 悬浮遮罩层 */
    .project-overlay {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0, 0, 0, 0.85); /* 深色遮罩 */
        display: flex;
        flex-direction: column;
        justify-content: center; /* 垂直居中 */
        align-items: center; /* 水平居中 */
        text-align: center;
        opacity: 0; /* 默认隐藏 */
        transition: opacity 0.4s ease;
        padding: 40px;
    }
    
    /* 鼠标悬停时的状态 */
    .project-card:hover .project-overlay { opacity: 1; }
    .project-card:hover .project-img { transform: scale(1.05); } /* 图片微放大 */

    .overlay-title {
        font-size: 32px;
        font-weight: 800;
        margin-bottom: 15px;
        text-transform: uppercase;
        color: #fff;
    }
    .overlay-desc {
        font-size: 16px;
        line-height: 1.6;
        color: #ccc;
        max-width: 80%;
    }
    .overlay-tag {
        margin-top: 20px;
        font-size: 12px;
        border: 1px solid #444;
        padding: 6px 16px;
        border-radius: 20px;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    /* 底部 Footer */
    .footer-section {
        margin-top: 120px;
        padding-top: 40px;
        border-top: 1px solid #222;
        text-align: center;
        color: #555;
    }
</style>
""", unsafe_allow_html=True)

# 3. 导航栏
st.markdown("""
    <div class="nav-container">
        <div class="logo">ZM</div>
        <div>
            <a href="#" class="nav-pill bg-orange">Home</a>
            <a href="#projects" class="nav-pill bg-green">Projects</a>
            <a href="#about" class="nav-pill bg-blue">About</a>
        </div>
    </div>
""", unsafe_allow_html=True)

# 4. Hero 区域 (ZAKI MAO 横排)
st.markdown('<div class="hero-title">ZAKI MAO.</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-subtitle">Independent Developer, Visual Designer & PM.<br>Based in the cloud, building for the future.</div>', unsafe_allow_html=True)

# 5. 项目网格 (Project Grid)
st.markdown('<div id="projects"></div>', unsafe_allow_html=True)

# 定义你的真实项目数据
projects = [
    {
        "name": "FotoZaki",
        "desc": "我的街头摄影数字档案。记录城市角落的光影与瞬间，一个纯粹的视觉日记。",
        "tag": "Photography / Website",
        "link": "https://fotozaki.com",
        "img": IMG_FOTOZAKI
    },
    {
        "name": "SpotMark",
        "desc": "专为产品经理打造的 Figma 插件。让设计稿与项目管理无缝对接，提升交付效率。",
        "tag": "Figma Plugin / Efficiency",
        "link": "#", # 填入你的插件链接
        "img": IMG_SPOTMARK
    },
    {
        "name": "LoveMark",
        "desc": "基于 Coze 平台的 AI 情感 Agent。当逻辑无法解决问题时，它为你提供感性的建议。",
        "tag": "AI Agent / LLM",
        "link": "#", # 填入你的 Coze 链接
        "img": IMG_LOVEMARK
    },
    {
        "name": "BeHolmes",
        "desc": "数据侦探分析工具。在海量信息的噪音中寻找信号，Web3 链上数据的可视化探索。",
        "tag": "Data Analysis / Web3",
        "link": "https://beholmes.com",
        "img": IMG_BEHOLMES
    }
]

col1, col2 = st.columns(2)

def render_card(project):
    return f"""
    <a href="{project['link']}" target="_blank" style="text-decoration:none;">
        <div class="project-card">
            <img src="{project['img']}" class="project-img">
            <div class="project-overlay">
                <div class="overlay-title">{project['name']}</div>
                <div class="overlay-desc">{project['desc']}</div>
                <div class="overlay-tag">{project['tag']}</div>
            </div>
        </div>
    </a>
    """

with col1:
    st.markdown(render_card(projects[0]), unsafe_allow_html=True) # FotoZaki
    st.markdown(render_card(projects[2]), unsafe_allow_html=True) # LoveMark

with col2:
    st.markdown(render_card(projects[1]), unsafe_allow_html=True) # SpotMark
    st.markdown(render_card(projects[3]), unsafe_allow_html=True) # BeHolmes

# 6. 底部 Footer
st.markdown("""
    <div class="footer-section">
        <p>DESIGNED & DEVELOPED BY ZAKI MAO © 2026</p>
    </div>
""", unsafe_allow_html=True)
