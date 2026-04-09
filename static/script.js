document.addEventListener('mousemove', (e) => {
    const cards = document.querySelectorAll('.card, .hero');
    const x = e.clientX;
    const y = e.clientY;

    cards.forEach(card => {
        const rect = card.getBoundingClientRect();
        const cardX = rect.left + rect.width / 2;
        const cardY = rect.top + rect.height / 2;

        const angleX = (cardY - y) / 30;
        const angleY = (x - cardX) / 30;

        // Apply 3D rotation only on hover (optional, or constant subtle move)
        if (card.matches(':hover')) {
            card.style.transform = `translateY(-10px) rotateX(${angleX}deg) rotateY(${angleY}deg)`;
        } else {
            // Subtle parallax for non-hovered hero
            if (card.classList.contains('hero')) {
                 card.style.transform = `rotateX(${angleX/5}deg) rotateY(${angleY/5}deg)`;
            } else {
                 card.style.transform = `translateY(0) rotateX(0deg) rotateY(0deg)`;
            }
        }
    });
});

// Smooth transition reset
document.addEventListener('mouseout', () => {
    const cards = document.querySelectorAll('.card, .hero');
    cards.forEach(card => {
        card.style.transform = `translateY(0) rotateX(0deg) rotateY(0deg)`;
    });
});