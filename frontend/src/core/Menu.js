import React, { Fragment, useContext } from "react";
import { Link, withRouter } from "react-router-dom";
// import BotPayloadContext from '../BotPayloadContext';
import UserContext from '../UserContext';
import { signout, isAuthenticated } from "../auth/helper";

const currentTab = (history, path) => {
    if (history.location.pathname === path) {
        return { color: "#blue" };
    } else {
        return { color: "#FFFFFF" };
    }
};

const Menu = ({ history, path }) => {
    // const { value, setValue } = useContext(BotPayloadContext);
    const { isAdmin, setIsAdmin } = useContext(UserContext);

    return (
        <div>
            <ul className="nav nav-tabs bg-dark">
                <li className="nav-item">
                    <Link
                        style={currentTab(history, "/")}
                        className="nav-link"
                        to="/"
                    >
                        GROWW
          </Link>

                </li>
                <li className="nav-item">

                    <Link
                        style={currentTab(history, "/cart")}
                        className="nav-link"
                        to="/cart"
                    >
                        MyCart
                    </Link>
                </li>
                {/* {isAuthenticated() && (
                    <li className="nav-item">
                        <Link
                            style={currentTab(history, "/user/dashboard")}
                            className="nav-link"
                            to="/user/dashboard"
                        >
                            dashboard
            </Link>
                    </li>
                )} */}
                {!isAuthenticated() && (
                    <Fragment>
                        <li className="nav-item">
                            <Link
                                style={currentTab(history, "/signup")}
                                className="nav-link"
                                to="/signup"
                            >
                                Signup
              </Link>
                        </li>
                        <li className="nav-item">
                            <Link
                                style={currentTab(history, "/signin")}
                                className="nav-link"
                                to="/signin"
                            >
                                Signin
              </Link>
                        </li>
                    </Fragment>
                )}

                {isAuthenticated() && (
                    <li className="nav-item">
                        <span
                            onClick={() => {
                                signout(() => {
                                    history.push("/");
                                    setIsAdmin(false)
                                });
                            }}
                            className="nav-link text-warning"
                        >
                            Signout
            </span>
                    </li>
                )}
            </ul>
        </div>
    );
};

export default withRouter(Menu);
