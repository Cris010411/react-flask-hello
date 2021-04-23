import React, { useContext, useState } from "react";
import { Context } from "../store/appContext";
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";
import "../../styles/home.scss";

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

	return (
		<div className="container mt-5">
			<div className="row">
				<div className="col-6">
					<h1>Bienvenido al memory test!</h1>
					<br />
					<br />
					<p>Resuelve problemas psicometricos y triunfa en todas sus entrevistas laborales</p>
				</div>
				<div className="col-6">
					<div className="Login">
						<Form onSubmit={handleSubmit}>
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
							<Button block size="lg" type="submit" disabled={!validateForm()}>
								Login
							</Button>
						</Form>
					</div>
				</div>
			</div>
		</div>
	);
};
