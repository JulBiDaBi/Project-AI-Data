
import React, { useMemo } from 'react';
import { ResponsiveContainer, Radar, RadarChart, PolarGrid, PolarAngleAxis, PolarRadiusAxis } from 'recharts';
import { SKILLS, STRENGTHS } from '../constants';

const Skills: React.FC = () => {
  const radarData = useMemo(() => {
    // Picking top diverse skills for the radar chart
    const radarSkills = [
      SKILLS.find(s => s.name === 'Python'),
      SKILLS.find(s => s.name === 'Power BI (Expert)'),
      SKILLS.find(s => s.name === 'Azure Data Factory'),
      SKILLS.find(s => s.name === 'YOLO'),
      SKILLS.find(s => s.name === 'Agile Scrum'),
      SKILLS.find(s => s.name === 'SQL'),
    ].filter(Boolean);

    return radarSkills.map(s => ({
      subject: s!.name,
      A: s!.level,
      fullMark: 100,
    }));
  }, []);

  const categories = ["Languages", "Data Viz", "ETL", "ML/AI", "Tools", "Methodologies"] as const;

  return (
    <section id="skills" className="py-24 bg-gray-950/50">
      <div className="container mx-auto px-6">
        <div className="text-center mb-20">
          <h2 className="text-4xl font-bold mb-4">Technical <span className="gradient-text">Proficiency</span></h2>
          <p className="text-gray-400 max-w-2xl mx-auto">Bridging technical complexity with business intelligence using a modern analytics stack.</p>
        </div>

        <div className="grid lg:grid-cols-2 gap-16 items-start">
          <div className="sticky top-32">
            <h3 className="text-xl font-bold mb-8 text-center lg:text-left">Competency Mapping</h3>
            <div className="h-[400px] w-full glass rounded-3xl p-6 mb-12">
              <ResponsiveContainer width="100%" height="100%">
                <RadarChart cx="50%" cy="50%" outerRadius="80%" data={radarData}>
                  <PolarGrid stroke="#374151" />
                  <PolarAngleAxis dataKey="subject" tick={{ fill: '#9ca3af', fontSize: 10 }} />
                  <PolarRadiusAxis angle={30} domain={[0, 100]} tick={false} axisLine={false} />
                  <Radar
                    name="Proficiency"
                    dataKey="A"
                    stroke="#60a5fa"
                    fill="#60a5fa"
                    fillOpacity={0.4}
                  />
                </RadarChart>
              </ResponsiveContainer>
            </div>
            
            <div className="grid grid-cols-2 gap-4">
              {STRENGTHS.map(s => (
                <div key={s.title} className="p-4 rounded-2xl glass border-gray-800/50">
                  <h4 className="text-sm font-bold text-blue-400 mb-1">{s.title}</h4>
                  <p className="text-xs text-gray-500 leading-tight">{s.desc}</p>
                </div>
              ))}
            </div>
          </div>

          <div className="space-y-10">
            {categories.map(cat => (
              <div key={cat}>
                <h3 className="text-xs font-bold text-gray-500 uppercase tracking-[0.3em] mb-4">{cat}</h3>
                <div className="flex flex-wrap gap-2">
                  {SKILLS.filter(s => s.category === cat).map(skill => (
                    <div key={skill.name} className="px-4 py-2 rounded-xl bg-gray-900 border border-gray-800 hover:border-blue-500/50 transition-all flex items-center gap-3">
                      <span className="text-sm text-gray-300 font-medium">{skill.name}</span>
                      <div className="w-8 h-1 bg-gray-800 rounded-full overflow-hidden">
                        <div className="h-full bg-blue-500" style={{ width: `${skill.level}%` }}></div>
                      </div>
                    </div>
                  ))}
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
};

export default Skills;
