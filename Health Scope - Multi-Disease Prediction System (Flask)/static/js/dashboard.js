// Dashboard JavaScript
document.addEventListener('DOMContentLoaded', function() {
    // ===================== Hero Slider Functionality =====================
    const sliderContainer = document.querySelector('.slider-container');
    const slides = document.querySelectorAll('.slide');
    const prevBtn = document.querySelector('.prev-slide');
    const nextBtn = document.querySelector('.next-slide');
    const dotsContainer = document.querySelector('.slider-dots');
    let currentSlide = 0;
    let slideInterval;

    // Create dots for slider navigation
    function createDots() {
        slides.forEach((_, index) => {
            dotsContainer.insertAdjacentHTML(
                'beforeend',
                `<button class="dot ${index === 0 ? 'active' : ''}" data-slide="${index}"></button>`
            );
        });
    }

    // Activate current slide
    function activateSlide(slideIndex) {
        // Remove active class from all slides and dots
        slides.forEach(slide => slide.classList.remove('active'));
        document.querySelectorAll('.dot').forEach(dot => dot.classList.remove('active'));
        
        // Add active class to current slide and dot
        slides[slideIndex].classList.add('active');
        document.querySelector(`.dot[data-slide="${slideIndex}"]`).classList.add('active');
        currentSlide = slideIndex;
    }

    // Next slide function
    function nextSlide() {
        currentSlide = (currentSlide + 1) % slides.length;
        activateSlide(currentSlide);
    }

    // Previous slide function
    function prevSlide() {
        currentSlide = (currentSlide - 1 + slides.length) % slides.length;
        activateSlide(currentSlide);
    }

    // Initialize slider
    function initSlider() {
        createDots();
        
        // Set up automatic sliding
        slideInterval = setInterval(nextSlide, 5000);
        
        // Pause slider on hover
        sliderContainer.addEventListener('mouseenter', () => clearInterval(slideInterval));
        sliderContainer.addEventListener('mouseleave', () => {
            clearInterval(slideInterval);
            slideInterval = setInterval(nextSlide, 5000);
        });
        
        // Button event listeners
        nextBtn.addEventListener('click', nextSlide);
        prevBtn.addEventListener('click', prevSlide);
        
        // Dot navigation
        dotsContainer.addEventListener('click', function(e) {
            if (e.target.classList.contains('dot')) {
                const slideIndex = parseInt(e.target.getAttribute('data-slide'));
                activateSlide(slideIndex);
                clearInterval(slideInterval);
                slideInterval = setInterval(nextSlide, 5000);
            }
        });
    }

    // ===================== Dropdown Menu Functionality =====================
    function setupDropdowns() {
        const dropdowns = document.querySelectorAll('.dropdown, .user-dropdown');
        
        dropdowns.forEach(dropdown => {
            const btn = dropdown.querySelector('.dropbtn, .user-profile');
            const content = dropdown.querySelector('.dropdown-content, .user-menu');
            
            btn.addEventListener('click', function(e) {
                e.stopPropagation();
                
                // Close all other dropdowns
                document.querySelectorAll('.dropdown-content, .user-menu').forEach(item => {
                    if (item !== content) {
                        item.style.display = 'none';
                    }
                });
                
                // Toggle current dropdown
                if (content.style.display === 'block') {
                    content.style.display = 'none';
                } else {
                    content.style.display = 'block';
                }
            });
        });
        
        // Close dropdowns when clicking outside
        document.addEventListener('click', function() {
            document.querySelectorAll('.dropdown-content, .user-menu').forEach(content => {
                content.style.display = 'none';
            });
        });
    }

    // ===================== Disease Info Tabs =====================
    function setupDiseaseTabs() {
        const tabBtns = document.querySelectorAll('.tab-btn');
        const tabContents = document.querySelectorAll('.tab-content');
        
        tabBtns.forEach(btn => {
            btn.addEventListener('click', function() {
                const tabId = this.getAttribute('data-tab');
                
                // Remove active class from all buttons and contents
                tabBtns.forEach(btn => btn.classList.remove('active'));
                tabContents.forEach(content => content.classList.remove('active'));
                
                // Add active class to clicked button and corresponding content
                this.classList.add('active');
                document.getElementById(`${tabId}-tab`).classList.add('active');
            });
        });
    }

    // ===================== Mobile Menu Toggle =====================
    function setupMobileMenu() {
        const hamburger = document.querySelector('.hamburger');
        const navLinks = document.querySelector('.nav-links');
        
        hamburger.addEventListener('click', function() {
            this.classList.toggle('active');
            navLinks.classList.toggle('active');
        });
    }

    // ===================== Theme Toggle =====================
    function setupThemeToggle() {
        const themeToggle = document.getElementById('themeToggle');
        const themeIcon = themeToggle.querySelector('i');
        const themeText = themeToggle.querySelector('span');
        
        // Check for saved theme preference or use preferred color scheme
        const savedTheme = localStorage.getItem('theme') || 
                          (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
        document.documentElement.setAttribute('data-theme', savedTheme);
        
        // Update toggle button based on current theme
        if (savedTheme === 'dark') {
            themeIcon.classList.replace('fa-moon', 'fa-sun');
            themeText.textContent = 'Light';
        }
        
        themeToggle.addEventListener('click', function() {
            const currentTheme = document.documentElement.getAttribute('data-theme');
            const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
            
            // Update theme
            document.documentElement.setAttribute('data-theme', newTheme);
            localStorage.setItem('theme', newTheme);
            
            // Update toggle button
            if (newTheme === 'dark') {
                themeIcon.classList.replace('fa-moon', 'fa-sun');
                themeText.textContent = 'Light';
            } else {
                themeIcon.classList.replace('fa-sun', 'fa-moon');
                themeText.textContent = 'Dark';
            }
        });
    }

    // ===================== Smooth Scrolling =====================
    function setupSmoothScrolling() {
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function(e) {
                e.preventDefault();
                
                const targetId = this.getAttribute('href');
                if (targetId === '#') return;
                
                const targetElement = document.querySelector(targetId);
                if (targetElement) {
                    window.scrollTo({
                        top: targetElement.offsetTop - 80, // Adjust for fixed header
                        behavior: 'smooth'
                    });
                    
                    // Close mobile menu if open
                    const hamburger = document.querySelector('.hamburger');
                    if (hamburger.classList.contains('active')) {
                        hamburger.classList.remove('active');
                        document.querySelector('.nav-links').classList.remove('active');
                    }
                }
            });
        });
    }

    // ===================== Initialize All Functions =====================
    initSlider();
    setupDropdowns();
    setupDiseaseTabs();
    setupMobileMenu();
    setupThemeToggle();
    setupSmoothScrolling();

    // ===================== Health Tips Carousel =====================
    const tipsCarousel = document.querySelector('.tips-carousel');
    if (tipsCarousel) {
        let isDragging = false;
        let startX, scrollLeft;
        
        // Mouse drag functionality
        tipsCarousel.addEventListener('mousedown', (e) => {
            isDragging = true;
            tipsCarousel.style.cursor = 'grabbing';
            startX = e.pageX - tipsCarousel.offsetLeft;
            scrollLeft = tipsCarousel.scrollLeft;
        });
        
        tipsCarousel.addEventListener('mousemove', (e) => {
            if (!isDragging) return;
            e.preventDefault();
            const x = e.pageX - tipsCarousel.offsetLeft;
            const walk = (x - startX) * 2;
            tipsCarousel.scrollLeft = scrollLeft - walk;
        });
        
        tipsCarousel.addEventListener('mouseup', () => {
            isDragging = false;
            tipsCarousel.style.cursor = 'grab';
        });
        
        tipsCarousel.addEventListener('mouseleave', () => {
            isDragging = false;
            tipsCarousel.style.cursor = 'grab';
        });
        
        // Touch support for mobile
        tipsCarousel.addEventListener('touchstart', (e) => {
            isDragging = true;
            startX = e.touches[0].pageX - tipsCarousel.offsetLeft;
            scrollLeft = tipsCarousel.scrollLeft;
        });
        
        tipsCarousel.addEventListener('touchmove', (e) => {
            if (!isDragging) return;
            const x = e.touches[0].pageX - tipsCarousel.offsetLeft;
            const walk = (x - startX) * 2;
            tipsCarousel.scrollLeft = scrollLeft - walk;
        });
        
        tipsCarousel.addEventListener('touchend', () => {
            isDragging = false;
        });
    }
});

