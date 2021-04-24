import React from "react";
import PropTypes from "prop-types";
import { Link, useParams } from "react-router-dom";
import { Context } from "../store/appContext";

export const Personal = () => {
	return (
		<div className="container mt-5">
			<div className="jumbotron">perfil del usuario</div>
			<Link to="/demo">
				<button className="btn btn-primary">Back home</button>
			</Link>
		</div>
	);
};
