
import React from 'react';
import { PROJECTS } from '../constants';

const Projects: React.FC = () => {
  return (
    <section id="projects" className="py-24">
      <div className="container mx-auto px-6">
        <div className="flex flex-col md:flex-row justify-between items-end mb-16 gap-4">
          <div>
            <h2 className="text-4xl font-bold mb-4">Featured <span className="gradient-text">Portfolio</span></h2>
            <p className="text-gray-400 max-w-xl">Showcasing projects in AI / Machine Learning and Data Engineering & Visualization.</p>
          </div>
          <a href="https://github.com/JulBiDaBi" target="_blank" className="text-blue-400 font-bold hover:text-blue-300 transition-colors flex items-center gap-2 group">
            GitHub Portfolio
            <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 group-hover:translate-x-1 transition-transform" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M17 8l4 4m0 0l-4 4m4-4H3" />
            </svg>
          </a>
        </div>

        <div className="grid md:grid-cols-2 gap-8">
          {PROJECTS.map((project) => (
            <div key={project.id} className="group glass rounded-3xl overflow-hidden border border-gray-800 hover:border-blue-500/20 transition-all duration-500">
              <div className="grid md:grid-cols-1 lg:grid-cols-2">
                <div className="aspect-video lg:aspect-square relative overflow-hidden h-full">
                  <img 
                    src={project.image} 
                    alt={project.title} 
                    className="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700"
                  />
                  <div className="absolute inset-0 bg-blue-600/10 mix-blend-multiply opacity-0 group-hover:opacity-100 transition-opacity"></div>
                </div>
                <div className="p-8 flex flex-col justify-between">
                  <div>
                    <span className="text-[10px] font-bold uppercase tracking-[0.2em] text-blue-500 mb-3 block">{project.category}</span>
                    <h3 className="text-xl font-bold mb-3 group-hover:text-blue-400 transition-colors">{project.title}</h3>
                    <p className="text-gray-400 text-sm leading-relaxed mb-6">{project.description}</p>
                    <div className="flex flex-wrap gap-2">
                      {project.tags.map(tag => (
                        <span key={tag} className="text-[10px] px-2 py-1 rounded bg-gray-900 border border-gray-800 text-gray-500">
                          {tag}
                        </span>
                      ))}
                    </div>
                  </div>
                  <div className="mt-8">
                    <a href={project.github} target="_blank" className="text-xs font-bold flex items-center gap-2 hover:text-blue-400 transition-colors">
                      Explore Repository 
                      <svg className="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.041-1.412-4.041-1.412-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg>
                    </a>
                  </div>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default Projects;
