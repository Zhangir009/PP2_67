-- Функция 1: Поиск по шаблону
CREATE OR REPLACE FUNCTION search_contacts(pattern TEXT)
RETURNS TABLE(
    id INTEGER,
    first_name VARCHAR,
    phone_number VARCHAR
) AS $$
BEGIN
    RETURN QUERY
    SELECT p.id, p.first_name, p.phone_number
    FROM phonebook p
    WHERE p.first_name ILIKE '%' || pattern || '%'
       OR p.phone_number ILIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;

-- Функция 2: Пагинация
CREATE OR REPLACE FUNCTION get_contacts_paginated(
    limit_count INTEGER,
    offset_count INTEGER
)
RETURNS TABLE(
    id INTEGER,
    first_name VARCHAR,
    phone_number VARCHAR
) AS $$
BEGIN
    RETURN QUERY
    SELECT p.id, p.first_name, p.phone_number
    FROM phonebook p
    ORDER BY p.id
    LIMIT limit_count
    OFFSET offset_count;
END;
$$ LANGUAGE plpgsql;

-- Функция 3: Проверка телефона
CREATE OR REPLACE FUNCTION is_valid_phone(phone TEXT)
RETURNS BOOLEAN AS $$
BEGIN
    RETURN phone ~ '^[78][0-9]{10}$';
END;
$$ LANGUAGE plpgsql;