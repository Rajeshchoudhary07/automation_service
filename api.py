from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from automation_functions import FUNCTIONS
from rag_model import rag_model
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

app = FastAPI()

class RequestModel(BaseModel):
    prompt: str

@app.post("/execute")
async def execute_function(request: RequestModel):
    try:
        # Retrieve the function name based on the user prompt
        function_name = rag_model.retrieve_function(request.prompt)
        function = FUNCTIONS[function_name]

        # Generate dynamic code
        code = f"""
from automation_functions import {function_name}

def main():
    try:
        result = {function_name}()
        print("Function executed successfully. Result: {{result}}")
    except Exception as e:
        print(f"Error executing function: {{e}}")

if __name__ == "__main__":
    main()
"""
        return {"function": function_name, "code": code}
    except Exception as e:
        logging.error(f"Error in executing function: {e}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)