import Navbar from "./components/Navbar";
import Hero from "./components/Hero";
import FeaturedJobs from "./components/FeaturedJobs";
import Insights from "./components/Insights";
import Testimonials from "./components/Testimonials";
import CTASection from "./components/CTASection";
import Footer from "./components/Footer";

function App(): JSX.Element {
  return (
    <div className="app">
      <Navbar />
      <main>
        <Hero />
        <FeaturedJobs />
        <Insights />
        <Testimonials />
        <CTASection />
      </main>
      <Footer />
    </div>
  );
}

export default App;
