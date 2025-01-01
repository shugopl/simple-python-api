from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict, Any

# Create FastAPI instance
app = FastAPI()

# Define data models
class InputData(BaseModel):
    name: str
    message: Optional[str] = None
    data: Dict[str, Any]

class ResponseData(BaseModel):
    status: str
    processed_data: Dict[str, Any]
    message: str

# Keep the existing GET endpoint
@app.get("/")
def hello():
    return "Hello from FastAPI with CI/CD"

# Add new POST endpoint
@app.post("/process", response_model=ResponseData)
async def process_data(input_data: InputData):
    try:
        # Process the input data
        processed_result = {
            "input_name": input_data.name,
            "input_message": input_data.message,
            "processed_fields": len(input_data.data),
            "data_keys": list(input_data.data.keys())
        }

        return ResponseData(
            status="success",
            processed_data=processed_result,
            message=f"Successfully processed data for {input_data.name}"
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Add endpoint for specific data processing
@app.post("/analyze")
async def analyze_data(input_data: Dict[str, Any]):
    try:
        # Example of data validation
        if not input_data:
            raise HTTPException(status_code=400, detail="Input data cannot be empty")

        # Process the data
        analysis_result = {
            "received_data": input_data,
            "data_type": str(type(input_data)),
            "number_of_fields": len(input_data),
            "timestamp": "2024-03-19"  # You might want to use actual datetime here
        }

        return {
            "status": "success",
            "analysis": analysis_result
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")