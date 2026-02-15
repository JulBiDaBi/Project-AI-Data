
import React from 'react';
import { USER_INFO } from '../constants';

const Hero: React.FC = () => {
  return (
    <section id="home" className="relative min-h-screen flex items-center pt-20 overflow-hidden">
      {/* Background Orbs */}
      <div className="absolute top-1/4 -left-20 w-96 h-96 bg-blue-600/10 rounded-full blur-[120px] pointer-events-none"></div>
      <div className="absolute bottom-1/4 -right-20 w-96 h-96 bg-purple-600/10 rounded-full blur-[120px] pointer-events-none"></div>

      <div className="container mx-auto px-6 grid md:grid-cols-2 gap-12 items-center relative z-10">
        <div className="space-y-8">
          <div className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full border border-gray-800 bg-gray-900/50 backdrop-blur text-sm font-medium text-blue-400">
            <span className="w-2 h-2 rounded-full bg-green-500 animate-pulse"></span>
            Available for new opportunities
          </div>
          <h1 className="text-7xl md:text-9xl font-bold leading-none tracking-tighter">
            Julien <span className="gradient-text">Hodonou</span>
          </h1>
          <h2 className="text-3xl md:text-4xl font-medium text-gray-400">
            {USER_INFO.title}
          </h2>
          <p className="text-xl text-gray-400 max-w-lg leading-relaxed">
            Unlocking business growth through <span className="text-white font-semibold">Machine Learning</span>, AI Vision, and advanced data storytelling.
          </p>
          <div className="flex flex-wrap gap-4 pt-4">
            <a href="mailto:julienhodonou21@gmail.com" className="px-8 py-4 rounded-xl bg-blue-600 hover:bg-blue-700 text-white font-semibold transition-all shadow-lg shadow-blue-900/20">
              Get in Touch
            </a>
            <a href={USER_INFO.github} target="_blank" className="px-8 py-4 rounded-xl border border-gray-800 hover:bg-gray-900 text-white font-semibold transition-all">
              GitHub
            </a>
          </div>
        </div>

        <div className="hidden md:block relative">
          <div className="relative z-10 w-full aspect-square rounded-3xl overflow-hidden border border-gray-800 animate-float bg-gray-900/50 flex items-center justify-center">
             <div className="text-center group">
               <span className="text-9xl font-bold text-gray-800 group-hover:text-blue-900/40 transition-colors">JH</span>
               <div className="mt-4 p-4 glass rounded-2xl border-gray-700/50">
                 <p className="text-gray-400 text-sm">2+ Years Excellence</p>
               </div>
             </div>
          </div>
          {/* Decorative elements */}
          <div className="absolute -top-6 -right-6 w-32 h-32 border-t-2 border-r-2 border-blue-500/30 rounded-tr-3xl"></div>
          <div className="absolute -bottom-6 -left-6 w-32 h-32 border-b-2 border-l-2 border-purple-500/30 rounded-bl-3xl"></div>
        </div>
      </div>
    </section>
  );
};

export default Hero;
