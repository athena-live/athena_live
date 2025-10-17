import { FormEvent } from "react";
import { motion } from "framer-motion";

const jobTypes = ["Any type", "Full-time", "Hybrid", "Remote", "Contract"];
const trendingRoles = ["Product design", "Staff engineering", "Growth lead", "AI research"];

function SearchCard(): JSX.Element {
  const handleSubmit = (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
  };

  return (
    <motion.section
      className="search-card"
      initial={{ opacity: 0, y: 24 }}
      whileInView={{ opacity: 1, y: 0 }}
      viewport={{ once: true, amount: 0.4 }}
      transition={{ duration: 0.6 }}
    >
      <form className="search-card__form" onSubmit={handleSubmit}>
        <div className="search-card__field">
          <label htmlFor="role">Role</label>
          <input id="role" name="role" placeholder="Try “Director of Product”" />
        </div>

        <div className="search-card__field">
          <label htmlFor="location">Location</label>
          <input id="location" name="location" placeholder="City, country, or remote" />
        </div>

        <div className="search-card__field">
          <label htmlFor="type">Work style</label>
          <select id="type" name="type" defaultValue={jobTypes[0]}>
            {jobTypes.map((type) => (
              <option key={type}>{type}</option>
            ))}
          </select>
        </div>

        <motion.button
          type="submit"
          className="btn btn--accent search-card__cta"
          whileHover={{ scale: 1.03 }}
          whileTap={{ scale: 0.98 }}
        >
          Discover roles
        </motion.button>
      </form>

      <div className="search-card__footer">
        <span className="search-card__hint">Trending searches</span>
        <div className="search-card__tags">
          {trendingRoles.map((role) => (
            <motion.button
              key={role}
              type="button"
              className="chip"
              whileHover={{ y: -2 }}
              whileTap={{ scale: 0.98 }}
            >
              {role}
            </motion.button>
          ))}
        </div>
      </div>
    </motion.section>
  );
}

export default SearchCard;
