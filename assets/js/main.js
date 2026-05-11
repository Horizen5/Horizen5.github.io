/**
 * Horizen5 Personal Homepage - Main JavaScript
 * Handles smooth scrolling, skill bar animations, and interactive elements
 */

document.addEventListener('DOMContentLoaded', function() {
    initSmoothScroll();
    initSkillBarAnimations();
    initNavbarScroll();
    initMobileMenu();
});

/**
 * Smooth scrolling for anchor links
 */
function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            const target = document.querySelector(targetId);
            
            if (target) {
                const navHeight = document.querySelector('nav').offsetHeight;
                const targetPosition = target.getBoundingClientRect().top + window.pageYOffset - navHeight;
                
                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });
}

/**
 * Animate skill bars when they enter the viewport
 */
function initSkillBarAnimations() {
    const observerOptions = {
        threshold: 0.3,
        rootMargin: '0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const progressBars = entry.target.querySelectorAll('.skill-progress');
                progressBars.forEach((bar, index) => {
                    const targetWidth = bar.getAttribute('data-width') || bar.style.width;
                    bar.setAttribute('data-width', targetWidth);
                    bar.style.width = '0';
                    
                    // Stagger animations
                    setTimeout(() => {
                        bar.style.width = targetWidth;
                    }, 100 + (index * 100));
                });
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    const skillsSection = document.querySelector('.skills');
    if (skillsSection) {
        observer.observe(skillsSection);
    }
}

/**
 * Navbar background change on scroll
 */
function initNavbarScroll() {
    const nav = document.querySelector('nav');
    
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            nav.style.background = 'rgba(255,255,255,0.15)';
            nav.style.boxShadow = '0 2px 20px rgba(0,0,0,0.1)';
        } else {
            nav.style.background = 'rgba(255,255,255,0.1)';
            nav.style.boxShadow = 'none';
        }
    });
}

/**
 * Mobile menu toggle
 */
function initMobileMenu() {
    // Create mobile menu button if it doesn't exist
    const nav = document.querySelector('nav .container');
    const navLinks = document.querySelector('.nav-links');
    
    if (!document.querySelector('.mobile-menu-btn')) {
        const mobileBtn = document.createElement('button');
        mobileBtn.className = 'mobile-menu-btn';
        mobileBtn.innerHTML = '☰';
        mobileBtn.style.cssText = `
            display: none;
            background: none;
            border: none;
            color: white;
            font-size: 24px;
            cursor: pointer;
        `;
        
        // Add mobile styles
        const style = document.createElement('style');
        style.textContent = `
            @media (max-width: 768px) {
                .mobile-menu-btn {
                    display: block !important;
                }
                .nav-links {
                    position: absolute;
                    top: 100%;
                    left: 0;
                    right: 0;
                    background: rgba(102, 126, 234, 0.95);
                    flex-direction: column;
                    padding: 20px;
                    gap: 15px;
                    transform: translateY(-100%);
                    opacity: 0;
                    visibility: hidden;
                    transition: all 0.3s ease;
                }
                .nav-links.active {
                    transform: translateY(0);
                    opacity: 1;
                    visibility: visible;
                }
            }
        `;
        document.head.appendChild(style);
        
        mobileBtn.addEventListener('click', () => {
            navLinks.classList.toggle('active');
        });
        
        nav.appendChild(mobileBtn);
    }
}

/**
 * Add scroll reveal animation for elements
 */
function initScrollReveal() {
    const revealElements = document.querySelectorAll('.project-card, .skill-item');
    
    const revealObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
                revealObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1 });
    
    revealElements.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(20px)';
        el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        revealObserver.observe(el);
    });
}

// Initialize scroll reveal when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initScrollReveal);
} else {
    initScrollReveal();
}
