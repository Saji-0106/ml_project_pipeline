from flask import Flask
from src.logger import logging

app = Flask(__name__)


@app.route('/',methods=['GET','POST'])
def index():
    try:
        raise Exception("we are testing custom file")
    except Exception as e:
       abc = CustmeException(e, sys)
       logging.info(abc.error_message)
       return  "welcome to ml_project_pipeline"


if __name__ =="__main__":
    app.run(debug=True)
