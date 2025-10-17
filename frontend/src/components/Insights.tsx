import { motion } from "framer-motion";
import { platformInsights } from "../data/jobs";
import Emoji from "./Emoji";

function Insights(): JSX.Element {
  return (
    <section className="insights">
      <div className="section-heading">
        <div>
          <span className="section-heading__eyebrow">Why candidates choose Athena</span>
          <h2>Signals, coaching, and momentum in one place</h2>
        </div>
      </div>

      <div className="insights__grid">
        {platformInsights.map((insight, index) => (
          <motion.article
            key={insight.id}
            className="insight-card"
            initial={{ opacity: 0, y: 24 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true, amount: 0.35 }}
            transition={{ duration: 0.6, delay: index * 0.08 }}
          >
            <Emoji
              symbol={insight.icon}
              label={insight.title}
              className="insight-card__icon"
            />
            <h3>{insight.title}</h3>
            <p>{insight.description}</p>
          </motion.article>
        ))}
      </div>
    </section>
  );
}

export default Insights;
