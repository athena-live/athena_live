export type JobType = "Full-time" | "Part-time" | "Contract" | "Hybrid" | "Remote";

export interface Job {
  id: number;
  title: string;
  company: string;
  location: string;
  salary: string;
  type: JobType;
  posted: string;
  tags: string[];
  logoColor: string;
}

export interface Testimonial {
  id: number;
  name: string;
  title: string;
  quote: string;
  avatar: string;
}

export interface Insight {
  id: number;
  title: string;
  description: string;
  icon: string;
}
