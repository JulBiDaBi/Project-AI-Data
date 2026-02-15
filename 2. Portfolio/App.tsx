
import React from 'react';
import Navbar from './components/Navbar';
import Hero from './components/Hero';
import Projects from './components/Projects';
import Skills from './components/Skills';
import AIAssistant from './components/AIAssistant';
import { EXPERIENCES, USER_INFO, EDUCATION, CERTIFICATIONS, LEADERSHIP } from './constants';

const EducationSection: React.FC = () => {
  return (
    <section id="education" className="py-24 bg-gray-950/30">
      <div className="container mx-auto px-6">
        <h2 className="text-5xl md:text-7xl font-bold mb-16 text-center tracking-tighter">Education & <span className="gradient-text">Background</span></h2>
        <div className="grid md:grid-cols-2 gap-8 max-w-5xl mx-auto mb-20">
          {EDUCATION.map((edu) => (
            <div key={edu.id} className="glass p-8 rounded-3xl border border-gray-800 hover:border-blue-500/30 transition-all">
              <span className="text-blue-500 font-bold text-sm mb-2 block">{edu.period}</span>
              <h3 className="text-2xl font-bold mb-1">{edu.degree}</h3>
              <p className="text-gray-400 font-medium mb-4">{edu.institution}</p>
              <p className="text-gray-500 text-sm leading-relaxed">{edu.description}</p>
            </div>
          ))}
        </div>

        <div className="max-w-5xl mx-auto">
          <h3 className="text-xl font-bold mb-10 text-center uppercase tracking-widest text-gray-500">Professional Certifications</h3>
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
            {CERTIFICATIONS.map((cert, idx) => (
              <div key={idx} className="p-4 rounded-xl border border-gray-900 bg-gray-900/40 text-sm text-gray-400 hover:text-white hover:border-gray-700 transition-colors flex items-center gap-3">
                <svg className="w-5 h-5 text-blue-500 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                {cert}
              </div>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
};

const ExperienceSection: React.FC = () => {
  return (
    <section id="experience" className="py-32">
      <div className="container mx-auto px-6">
        <h2 className="text-5xl md:text-7xl font-bold mb-24 text-center tracking-tighter">Professional <span className="gradient-text">Experience</span></h2>
        <div className="max-w-6xl mx-auto space-y-24">
          {EXPERIENCES.map((exp, index) => (
            <div key={exp.id} className="grid lg:grid-cols-12 gap-8 lg:gap-16 items-start group">
              {/* Date & Company Sticky Column */}
              <div className="lg:col-span-4 lg:sticky lg:top-32 space-y-2">
                <div className="flex items-center gap-3 mb-2">
                  <span className="text-blue-500 font-bold text-lg">0{index + 1}</span>
                  <div className="h-px w-8 bg-blue-500/30"></div>
                </div>
                <h3 className="text-3xl font-bold group-hover:text-blue-400 transition-colors">{exp.company}</h3>
                <p className="text-sm text-gray-500 uppercase tracking-[0.2em] font-bold">{exp.period}</p>
                <div className="pt-4 flex flex-wrap gap-2">
                  {exp.stack.map(tech => (
                    <span key={tech} className="text-[10px] px-2 py-0.5 rounded-md bg-blue-500/10 text-blue-400 border border-blue-500/20">{tech}</span>
                  ))}
                </div>
              </div>

              {/* Achievements Column */}
              <div className="lg:col-span-8 space-y-8 glass p-8 lg:p-12 rounded-[2.5rem] border-gray-800/50">
                <div>
                  <h4 className="text-2xl font-bold mb-2">{exp.role}</h4>
                  <p className="text-sm text-gray-500 italic mb-6">{exp.location}</p>
                </div>
                
                <ul className="space-y-4">
                  {exp.description.map((desc, i) => (
                    <li key={i} className="text-gray-400 text-lg leading-relaxed flex gap-4">
                      <span className="text-blue-500 mt-2 flex-shrink-0">
                        <div className="w-1.5 h-1.5 rounded-full bg-blue-500"></div>
                      </span>
                      {desc}
                    </li>
                  ))}
                </ul>

                <div className="mt-8 pt-8 border-t border-gray-800">
                  <div className="flex items-start gap-4">
                    <div className="w-10 h-10 rounded-xl bg-blue-500/10 flex items-center justify-center flex-shrink-0">
                      <svg className="w-5 h-5 text-blue-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
                    </div>
                    <div>
                      <p className="text-xs font-bold text-blue-500 uppercase tracking-widest mb-1">Impact & Results</p>
                      <p className="text-gray-300 italic leading-relaxed">{exp.results}</p>
                    </div>
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

const LeadershipSection: React.FC = () => {
  return (
    <section id="leadership" className="py-24 bg-gray-950/30">
      <div className="container mx-auto px-6">
        <h2 className="text-5xl md:text-7xl font-bold mb-16 text-center tracking-tighter">Leadership & <span className="gradient-text">Community</span></h2>
        <div className="grid md:grid-cols-2 gap-12 max-w-5xl mx-auto">
          <div className="glass p-10 rounded-[3rem] border-gray-800">
            <h3 className="text-2xl font-bold mb-6 flex items-center gap-3">
              <span className="w-8 h-8 rounded-full bg-blue-500/20 flex items-center justify-center text-blue-500 text-sm">01</span>
              Community Involvement
            </h3>
            <ul className="space-y-4 text-gray-400">
              {LEADERSHIP.community.map((item, idx) => (
                <li key={idx} className="flex gap-3">
                  <span className="text-blue-500">✓</span>
                  {item}
                </li>
              ))}
            </ul>
          </div>
          <div className="glass p-10 rounded-[3rem] border-gray-800">
            <h3 className="text-2xl font-bold mb-6 flex items-center gap-3">
              <span className="w-8 h-8 rounded-full bg-purple-500/20 flex items-center justify-center text-purple-500 text-sm">02</span>
              Professional Development
            </h3>
            <ul className="space-y-4 text-gray-400">
              {LEADERSHIP.development.map((item, idx) => (
                <li key={idx} className="flex gap-3">
                  <span className="text-purple-500">✓</span>
                  {item}
                </li>
              ))}
            </ul>
          </div>
        </div>
      </div>
    </section>
  );
};

const Footer: React.FC = () => {
  return (
    <footer id="contact" className="py-24 border-t border-gray-900">
      <div className="container mx-auto px-6">
        <div className="grid lg:grid-cols-2 gap-16 mb-20 items-center">
          <div>
            <h2 className="text-5xl md:text-6xl font-bold mb-8 leading-tight tracking-tighter">Let's solve your <span className="gradient-text">data</span> challenges.</h2>
            <p className="text-gray-400 mb-12 text-lg max-w-md">I'm always interested in new opportunities and collaborations. Let's connect and explore how we can work together.</p>
            
            <div className="space-y-6">
              <a href={`mailto:${USER_INFO.email}`} className="flex items-center gap-6 group">
                <div className="w-14 h-14 rounded-2xl bg-gray-900 flex items-center justify-center group-hover:bg-blue-600 transition-colors">
                  <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path></svg>
                </div>
                <div>
                  <p className="text-xs text-gray-500 font-bold uppercase tracking-widest">Email Julien</p>
                  <p className="text-xl font-medium">{USER_INFO.email}</p>
                </div>
              </a>
              <a href={USER_INFO.linkedin} target="_blank" className="flex items-center gap-6 group">
                <div className="w-14 h-14 rounded-2xl bg-gray-900 flex items-center justify-center group-hover:bg-blue-600 transition-colors">
                  <svg className="w-6 h-6" fill="currentColor" viewBox="0 0 24 24"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg>
                </div>
                <div>
                  <p className="text-xs text-gray-500 font-bold uppercase tracking-widest">LinkedIn</p>
                  <p className="text-xl font-medium">/julien-hodonou</p>
                </div>
              </a>
            </div>
          </div>

          <form className="glass p-10 rounded-[3rem] border border-gray-800 space-y-6">
            <div className="grid grid-cols-2 gap-6">
              <div className="space-y-2">
                <label className="text-[10px] font-bold text-gray-500 uppercase tracking-[0.2em]">Your Name</label>
                <input type="text" className="w-full bg-gray-950 border border-gray-800 rounded-2xl px-5 py-4 focus:outline-none focus:border-blue-500 transition-colors" placeholder="Jane Doe" />
              </div>
              <div className="space-y-2">
                <label className="text-[10px] font-bold text-gray-500 uppercase tracking-[0.2em]">Email Address</label>
                <input type="email" className="w-full bg-gray-950 border border-gray-800 rounded-2xl px-5 py-4 focus:outline-none focus:border-blue-500 transition-colors" placeholder="jane@example.com" />
              </div>
            </div>
            <div className="space-y-2">
              <label className="text-[10px] font-bold text-gray-500 uppercase tracking-[0.2em]">Message</label>
              <textarea rows={4} className="w-full bg-gray-950 border border-gray-800 rounded-2xl px-5 py-4 focus:outline-none focus:border-blue-500 transition-colors" placeholder="Let's connect and explore how we can work together."></textarea>
            </div>
            <button className="w-full py-5 rounded-2xl bg-blue-600 text-white font-bold hover:bg-blue-700 transition-all shadow-xl shadow-blue-900/20">Send Inquiry</button>
          </form>
        </div>

        <div className="pt-12 border-t border-gray-900 flex flex-col md:flex-row justify-between items-center gap-6">
          <p className="text-sm text-gray-600">© 2024 {USER_INFO.name}. Built with Modern Data Stack Expertise.</p>
          <div className="flex gap-8">
            <a href={USER_INFO.github} target="_blank" className="text-sm text-gray-600 hover:text-white transition-colors">GitHub</a>
            <a href={USER_INFO.linkedin} target="_blank" className="text-sm text-gray-600 hover:text-white transition-colors">LinkedIn</a>
          </div>
        </div>
      </div>
    </footer>
  );
};

const App: React.FC = () => {
  return (
    <div className="min-h-screen selection:bg-blue-500 selection:text-white">
      <Navbar />
      <Hero />
      <div id="about" className="py-32 bg-gray-950/20 border-y border-gray-900">
        <div className="container mx-auto px-6 max-w-4xl text-center">
          <span className="text-[10px] font-bold text-blue-500 uppercase tracking-[0.4em] mb-10 block">Professional Summary</span>
          <h2 className="text-xl md:text-2xl font-normal leading-relaxed text-gray-300">
            {USER_INFO.about}
          </h2>
        </div>
      </div>
      <ExperienceSection />
      <EducationSection />
      <Projects />
      <Skills />
      <LeadershipSection />
      <Footer />
      <AIAssistant />
    </div>
  );
};

export default App;
