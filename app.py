from fastapi import FastAPI
from models import TextRequest, QARequest
from services.ai_service import summarize_text, improve_grammar, answer_question

app = FastAPI(title="AI text-processign API")

@app.post("/summarize")
def summarize(req: TextRequest):
    try:
        result = summarize_text(req.text)
        return {
        "status": "success",
        "data": {"summary": result}
    }
    except Exception as e:
        return {
        "status": "error",
        "message": "Failed to process request"
    }

@app.post("/improve-grammar")
def grammar(req: TextRequest):
    try:
        result = improve_grammar(req.text)
        return {
        "status": "success",
        "data": {"improved_text": result}
    }
    except Exception as e:
        return {
        "status": "error",
        "message": "Failed to process request"
    }


@app.post("/ask")
def ask(req: QARequest ):
   try:
    result = answer_question(req.context, req.question)
    return {
        "status": "success",
        "data": {"answer": result}
    }
   except Exception as e:
        return {
        "status": "error",
        "message": "Failed to process request"
    }
    
