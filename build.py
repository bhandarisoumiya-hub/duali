import os

html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Duali Tableware Showcase — {title}</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400&family=Montserrat:wght@300;400;500&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="{css_file}">
</head>
<body>
    <div id="stage">
        <!-- Seal View -->
        <div id="seal-view">
            <div class="seal" id="seal">
                <img src="image.png" alt="Logo" class="seal-logo">
            </div>
            <p class="hint">tap to open</p>
        </div>

        <!-- Invite View -->
        <div id="invite-view">
            <div class="invite-card">
                
                <img src="image.png" alt="Logo" class="card-logo animate-up" style="--delay: 0.1s">
                
                <p class="eyebrow animate-up" style="--delay: 0.2s">You are cordially invited to the</p>
                <h1 class="animate-up" style="--delay: 0.3s">Duali Tableware Showcase</h1>
                <p class="lede animate-up" style="--delay: 0.4s">Join us as we present our complete collection of<br>handcrafted functional art and tableware created to date.</p>
                
                <div class="divider animate-up" style="--delay: 0.5s"></div>
                
                <div class="scratch-wrap animate-up" id="scratch-wrap" style="--delay: 0.6s">
                    <div class="scratch-content">
                        <div class="dates">
                            <div class="date-block">
                                <span class="day">Saturday</span>
                                <span class="num">18</span>
                                <span class="month">September</span>
                            </div>
                            <span class="amp">&amp;</span>
                            <div class="date-block">
                                <span class="day">Sunday</span>
                                <span class="num">19</span>
                                <span class="month">September 2026</span>
                            </div>
                        </div>
                        <p class="time">11:00 AM – 6:00 PM</p>
                        <p class="walkin">Walk-ins welcome throughout the day</p>
                        <p class="venue">079 Stories, Bodakdev,<br>Ahmedabad</p>
                    </div>
                    <!-- The Canvas layer that gets scratched off -->
                    <canvas id="scratch-canvas"></canvas>
                </div>

                <p class="closing animate-up" style="--delay: 0.7s">We look forward to welcoming you.</p>
                
                <div class="animate-up" style="--delay: 0.8s">
                    <a href="https://instagram.com/dualidesigns" target="_blank" class="rsvp-btn">RSVP NOW</a>
                </div>

            </div>
        </div>
    </div>

    <script src="{js_file}"></script>
</body>
</html>"""

css_template = """{root_vars}

body {
    background: var(--bg);
    color: var(--ink);
    font-family: 'Montserrat', sans-serif;
    margin: 0;
    overflow-x: hidden;
    -webkit-font-smoothing: antialiased;
}

.hidden {
    display: none !important;
}

#stage {
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    background: var(--bg);
    position: relative;
}

#seal-view {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 30px;
    transition: opacity 0.5s ease, transform 0.5s ease;
    position: absolute;
    inset: 0;
    margin: auto;
}

.seal {
    width: 140px;
    height: 140px;
    border-radius: 50%;
    cursor: pointer;
    background: var(--primary-gradient);
    box-shadow: 
        0 15px 35px rgba(0,0,0,0.15),
        inset 0 2px 5px rgba(255,255,255,0.2),
        inset 0 -4px 10px rgba(0,0,0,0.4);
    display: flex;
    align-items: center;
    justify-content: center;
    animation: breathe 4s ease-in-out infinite;
    position: relative;
}

.seal::after {
    content: '';
    position: absolute;
    inset: 6px;
    border-radius: 50%;
    border: 1px dashed rgba(255,255,255,0.3);
}

.seal-logo {
    width: 70%;
    height: 70%;
    object-fit: contain;
    transition: transform 0.3s ease;
    filter: drop-shadow(0 2px 3px rgba(0,0,0,0.3));
    z-index: 2;
}

.seal:hover .seal-logo {
    transform: scale(1.05);
}

@keyframes breathe {
    0%, 100% { transform: scale(1); }
    50% { transform: scale(1.03); }
}

.hint {
    font-size: 11.5px;
    letter-spacing: 4px;
    color: var(--ink-soft);
    text-transform: uppercase;
    margin: 0;
    animation: pulse 2s infinite;
}

@keyframes pulse {
    0%, 100% { opacity: 0.5; }
    50% { opacity: 1; }
}

.seal.opening {
    animation: none;
    transform: scale(0.4) translateY(-60px) rotate(15deg);
    opacity: 0;
    transition: transform 0.6s cubic-bezier(0.6,-0.1,0.3,1.3), opacity 0.4s ease 0.2s;
    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
}

#invite-view {
    width: 100%;
    display: none; 
    justify-content: center;
    opacity: 0;
    padding: 40px 20px; 
    box-sizing: border-box;
    transition: opacity 0.8s ease;
    min-height: 100vh;
}

#invite-view.show {
    opacity: 1;
}

.invite-card {
    background: var(--card-bg);
    width: 100%;
    max-width: 600px;
    padding: 50px 40px;
    box-shadow: 0 25px 60px rgba(0,0,0,0.06), 0 0 0 1px rgba(0,0,0,0.02);
    border-radius: 16px;
    text-align: center;
    position: relative;
    margin: auto; 
}

.animate-up {
    opacity: 0;
    transform: translateY(25px);
    transition: opacity 0.8s ease var(--delay), transform 0.8s cubic-bezier(0.2, 0.8, 0.2, 1) var(--delay);
}

#invite-view.show .animate-up {
    opacity: 1;
    transform: translateY(0);
}

.card-logo {
    width: 80px;
    height: 80px;
    object-fit: contain;
    margin-bottom: 25px;
}

.eyebrow {
    font-size: 11px;
    letter-spacing: 2px;
    color: var(--primary-dark);
    text-transform: uppercase;
    margin: 0 0 16px;
    line-height: 1.5;
}

.invite-card h1 {
    font-family: 'Cormorant Garamond', serif;
    font-size: 46px;
    font-weight: 500;
    margin: 0 0 20px;
    color: var(--ink);
    letter-spacing: 1px;
}

.lede {
    font-size: 14.5px;
    line-height: 1.7;
    color: var(--ink-soft);
    margin: 0 auto 35px;
    font-weight: 300;
}

.divider {
    width: 50px;
    height: 1px;
    background-color: var(--primary);
    opacity: 0.5;
    margin: 0 auto 45px;
}

.scratch-wrap {
    position: relative;
    background: #faf9f6;
    margin-bottom: 45px;
    min-height: 250px;
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: inset 0 2px 10px rgba(0,0,0,0.04);
    border: 1px solid rgba(0,0,0,0.05);
    overflow: hidden;
}

.scratch-content {
    padding: 40px 20px;
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%;
}

.dates {
    display: flex;
    align-items: baseline;
    justify-content: center;
    gap: 16px;
    margin-bottom: 15px;
}

.date-block {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 4px;
}

.date-block .day { 
    font-size: 11px; 
    letter-spacing: 2.5px; 
    text-transform: uppercase; 
    color: var(--primary-dark); 
}

.date-block .num { 
    font-family: 'Cormorant Garamond', serif; 
    font-size: 48px; 
    color: var(--ink); 
    line-height: 1; 
}

.date-block .month { 
    font-size: 12.5px; 
    letter-spacing: 1px; 
    color: var(--ink-soft); 
}

.amp {
    font-family: 'Cormorant Garamond', serif;
    font-style: italic;
    font-size: 24px;
    color: var(--ink-soft);
    transform: translateY(-8px);
}

.time { 
    margin: 5px 0; 
    font-size: 15px; 
    color: var(--ink); 
    font-weight: 400;
}

.walkin {
    font-size: 13.5px;
    color: var(--ink-soft);
    margin: 2px 0 16px;
    font-style: italic;
    font-family: 'Cormorant Garamond', serif;
}

.venue { 
    font-size: 14px; 
    color: var(--ink); 
    margin: 10px 0 0;
    padding-top: 15px;
    border-top: 1px solid var(--line);
    width: 100%;
    max-width: 250px;
    letter-spacing: 0.5px;
    line-height: 1.4;
}

#scratch-canvas {
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    cursor: crosshair;
    touch-action: none;
}

.closing {
    font-family: 'Cormorant Garamond', serif;
    font-style: italic;
    font-size: 21px;
    color: var(--ink);
    margin: 0 0 35px;
}

.rsvp-btn {
    display: inline-block;
    padding: 16px 50px;
    background: var(--primary-gradient);
    color: #ffffff;
    text-decoration: none;
    font-size: 13px;
    letter-spacing: 4px;
    text-transform: uppercase;
    border-radius: 40px;
    transition: all 0.3s ease;
    box-shadow: 0 10px 20px rgba(0,0,0,0.15);
    border: 1px solid rgba(255,255,255,0.4);
}

.rsvp-btn:hover {
    transform: translateY(-3px);
    box-shadow: 0 15px 30px rgba(0,0,0,0.25);
    filter: brightness(1.1);
}

@media (max-width: 500px) {
    .invite-card {
        padding: 40px 20px;
    }
    .invite-card h1 {
        font-size: 34px;
    }
    .dates {
        flex-direction: column;
        align-items: center;
        gap: 15px;
    }
    .amp { display: none; }
}
"""

js_template = """document.addEventListener('DOMContentLoaded', () => {
    const seal = document.getElementById('seal');
    const sealView = document.getElementById('seal-view');
    const inviteView = document.getElementById('invite-view');

    seal.addEventListener('click', () => {
        if (seal.classList.contains('opening')) return;
        seal.classList.add('opening');
        
        setTimeout(() => {
            sealView.style.display = 'none'; 
            inviteView.style.display = 'flex';
            
            requestAnimationFrame(() => {
                inviteView.classList.add('show');
                initScratch();
            });
        }, 450); 
    });

    let scratchInitialized = false;

    function initScratch() {
        if (scratchInitialized) return;
        scratchInitialized = true;

        const wrap = document.getElementById('scratch-wrap');
        const canvas = document.getElementById('scratch-canvas');
        const ctx = canvas.getContext('2d', { willReadFrequently: true });

        function sizeCanvas() {
            const rect = wrap.getBoundingClientRect();
            canvas.width = rect.width;
            canvas.height = rect.height;
            drawScratchLayer();
        }

        function drawScratchLayer() {
            const w = canvas.width, h = canvas.height;
            
{scratch_fill}

            // Shimmer/Noise for realistic foil
            for(let i=0; i<1500; i++){
                ctx.fillStyle = `rgba(255,255,255,${Math.random()*0.06})`;
                ctx.fillRect(Math.random()*w, Math.random()*h, 1.5, 1.5);
            }
            
            // Add text to the scratch foil
            ctx.fillStyle = '#ffffff';
            ctx.font = '500 13.5px Montserrat, sans-serif';
            ctx.textAlign = 'center';
            ctx.letterSpacing = '6px';
            ctx.shadowColor = 'rgba(0,0,0,0.2)';
            ctx.shadowBlur = 5;
            ctx.fillText('SCRATCH TO REVEAL', w / 2, h / 2 - 12);
            
            ctx.font = 'italic 17px "Cormorant Garamond", serif';
            ctx.letterSpacing = '1px';
            ctx.fillText('the date & time', w / 2, h / 2 + 18);
            ctx.shadowColor = 'transparent';
        }

        sizeCanvas();
        window.addEventListener('resize', sizeCanvas);
        
        let isDown = false;
        let cleared = false;

        function pos(e) {
            const rect = canvas.getBoundingClientRect();
            const clientX = e.touches ? e.touches[0].clientX : e.clientX;
            const clientY = e.touches ? e.touches[0].clientY : e.clientY;
            return { x: clientX - rect.left, y: clientY - rect.top };
        }

        function scratchAt(x, y) {
            ctx.globalCompositeOperation = 'destination-out';
            ctx.beginPath();
            ctx.arc(x, y, 32, 0, Math.PI * 2);
            ctx.fill();
        }

        function checkClearedAmount() {
            if (cleared) return;
            const w = canvas.width, h = canvas.height;
            const sampleStep = 8;
            let transparent = 0, total = 0;
            const data = ctx.getImageData(0, 0, w, h).data;
            for (let y = 0; y < h; y += sampleStep) {
                for (let x = 0; x < w; x += sampleStep) {
                    const idx = (y * w + x) * 4 + 3;
                    total++;
                    if (data[idx] < 40) transparent++;
                }
            }
            if (total > 0 && transparent / total > 0.45) {
                cleared = true;
                canvas.style.transition = 'opacity 0.8s ease';
                canvas.style.opacity = '0';
                setTimeout(() => canvas.style.display = 'none', 800);
            }
        }

        function start(e) {
            isDown = true;
            const p = pos(e);
            scratchAt(p.x, p.y);
            if (e.cancelable) e.preventDefault();
        }
        
        function move(e) {
            if (!isDown || cleared) return;
            const p = pos(e);
            scratchAt(p.x, p.y);
            if (e.cancelable) e.preventDefault();
        }
        
        function end() {
            if (isDown) checkClearedAmount();
            isDown = false;
        }

        canvas.addEventListener('mousedown', start);
        canvas.addEventListener('mousemove', move);
        window.addEventListener('mouseup', end);

        canvas.addEventListener('touchstart', start, { passive: false });
        canvas.addEventListener('touchmove', move, { passive: false });
        window.addEventListener('touchend', end);
    }
});
"""

index_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Duali Tableware Showcase — Theme Selector</title>
    <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400&family=Montserrat:wght@300;400;500&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Montserrat', sans-serif; background: #fdfcf9; display: flex; align-items: center; justify-content: center; height: 100vh; margin: 0; text-align: center; color: #1a1a1a; }
        .container { display: flex; gap: 30px; flex-wrap: wrap; justify-content: center; }
        a { display: block; padding: 20px 40px; border-radius: 8px; text-decoration: none; font-size: 15px; font-weight: 500; text-transform: uppercase; letter-spacing: 3px; transition: transform 0.2s, box-shadow 0.2s; }
        a:hover { transform: translateY(-3px); box-shadow: 0 10px 20px rgba(0,0,0,0.1); }
        .golden { background: linear-gradient(135deg, #d4af37 0%, #b8943e 100%); color: white; border: 1px solid rgba(255,255,255,0.4); }
        .green { background: linear-gradient(135deg, #324f3e 0%, #19291f 100%); color: white; border: 1px solid rgba(255,255,255,0.4); }
        h1 { margin-bottom: 40px; font-family: 'Cormorant Garamond', serif; font-size: 40px; }
    </style>
</head>
<body>
    <div>
        <h1>Select your theme</h1>
        <div class="container">
            <a href="golden.html" class="golden">Golden Theme</a>
            <a href="green.html" class="green">Green Theme</a>
        </div>
    </div>
</body>
</html>"""

# Write Golden Files
with open('golden.html', 'w') as f:
    f.write(html_template.replace('{title}', 'Golden Edition').replace('{css_file}', 'styles-golden.css').replace('{js_file}', 'script-golden.js'))

golden_root = """:root {
    --bg: #fdfbf7;
    --ink: #1f1d1b;
    --ink-soft: #63615e;
    --primary: #d4af37;
    --primary-dark: #b39126;
    --primary-gradient: linear-gradient(135deg, #e5cf8c 0%, #b8943e 100%);
    --card-bg: #ffffff;
    --line: #e6e2d8;
}"""
with open('styles-golden.css', 'w') as f:
    f.write(css_template.replace('{root_vars}', golden_root))

golden_js_fill = """            const grad = ctx.createLinearGradient(0, 0, w, h);
            grad.addColorStop(0, '#e8d5a5');
            grad.addColorStop(0.3, '#d4af37');
            grad.addColorStop(0.7, '#c59b43');
            grad.addColorStop(1, '#9e7323');
            ctx.globalCompositeOperation = 'source-over';
            ctx.fillStyle = grad;
            ctx.fillRect(0, 0, w, h);"""
with open('script-golden.js', 'w') as f:
    f.write(js_template.replace('{scratch_fill}', golden_js_fill))

# Write Green Files
with open('green.html', 'w') as f:
    f.write(html_template.replace('{title}', 'Green Edition').replace('{css_file}', 'styles-green.css').replace('{js_file}', 'script-green.js'))

green_root = """:root {
    --bg: #ffffff;
    --ink: #1f1d1b;
    --ink-soft: #63615e;
    --primary: #263c2f;
    --primary-dark: #19291f;
    --primary-gradient: linear-gradient(135deg, #324f3e 0%, #19291f 100%);
    --card-bg: #ffffff;
    --line: #e6e2d8;
}"""
with open('styles-green.css', 'w') as f:
    f.write(css_template.replace('{root_vars}', green_root))

green_js_fill = """            ctx.globalCompositeOperation = 'source-over';
            ctx.fillStyle = '#263c2f';
            ctx.fillRect(0, 0, w, h);"""
with open('script-green.js', 'w') as f:
    f.write(js_template.replace('{scratch_fill}', green_js_fill))

# Write Index File
with open('index.html', 'w') as f:
    f.write(index_html)
