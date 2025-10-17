import { useState } from "react";
import { motion } from "framer-motion";

const navItems = ["Positions", "Insights", "Stories"];

function Navbar(): JSX.Element {
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  const toggleMenu = (): void => {
    setIsMenuOpen((prev) => !prev);
  };

  const closeMenu = (): void => {
    setIsMenuOpen(false);
  };

  return (
    <header className="navbar">
      <motion.div
        className="navbar__brand"
        initial={{ opacity: 0, y: -12 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.6 }}
      >
        <span className="navbar__title">Jobs</span>
      </motion.div>

      <button
        type="button"
        className={`navbar__toggle ${isMenuOpen ? "navbar__toggle--open" : ""}`}
        onClick={toggleMenu}
        aria-label="Toggle navigation"
        aria-expanded={isMenuOpen}
      >
        <span />
        <span />
        <span />
      </button>

      <nav className={`navbar__links ${isMenuOpen ? "navbar__links--open" : ""}`}>
        {navItems.map((item, index) => (
          <motion.a
            key={item}
            href="#"
            className="navbar__link"
            initial={{ opacity: 0, y: -10 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.1 * index + 0.2, duration: 0.4 }}
            onClick={closeMenu}
          >
            {item}
          </motion.a>
        ))}
      </nav>

      <motion.div
        className="navbar__actions"
        initial={{ opacity: 0, y: -12 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.6, delay: 0.4 }}
      >
        <button className="btn btn--ghost">Sign in</button>
        <button className="btn btn--primary">Join the network</button>
      </motion.div>
    </header>
  );
}

export default Navbar;
