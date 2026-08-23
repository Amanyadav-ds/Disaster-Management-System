USE disaster_management;

-- ============================================================
-- INITIAL ADMIN USER
-- ============================================================
-- Password hash corresponds to the password you generated
-- with your bcrypt script.
--
-- IMPORTANT:
-- Replace the value below with your actual bcrypt hash.
-- ============================================================

INSERT INTO users
(full_name, username, email, password_hash, role)
VALUES
(
    'Aman Yadav',
    'aman',
    'aman@gmail.com',
    '$2b$12$QySaIcV/ZtMG7hbwWrJiWOyLcPPh0hcV8d86iuQ3Uy1kFVb2zNlDe',
    'Admin'
);

-- ============================================================
-- SAMPLE DISASTER
-- ============================================================

INSERT INTO disasters
(disaster_name, disaster_type, description, location, severity, start_date, status)
VALUES
(
    'Sample Flood',
    'Flood',
    'Sample disaster record for testing the system.',
    'Mumbai',
    'High',
    '2026-08-01',
    'Active'
);

-- ============================================================
-- SAMPLE RELIEF CAMP
-- ============================================================

INSERT INTO relief_camps
(camp_name, location, capacity, occupied_capacity, contact_number, status, disaster_id)
VALUES
(
    'Central Relief Camp',
    'Mumbai',
    500,
    120,
    '9876543210',
    'Active',
    1
);

-- ============================================================
-- SAMPLE RESOURCE
-- ============================================================

INSERT INTO resources
(resource_name, resource_type, quantity, unit, location, minimum_required, status, disaster_id)
VALUES
(
    'Drinking Water',
    'Water',
    1000,
    'Litres',
    'Central Warehouse',
    300,
    'Available',
    1
);