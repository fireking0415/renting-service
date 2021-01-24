from flask import jsonify
from werkzeug.exceptions import default_exceptions, HTTPException, abort

import project


def operator_common_error(app):
    def error_handling(error):
        if isinstance(error, HTTPException):
            result = {"code": error.code, "data": None, "message": str(error)}
        else:
            result = {"code": 500, "data": None, "message": str(error)}

        resp = jsonify(result)
        resp.status_code = result["code"]
        return resp

    for code in default_exceptions.keys():
        app.register_error_handler(code, error_handling)

    return app


if __name__ == '__main__':
    app = project.create_app()
    app = operator_common_error(app)
    app.run(
        host='0.0.0.0',
        port=9999,
        debug=True
    )
