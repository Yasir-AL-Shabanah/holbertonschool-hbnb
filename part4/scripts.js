const API_URL = 'http://127.0.0.1:5000/api/v1';

document.addEventListener('DOMContentLoaded', () => {
    // 1. Check Login State
    const token = getCookie('token');
    const loginLink = document.getElementById('login-link');
    
    if (token && loginLink) {
        loginLink.style.display = 'none'; // Hide login button if logged in
    }

    // 2. Load Places (Index Page)
    if (document.getElementById('places-list')) {
        fetchPlaces();
    }

    // 3. Handle Login
    const loginForm = document.getElementById('login-form');
    if (loginForm) {
        loginForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;
            const errorMsg = document.getElementById('error-message');

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
                    errorMsg.style.display = 'block';
                }
            } catch (error) {
                console.error('Login Error:', error);
                errorMsg.textContent = 'Connection error';
                errorMsg.style.display = 'block';
            }
        });
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
                <span class="price">$${place.price}</span>
                <h2>${place.title}</h2>
                <p>${place.description}</p>
                <button class="details-btn" onclick="alert('Details page coming soon for ID: ${place.id}')">View Details</button>
            `;
            container.appendChild(card);
        });
    } catch (error) {
        console.error('Error fetching places:', error);
    }
}

function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}
