# main.py
from api import app

if __name__ == '__main__':
    # 运行Flask应用
    app.run(host='0.0.0.0', port=15001)
