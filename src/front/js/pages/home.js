import React, { useContext, useState } from "react";
import { Context } from "../store/appContext";
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";
import { Link } from "react-router-dom";
import "../../styles/home.scss";
import logo from "../../img/logo.png";

export const Home = () => {
	const { store, actions } = useContext(Context);
	const [email, setEmail] = useState("");
	const [password, setPassword] = useState("");

	function validateForm() {
		return email.length > 0 && password.length > 0;
	}
	function handleSubmit(event) {
		event.preventDefault();
	}

	function ingreso() {
		return (window.location.href = "./demo");
	}
	return (
		<div className="container">
			<div className="row">
				<div className="col-8 mt-5">
					<h1>Bienvenido al memory test!</h1>
					<br />
					<br />
					<p>Resuelve problemas psicometricos y triunfa en todas sus entrevistas laborales</p>
				</div>
				<div className="col-4 text-center">
					<img style={{ width: "12rem" }} src={logo} />
					<div className="Login text-left">
						<h5 className="mt-3">
							<strong>Inicia sesión</strong>
						</h5>
						<Form className="mt-2" onSubmit={handleSubmit}>
							<Form.Group size="lg" controlId="email">
								<Form.Label>Email</Form.Label>
								<Form.Control
									autoFocus
									type="email"
									value={email}
									onChange={e => setEmail(e.target.value)}
								/>
							</Form.Group>
							<Form.Group size="lg" controlId="password">
								<Form.Label>Password</Form.Label>
								<Form.Control
									type="password"
									value={password}
									onChange={e => setPassword(e.target.value)}
								/>
							</Form.Group>
							<Link to="/demo">
								<Button
									block
									size="lg"
									type="submit"
									disabled={!validateForm()}
									onclick={() => ingreso()}>
									Login
								</Button>
							</Link>
							<br />
							<Link to="/register">
								<a href="#" className="text-decoration-none">
									Crear una cuenta
								</a>
							</Link>
						</Form>
					</div>
				</div>
			</div>
		</div>
	);
};
