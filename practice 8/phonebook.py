import psycopg2
from config import load_config

def get_connection():
    """Establishes a connection to the PostgreSQL database"""
    params = load_config()
    return psycopg2.connect(**params)

def search_contacts(pattern):
    """Использует функцию search_contacts для поиска"""
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.callproc('search_contacts', (pattern,))
                results = cur.fetchall()
                if not results:
                    print("No contacts found.")
                else:
                    print("\n--- Search Results ---")
                    for contact in results:
                        print(f"ID: {contact[0]} | Name: {contact[1]} | Phone: {contact[2]}")
                return results
    except Exception as e:
        print(f"Error: {e}")

def insert_or_update_contact(name, phone):
    """Использует процедуру insert_or_update_contact"""
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("CALL insert_or_update_contact(%s, %s)", (name, phone))
            conn.commit()
            print(f"✅ Contact '{name}' processed successfully")
    except Exception as e:
        print(f"Error: {e}")

def get_paginated_contacts(limit_num, offset_num):
    """Использует функцию get_contacts_paginated"""
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.callproc('get_contacts_paginated', (limit_num, offset_num))
                results = cur.fetchall()
                print(f"\n--- Page (LIMIT={limit_num}, OFFSET={offset_num}) ---")
                for contact in results:
                    print(f"ID: {contact[0]} | Name: {contact[1]} | Phone: {contact[2]}")
                return results
    except Exception as e:
        print(f"Error: {e}")

def delete_contact(identifier):
    """Использует процедуру delete_contact_by_name_or_phone"""
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("CALL delete_contact_by_name_or_phone(%s)", (identifier,))
            conn.commit()
            print(f"✅ Delete operation completed")
    except Exception as e:
        print(f"Error: {e}")

def insert_many_contacts(contacts_list):
    """
    Вставляет много контактов за раз
    contacts_list: список кортежей [(name, phone), (name, phone), ...]
    """
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                valid_count = 0
                invalid_count = 0
                
                for name, phone in contacts_list:
                    try:
                        cur.execute("CALL insert_or_update_contact(%s, %s)", (name, phone))
                        conn.commit()
                        print(f"  ✅ Added/Updated: {name} - {phone}")
                        valid_count += 1
                    except Exception as e:
                        print(f"  ❌ Failed: {name} - {phone}")
                        invalid_count += 1
                
                print(f"\n📊 Results: {valid_count} successful, {invalid_count} failed")
                
    except Exception as e:
        print(f"Error inserting many contacts: {e}")

def main_menu():
    while True:
        print("\n===== PhoneBook with Functions & Procedures =====")
        print("1. Search contacts (function)")
        print("2. Insert or update contact (procedure)")
        print("3. Get paginated contacts (function with LIMIT/OFFSET)")
        print("4. Delete contact (procedure)")
        print("5. Insert many contacts (procedure with validation)")
        print("6. Exit")
        
        choice = input("\nSelect an option (1-6): ")
        
        if choice == '1':
            pattern = input("Enter search pattern: ")
            search_contacts(pattern)
        elif choice == '2':
            name = input("Enter name: ")
            phone = input("Enter phone (11 digits, starts with 7 or 8): ")
            insert_or_update_contact(name, phone)
        elif choice == '3':
            try:
                limit_num = int(input("Enter LIMIT (how many rows): "))
                offset_num = int(input("Enter OFFSET (skip rows): "))
                get_paginated_contacts(limit_num, offset_num)
            except ValueError:
                print("Please enter valid numbers")
        elif choice == '4':
            identifier = input("Enter name or phone to delete: ")
            delete_contact(identifier)
        elif choice == '5':
            print("\n--- Insert Multiple Contacts ---")
            print("Enter contacts in format: name,phone")
            print("Example: John,87012223344")
            print("Type 'done' when finished")
            print("-" * 40)
            
            contacts = []
            while True:
                entry = input("➜ ")
                
                if entry.lower() == 'done':
                    break
                
                if ',' not in entry:
                    print("  ❌ Invalid format! Use: name,phone")
                    continue
                
                parts = entry.split(',')
                if len(parts) != 2:
                    print("  ❌ Invalid format! Use: name,phone")
                    continue
                
                name = parts[0].strip()
                phone = parts[1].strip()
                
                if not name or not phone:
                    print("  ❌ Name and phone cannot be empty!")
                    continue
                
                contacts.append((name, phone))
                print(f"  ✅ Added to queue: {name} - {phone}")
            
            if contacts:
                print(f"\n📋 Processing {len(contacts)} contacts...")
                insert_many_contacts(contacts)
            else:
                print("❌ No contacts to insert")
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main_menu()