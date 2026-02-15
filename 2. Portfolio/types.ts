
export interface Project {
  id: string;
  title: string;
  description: string;
  image: string;
  tags: string[];
  link?: string;
  github?: string;
  category: string;
}

export interface Experience {
  id: string;
  role: string;
  company: string;
  period: string;
  location: string;
  description: string[];
  results: string;
  stack: string[];
}

export interface Skill {
  name: string;
  level: number;
  category: 'Languages' | 'Data Viz' | 'ETL' | 'ML/AI' | 'Databases' | 'Tools' | 'Methodologies';
}

export interface Education {
  id: string;
  degree: string;
  institution: string;
  period: string;
  description: string;
}

export interface Message {
  role: 'user' | 'assistant';
  content: string;
}
