function Footer(): JSX.Element {
  const year = new Date().getFullYear();

  return (
    <footer className="footer">
      <div className="footer__brand">
        <span className="navbar__logo">A</span>
        <span className="navbar__title">Athena Talent</span>
      </div>
      <div className="footer__links">
        <a href="#">Privacy</a>
        <a href="#">Terms</a>
        <a href="#">Careers</a>
        <a href="#">Partner with us</a>
      </div>
      <span className="footer__copyright">© {year} Athena Talent Collective</span>
    </footer>
  );
}

export default Footer;
