# Automation Service

## Overview

The **Automation Service** is a Python-based API that dynamically retrieves and executes automation functions using Retrieval-Augmented Generation (RAG) with a language model. This service allows users to perform various automation tasks such as opening applications, retrieving system monitoring data, and executing shell commands through a simple API interface.

## Features

- **Open Applications**: Launch common applications like Chrome, Calculator, and Notepad.
- **System Monitoring**: Retrieve CPU and RAM usage statistics.
- **Command Execution**: Execute shell commands and retrieve their output.
- **Dynamic Code Generation**: Generate structured Python code for function invocation based on user prompts.
- **RAG Model**: Utilize a retrieval-augmented generation model to map user queries to predefined functions.

## Project Structure

## Requirements

- Python 3.7 or higher
- Install the required packages using the following command:

```bash
pip install -r requirements.txt

 

## Running the API
### Start the FastAPI server:

Open your terminal and navigate to the project directory, then run:

bash
Run
Copy code
python api.py
The API will be available at http://localhost:8000.

## Testing the API:

You can use tools like Postman or curl to test the API. For example, to open the calculator, send a POST request to http://localhost:8000/execute with the following JSON body:

json
Run
Copy code
{
    "prompt": "Open calculator"
}
### Example Response
json
Run
Copy code
{
    "function": "open_calculator",
    "code": "from automation_functions import open_calculator\n\ndef main():\n    try:\n        result = open_calculator()\n        print(\"Function executed successfully. Result: {result}\")\n    except Exception as e:\n        print(f\"Error executing function: {e}\")\n\nif __name__ == \"__main__\":\n    main()"
}


## Contributing
Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request. Please follow these steps:
Fork the repository.
1 Create a new branch for your feature or bug fix.
2 Make your changes and commit them with a descriptive message.
3 Push your changes to your forked repository.
4 Open a pull request to the main repository.
