-- Процедура 1: Вставить или обновить
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
        RAISE NOTICE 'Contact % updated', p_first_name;
    ELSE
        INSERT INTO phonebook (first_name, phone_number)
        VALUES (p_first_name, p_phone_number);
        RAISE NOTICE 'Contact % inserted', p_first_name;
    END IF;
END;
$$;

-- Процедура 2: Удалить по имени или телефону
CREATE OR REPLACE PROCEDURE delete_contact_by_name_or_phone(
    identifier VARCHAR
)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM phonebook 
    WHERE first_name = identifier OR phone_number = identifier;
    
    IF FOUND THEN
        RAISE NOTICE 'Contact(s) with "%" deleted', identifier;
    ELSE
        RAISE NOTICE 'No contact found with "%"', identifier;
    END IF;
END;
$$;