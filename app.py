import traceback
from flask import request
# from controllers import session_controller, tenant_controller , grafana_dashboard_controller
from init import app
#from responsors import common_responsor


# @app.errorhandler(500)
# def handle_500(ex):
#     traceback.print_exc()
#     return common_responsor.get_message('Something went wrong. Please contact server administrator.'), 500

#
# @app.route("/tenant/database/create", methods=['POST'])
# def create_tenant_database():
#     return tenant_controller.tenant_db_create(request.form, request.headers)
#
#
# @app.route("/tenant/database/stop/<tenant_name>", methods=['GET'])
# def stop_tenant_database(tenant_name):
#     print(request.form)
#     return tenant_controller.tenant_db_stop(tenant_name)


# @app.route("/tenant/database/start/<tenant_name>", methods=['GET'])
# def start_tenant_database(tenant_name):
#     print(request.form)
#     return tenant_controller.tenant_db_start(tenant_name)
#
#
# @app.route("/tenant/database/delete/<tenant_name>", methods=['DELETE'])
# def delete_tenant_database(tenant_name):
#     print(request.form)
#     return tenant_controller.tenant_db_remove(tenant_name)
#
#
# @app.route("/tenant/database/images/<tenant_name>", methods=['GET'])
# def get_tenant_images_list(tenant_name):
#     print(request.form)
#     return tenant_controller.perform_pre_checks(tenant_name)
#
#
# @app.route("/tenant/database/status", methods=['POST'])
# @session_controller.check_for_token
# def fetch_tenant_database():
#     print(request.form)
#     return tenant_controller.tenant_db_restart(request.form)
#
#
# @app.route("/tenant/database/restore", methods=['POST'])
# @session_controller.check_for_token
# def restore_tenant_database():
#     print(request.form)
#     return tenant_controller.tenant_db_start(request.form)


#print(grafana_dashboard_controller.create_datasource())


if __name__ == "__main__":
    app.run(port=6011)