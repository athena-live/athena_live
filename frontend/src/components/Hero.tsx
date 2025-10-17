import { motion } from "framer-motion";
import SearchCard from "./SearchCard";
import Metrics from "./Metrics";

const partners = [
  "LinearShift",
  "Northbeam",
  "NovaLabs",
  "Beacon AI",
  "Atlas Collective",
  "Arcadia"
];

function Hero(): JSX.Element {
  return (
    <section className="hero">
      <motion.div
        className="hero__content"
        initial={{ opacity: 0, y: 30 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.7 }}
      >
        <span className="hero__eyebrow">Intelligent career orchestration</span>
        <h1 className="hero__title">
          Navigate your next role with <span className="gradient-text">Athena Talent</span>
        </h1>
        <p className="hero__subtitle">
          We pair human insight with data-backed coaching so high-impact operators can meet teams
          scaling with intention.
        </p>
      </motion.div>

      <SearchCard />

      <Metrics />

      <motion.div
        className="hero__partners"
        initial="hidden"
        whileInView="visible"
        viewport={{ once: true, amount: 0.4 }}
        variants={{
          hidden: { opacity: 0, y: 20 },
          visible: { opacity: 1, y: 0, transition: { staggerChildren: 0.08 } }
        }}
      >
        <span className="hero__partners-label">Trusted by teams crafting the future</span>
        <div className="hero__partners-logos">
          {partners.map((partner) => (
            <motion.span
              key={partner}
              className="hero__partner"
              variants={{ hidden: { opacity: 0, y: 10 }, visible: { opacity: 1, y: 0 } }}
            >
              {partner}
            </motion.span>
          ))}
        </div>
      </motion.div>
    </section>
  );
}

export default Hero;
