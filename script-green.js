document.addEventListener('DOMContentLoaded', () => {
    // 1. Seal Animation & Transition
    const flapTop = document.getElementById('flap-top');
    const envelope = document.getElementById('envelope');
    const envelopeView = document.getElementById('envelope-view');
    const inviteView = document.getElementById('invite-view');
    const hint = document.getElementById('hint');
    const ambientContainer = document.querySelector('.ambient-dust');

    flapTop.addEventListener('click', () => {
        if (envelope.classList.contains('open')) return;
        envelope.classList.add('open');
        if (hint) hint.style.opacity = '0';
        
        // After flap opens, transition out the envelope and show the card
        setTimeout(() => {
            envelopeView.style.transform = 'translateY(100px)';
            envelopeView.style.opacity = '0';
            if (ambientContainer) ambientContainer.style.opacity = '0';
            
            setTimeout(() => {
                envelopeView.style.display = 'none';
                inviteView.style.display = 'flex';
                requestAnimationFrame(() => {
                    inviteView.classList.add('show');
                    initScratch();
                    startCelebration();
                });
            }, 1200);
        }, 800); // Time for the flap to open
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
            
            // Ultra-premium Emerald Green Foil Gradient
            const grad = ctx.createLinearGradient(0, 0, w, h);
            grad.addColorStop(0, '#a8bb5f');
            grad.addColorStop(0.3, '#8a9848');
            grad.addColorStop(0.7, '#6b7a33');
            grad.addColorStop(1, '#586626');
            
            ctx.globalCompositeOperation = 'source-over';
            ctx.fillStyle = grad;
            ctx.fillRect(0, 0, w, h);

            // High density Shimmer/Noise for realistic foil
            for(let i=0; i<2500; i++){
                ctx.fillStyle = `rgba(255,255,255,${Math.random()*0.08})`;
                ctx.fillRect(Math.random()*w, Math.random()*h, 1, 1);
            }
            // Add some dark speckles for depth
            for(let i=0; i<500; i++){
                ctx.fillStyle = `rgba(0,0,0,${Math.random()*0.1})`;
                ctx.fillRect(Math.random()*w, Math.random()*h, 1.5, 1.5);
            }
            
            // Text on scratch foil
            ctx.fillStyle = '#ffffff';
            ctx.font = '500 13px Montserrat, sans-serif';
            ctx.textAlign = 'center';
            ctx.letterSpacing = '6px';
            ctx.shadowColor = 'rgba(0,0,0,0.4)';
            ctx.shadowBlur = 8;
            ctx.fillText('SCRATCH TO REVEAL', w / 2, h / 2 - 12);
            
            ctx.font = 'italic 18px "Playfair Display", serif';
            ctx.letterSpacing = '1px';
            ctx.fillText('the date & time', w / 2, h / 2 + 20);
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
            ctx.arc(x, y, 35, 0, Math.PI * 2);
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
                canvas.style.transition = 'opacity 1s ease';
                canvas.style.opacity = '0';
                setTimeout(() => canvas.style.display = 'none', 1000);
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

    // 3. Countdown Logic
    function initCountdown() {
        const targetDate = new Date('September 18, 2026 11:00:00').getTime();
        
        const daysEl = document.getElementById('cd-days');
        const hoursEl = document.getElementById('cd-hours');
        const minsEl = document.getElementById('cd-mins');
        const secsEl = document.getElementById('cd-secs');
        const titleEl = document.querySelector('.countdown-title');
        const wrapperEl = document.getElementById('countdown');

        function updateCountdown() {
            const now = new Date().getTime();
            const distance = targetDate - now;

            if (distance < 0) {
                if (titleEl) titleEl.innerText = "The showcase has begun!";
                if (wrapperEl) wrapperEl.style.display = "none";
                return;
            }

            const days = Math.floor(distance / (1000 * 60 * 60 * 24));
            const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
            const seconds = Math.floor((distance % (1000 * 60)) / 1000);

            if (daysEl) daysEl.innerText = days.toString().padStart(2, '0');
            if (hoursEl) hoursEl.innerText = hours.toString().padStart(2, '0');
            if (minsEl) minsEl.innerText = minutes.toString().padStart(2, '0');
            if (secsEl) secsEl.innerText = seconds.toString().padStart(2, '0');
        }

        updateCountdown();
        setInterval(updateCountdown, 1000);
    }

    // Initialize countdown right away
    initCountdown();
});



    // Celebration Confetti
    function startCelebration() {
        const container = document.getElementById('celebration-container');
        if (!container) return;
        
        const colors = ['#8a9848', '#a8bb5f', '#6b7a33', '#ebd188']; // green and subtle gold
        
        for (let i = 0; i < 40; i++) {
            setTimeout(() => {
                const conf = document.createElement('div');
                conf.classList.add('confetti');
                conf.style.left = Math.random() * 100 + 'vw';
                conf.style.background = colors[Math.floor(Math.random() * colors.length)];
                
                // Randomize leaf shape slightly
                if (Math.random() > 0.5) {
                    conf.style.borderRadius = '0 50% 0 50%';
                }
                
                const duration = Math.random() * 3 + 3; // 3 to 6 seconds
                conf.style.animationDuration = duration + 's';
                
                // Random horizontal drift using a custom keyframe wouldn't be dynamic easily, 
                // so we just rely on rotation to make it look nice. 
                // Add scale variation
                conf.style.transform = 'scale(' + (Math.random() * 0.8 + 0.5) + ')';
                
                container.appendChild(conf);
                
                setTimeout(() => {
                    conf.remove();
                }, duration * 1000);
            }, Math.random() * 2000);
        }
    }



