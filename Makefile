
**Makefile**

```makefile
run:
    python .\db\migrations\initialize_db.py
    uvicorn main:app --reload
