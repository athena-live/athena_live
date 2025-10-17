import { motion } from "framer-motion";

const metrics = [
  { value: "12k+", label: "Curated roles posted with Athena signals" },
  { value: "94%", label: "Candidates reaching final stage with coaching" },
  { value: "18", label: "Average days to secure tailored offers" }
];

function Metrics(): JSX.Element {
  return (
    <section className="metrics">
      {metrics.map((metric, index) => (
        <motion.div
          key={metric.value}
          className="metric"
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true, amount: 0.4 }}
          transition={{ delay: index * 0.1, duration: 0.5 }}
        >
          <span className="metric__value">{metric.value}</span>
          <span className="metric__label">{metric.label}</span>
        </motion.div>
      ))}
    </section>
  );
}

export default Metrics;
