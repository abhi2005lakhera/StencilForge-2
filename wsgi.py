import os
from flask import Flask

if __name__ == "__main__":
    port = int(os.getenv("PORT", 4000)) 
    app.run(host="0.0.0.0", port=port)
