import ThemeSwitcher from "./ThemeSwitcher";

const HeaderNav = () => {
  return (
    <nav className="navbar">
      <div className="navbar-left">
        <a href="/" className="logo">
          Unio
        </a>
      </div>
      <div className="navbar-right">
        <ul className="nav-links">
          <li>
            <a href="/login">Login</a>
          </li>
          <li>
            <a href="/about">About</a>
          </li>
          <li>
            <a href="/contact">Contact</a>
          </li>
          <ThemeSwitcher />
        </ul>
      </div>
    </nav>
  );
};

export default HeaderNav;
