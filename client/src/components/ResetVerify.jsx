import React, { useState } from 'react';
import { Redirect } from 'react-router';
import { useParams } from 'react-router-dom';
import { FormGroup } from 'react-bootstrap';

import Input from './Input';
import Button from './Button';

const { REACT_APP_PROXY } = process.env;

const ResetVerify = () => {
    const [password, setPassword] = useState("");
    const [error, setError] = useState();
    const [redirect, setRedirect] = useState(false);

    const { uid, token } = useParams();

    const handleFormSubmit = (e) => {
        e.preventDefault();

        fetch(REACT_APP_PROXY + `/api/v1/password-reset-confirm/${uid}/${token}/`, {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                'password': password
            })
        }).then(jsob => jsob.json())
        .then(json => {
            if (json.error) {
                console.log(json.error);
                setError(json.error);
            } else {
                setRedirect(true);
            }
        }).catch(err => {
            console.log(err);
            setError("Internal server error");
        });
    }

    return (
        <div className="verify-password-reset">
            { redirect && <Redirect to="/" /> }
            <h1>Change Password</h1>
            <form
                onSubmit={handleFormSubmit}
                className="container-fluid"
                id="reset-password-form"
                noValidate>
                <FormGroup>
                    <div className="form-group col-md-8">
                        <Input
                            className={"required"}
                            type={"text"}
                            title={"Password"}
                            name={"password"}
                            value={password}
                            placeholder={"Password"}
                            handleChange={(e) => setPassword(e.target.value)}
                            error={error}
                        />
                    </div>
                    <div className="form-group col-md-6" align="center">
                        <Button buttonType={"primary"} type={"submit"} title={"Reset Password"} />
                    </div>
                </FormGroup>
            </form>
            { error && <span style={{ color: "red" }}>{ error }</span> }
        </div>
    );
}

export default ResetVerify;