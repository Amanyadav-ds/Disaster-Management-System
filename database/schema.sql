-- ============================================================
-- Disaster Relief Resource Management System
-- Database Schema
-- ============================================================

CREATE DATABASE IF NOT EXISTS disaster_management;

USE disaster_management;

-- ============================================================
-- USERS
-- ============================================================

CREATE TABLE IF NOT EXISTS users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    role ENUM('Admin', 'Coordinator', 'Volunteer') NOT NULL DEFAULT 'Volunteer',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ============================================================
-- DISASTERS
-- ============================================================

CREATE TABLE IF NOT EXISTS disasters (
    disaster_id INT AUTO_INCREMENT PRIMARY KEY,
    disaster_name VARCHAR(100) NOT NULL,
    disaster_type VARCHAR(50) NOT NULL,
    description TEXT,
    location VARCHAR(150) NOT NULL,
    severity ENUM('Low', 'Medium', 'High', 'Critical') NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    status ENUM('Active', 'Resolved', 'Under Control') DEFAULT 'Active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ============================================================
-- RELIEF CAMPS
-- ============================================================

CREATE TABLE IF NOT EXISTS relief_camps (
    camp_id INT AUTO_INCREMENT PRIMARY KEY,
    camp_name VARCHAR(100) NOT NULL,
    location VARCHAR(150) NOT NULL,
    capacity INT NOT NULL,
    occupied_capacity INT DEFAULT 0,
    contact_number VARCHAR(20),
    status ENUM('Active', 'Full', 'Closed') DEFAULT 'Active',
    disaster_id INT,
    
    FOREIGN KEY (disaster_id)
        REFERENCES disasters(disaster_id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);

-- ============================================================
-- VICTIMS
-- ============================================================

CREATE TABLE IF NOT EXISTS victims (
    victim_id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    age INT,
    gender ENUM('Male', 'Female', 'Other'),
    contact_number VARCHAR(20),
    address VARCHAR(255),
    medical_condition VARCHAR(255),
    family_size INT DEFAULT 1,
    camp_id INT,
    disaster_id INT,
    status ENUM('Missing', 'Rescued', 'Injured', 'Safe', 'Deceased')
        DEFAULT 'Missing',
    registered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (camp_id)
        REFERENCES relief_camps(camp_id)
        ON DELETE SET NULL
        ON UPDATE CASCADE,

    FOREIGN KEY (disaster_id)
        REFERENCES disasters(disaster_id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);

-- ============================================================
-- VOLUNTEERS
-- ============================================================

CREATE TABLE IF NOT EXISTS volunteers (
    volunteer_id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    age INT,
    gender ENUM('Male', 'Female', 'Other'),
    contact_number VARCHAR(20) NOT NULL,
    email VARCHAR(100),
    skill VARCHAR(150),
    availability ENUM('Available', 'Busy', 'Unavailable')
        DEFAULT 'Available',
    disaster_id INT,

    FOREIGN KEY (disaster_id)
        REFERENCES disasters(disaster_id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);

-- ============================================================
-- RESOURCES
-- ============================================================

CREATE TABLE IF NOT EXISTS resources (
    resource_id INT AUTO_INCREMENT PRIMARY KEY,
    resource_name VARCHAR(100) NOT NULL,
    resource_type VARCHAR(50) NOT NULL,
    quantity INT NOT NULL DEFAULT 0,
    unit VARCHAR(30),
    location VARCHAR(150),
    minimum_required INT DEFAULT 0,
    status ENUM('Available', 'Low Stock', 'Out of Stock')
        DEFAULT 'Available',
    disaster_id INT,

    FOREIGN KEY (disaster_id)
        REFERENCES disasters(disaster_id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);

-- ============================================================
-- DONATIONS
-- ============================================================

CREATE TABLE IF NOT EXISTS donations (
    donation_id INT AUTO_INCREMENT PRIMARY KEY,
    donor_name VARCHAR(100) NOT NULL,
    donor_contact VARCHAR(50),
    donation_type ENUM('Money', 'Food', 'Medicine', 'Clothing', 'Other')
        NOT NULL,
    amount DECIMAL(12,2) DEFAULT 0,
    description TEXT,
    donation_date DATE NOT NULL,
    disaster_id INT,

    FOREIGN KEY (disaster_id)
        REFERENCES disasters(disaster_id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);

-- ============================================================
-- RESOURCE DISTRIBUTION
-- ============================================================

CREATE TABLE IF NOT EXISTS resource_distribution (
    distribution_id INT AUTO_INCREMENT PRIMARY KEY,
    resource_id INT NOT NULL,
    camp_id INT,
    quantity_distributed INT NOT NULL,
    distribution_date DATE NOT NULL,
    distributed_by INT,

    FOREIGN KEY (resource_id)
        REFERENCES resources(resource_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,

    FOREIGN KEY (camp_id)
        REFERENCES relief_camps(camp_id)
        ON DELETE SET NULL
        ON UPDATE CASCADE,

    FOREIGN KEY (distributed_by)
        REFERENCES users(user_id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);

-- ============================================================
-- VOLUNTEER ASSIGNMENTS
-- ============================================================

CREATE TABLE IF NOT EXISTS volunteer_assignments (
    assignment_id INT AUTO_INCREMENT PRIMARY KEY,
    volunteer_id INT NOT NULL,
    camp_id INT,
    assignment_role VARCHAR(100),
    assigned_date DATE NOT NULL,
    status ENUM('Assigned', 'Completed', 'Cancelled')
        DEFAULT 'Assigned',

    FOREIGN KEY (volunteer_id)
        REFERENCES volunteers(volunteer_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,

    FOREIGN KEY (camp_id)
        REFERENCES relief_camps(camp_id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);

-- ============================================================
-- END OF SCHEMA
-- ============================================================