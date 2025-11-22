import os

file_path = "alembic.ini"

with open(file_path, "r") as f:
    content = f.read()

bad_line = "sqlalchemy.url = driver://user:pass@localhost/dbname"
good_line = "sqlalchemy.url = sqlite:///database.db"

if bad_line in content:
    new_content = content.replace(bad_line, good_line)
    
    with open(file_path, "w") as f:
        f.write(new_content)
    print("✅ SUCCESS: I found the bad line and replaced it with sqlite:///database.db")
elif good_line in content:
    print("ℹ️ NOTE: The file is ALREADY correct. The error might be coming from a different folder?")
else:
    print("❌ ERROR: I couldn't find the 'driver' line. Please check alembic.ini manually.")