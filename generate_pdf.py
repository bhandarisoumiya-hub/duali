from playwright.sync_api import sync_playwright
import os

def generate():
    html_path = f"file:///{os.path.abspath('duali-invitation.html').replace(chr(92), '/')}"
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(html_path)
        
        page.evaluate('''() => {
            document.getElementById('envelope-view').style.display = 'none';
            document.getElementById('invite-view').style.display = 'flex';
            document.getElementById('invite-view').style.opacity = '1';
            document.getElementById('invite-view').classList.add('show');
            
            // Disable animations and set opacity to 1 immediately
            const animatedElems = document.querySelectorAll('.animate-down');
            animatedElems.forEach(el => {
                el.style.opacity = '1';
                el.style.transform = 'none';
                el.style.animation = 'none';
                el.style.transition = 'none';
            });
            
            // Scratch off canvas
            const scratchWrap = document.getElementById('scratch-wrap');
            if (scratchWrap) {
                const canvas = document.getElementById('scratch-canvas');
                if (canvas) {
                    canvas.style.display = 'none';
                }
            }
            
            // Hide unwanted elements for the invitation print
            const btn = document.getElementById('rsvp-now-btn');
            if (btn) btn.style.display = 'none';
            
            const countdown = document.querySelector('.countdown-wrapper');
            if (countdown) countdown.style.display = 'none';
            
            // Fix dimensions for print
            const card = document.querySelector('.invite-card');
            if (card) {
                card.style.margin = '0 auto';
                card.style.boxShadow = 'none';
            }
            
            const dust = document.querySelector('.ambient-dust');
            if (dust) dust.style.display = 'none';
            
            document.body.style.background = '#ffffff';
            document.getElementById('stage').style.background = '#ffffff';
        }''')
        
        # Wait a bit for images/fonts
        page.wait_for_timeout(2000)
        
        page.screenshot(path="screenshot.png")

        height = page.evaluate('() => { const card = document.querySelector(".invite-card"); return card ? card.getBoundingClientRect().height : 800; }')
        
        page.pdf(
            path="Duali_Invitation.pdf",
            print_background=True,
            width="420px",
            height=f"{int(height) + 80}px"
        )
        print("PDF and Screenshot Generated")
        browser.close()

if __name__ == '__main__':
    generate()
