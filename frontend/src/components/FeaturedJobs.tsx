import { motion } from "framer-motion";
import { featuredJobs } from "../data/jobs";

function FeaturedJobs(): JSX.Element {
  return (
    <section className="featured">
      <div className="section-heading">
        <div>
          <span className="section-heading__eyebrow">Featured roles</span>
          <h2>Opportunities calibrated for velocity</h2>
        </div>
        <motion.a
          href="#"
          className="btn btn--ghost"
          whileHover={{ x: 4 }}
        >
          View the full roster →
        </motion.a>
      </div>

      <div className="featured__grid">
        {featuredJobs.map((job, index) => (
          <motion.article
            key={job.id}
            className="job-card"
            initial={{ opacity: 0, y: 30 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true, amount: 0.4 }}
            transition={{ duration: 0.6, delay: index * 0.1 }}
          >
            <div className="job-card__header">
              <span className="job-card__avatar" style={{ background: job.logoColor }}>
                {job.company[0]}
              </span>
              <div>
                <h3>{job.title}</h3>
                <p>{job.company}</p>
              </div>
            </div>

            <p className="job-card__location">{job.location}</p>

            <div className="job-card__meta">
              <span>{job.type}</span>
              <span>{job.salary}</span>
              <span>{job.posted}</span>
            </div>

            <div className="job-card__tags">
              {job.tags.map((tag) => (
                <span key={tag} className="chip chip--subtle">
                  {tag}
                </span>
              ))}
            </div>

            <button className="btn btn--secondary job-card__cta">See role details</button>
          </motion.article>
        ))}
      </div>
    </section>
  );
}

export default FeaturedJobs;
