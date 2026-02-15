from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pfag.core.coordinate_conversion import convert_coordinates, CoordinateConversionError

app = FastAPI()

class CoordinateConvertRequest(BaseModel):
    x_img: int
    y_img: int
    img_width: int
    img_height: int
    pdf_width: float
    pdf_height: float

class CoordinateConvertResponse(BaseModel):
    x_pdf: float
    y_pdf: float
    error_x: float
    error_y: float

@app.post("/coordinate-convert", response_model=CoordinateConvertResponse)
def coordinate_convert(req: CoordinateConvertRequest):
    try:
        x_pdf, y_pdf = convert_coordinates(
            req.x_img, req.y_img, req.img_width, req.img_height, req.pdf_width, req.pdf_height
        )
        # 誤差計算（理論値と比較）
        expected_x = req.x_img * (req.pdf_width / req.img_width)
        expected_y = req.pdf_height - (req.y_img * (req.pdf_height / req.img_height))
        error_x = abs(x_pdf - expected_x)
        error_y = abs(y_pdf - expected_y)
        return CoordinateConvertResponse(
            x_pdf=x_pdf, y_pdf=y_pdf, error_x=error_x, error_y=error_y
        )
    except CoordinateConversionError as e:
        raise HTTPException(status_code=400, detail=str(e))
