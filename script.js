document.addEventListener('DOMContentLoaded', () => {
    // 1. Seal Animation & Transition
    const seal = document.getElementById('seal');
    const sealView = document.getElementById('seal-view');
    const inviteView = document.getElementById('invite-view');

    seal.addEventListener('click', () => {
        if (seal.classList.contains('opening')) return;
        seal.classList.add('opening');
        
        setTimeout(() => {
            sealView.style.display = 'none'; 
            
            // Set to flex so it's part of document flow, allowing scroll if it overflows
            inviteView.style.display = 'flex';
            
            // Allow a tiny reflow frame before adding 'show' so animations trigger
            requestAnimationFrame(() => {
                inviteView.classList.add('show');
                initScratch();
            });
        }, 450); 
    });

    // 2. Scratch Canvas Logic
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
            
            // Gorgeous Gold Foil Gradient
            const grad = ctx.createLinearGradient(0, 0, w, h);
            grad.addColorStop(0, '#e8d5a5');
            grad.addColorStop(0.3, '#d4af37');
            grad.addColorStop(0.7, '#c59b43');
            grad.addColorStop(1, '#9e7323');
            
            ctx.globalCompositeOperation = 'source-over';
            ctx.fillStyle = grad;
            ctx.fillRect(0, 0, w, h);

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
            if (total > 0 && transparent / total > 0.45) { // Clear at 45%
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
