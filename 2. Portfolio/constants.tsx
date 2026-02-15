
import { Project, Experience, Skill, Education } from './types';

export const USER_INFO = {
  name: "Julien HODONOU",
  title: "Data Scientist | Analytics Engineer",
  about: "Passionate about data with proven expertise in data analysis, machine learning, statistical modeling, and data visualization. Skilled in SQL, Python, and modern analytical tools. Strong ability to translate business needs into actionable analytical solutions and communicate insights effectively. Motivated to contribute to a dynamic company by leveraging data to drive growth and innovation.",
  location: "France",
  email: "julienhodonou21@gmail.com",
  linkedin: "https://www.linkedin.com/in/julien-hodonou",
  github: "https://github.com/JulBiDaBi",
  resumeUrl: "#",
};

export const PROJECTS: Project[] = [
  {
    id: "p1",
    title: "Real-time Hand Gesture Detection",
    category: "AI / Machine Learning",
    description: "Developed a system to detect and recognize hand gestures in real-time for sign language interpretation.",
    image: "https://images.unsplash.com/photo-1587560699334-bea93391dcef?q=80&w=800&auto=format&fit=crop",
    tags: ["OpenCV", "MediaPipe", "TensorFlow"],
    github: "https://github.com/JulBiDaBi"
  },
  {
    id: "p2",
    title: "Emotion Detection System",
    category: "AI / Machine Learning",
    description: "Built a facial emotion recognition system capable of identifying human emotions.",
    image: "https://images.unsplash.com/photo-1554177255-61502b352de3?q=80&w=800&auto=format&fit=crop",
    tags: ["Keras", "YOLO"],
    github: "https://github.com/JulBiDaBi"
  },
  {
    id: "p3",
    title: "Medical Intelligent Chatbot",
    category: "AI / Machine Learning",
    description: "Created an AI-powered medical chatbot for intelligent healthcare assistance.",
    image: "https://images.unsplash.com/photo-1576091160550-2173dba999ef?q=80&w=800&auto=format&fit=crop",
    tags: ["NLTK", "Transformers", "LangChain", "LLaMA"],
    github: "https://github.com/JulBiDaBi"
  },
  {
    id: "p4",
    title: "Movie Recommendation System",
    category: "AI / Machine Learning",
    description: "Designed a recommendation engine using collaborative filtering and matrix factorization.",
    image: "https://images.unsplash.com/photo-1536440136628-849c177e76a1?q=80&w=800&auto=format&fit=crop",
    tags: ["Collaborative Filtering", "Matrix Factorization"],
    github: "https://github.com/JulBiDaBi"
  },
  {
    id: "p5",
    title: "Speech Transcription System",
    category: "AI / Machine Learning",
    description: "Implemented automatic speech-to-text transcription system.",
    image: "https://images.unsplash.com/photo-1589254065878-42c9da997008?q=80&w=800&auto=format&fit=crop",
    tags: ["DeepSpeech", "Whisper", "Librosa"],
    github: "https://github.com/JulBiDaBi"
  },
  {
    id: "p6",
    title: "Sentiment Analysis on Customer Reviews",
    category: "AI / Machine Learning",
    description: "Analyzed customer sentiment from reviews using NLP techniques.",
    image: "https://images.unsplash.com/photo-1551288049-bebda4e38f71?q=80&w=800&auto=format&fit=crop",
    tags: ["NLTK", "BERT"],
    github: "https://github.com/JulBiDaBi"
  },
  {
    id: "p7",
    title: "End-to-End Azure Data Pipeline",
    category: "Data Engineering & Viz",
    description: "Built complete data injection pipeline for Adventure Works and Yahoo data using Microsoft Azure (ADF, Databricks, Synapse).",
    image: "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?q=80&w=800&auto=format&fit=crop",
    tags: ["ADF", "Databricks", "Synapse", "Power BI"],
    github: "https://github.com/JulBiDaBi"
  },
  {
    id: "p8",
    title: "URSAFF Power BI Report",
    category: "Data Engineering & Viz",
    description: "Created comprehensive Power BI report analyzing URSAFF data with complex data modeling.",
    image: "https://images.unsplash.com/photo-1460925895917-afdab827c52f?q=80&w=800&auto=format&fit=crop",
    tags: ["Power Query", "DAX", "Data Modeling"],
    github: "https://github.com/JulBiDaBi"
  }
];

export const EXPERIENCES: Experience[] = [
  {
    id: "bel",
    role: "Data Scientist / AI Vision Project Manager",
    company: "Groupe BEL",
    location: "Suresnes, France",
    period: "Sept. 2024 – Sept. 2025",
    description: [
      "Designed and developed consolidated international tracking dashboards (Power BI)",
      "Automated label traceability workflows (PowerApps, Power Automate, SharePoint)",
      "Collected, integrated, and processed multi-source data (Power Query)",
      "Drafted Computer Vision specifications with business teams",
      "Improved production line quality using AI vision systems (YOLO, PyTorch)",
      "Built virtual factory simulations (Plant Simulation)"
    ],
    results: "Designed and deployed a unified AI architecture (edge/cloud) for 27 factories, including an AI Model Foundry, Dataset Repository, and AI Marketplace.",
    stack: ["Power BI", "PowerApps", "YOLO", "PyTorch", "Plant Simulation", "Power Query"]
  },
  {
    id: "bf",
    role: "Data Quality Analyst",
    company: "Business France",
    location: "Paris, France",
    period: "Mar. 2024 – Sept. 2024",
    description: [
      "Facilitated workshops to identify key business indicators",
      "Designed data models, KPIs, and dashboards (Power BI)",
      "Extracted and transformed data from multiple sources",
      "Conducted statistical and quantitative analyses",
      "Implemented quality test protocols (Azure Data Factory)",
      "Contributed to data migration and consistency"
    ],
    results: "Industrialized KPIs, automated testing, and improved dashboard stability and cross-application consistency.",
    stack: ["Power BI", "Azure Data Factory", "SQL", "Python", "Excel"]
  },
  {
    id: "sector",
    role: "Business Intelligence Analyst",
    company: "Sector Alarm",
    location: "Massy, France",
    period: "June 2023 – Sept. 2023",
    description: [
      "Identified business needs and prepared data (SQL, Python)",
      "Built KPIs and dashboards (Power BI, Excel)",
      "Automated weekly reporting",
      "Performed ad hoc analyses and contributed to budget planning"
    ],
    results: "Unified performance view and significant weekly time savings.",
    stack: ["Power BI", "SQL", "Python", "Excel"]
  }
];

export const EDUCATION: Education[] = [
  {
    id: "edu1",
    degree: "Master’s in Big Data & Business Intelligence",
    institution: "Université Sorbonne Paris Nord",
    period: "2022 – 2024",
    description: "Advanced analytics, machine learning, statistical modeling, BI solutions."
  },
  {
    id: "edu2",
    degree: "Master’s Research in International Economics & Development",
    institution: "Université de Kara",
    period: "2020 – 2022",
    description: "Economic analysis, quantitative methods, development economics."
  }
];

export const SKILLS: Skill[] = [
  { name: "Python", level: 95, category: "Languages" },
  { name: "SQL", level: 90, category: "Languages" },
  { name: "R", level: 85, category: "Languages" },
  { name: "PySpark", level: 88, category: "Languages" },
  { name: "Power BI (Expert)", level: 98, category: "Data Viz" },
  { name: "Looker Studio", level: 82, category: "Data Viz" },
  { name: "Excel (Advanced)", level: 95, category: "Data Viz" },
  { name: "Azure Data Factory", level: 90, category: "ETL" },
  { name: "Dataiku", level: 88, category: "ETL" },
  { name: "Talend", level: 80, category: "ETL" },
  { name: "PyTorch / YOLO", level: 92, category: "ML/AI" },
  { name: "Scikit-learn", level: 90, category: "ML/AI" },
  { name: "TensorFlow", level: 85, category: "ML/AI" },
  { name: "OpenCV", level: 88, category: "ML/AI" },
  { name: "LLM/NLP", level: 85, category: "ML/AI" },
  { name: "SQL Server / SAP", level: 85, category: "Databases" },
  { name: "Microsoft Azure", level: 90, category: "Tools" },
  { name: "Azure DevOps", level: 85, category: "Tools" },
  { name: "Agile Scrum / Kanban", level: 90, category: "Methodologies" }
];

export const CERTIFICATIONS = [
  "Databricks Fundamentals",
  "Databricks Lakehouse Platform",
  "Dataiku Core Designer",
  "Dataiku Generative AI Practitioner",
  "Dataiku Advanced Designer",
  "Dataiku MLOps Practitioner",
  "Microsoft Power BI – PL300 (in progress)"
];

export const STRENGTHS = [
  { title: "Statistical Analysis", desc: "Forecasting, classification, and predictive analytics." },
  { title: "Data Quality", desc: "Validation, consistency checks, and monitoring." },
  { title: "Visualization", desc: "Expert Power BI and advanced Excel dashboards." },
  { title: "Automation", desc: "ETL pipelines and integrated cloud workflows." },
  { title: "Collaboration", desc: "Translating business needs into technical solutions." },
  { title: "Communication", desc: "Presenting complex data insights to stakeholders." }
];

export const LEADERSHIP = {
  community: [
    "Active participant in data science communities",
    "Contributor to data science forums and Stack Overflow",
    "Mentor for junior data professionals",
    "Speaker at local tech meetups"
  ],
  development: [
    "Pursuing advanced certifications in cloud and AI",
    "Active on Coursera, edX, Udacity",
    "Researching cutting-edge AI and ML techniques"
  ]
};
