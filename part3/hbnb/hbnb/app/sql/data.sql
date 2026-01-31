USE hbnb_dev_db;

-- ======================
-- ADMIN USER
-- ======================
INSERT INTO users (
    id, email, password, first_name, last_name, is_admin, created_at, updated_at
) VALUES (
    "admin-id-001",
    "admin@hbnb.io",
    "admin123",
    "Admin",
    "User",
    TRUE,
    NOW(),
    NOW()
);

-- ======================
-- AMENITIES
-- ======================
INSERT INTO amenities (id, name, created_at, updated_at) VALUES
("amenity-001", "WiFi", NOW(), NOW()),
("amenity-002", "Air conditioning", NOW(), NOW()),
("amenity-003", "Parking", NOW(), NOW()),
("amenity-004", "Swimming pool", NOW(), NOW()),
("amenity-005", "Gym", NOW(), NOW());
