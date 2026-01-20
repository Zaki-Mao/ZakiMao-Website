import streamlit as st

# ==========================================
# 🏠 HOME PAGE 逻辑封装
# ==========================================
def home_page():
    # 1. 页面配置
    st.set_page_config(
        page_title="Zaki Mao | Portfolio",
        page_icon="⚫",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    # 2. 图片配置 (保持不变)
    IMG_FOTOZAKI = "https://images.unsplash.com/photo-1542038784424-48ed38935839?q=80&w=1200&auto=format&fit=crop" 
    IMG_SPOTMARK = "https://images.unsplash.com/photo-1611162617474-5b21e879e113?q=80&w=1200&auto=format&fit=crop"
    IMG_LOVEMARK = "https://images.unsplash.com/photo-1518531933037-91b2f5f229cc?q=80&w=1200&auto=format&fit=crop"
    IMG_BEHOLMES = "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?q=80&w=1200&auto=format&fit=crop"

    # 3. CSS 样式 (核心更新)
    st.markdown("""
    <style>
        /* 【改动 1】时尚渐变背景 */
        .stApp {
            background: linear-gradient(135deg, #0f0c29, #302b63, #24243e); /* 时尚深色渐变 */
            background-attachment: fixed; /* 确保背景固定，不随滚动条移动 */
            color: #ffffff;
            font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        }
        
        /* 隐藏默认元素 */
        #MainMenu, footer, header {visibility: hidden;}
        /* 修复可能的全局链接蓝框 */
        a:focus, a:hover { outline: none; border: none; }
        
        /* 【改动 2】导航栏间距缩小 */
        .nav-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 15px 0; /* 从 30px 减小到 15px */
            border-bottom: 1px solid rgba(255,255,255,0.1); /* 让分割线更柔和 */
            margin-bottom: 40px; /* 从 60px 减小到 40px */
        }
        .logo { font-size: 24px; font-weight: 800; border: 2px solid white; border-radius: 50%; width: 44px; height: 44px; display: flex; align-items: center; justify-content: center; color: white; text-decoration: none; }
        .nav-links { display: flex; gap: 15px; }
        .nav-pill { padding: 8px 24px; border-radius: 100px; text-decoration: none; color: #000 !important; font-weight: 700; font-size: 14px; transition: transform 0.2s; }
        .nav-pill:hover { transform: scale(1.05); }
        .bg-orange { background-color: #FF5C00; }
        .bg-green { background-color: #00D26A; }
        .bg-blue { background-color: #5C95FF; }

        /* Hero 标题 */
        .hero-container { margin-top: -20px; } /* 稍微向上提拉 */
        .hero-title { font-size: clamp(60px, 11vw, 180px); font-weight: 900; line-height: 0.9; letter-spacing: -0.04em; white-space: nowrap; margin: 0; }
        .hero-subtitle { font-size: 20px; color: rgba(255,255,255,0.7); max-width: 600px; margin-top: 20px; line-height: 1.5; }

        /* 卡片交互 */
        .project-card { position: relative; width: 100%; height: 400px; border-radius: 12px; /* 圆角稍微加大一点 */ overflow: hidden; margin-bottom: 30px; cursor: pointer; box-shadow: 0 10px 30px rgba(0,0,0,0.2); }
        .project-img { width: 100%; height: 100%; object-fit: cover; transition: transform 0.6s cubic-bezier(0.25, 0.46, 0.45, 0.94); filter: grayscale(10%); }
        .project-overlay { position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0, 0, 0, 0.85); display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; opacity: 0; transition: opacity 0.4s ease; padding: 30px; }
        .project-card:hover .project-overlay { opacity: 1; }
        .project-card:hover .project-img { transform: scale(1.05); }
        .overlay-title { font-size: 32px; font-weight: 800; margin-bottom: 15px; color: #fff; text-transform: uppercase; }
        .overlay-desc { font-size: 16px; line-height: 1.5; color: #ccc; margin-bottom: 20px; }
        .overlay-tag { font-size: 12px; border: 1px solid #444; padding: 6px 16px; border-radius: 20px; text-transform: uppercase; letter-spacing: 1px; color: #888; }
        
        .footer { margin-top: 80px; padding-top: 40px; border-top: 1px solid rgba(255,255,255,0.1); text-align: center; color: rgba(255,255,255,0.5); font-size: 12px; }
    </style>
    """, unsafe_allow_html=True)

    # 4. 页面内容渲染
    st.markdown("""
        <div class="nav-container">
            <a href="/" class="logo" target="_self">ZM</a>
            <div class="nav-links">
                <a href="/" class="nav-pill bg-orange" target="_self">Home</a>
                <a href="#projects" class="nav-pill bg-green">Work</a>
                <a href="/about" class="nav-pill bg-blue" target="_self">About</a>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="hero-container">
            <div class="hero-title">ZAKI MAO.</div>
            <div class="hero-subtitle">
                Independent Developer, Visual Designer & PM.<br>
                Based in the cloud, building digital artifacts for the future.
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown('<div id="projects" style="margin-top: 60px;"></div>', unsafe_allow_html=True)

    projects = [
        {"name": "FotoZaki", "desc": "Street photography archive.", "tag": "Photography", "link": "https://fotozaki.com", "img": IMG_FOTOZAKI},
        {"name": "SpotMark", "desc": "Figma plugin for PMs.", "tag": "Tool", "link": "#", "img": IMG_SPOTMARK},
        {"name": "LoveMark", "desc": "AI emotional agent.", "tag": "AI", "link": "#", "img": IMG_LOVEMARK},
        {"name": "BeHolmes", "desc": "Web3 data detective.", "tag": "Web3", "link": "https://beholmes.com", "img": IMG_BEHOLMES}
    ]

    # ==========================================
    # 【改动 3 & 4】 规整网格渲染 & 修复蓝框
    # ==========================================
    def render_card(p):
        # 在 <a> 标签中增加了 style="outline: none; border: none;" 来强制消除可能的蓝框
        return f"""<a href="{p['link']}" target="_blank" style="text-decoration:none; outline: none; border: none;"><div class="project-card"><img src="{p['img']}" class="project-img"><div class="project-overlay"><div class="overlay-title">{p['name']}</div><div class="overlay-desc">{p['desc']}</div><div class="overlay-tag">{p['tag']}</div></div></div></a>"""

    # 创建 2x2 网格循环
    rows = [projects[i:i+2] for i in range(0, len(projects), 2)]
    for row_projects in rows:
        cols = st.columns(2) # 每一行创建两个列
        for i, project in enumerate(row_projects):
            with cols[i]:
                st.markdown(render_card(project), unsafe_allow_html=True)
    # ==========================================

    st.markdown('<div class="footer">DESIGNED & DEVELOPED BY ZAKI MAO © 2026</div>', unsafe_allow_html=True)

# ==========================================
# 🚀 路由配置 (ROUTER)
# ==========================================
pg = st.navigation([
    st.Page(home_page, title="Home", url_path="/"),      
    st.Page("about.py", title="About", url_path="about") 
], position="hidden")

pg.run()
