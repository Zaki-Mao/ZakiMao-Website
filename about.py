import streamlit as st
import streamlit.components.v1 as components

# 页面配置
st.set_page_config(page_title="About | Zaki Mao", page_icon="⚫", layout="wide", initial_sidebar_state="collapsed")

# 隐藏 Streamlit 自带的 UI，让 HTML 全屏显示
st.markdown("""
    <style>
        #MainMenu, footer, header {visibility: hidden;}
        .stApp { padding: 0 !important; margin: 0 !important; overflow: hidden; }
        .block-container { padding: 0 !important; margin: 0 !important; max-width: 100%; }
    </style>
""", unsafe_allow_html=True)

# 你的 HTML 代码 (已修改占位符和返回链接)
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ABOUT | VISUAL ARCHIVE</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;900&display=swap" rel="stylesheet">
    <style>
        :root { --bg: #ffffff; --text: #000000; --transition: cubic-bezier(0.4, 0, 0.2, 1); }
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Inter', sans-serif; background: var(--bg); color: var(--text); overflow-x: hidden; }

        .about-container { display: flex; min-height: 100vh; }
        
        /* 左侧海报 (2/3 宽度) */
        .profile-side {
            width: 66.666%;
            height: 100vh;
            position: fixed; top: 0; left: 0;
            background: #f0f0f0; overflow: hidden; z-index: 1;
        }
        /* 👇👇👇 在这里替换你的头像链接 👇👇👇 */
        .profile-img { 
            width: 100%; height: 100%; object-fit: cover; transition: transform 1.5s ease-out; 
            content: url("https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?q=80&w=1000&auto=format&fit=crop"); 
        }
        .profile-side:hover .profile-img { transform: scale(1.03); }

        /* 右侧内容区 (1/3 宽度) */
        .content-side {
            width: 33.333%; margin-left: 66.666%; padding: 140px 60px 100px; 
            display: flex; flex-direction: column; justify-content: center; background: #fff;
        }

        .huge-title { font-size: 60px; font-weight: 900; line-height: 1.3; margin-bottom: 40px; letter-spacing: -2px; }
        .bio-text { font-size: 15px; line-height: 1.8; margin-bottom: 25px; color: #333; }
        
        .gear-section { margin-top: 60px; border-top: 1px solid #000; padding-top: 25px; width: 100%; }
        .gear-header { font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 20px; }
        .gear-row { display: flex; justify-content: space-between; margin-bottom: 12px; font-size: 13px; border-bottom: 1px solid #eee; padding-bottom: 8px; }
        .gear-label { color: #888; font-weight: 500; }

        .contact-btn { 
            display: block; width: 100%; margin-top: 40px; padding: 20px 0;
            background: #000; color: #fff; text-decoration: none; font-weight: 700; 
            text-transform: uppercase; letter-spacing: 1px; text-align: center; 
            transition: 0.3s; cursor: pointer; border: none;
        }
        .contact-btn:hover { background: #333; }

        /* HEADER & NAV */
        header {
            position: fixed; top: 0; left: 0; width: 100%; height: 80px; z-index: 100;
            display: flex; align-items: center; justify-content: space-between; padding: 0 40px;
            pointer-events: none; 
        }
        .logo { font-weight: 900; font-size: 20px; text-decoration: none; color: #fff; mix-blend-mode: difference; pointer-events: auto; }
        .header-right { display: flex; align-items: center; gap: 30px; pointer-events: auto; }
        .lang-switch, .menu-trigger { font-weight: 700; font-size: 11px; letter-spacing: 1px; cursor: pointer; color: #000; }

        /* CONTACT MODAL */
        .modal-overlay {
            position: fixed; inset: 0; background: rgba(0,0,0,0.6); backdrop-filter: blur(8px);
            z-index: 1000; display: flex; align-items: center; justify-content: center;
            opacity: 0; pointer-events: none; transition: opacity 0.4s ease;
        }
        .modal-overlay.active { opacity: 1; pointer-events: auto; }
        .contact-modal {
            background: #fff; width: 90%; max-width: 450px; padding: 50px 40px;
            text-align: center; position: relative; transform: scale(0.95);
            transition: transform 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
        }
        .modal-overlay.active .contact-modal { transform: scale(1); }
        .modal-close-btn { position: absolute; top: 20px; right: 20px; font-size: 24px; cursor: pointer; }

        /* MOBILE */
        @media (max-width: 768px) {
            .about-container { flex-direction: column; }
            .profile-side { position: relative; width: 100%; height: 50vh; }
            .content-side { width: 100%; margin-left: 0; padding: 60px 30px; }
        }
    </style>
</head>
<body>
    <header>
        <a href="/" target="_self" class="logo">FotoZaki</a> 
        <div class="header-right">
            <div class="lang-switch" id="langSwitch">EN / 中</div>
        </div>
    </header>

    <div class="about-container">
        <div class="profile-side">
            <div class="profile-img"></div>
        </div>

        <div class="content-side">
            <h1 class="huge-title" data-en="Hello,<br>I'm Zaki." data-cn="你好，<br>我是 Zaki。">Hello,<br>I'm Zaki.</h1>
            
            <p class="bio-text" 
               data-en="[INSERT YOUR ENGLISH INTRO HERE. Example: I am a photographer based in Shanghai...]"
               data-cn="[在这里填写你的中文介绍。例如：我是一名常驻上海的摄影师...]">
               [INSERT YOUR ENGLISH INTRO HERE. Example: I am a photographer based in Shanghai...]
            </p>
            
            <p class="bio-text"
               data-en="[INSERT SECOND PARAGRAPH HERE. Example: Photography harnesses light and shadow...]"
               data-cn="[在这里填写第二段中文介绍...]">
               [INSERT SECOND PARAGRAPH HERE. Example: Photography harnesses light and shadow...]
            </p>

            <div class="gear-section">
                <div class="gear-header" data-en="Essential Gear" data-cn="常用器材">Essential Gear</div>
                <div class="gear-row">
                    <span class="gear-label">Camera</span> 
                    <span>Nikon Zf</span>
                </div>
                <div class="gear-row">
                    <span class="gear-label">Lens</span> 
                    <span>Nikkor 50mm f/1.8s</span>
                </div>
            </div>

            <button id="showContact" class="contact-btn" data-en="GET IN TOUCH" data-cn="联系我">GET IN TOUCH</button>
            <a href="/" target="_self" style="display:block; text-align:center; margin-top:20px; color:#000; font-size:12px; font-weight:bold; text-decoration:none;">← BACK TO HOME</a>
        </div>
    </div>

    <div class="modal-overlay" id="contactModal">
        <div class="contact-modal">
            <div class="modal-close-btn" id="closeContact">×</div>
            <div style="font-size:24px; font-weight:900; margin-bottom:30px;">Let's Connect</div>
            <div style="margin-bottom:20px;">
                <div style="font-size:10px; font-weight:700; color:#999; margin-bottom:5px;">EMAIL</div>
                <a href="mailto:maozunjie@gmail.com" style="color:#000; font-size:18px; font-weight:600; text-decoration:none;">maozunjie@gmail.com</a>
            </div>
        </div>
    </div>

    <script>
        // 语言切换逻辑
        const langBtn = document.getElementById('langSwitch');
        const translatableElements = document.querySelectorAll('[data-en]');
        let currentLang = 'en'; 
        langBtn.onclick = () => {
            currentLang = currentLang === 'en' ? 'cn' : 'en';
            translatableElements.forEach(el => {
                if(el.getAttribute(`data-${currentLang}`)) {
                    el.innerHTML = el.getAttribute(`data-${currentLang}`);
                }
            });
            langBtn.textContent = currentLang === 'en' ? 'EN / 中' : '中 / EN';
        };

        // 弹窗逻辑
        const showContactBtn = document.getElementById('showContact');
        const contactModal = document.getElementById('contactModal');
        const closeContactBtn = document.getElementById('closeContact');
        const toggleModal = () => { contactModal.classList.toggle('active'); };
        showContactBtn.onclick = toggleModal;
        closeContactBtn.onclick = toggleModal;
        contactModal.onclick = (e) => { if (e.target === contactModal) toggleModal(); };
    </script>
</body>
</html>
"""

# 渲染 HTML 组件 (高度设为 1200 以适应长内容)
components.html(html_content, height=1200, scrolling=True)
