// eslint-disable-next-line react/prop-types
function Login({ onSwitch }) {
  return (
    <div className="form-container">
      <h2>Login</h2>
      <form>
        <label htmlFor="email">Email:</label>
        <input type="email" id="email" required />

        <label htmlFor="password">Password:</label>
        <input type="password" id="password" required />

        <button type="submit">Login</button>
      </form>
      <p>
        Don&apos;t have an account? <button onClick={onSwitch}>Sign Up</button>
      </p>
    </div>
  );
}

export default Login;
