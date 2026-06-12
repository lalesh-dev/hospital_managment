from configs.mysql_config import MYSQLConfig
from extension.sqlalchemy import db
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config.from_object(MYSQLConfig)
db.init_app(app)

app.register_blueprint(user_bp)

with app.app_context():
    db.create_all()

print("/n Registered Endpoint :/n")
for rule in app.url_map.iter_rules():
    method = ',' .join (rule.methods  - { 'HEAD','OPTIONS'})

    print(f"Endpoint : {rule.endpoint}")
    print(f"Methods : {rule.methods}")
    print(f"URL : {rule.rule}")
    print("-" * 50 )

if __name__=='__main__':
    app.run(debug = True)    
