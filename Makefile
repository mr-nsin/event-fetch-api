
**Makefile**

```makefile
run:
    python initialize_db.py
    uvicorn main:app --reload
