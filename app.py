import streamlit as st

# ==========================================
# 🏠 HOME PAGE 逻辑封装
# ==========================================
def home_page():
    # 1. 页面配置 (必须在函数内第一行)
    st.set_page_config(
        page_title="Zaki Mao | Portfolio",
        page_icon="⚫",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    # 2. 图片配置
    IMG_FOTOZAKI = "https://images.unsplash.com/photo-1542038784424-48ed38935839?q=80&w=1200&auto=format&fit=crop" 
    IMG_SPOTMARK = "https://images.unsplash.com/photo-1611162617474-5b21e879e113?q=80&w=1200&auto=format&fit=crop"
    IMG_LOVEMARK = "https://images.unsplash.com/photo-1518531933037-91b2f5f229cc?q=80&w=1200&auto=format&fit=crop"
    IMG_BEHOLMES = "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?q=80&w=1200&auto=format&fit=crop"

    # 3. CSS 样式
    st.markdown("""
    <style>
        .stApp { background-color: #050505; color: #ffffff; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; }
        #MainMenu, footer, header {visibility: hidden;}
        
        /* 导航栏 */
        .nav-container { display: flex; justify-content: space-between; align-items: center; padding: 30px 0; border-bottom: 1px solid #222; margin-bottom: 60px; }
        .logo { font-size: 24px; font-weight: 800; border: 2px solid white; border-radius: 50%; width: 44px; height: 44px; display: flex; align-items: center; justify-content: center; color: white; text-decoration: none; }
        .nav-links { display: flex; gap: 15px; }
        .nav-pill { padding: 8px 24px; border-radius: 100px; text-decoration: none; color: #000 !important; font-weight: 700; font-size: 14px; transition: transform 0.2s; }
        .nav-pill:hover { transform: scale(1.05); }
        .bg-orange { background-color: #FF5C00; }
        .bg-green { background-color: #00D26A; }
        .bg-blue { background-color: #5C95FF; }

        /* Hero 标题 */
        .hero-title { font-size: clamp(60px, 11vw, 180px); font-weight: 900; line-height: 0.9; letter-spacing: -0.04em; white-space: nowrap; margin: 0; }
        .hero-subtitle { font-size: 20px; color: #888; max-width: 600px; margin-top: 20px; line-height: 1.5; }

        /* 卡片交互 */
        .project-card { position: relative; width: 100%; height: 400px; border-radius: 8px; overflow: hidden; margin-bottom: 40px; cursor: pointer; }
        .project-img { width: 100%; height: 100%; object-fit: cover; transition: transform 0.6s cubic-bezier(0.25, 0.46, 0.45, 0.94); filter: grayscale(10%); }
        .project-overlay { position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0, 0, 0, 0.85); display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; opacity: 0; transition: opacity 0.4s ease; padding: 30px; }
        .project-card:hover .project-overlay { opacity: 1; }
        .project-card:hover .project-img { transform: scale(1.05); }
        .overlay-title { font-size: 32px; font-weight: 800; margin-bottom: 15px; color: #fff; text-transform: uppercase; }
        .overlay-desc { font-size: 16px; line-height: 1.5; color: #ccc; margin-bottom: 20px; }
        .overlay-tag { font-size: 12px; border: 1px solid #444; padding: 6px 16px; border-radius: 20px; text-transform: uppercase; letter-spacing: 1px; color: #888; }
        
        .footer { margin-top: 100px; padding-top: 40px; border-top: 1px solid #222; text-align: center; color: #444; font-size: 12px; }
    </style>
    """, unsafe_allow_html=True)

    # 4. 页面内容渲染
    # 注意：这里的 href="/about" 将会匹配我们在底部定义的 URL 路径
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

    st.markdown('<div id="projects"></div>', unsafe_allow_html=True)

    projects = [
        {"name": "FotoZaki", "desc": "Street photography archive.", "tag": "Photography", "link": "https://fotozaki.com", "img": IMG_FOTOZAKI},
        {"name": "SpotMark", "desc": "Figma plugin for PMs.", "tag": "Tool", "link": "#", "img": IMG_SPOTMARK},
        {"name": "LoveMark", "desc": "AI emotional agent.", "tag": "AI", "link": "#", "img": IMG_LOVEMARK},
        {"name": "BeHolmes", "desc": "Web3 data detective.", "tag": "Web3", "link": "https://beholmes.com", "img": IMG_BEHOLMES}
    ]

    col1, col2 = st.columns(2)
    def render_card(p):
        return f"""<a href="{p['link']}" target="_blank" style="text-decoration:none;"><div class="project-card"><img src="{p['img']}" class="project-img"><div class="project-overlay"><div class="overlay-title">{p['name']}</div><div class="overlay-desc">{p['desc']}</div><div class="overlay-tag">{p['tag']}</div></div></div></a>"""

    with col1: st.markdown(render_card(projects[0]), unsafe_allow_html=True); st.markdown(render_card(projects[2]), unsafe_allow_html=True)
    with col2: st.markdown(render_card(projects[1]), unsafe_allow_html=True); st.markdown(render_card(projects[3]), unsafe_allow_html=True)

    st.markdown('<div class="footer">DESIGNED & DEVELOPED BY ZAKI MAO © 2026</div>', unsafe_allow_html=True)

# ==========================================
# 🚀 路由配置 (ROUTER)
# ==========================================
# 这里定义了只有两个页面：一个是本文件里的 Home 函数，一个是同目录下的 about.py 文件
pg = st.navigation([
    st.Page(home_page, title="Home", url_path="/"),       # 首页路径为 /
    st.Page("about.py", title="About", url_path="about")  # About页路径为 /about
], position="hidden") # position="hidden" 隐藏左侧默认侧边栏，使用我们自定义的按钮导航

pg.run()
