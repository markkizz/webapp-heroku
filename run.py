import os

from flask import Flask, render_template

data = {
    'app_name': os.getenv('NAMESPACE') if os.getenv('NAMESPACE') else 'WebApp Local'
    # 'namespace': os.getenv('NAMESPACE'),
    # 'pod_name': os.getenv('POD_NAME'),
    # 'pod_ip': os.getenv('POD_IP'),
    # 'node_name': os.getenv('NODE_NAME')
}

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('demo.html', data=data)


if __name__ == "__main__":
    app.run()
