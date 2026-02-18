const API_URL = 'http://127.0.0.1:5000/api/v1';

document.addEventListener('DOMContentLoaded', () => {
    const token = getCookie('token');
    const loginLink = document.getElementById('login-link');

    // 1. إدارة حالة تسجيل الدخول
    if (token) {
        if (loginLink) {
            loginLink.innerHTML = '<a href="#" onclick="logout()" class="login-btn">Logout</a>';
        }
        // إظهار فورم المراجعة إذا كنا في صفحة التفاصيل
        const reviewForm = document.getElementById('add-review');
        if (reviewForm) reviewForm.style.display = 'block';
    } else {
        // حماية الصفحات
        if (window.location.pathname.includes('add_review.html')) {
            window.location.href = 'index.html';
        }
    }

    // 2. توجيه الكود حسب الصفحة الحالية
    const path = window.location.pathname;
    if (path.includes('place.html')) {
        fetchPlaceDetails();
    } else if (path.includes('login.html')) {
        initLoginForm();
    } else {
        // الافتراضي هو الصفحة الرئيسية
        if (document.getElementById('places-list')) fetchPlaces();
    }
});

async function fetchPlaces() {
    try {
        const response = await fetch(`${API_URL}/places`);
        const places = await response.json();
        const container = document.getElementById('places-list');
        container.innerHTML = '';
        places.forEach(place => {
            const card = document.createElement('div');
            card.className = 'place-card';
            card.innerHTML = `
                <div class="card-header">
                    <span class="price">$${place.price}</span>
                    <h3>${place.title}</h3>
                </div>
                <div class="card-body">
                    <button class="details-btn" onclick="window.location.href='place.html?id=${place.id}'">View Details</button>
                </div>
            `;
            container.appendChild(card);
        });
    } catch (error) {
        console.error('Error:', error);
    }
}

async function fetchPlaceDetails() {
    const urlParams = new URLSearchParams(window.location.search);
    const placeId = urlParams.get('id');
    if (!placeId) return window.location.href = 'index.html';

    try {
        const response = await fetch(`${API_URL}/places/${placeId}`);
        if (!response.ok) throw new Error('Place not found');
        const place = await response.json();

        document.getElementById('place-title').textContent = place.title;
        document.getElementById('place-price').textContent = `$${place.price} / night`;
        document.getElementById('place-description').textContent = place.description;
        document.getElementById('place-owner').textContent = place.owner_id; // أو place.owner.first_name لو الـ API يدعم
        document.getElementById('place-location').textContent = `City ID: ${place.city_id}`;
        
    } catch (error) {
        document.querySelector('.details-container').innerHTML = '<h2>Error loading place details</h2>';
    }
}

function initLoginForm() {
    const form = document.getElementById('login-form');
    if (!form) return;
    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        const email = document.getElementById('email').value;
        const password = document.getElementById('password').value;
        try {
            const response = await fetch(`${API_URL}/auth/login`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ email, password })
            });
            if (response.ok) {
                const data = await response.json();
                document.cookie = `token=${data.access_token}; path=/`;
                window.location.href = 'index.html';
            } else {
                const err = document.getElementById('error-message');
                err.textContent = 'Login failed: Invalid credentials';
                err.style.display = 'block';
            }
        } catch (error) {
            console.error(error);
        }
    });
}

function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}

function logout() {
    document.cookie = "token=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
    window.location.reload();
}
