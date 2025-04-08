from app import app
from mangum import Mangum

# Testing
handler = Mangum(app)
