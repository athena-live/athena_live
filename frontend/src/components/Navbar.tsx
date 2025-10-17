import { motion } from "framer-motion";

const navItems = ["Platform", "Positions", "Insights", "Pricing", "Stories"];

function Navbar(): JSX.Element {
  return (
    <header className="navbar">
      <motion.div
        className="navbar__brand"
        initial={{ opacity: 0, y: -12 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.6 }}
      >
        <span className="navbar__logo">A</span>
        <span className="navbar__title">Athena Talent</span>
      </motion.div>

      <nav className="navbar__links">
        {navItems.map((item, index) => (
          <motion.a
            key={item}
            href="#"
            className="navbar__link"
            initial={{ opacity: 0, y: -10 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.1 * index + 0.2, duration: 0.4 }}
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
