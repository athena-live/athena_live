import type { Insight, Job, Testimonial } from "../types";

export const featuredJobs: Job[] = [
  {
    id: 1,
    title: "Senior Product Designer",
    company: "NovaLabs",
    location: "New York, NY · Hybrid",
    salary: "$145k - $175k",
    type: "Hybrid",
    posted: "2d ago",
    tags: ["Product", "Design Systems", "Figma"],
    logoColor: "#4338CA"
  },
  {
    id: 2,
    title: "Staff Machine Learning Engineer",
    company: "Beacon AI",
    location: "Remote · North America",
    salary: "$180k - $220k",
    type: "Remote",
    posted: "4d ago",
    tags: ["AI/ML", "Python", "MLOps"],
    logoColor: "#0EA5E9"
  },
  {
    id: 3,
    title: "Head of Growth Marketing",
    company: "Atlas Collective",
    location: "San Francisco, CA",
    salary: "$160k - $200k",
    type: "Full-time",
    posted: "1w ago",
    tags: ["Lifecycle", "Analytics", "Experimentation"],
    logoColor: "#6366F1"
  }
];

export const platformInsights: Insight[] = [
  {
    id: 1,
    title: "Curated talent matching",
    description: "A vetting process that aligns skills, values, and growth trajectories with hiring teams.",
    icon: "🎯"
  },
  {
    id: 2,
    title: "Signals that stand out",
    description: "Adaptive profiles turn your achievements into compelling narratives hiring managers notice.",
    icon: "📈"
  },
  {
    id: 3,
    title: "Coaching on demand",
    description: "Expert mentors refine your interview stories and help you negotiate competitive offers.",
    icon: "🤝"
  }
];

export const testimonials: Testimonial[] = [
  {
    id: 1,
    name: "Samantha Ortiz",
    title: "Director of Product · Lumen",
    quote:
      "Athena unlocked senior opportunities I never saw on the usual boards. The prep sprints and signal deck helped me land an offer I am proud of.",
    avatar: "SO"
  },
  {
    id: 2,
    name: "Michael Chen",
    title: "Head of Engineering · LinearShift",
    quote:
      "We filled a pivotal staff engineer role in 18 days. The candidates were vetted, engaged, and ready with context from day one.",
    avatar: "MC"
  },
  {
    id: 3,
    name: "Priya Desai",
    title: "Growth Lead · Northbeam",
    quote:
      "The platform felt like a strategist on my side. Every interaction—from role briefings to negotiation—was thoughtful and data-backed.",
    avatar: "PD"
  }
];
