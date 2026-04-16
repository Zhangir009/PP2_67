-- =====================================================
-- Процедура 1: Вставить или обновить одного пользователя
-- =====================================================
CREATE OR REPLACE PROCEDURE insert_or_update_contact(
    p_first_name VARCHAR,
    p_phone_number VARCHAR
)
LANGUAGE plpgsql
AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM phonebook WHERE first_name = p_first_name) THEN
        UPDATE phonebook 
        SET phone_number = p_phone_number 
        WHERE first_name = p_first_name;
        RAISE NOTICE '✅ Contact % updated', p_first_name;
    ELSE
        INSERT INTO phonebook (first_name, phone_number)
        VALUES (p_first_name, p_phone_number);
        RAISE NOTICE '✅ Contact % inserted', p_first_name;
    END IF;
END;
$$;

-- =====================================================
-- Процедура 2: Удалить по имени или телефону
-- =====================================================
CREATE OR REPLACE PROCEDURE delete_contact_by_name_or_phone(
    identifier VARCHAR
)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM phonebook 
    WHERE first_name = identifier OR phone_number = identifier;
    
    IF FOUND THEN
        RAISE NOTICE '✅ Contact(s) with "%" deleted', identifier;
    ELSE
        RAISE NOTICE '❌ No contact found with "%"', identifier;
    END IF;
END;
$$;

-- =====================================================
-- Процедура 3: Вставить много пользователей с валидацией
-- =====================================================
CREATE OR REPLACE PROCEDURE insert_many_contacts(
    contacts_data TEXT[][]
)
LANGUAGE plpgsql
AS $$
DECLARE
    i INTEGER;
    contact_name VARCHAR;
    contact_phone VARCHAR;
    invalid_contacts TEXT := '';
    valid_count INTEGER := 0;
    invalid_count INTEGER := 0;
BEGIN
    IF contacts_data IS NULL OR array_length(contacts_data, 1) IS NULL THEN
        RAISE NOTICE 'No contacts to insert';
        RETURN;
    END IF;
    
    FOR i IN 1..array_length(contacts_data, 1) LOOP
        contact_name := contacts_data[i][1];
        contact_phone := contacts_data[i][2];
        
        IF contact_phone ~ '^[78][0-9]{10}$' THEN
            IF EXISTS (SELECT 1 FROM phonebook WHERE first_name = contact_name) THEN
                UPDATE phonebook SET phone_number = contact_phone WHERE first_name = contact_name;
                RAISE NOTICE '✅ Updated: % -> %', contact_name, contact_phone;
            ELSE
                INSERT INTO phonebook (first_name, phone_number) VALUES (contact_name, contact_phone);
                RAISE NOTICE '✅ Inserted: % -> %', contact_name, contact_phone;
            END IF;
            valid_count := valid_count + 1;
        ELSE
            invalid_contacts := invalid_contacts || format('(%s, %s) ', contact_name, contact_phone);
            invalid_count := invalid_count + 1;
            RAISE NOTICE '❌ Invalid phone (skipped): % -> %', contact_name, contact_phone;
        END IF;
    END LOOP;
    
    RAISE NOTICE '=====================================';
    RAISE NOTICE '✅ Valid contacts added/updated: %', valid_count;
    RAISE NOTICE '❌ Invalid contacts skipped: %', invalid_count;
    
    IF invalid_contacts <> '' THEN
        RAISE NOTICE '❌ Skipped contacts: %', invalid_contacts;
    END IF;
    RAISE NOTICE '=====================================';
END;
$$;
