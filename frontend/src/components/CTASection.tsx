import { motion } from "framer-motion";

function CTASection(): JSX.Element {
  return (
    <section className="cta">
      <motion.div
        className="cta__card"
        initial={{ opacity: 0, scale: 0.96 }}
        whileInView={{ opacity: 1, scale: 1 }}
        viewport={{ once: true, amount: 0.6 }}
        transition={{ duration: 0.6 }}
      >
        <span className="cta__eyebrow">Let’s map your next chapter</span>
        <h2>Bring clarity to your search and momentum to your negotiations.</h2>
        <p>
          Join a private network of high-signal operators, founders, and product builders. We align
          ambition, opportunity, and timing.
        </p>
        <div className="cta__actions">
          <motion.button className="btn btn--primary" whileHover={{ x: 4 }} whileTap={{ scale: 0.97 }}>
            Request an invite
          </motion.button>
          <motion.button className="btn btn--ghost" whileHover={{ x: 4 }} whileTap={{ scale: 0.97 }}>
            Explore candidate stories
          </motion.button>
        </div>
      </motion.div>
    </section>
  );
}

export default CTASection;
