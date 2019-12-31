import React from "react";
import ReactDOM from "react-dom";
import { createBrowserHistory } from "history";
import { Router, Route, Switch, Redirect } from "react-router-dom";

// core components
import LecturerLogin from "layouts/LecturerLogin.js";
import LecturerAdmin from "layouts/LecturerAdmin.js";
import StudentLogin from "layouts/StudentLogin.js";
import StudentAdmin from "layouts/StudentAdmin.js";

import "assets/css/attendance-web-app.css?v=1.8.0";

const hist = createBrowserHistory();

ReactDOM.render(
    <Router history={hist}>
        <Switch>
            <Route path="/lecturer" component={LecturerLogin} />
            <Route path="/student" component={StudentLogin} />
            <Route path="/lecturer/admin" component={LecturerAdmin} />
            <Route path="/student/admin" component={StudentAdmin} />
            <Redirect from="/" to="/student" />
        </Switch>
    </Router>,
    document.getElementById("root")
);