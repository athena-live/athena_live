import { motion } from "framer-motion";
import { testimonials } from "../data/jobs";

function Testimonials(): JSX.Element {
  return (
    <section className="testimonials">
      <div className="section-heading">
        <div>
          <span className="section-heading__eyebrow">Outcomes that resonate</span>
          <h2>Stories from operators and hiring leaders</h2>
        </div>
        <p className="testimonials__intro">
          A curated network means both sides of the table are prepared. Here is how the Athena
          experience translates into momentum.
        </p>
      </div>

      <div className="testimonials__grid">
        {testimonials.map((item, index) => (
          <motion.blockquote
            key={item.id}
            className="testimonial-card"
            initial={{ opacity: 0, y: 24 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true, amount: 0.3 }}
            transition={{ duration: 0.6, delay: index * 0.1 }}
          >
            <p>“{item.quote}”</p>
            <footer>
              <span className="testimonial-card__avatar">{item.avatar}</span>
              <div>
                <strong>{item.name}</strong>
                <span>{item.title}</span>
              </div>
            </footer>
          </motion.blockquote>
        ))}
      </div>
    </section>
  );
}

export default Testimonials;
