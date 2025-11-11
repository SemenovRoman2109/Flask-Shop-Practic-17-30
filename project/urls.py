import home_app

home_app.home.add_url_rule(rule = '/', view_func = home_app.render_home, methods = ["GET", "POST"])
home_app.home.add_url_rule(rule = '/reg', view_func = home_app.render_registation, methods = ["GET", "POST"])
home_app.home.add_url_rule(rule = '/login', view_func = home_app.render_login, methods = ["GET", "POST"])
home_app.home.add_url_rule(rule = '/users', view_func = home_app.render_listusers, methods = ["GET", "POST"])
home_app.home.add_url_rule(rule = '/logout', view_func = home_app.logout)