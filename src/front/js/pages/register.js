import React, { useState, useEffect, useContext } from "react";
import { Link } from "react-router-dom";
import { Context } from "../store/appContext";

export const Register = () => {
	const { store, actions } = useContext(Context);

	return (
		<div className="container mt-5">
			inicia aqui tu registro
			<br />
			<Link to="/demo">
				<button className="btn btn-primary">save</button>
			</Link>
		</div>
	);
};
