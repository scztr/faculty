document.querySelectorAll('[data-slider]').forEach((slider) => {
    const slides = [...slider.querySelectorAll('[data-slide]')];
    const dots = [...slider.querySelectorAll('[data-dot]')];
    const pauseButton = slider.querySelector('[data-pause]');
    const motion = window.matchMedia('(prefers-reduced-motion: reduce)');
    let current = 0;
    let paused = motion.matches;
    let hovered = false;
    let focused = false;

    function show(index) {
        current = (index + slides.length) % slides.length;
        slides.forEach((slide, i) => {
            slide.classList.toggle('is-active', i === current);
            slide.setAttribute('aria-hidden', String(i !== current));
            dots[i].setAttribute('aria-pressed', String(i === current));
        });
    }

    function setPaused(value) {
        paused = value;
        pauseButton.textContent = paused ? '▶' : 'Ⅱ';
        pauseButton.setAttribute('aria-pressed', String(paused));
        pauseButton.setAttribute('aria-label', paused
            ? 'Увімкнути автоматичну зміну' : 'Призупинити автоматичну зміну');
    }

    function select(index) {
        show(index);
        setPaused(true);
    }

    slider.querySelector('[data-controls]').hidden = false;
    slider.querySelector('[data-prev]').addEventListener('click', () => select(current - 1));
    slider.querySelector('[data-next]').addEventListener('click', () => select(current + 1));
    dots.forEach((dot, i) => dot.addEventListener('click', () => select(i)));
    pauseButton.addEventListener('click', () => setPaused(!paused));
    slider.addEventListener('mouseenter', () => { hovered = true; });
    slider.addEventListener('mouseleave', () => { hovered = false; });
    slider.addEventListener('focusin', () => { focused = true; });
    slider.addEventListener('focusout', (event) => {
        focused = slider.contains(event.relatedTarget);
    });
    motion.addEventListener('change', (event) => {
        if (event.matches) setPaused(true);
    });
    setPaused(paused);
    window.setInterval(() => {
        if (!paused && !hovered && !focused && !document.hidden) show(current + 1);
    }, 6000);
});
